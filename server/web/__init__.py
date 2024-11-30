from flask import Flask
from model.models import db
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['JSON_AS_ASCII'] = False
    # 查询时会显示原始SQL语句
    app.config['SQLALCHEMY_ECHO'] = False
    # 注册蓝图
    from web.user import user
    app.register_blueprint(user)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app
