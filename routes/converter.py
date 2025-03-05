import re

from flask import Blueprint, request, jsonify, current_app, render_template

from models.conversion import ConversionDAO
from services.llm_service import LLMProviderFactory

bp = Blueprint('converter', __name__)


def detect_language(code: str) -> str:
    """使用简单启发式规则进行基础语言检测"""
    patterns = {
        'Python': (r'\b(def|print|import)\b', r'^\s*#'),
        'JavaScript': (r'\b(function|let|const|=>)\b', r'//'),
        'Java': (r'\b(public\s+class|System\.out\.println)\b', r'//'),
        'C++': (r'\b(#include|using\s+namespace|std::)\b', r'//'),
        'C#': (r'\b(using\s+System|Console\.WriteLine)\b', r'//')
    }

    for lang, (keywords, comments) in patterns.items():
        if re.search(keywords, code) or re.search(comments, code):
            return lang
    return 'Unknown'


@bp.route('/')
def index():
    # print(url_for('static', filename='style.css'))
    return render_template('index.html')


@bp.route('/convert', methods=['POST'])
def convert():
    data = request.json
    source_code = data['code'].strip()
    target_lang = data['targetLang']

    # 输入验证
    if not source_code:
        return jsonify({'error': 'Empty source code'}), 400

    # 语言检测
    # detected_lang = detect_language(source_code)
    # if detected_lang == 'Unknown':
    #     return jsonify({'error': 'Language detection failed'}), 400

    try:
        # 获取LLM服务
        llm_service = LLMProviderFactory.create_service(current_app.config)
        converted_code = llm_service.convert_code(source_code, target_lang)
        detected_lang = llm_service.detect_language(source_code)

        # 存储记录
        dao = ConversionDAO(current_app.config)
        dao.create_record(source_code, detected_lang,
                          target_lang, converted_code)

        return jsonify({
            'convertedCode': converted_code,
            'detectedLang': detected_lang
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500
