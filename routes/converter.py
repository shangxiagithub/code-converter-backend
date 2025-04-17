from datetime import datetime

from flask import Blueprint, request, jsonify, current_app, render_template

from models.conversion import ConversionDAO
from services.llm_service import LLMProviderFactory

bp = Blueprint('converter', __name__)


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

    try:
        # 获取LLM服务
        llm_service = LLMProviderFactory.create_service(current_app.config)
        converted_code = llm_service.convert_code(source_code, target_lang)
        # detected_lang = llm_service.detect_language(source_code)

        # 存储记录
        dao = ConversionDAO(current_app.config)
        dao.create_record(source_code, "java",
                          target_lang, converted_code)

        return jsonify({
            'convertedCode': converted_code,
            'detectedLang': 'java',
            'timestamp': datetime.now().isoformat()
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500
