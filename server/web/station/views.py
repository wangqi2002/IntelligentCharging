from . import station
from flask import request, jsonify
from model.models import db, OmindStation
from utils import util

# 获取站点详情
@station.route('/station/info', methods=['GET'])
def get_station_info():
    id = request.args.get("station_id", type=str)
    station_data = OmindStation.query.filter_by(station_id=id, station_status=50).first()
    if not station_data:
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
            "data": station_data.to_json(),
            "code": status_code
        }
    return jsonify(result)


# 获取站点列表
@station.route('/station/list', methods=['GET'])
def get_station_list():
    station_list = OmindStation.query.filter_by(station_status=50).all()
    if not station_list:
        status_code = 400
        result = {
            "msg": "Query failed!",
            "data": {},
            "code": status_code
        }
    else:
        status_code = 200
        list = util.back_list(station_list)
        result = {
            "msg": "Query successful.",
            "data": list,
            "code": status_code
        }
    return jsonify(result)
