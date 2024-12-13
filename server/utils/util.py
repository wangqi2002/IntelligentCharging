import random

moveTup = ({"axis": "x", "step": "5", "isPositive": True}, {"axis": "x", "step": "5", "isPositive": False},
           {"axis": "y", "step": "5", "isPositive": True}, {"axis": "y", "step": "5", "isPositive": False},
           {"axis": "z", "step": "5", "isPositive": True}, {"axis": "z", "step": "5", "isPositive": False},
           {"axis": "rotate", "step": "10", "isPositive": True}, {"axis": "xrotate", "step": "10", "isPositive": False})


# python随机生成包含字母数字的六位验证码
def v_code():
    ret = ""
    for i in range(6):
        num = random.randint(0, 9)
        # num = chr(random.randint(48,57))#ASCII表示数字
        letter = chr(random.randint(97, 122))  # 取小写字母
        Letter = chr(random.randint(65, 90))  # 取大写字母
        s = str(random.choice([num, letter, Letter]))
        ret += s
    return ret


def back_list(obj):
    list = []
    for item in obj:
        list.append(item.to_json())
    return list
