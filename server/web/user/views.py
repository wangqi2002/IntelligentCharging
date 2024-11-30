from . import user
from flask import request, jsonify
from model.models import db, OmindApp


# 增
# @user.route('/add_us_data_by_json', methods=['POST'])
# def add_us_data_by_json():
#     add_us_data = request.get_json()
#     try:
#         new_user = User(username=add_us_data['username'], email=add_us_data['email'])
#         db.session.add(new_user)
#         db.session.commit()  # 提交事务以保存到数据库
#         status_code = 200
#         result = {
#             "msg": "Add successful.",
#             "code": status_code
#         }
#     except:
#         db.session.rollback()
#         status_code = 400
#         result = {
#             "msg": "Add failed! Please check the query data.",
#             "code": status_code
#         }
#     return jsonify(result), status_code
#
#
# # 删
# @user.route('/delete_us_data/<id>', methods=['DELETE'])
# def delete_us_data(id):
#     user = User.query.get(int(id))  # 通过 id 查询
#     if user:
#         db.session.delete(user)
#         db.session.commit()  # 提交事务以删除记录
#         status_code = 200
#         result = {
#             "msg": "Delete successfully.",
#             "code": status_code
#         }
#     else:
#         db.session.rollback()
#         status_code = 400
#         result = {
#             "msg": "Delete failed! Please check the query data.",
#             "code": status_code
#         }
#     return jsonify(result), status_code
#
#
# # 改
# @user.route('/up_us_data/<id>', methods=['PUT'])
# def up_us_data(id):
#     add_us_data = request.get_json()
#     user = User.query.get(int(id))
#     if user:
#         user.email = add_us_data['email']
#         user.username = add_us_data['username']
#         db.session.commit()  # 提交事务以保存更新
#         status_code = 200
#         result = {
#             "msg": "Updated successfully.",
#             "code": status_code
#         }
#     else:
#         db.session.rollback()
#         status_code = 400
#         result = {
#             "msg": "Updated failed! Please check the query data.",
#             "code": status_code
#         }
#     return jsonify(result), status_code
#
#
# # 查
# @user.route('/get_data_by_us_name', methods=['GET'])
# def get_data_by_us_name():
#     us_id = request.args.get("id", type=int)
#     us_data = User.query.get(us_id)
#     if not us_data:
#         status_code = 400
#         result = {
#             "msg": "Query failed! Please check the query username.",
#             "us_data": {},
#             "code": status_code
#         }
#     else:
#         us_data_get = {
#             "id": us_data.id,
#             "username": us_data.username,
#             "email": us_data.email
#         }
#         status_code = 200
#         result = {
#             "msg": "Query successful.",
#             "us_data": us_data_get,
#             "code": status_code
#         }
#     return jsonify(result), status_code