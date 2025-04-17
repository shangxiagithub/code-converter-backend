from flask import Blueprint, current_app, jsonify

from models.conversion import ConversionDAO

bp = Blueprint('history', __name__)


@bp.route('/history')
def conversion_history():
    try:
        # 存储记录
        dao = ConversionDAO(current_app.config)
        records = dao.get_history()
        return jsonify([{
            'id': r['id'],
            'source': r['source_code'],
            'target': r['converted_code'],
            'fromLang': r['detected_lang'],
            'toLang': r['target_lang'],
            'timestamp': r['conversion_date'].isoformat()
        } for r in records])
    except Exception as e:
        return str(e), 500
