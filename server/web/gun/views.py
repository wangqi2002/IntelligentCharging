from . import gun
from flask import request, jsonify
from model.models import db, OmindEquipment
from utils import util


# 查
@gun.route('/gun/info', methods=['GET'])
def get_gun_info():
    id = request.args.get("id", type=int)
    station_id = request.args.get("station_id", type=str)
    gun_data = OmindEquipment.query.filter_by(id=id,station_id=station_id).first()
    if not gun_data:
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
            "data": gun_data.to_json(),
            "code": status_code
        }
    return jsonify(result)


# 查
@gun.route('/gun/list', methods=['GET'])
def get_gun_list():
    id = request.args.get("station_id", type=str)
    gun_list = OmindEquipment.query.filter_by(station_id=id).all()
    if not gun_list:
        status_code = 400
        result = {
            "msg": "Query failed!",
            "data": {},
            "code": status_code
        }
    else:
        status_code = 200
        list = util.back_list(gun_list)
        result = {
            "msg": "Query successful.",
            "data": list,
            "code": status_code
        }
    return jsonify(result)
