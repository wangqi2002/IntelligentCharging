from flask import Flask
from model.models import db
from config import Config
from web.user import user
from web.car import car
from web.gun import gun
from web.order import order
from web.station import station
from web.communication import communication
from mqtt.mqtt_conncet import connect_mqtt
from store import globalfile


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['JSON_AS_ASCII'] = False
    # 查询时会显示原始SQL语句
    app.config['SQLALCHEMY_ECHO'] = False
    # 注册蓝图
    app.register_blueprint(user, url_prefix='/api/app')
    app.register_blueprint(car, url_prefix='/api/app')
    app.register_blueprint(order, url_prefix='/api/app')
    app.register_blueprint(station, url_prefix='/api/app')
    app.register_blueprint(gun, url_prefix='/api/app')
    app.register_blueprint(communication, url_prefix='/api/app')
    db.init_app(app)
    globalfile.update_client(connect_mqtt())
    globalfile.update_client1(connect_mqtt())
    print(globalfile.CLIENT == globalfile.CLIENT1)
    with app.app_context():
        db.create_all()
    return app
