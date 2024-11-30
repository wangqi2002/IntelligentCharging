from . import gun
from flask import request, jsonify
from model.models import db, OmindUserCar


# 增
@OmindUserCar.route('/car/create', methods=['POST'])
def add_us_data_by_json():
    add_us_data = request.get_json()
    try:
        new_user = OmindUserCar(username=add_us_data['username'], email=add_us_data['email'])
        db.session.add(new_user)
        db.session.commit()  # 提交事务以保存到数据库
        status_code = 200
        result = {
            "msg": "Add successful.",
            "code": status_code
        }
    except:
        db.session.rollback()
        status_code = 400
        result = {
            "msg": "Add failed! Please check the query data.",
            "code": status_code
        }
    return jsonify(result), status_code


# 删
@OmindUserCar.route('/car/delete/<id>', methods=['DELETE'])
def delete_us_data(id):
    user = OmindUserCar.query.get(int(id))  # 通过 id 查询
    if user:
        db.session.delete(user)
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
    return jsonify(result), status_code


# 改
@OmindUserCar.route('/car/changeIfon/<id>', methods=['PUT'])
def up_us_data(id):
    add_us_data = request.get_json()
    user = OmindUserCar.query.get(int(id))
    if user:
        user.email = add_us_data['email']
        user.username = add_us_data['username']
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
    return jsonify(result), status_code


# 查
@OmindUserCar.route('/car/info', methods=['GET'])
def get_data_by_us_name():
    car_id = request.args.get("id", type=int)
    car_data = OmindUserCar.query.get(car_id)
    if not car_data:
        status_code = 400
        result = {
            "msg": "Query failed! Please check the query username.",
            "us_data": {},
            "code": status_code
        }
    else:
        status_code = 200
        result = {
            "msg": "Query successful.",
            "car_data": car_data,
            "code": status_code
        }
    return jsonify(result), status_code


# 查
@OmindUserCar.route('/car/list', methods=['GET'])
def get_data_by_us_name():
    car_list = OmindUserCar.query.get()
    if not car_list:
        status_code = 400
        result = {
            "msg": "Query failed! Please check the query username.",
            "car_data": {},
            "code": status_code
        }
    else:
        status_code = 200
        result = {
            "msg": "Query successful.",
            "car_list": car_list,
            "code": status_code
        }
    return jsonify(result), status_code
