from flask import Flask
from config import Config
from routes.converter import bp as converter_bp
from routes.history import bp as history_bp


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # # 初始化数据库
    # from database import init_db
    # init_db(app)

    # 注册蓝图
    app.register_blueprint(converter_bp)
    app.register_blueprint(history_bp)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
