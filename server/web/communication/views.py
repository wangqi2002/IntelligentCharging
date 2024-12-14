from . import communication
from flask import request, jsonify
from model.models import db, OmindUserCar
from utils import util
from store import globalfile
from mqtt import mqtt_pub, mqtt_sub


# 通信连接
@communication.route('/communication/connect', methods=['POST'])
def connect():
    r_data = request.get_json()
    mqtt_sub.subscribe(globalfile.CLIENT1, r_data["topic"])
    mqtt_pub.publish(globalfile.CLIENT, r_data["topic"], "connect")
    # mqtt_sub.unsubscribe(globalfile.CLIENT1, r_data["topic"])
    try:
        if r_data:
            status_code = 200
            result = {
                "msg": "Connect successful.",
                "code": status_code
            }
        else:
            status_code = 401
            result = {
                "msg": "Connect failed!",
                "code": status_code
            }
    except:
        status_code = 400
        result = {
            "msg": "Connect failed!",
            "code": status_code
        }
    return jsonify(result)


# 运动控制
@communication.route('/communication/control', methods=['POST'])
def control():
    r_data = request.get_json()
    mqtt_pub.publish(globalfile.CLIENT, r_data["topic"], str(util.moveTup[r_data["orientation"]]))
    if r_data:
        status_code = 200
        result = {
            "msg": "Delete successfully.",
            "code": status_code
        }
    else:
        status_code = 400
        result = {
            "msg": "Delete failed! Please check the query data.",
            "code": status_code
        }
    return jsonify(result)


# 归位操作
@communication.route('/communication/home', methods=['POST'])
def home():
    r_data = request.get_json()
    mqtt_sub.subscribe(globalfile.CLIENT, r_data["topic"])
    mqtt_pub.publish(globalfile.CLIENT, r_data["topic"], "home")
    mqtt_sub.unsubscribe(globalfile.CLIENT, r_data["topic"])
    if r_data:
        status_code = 200
        result = {
            "msg": "Homing successfully.",
            "code": status_code
        }
    else:
        status_code = 400
        result = {
            "msg": "Homing failed!",
            "code": status_code
        }
    return jsonify(result)


# 连接检测
@communication.route('/communication/keeping', methods=['POST'])
def keeping():
    r_data = request.get_json()
    mqtt_sub.subscribe(globalfile.CLIENT, r_data["topic"])
    mqtt_pub.publish(globalfile.CLIENT, r_data["topic"], "keeping")
    mqtt_sub.unsubscribe(globalfile.CLIENT, r_data["topic"])
    if r_data:
        status_code = 200
        result = {
            "msg": "Keep connection.",
            "code": status_code
        }
    else:
        status_code = 400
        result = {
            "msg": "Connection down",
            "code": status_code
        }
    return jsonify(result)


# 目标运动
@communication.route('/communication/auto', methods=['POST'])
def auto():
    r_data = request.get_json()
    mqtt_sub.subscribe(globalfile.CLIENT, r_data["topic"])
    mqtt_pub.publish(globalfile.CLIENT, r_data["topic"], "auto")
    mqtt_sub.unsubscribe(globalfile.CLIENT, r_data["topic"])
    if r_data:
        status_code = 200
        result = {
            "msg": "Updated successfully.",
            "code": status_code
        }
    else:
        status_code = 400
        result = {
            "msg": "Updated failed! Please check the query data.",
            "code": status_code
        }
    return jsonify(result)
