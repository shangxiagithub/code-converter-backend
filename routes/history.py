from flask import Blueprint, current_app, render_template

from models.conversion import ConversionDAO

bp = Blueprint('history', __name__)


@bp.route('/history')
def conversion_history():
    try:
        # 存储记录
        dao = ConversionDAO(current_app.config)
        records = dao.get_history()
        return render_template('history.html', records=records)
    except Exception as e:
        return str(e), 500
