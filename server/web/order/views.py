from . import order
from flask import request, jsonify
from model.models import db, OmindBill
from utils import util


# 创建订单
@order.route('/order/create', methods=['POST'])
def add_order():
    r_data = request.get_json()
    try:
        new_order = OmindBill(station_id=r_data['station_id'], connector_id=r_data['connector_id'], start_charge_seq_stat=r_data['start_charge_seq_stat'],
                                 user_id=r_data['user_id'], plate_no=r_data['plate_no'])
        db.session.add(new_order)
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
    return jsonify(result)


# 删除订单
@order.route('/order/delete', methods=['POST'])
def delete_order():
    r_data = request.get_json()
    order_data = OmindBill.query.filter_by(id=r_data["id"]).first()
    if order_data:
        db.session.delete(order_data)
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


# 修改订单状态
@order.route('/order/changeStatus', methods=['POST'])
def up_data_status():
    r_data = request.get_json()
    order_data = OmindBill.query.filter_by(id=r_data["id"]).first()
    if order_data:
        order_data.start_charge_seq_stat = r_data['status']
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


# 获取订单详细信息
@order.route('/order/info', methods=['GET'])
def get_order_info():
    id = request.args.get("id", type=int)
    user_id = request.args.get("user_id", type=int)
    order_data = OmindBill.query.filter_by(id=id, user_id=user_id).first()
    if not order_data:
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
            "data": order_data.to_json(),
            "code": status_code
        }
    return jsonify(result)


# 获取订单列表
@order.route('/order/list', methods=['GET'])
def get_order_list():
    user_id = request.args.get("user_id", type=int)
    order_list = OmindBill.query.filter_by(user_id=user_id).all()
    if not order_list:
        status_code = 400
        result = {
            "msg": "Query failed!",
            "data": {},
            "code": status_code
        }
    else:
        status_code = 200
        list = util.back_list(order_list)
        result = {
            "msg": "Query successful.",
            "data": list,
            "code": status_code
        }
    return jsonify(result)


# 获取订单列表-状态
@order.route('/order/listByStatus', methods=['GET'])
def get_order_list_status():
    user_id = request.args.get("user_id", type=int)
    status = request.args.get("status", type=int)
    order_list = OmindBill.query.filter_by(user_id=user_id,start_charge_seq_stat=status).all()
    if not order_list:
        status_code = 400
        result = {
            "msg": "Query failed!",
            "data": {},
            "code": status_code
        }
    else:
        status_code = 200
        list = util.back_list(order_list)
        result = {
            "msg": "Query successful.",
            "data": list,
            "code": status_code
        }
    return jsonify(result)
