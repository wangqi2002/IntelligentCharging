from . import user
from flask import request, jsonify
from model.models import db, OmindUser
from utils import util
from store import globalfile

@user.route('/user/register', methods=['POST'])
def register():
    us_data = request.get_json()
    try:
        new_us = OmindUser(mobile=us_data['mobile'], email=us_data['email'])
        db.session.add(new_us)
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
            "msg": "Add failed! Please check the query data!",
            "code": status_code
        }
    return jsonify(result), status_code

# 短信登陆
@user.route('/user/smsLogin', methods=['POST'])
def smsLogin():
    us_data = request.get_json()
    try:
        us_account = us_data['account']
        us_captcha = us_data['captcha']
        us_data = OmindUser.query.filter_by(account=us_account)
        if us_captcha == globalfile.CAPTCHA:
            if not us_data:
                new_us = OmindUser(mobile=us_data['mobile'], password=us_data['password'])
                db.session.add(new_us)
                db.session.commit()  # 提交事务以保存到数据库
                status_code = 200
                result = {
                    "msg": "register successful.",
                    "code": status_code
                }
            else:
                status_code = 200
                result = {
                    "msg": "login successful.",
                    "code": status_code
                }
        else:
            status_code = 401
            result = {
                "msg": "captcha failed! Please check the captcha.",
                "code": status_code
            }

    except:
        db.session.rollback()
        status_code = 402
        result = {
            "msg": "verify failed!",
            "code": status_code
        }
    return jsonify(result), status_code


# 账号密码登陆
@user.route('/user/accountLogin', methods=['POST'])
def accountLogin():
    us_data = request.get_json()
    try:
        us_account = us_data['account']
        us_pass = us_data['pass']
        us_data = OmindUser.query.filter_by(account=us_account)
        if not us_data:
            status_code = 400
            result = {
                "msg": "Find failed! Please check the account.",
                "code": status_code
            }
        else:
            if us_pass == us_data['pass']:
                status_code = 200
                result = {
                    "msg": "login successful.",
                    "code": status_code
                }
            else:
                status_code = 401
                result = {
                    "msg": "password failed! Please check the password.",
                    "code": status_code
                }
    except:
        db.session.rollback()
        status_code = 402
        result = {
            "msg": "verify failed!",
            "code": status_code
        }
    return jsonify(result), status_code


# 获取验证码
@user.route('/user/sendCode', methods=['GET'])
def sendCode(phone):
    us_mobile = request.args.get("mobile", type=str)
    us_data = OmindUser.query.get(us_mobile)
    if not us_data:
        status_code = 400
        result = {
            "msg": "Query failed! Please check the phone number.",
            "code": status_code
        }
    else:
        # 调用验证码发送接口，目前无验证码发送接口，使用伪验证码替代
        globalfile.update_var(util.v_code())
        captcha=globalfile.CAPTCHA
        status_code = 200
        result = {
            "msg": "captcha successful.",
            "captcha": captcha,
            "code": status_code
        }
    return jsonify(result), status_code


# 修改个人信息
@user.route('/user/changeInfo', methods=['POST'])
def changeInfo():
    add_us_data = request.get_json()
    try:
        new_user = OmindUser(username=add_us_data['username'], email=add_us_data['email'])
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

#修改密码
@user.route('/user/changePass', methods=['POST'])
def changePass():
    add_us_data = request.get_json()
    try:
        new_user = OmindUser(username=add_us_data['username'], email=add_us_data['email'])
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

# 上传头像
@user.route('/user/uploadAvatar', methods=['POST'])
def uploadAvatar():
    add_us_data = request.get_json()
    try:
        new_user = OmindUser(username=add_us_data['username'], email=add_us_data['email'])
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


# 获取个人信息
@user.route('/user/info', methods=['GET'])
def getInfo():
    us_mobile = request.args.get("mobile", type=str)
    us_data = OmindUser.query.filter_by(mobile=us_mobile)
    print(us_mobile)
    if not us_data:
        status_code = 400
        result = {
            "msg": "Query failed! Please check the query mobile.",
            "code": status_code
        }
    else:
        status_code = 200
        result = {
            "msg": "Query successful.",
            "us_data": us_data,
            "code": status_code
        }
    return jsonify(result), status_code

# # 删
# @user.route('/delete_us_data/<id>', methods=['DELETE'])
# def delete_us_data(id):
#     user = OmindUser.query.get(int(id))  # 通过 id 查询
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
#     user = OmindUser.query.get(int(id))
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
#     us_data = OmindUser.query.get(us_id)
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
