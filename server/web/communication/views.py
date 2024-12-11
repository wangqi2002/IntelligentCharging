from . import communication
from flask import request, jsonify
from model.models import db, OmindUserCar
from utils import util
from store import globalfile


# 增加车辆
@communication.route('/communication/create', methods=['POST'])
def add_car():
    r_data = request.get_json()
    try:
        car_data = OmindUserCar.query.filter_by(plate_no=r_data['plate_no']).first()
        if not car_data:
            new_car = OmindUserCar(user_id=r_data['user_id'], plate_no=r_data['plate_no'],owner=r_data['owner'])
            db.session.add(new_car)
            db.session.commit()  # 提交事务以保存到数据库
            status_code = 200
            result = {
                "msg": "Add successful.",
                "code": status_code
            }
        else:
            status_code = 401
            result = {
                "msg": "Add failed! Vehicle already exists",
                "code": status_code
            }
    except:
        db.session.rollback()
        status_code = 400
        result = {
            "msg": "Add failed! Please check the query data.",
            "code": status_code
        }
    return jsonify(result)


# 删除车辆
@communication.route('/communication/delete', methods=['POST'])
def delete_car():
    r_data = request.get_json()
    car_data = OmindUserCar.query.filter_by(plate_no=r_data["plate_no"]).first()
    if car_data:
        db.session.delete(car_data)
        db.session.commit()  # 提交事务以删除记录
        status_code = 200
        result = {
            "msg": "Delete successfully.",
            "code": status_code
        }
    else:
        db.session.rollback()
        status_code = 400
        result = {
            "msg": "Delete failed! Please check the query data.",
            "code": status_code
        }
    return jsonify(result)


# 修改车辆信息
@communication.route('/communication/changeInfo', methods=['POST'])
def up_car():
    r_data = request.get_json()
    car_data = OmindUserCar.query.filter_by(plate_no=r_data["plate_no"]).first()
    if car_data:
        car_data.owner = r_data['owner']
        car_data.address = r_data['address']
        db.session.commit()  # 提交事务以保存更新
        status_code = 200
        result = {
            "msg": "Updated successfully.",
            "code": status_code
        }
    else:
        db.session.rollback()
        status_code = 400
        result = {
            "msg": "Updated failed! Please check the query data.",
            "code": status_code
        }
    return jsonify(result)


# 获取车辆详细信息
@communication.route('/communication/info', methods=['GET'])
def get_car_info():
    user_id = request.args.get("user_id", type=int)
    plate_no = request.args.get("plate_no", type=str)
    car_data = OmindUserCar.query.filter_by(user_id=user_id, plate_no=plate_no).first()
    if not car_data:
        status_code = 400
        result = {
            "msg": "Query failed! Please check the query username.",
            "data": {},
            "code": status_code
        }
    else:
        status_code = 200
        result = {
            "msg": "Query successful.",
            "data": car_data.to_json(),
            "code": status_code
        }
    return jsonify(result)


# 获取车辆列表
@communication.route('/communication/list', methods=['GET'])
def get_car_list():
    car_id = request.args.get("user_id", type=int)
    car_list = OmindUserCar.query.filter_by(user_id=car_id).all()
    if not car_list:
        status_code = 400
        result = {
            "msg": "Query failed!",
            "data": {},
            "code": status_code
        }
    else:
        status_code = 200
        list = []
        for item in car_list:
            list.append(item.to_json())
        result = {
            "msg": "Query successful.",
            "data": list,
            "code": status_code
        }
    return jsonify(result)
