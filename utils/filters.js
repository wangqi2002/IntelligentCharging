import Foundation from "./Foundation.js";
import storage from "@/utils/storage.js";
import { getUserInfo } from "@/api/members";
import Vue from "vue";
/**
 * 金钱单位置换  2999 --> 2,999.00
 * @param val
 * @param unit
 * @param location
 * @returns {*}
 */
export function unitPrice(val, unit, location) {
  if (!val) val = 0;
  val = Number(val)
  let price = Foundation.formatPrice(val);
  if (location === "before") {
    return price.substr(0, price.length - 3);
  }
  if (location === "after") {
    return price.substr(-2);
  }
  return (unit || "") + price;
}

export function getStringLength(str) {
  if(str == null) return 0;
  let emoji_exp = /(\u00a9|\u00ae|[\u2000-\u3300]|\ud83c[\ud000-\udfff]|\ud83d[\ud000-\udfff]|\ud83e[\ud000-\udfff])/g;
  const ms = [...str.matchAll(emoji_exp)];
  console.log(ms)
  if (!ms || !ms.length) return str.length;

  let emojiSize = 0;
  for (const m of ms) emojiSize += m.length - 1;
  return str.length - emojiSize;
};

/**
 * 格式化价格  1999 --> [1999,00]
 * @param {*} val
 * @returns
 */
export function stationFormatPrice(val) {
  if (typeof val == "undefined") {
    return val;
  }
  let valNum = new Number(val);
  return valNum.toFixed(2).split(".");
}

/**
 * 距离计算
 * @param {*} val
 * @returns
 */
export function calcDistance(lon1, lat1, lon2, lat2) {
  let PI = 3.14159265358979323; //圆周率
  let R = 6371229; //地球半径

  let x, y, distance;
  let lonres = lon1 > lon2 ? lon1 - lon2 : lon2 - lon1;
  let latres = lat1 > lat2 ? lat1 - lat2 : lat2 - lat1;
  x = (lonres * PI * R * Math.cos((((lat1 + lat2) / 2) * PI) / 180)) / 180;
  y = ((lat2 - lat1) * PI * R) / 180;
  distance = Math.hypot(x, y);

  return distance;
}

/**
 * 脱敏姓名
 */

export function noPassByName(str) {
  if (null != str && str != undefined) {
    if (str.length <= 3) {
      return "*" + str.substring(1, str.length);
    } else if (str.length > 3 && str.length <= 6) {
      return "**" + str.substring(2, str.length);
    } else if (str.length > 6) {
      return str.substring(0, 2) + "****" + str.substring(6, str.length);
    }
  } else {
    return "";
  }
}

/**
 * 处理日期，转换为可阅读时间格式
 * @param time
 * @param pattern
 * @returns {*|string}
 */
export function parseTime(time, pattern) {
  if (arguments.length === 0 || !time) {
    return null;
  }
  const format = pattern || "{y}-{m}-{d} {h}:{i}:{s}";
  let date;
  if (typeof time === "object") {
    date = time;
  } else {
    if (typeof time === "string" && /^[0-9]+$/.test(time)) {
      time = parseInt(time);
    } else if (typeof time === "string") {
      // @TODO: 不替换-，可能有问题，待测
      time = time.replace(new RegExp(/-/gm), '/')
    }
    if (typeof time === "number" && time.toString().length === 10) {
      time = time * 1000;
    }
    date = new Date(time);
  }
  const formatObj = {
    y: date.getFullYear(),
    m: date.getMonth() + 1,
    d: date.getDate(),
    h: date.getHours(),
    i: date.getMinutes(),
    s: date.getSeconds(),
    a: date.getDay(),
  };
  const time_str = format.replace(/{(y|m|d|h|i|s|a)+}/g, (result, key) => {
    let value = formatObj[key];
    // Note: getDay() returns 0 on Sunday
    if (key === "a") {
      return ["日", "一", "二", "三", "四", "五", "六"][value];
    }
    if (result.length > 0 && value < 10) {
      value = "0" + value;
    }
    return value || 0;
  });
  return time_str;
}

/**
 * 处理unix时间戳，转换为可阅读时间格式
 * @param unix
 * @param format
 * @returns {*|string}
 */
export function unixToDate(unix, format) {
  let _format = format || "yyyy-MM-dd hh:mm:ss";
  const d = new Date(unix * 1000);
  const o = {
    "M+": d.getMonth() + 1,
    "d+": d.getDate(),
    "h+": d.getHours(),
    "m+": d.getMinutes(),
    "s+": d.getSeconds(),
    "q+": Math.floor((d.getMonth() + 3) / 3),
    S: d.getMilliseconds(),
  };
  if (/(y+)/.test(_format))
    _format = _format.replace(
      RegExp.$1,
      (d.getFullYear() + "").substr(4 - RegExp.$1.length)
    );
  for (const k in o)
    if (new RegExp("(" + k + ")").test(_format))
      _format = _format.replace(
        RegExp.$1,
        RegExp.$1.length === 1 ? o[k] : ("00" + o[k]).substr(("" + o[k]).length)
      );
  return _format;
}

/**
 * 13888888888 -> 138****8888
 * @param mobile
 * @returns {*}
 */
export function secrecyMobile(mobile) {
  mobile = String(mobile);
  if (!/\d{11}/.test(mobile)) {
    return mobile;
  }
  return mobile.replace(/(\d{3})(\d{4})(\d{4})/, "$1****$3");
}

/**
 * 清除逗号
 *
 */
export function clearStrComma(str) {
  str = str.replace(/,/g, ""); //取消字符串中出现的所有逗号
  return str;
}

/**
 * 判断用户是否登录
 * @param val  如果为auth则判断是否登录
 * 如果传入 auth 则为判断是否登录
 */
export function isLogin(val) {
  let userInfo = storage.getUserInfo();
  if (val == "auth") {
    // return userInfo && userInfo.userId ? true : false;
    return userInfo && userInfo.mobile ? true : false;
  } else {
    return storage.getUserInfo();
  }
}

export function tipsToLogin() {
  if (!isLogin("auth")) {
    uni.showModal({
      title: "提示",
      content: "当前用户未登录是否登录？",
      confirmText: "确定",
      cancelText: "取消",
      confirmColor: Vue.prototype.$mainColor,
      success: (res) => {
        if (res.confirm) {
          navigateToLogin();
        } else if (res.cancel) {
          uni.navigateBack();
        }
      },
    });
    return false;
  }
  return true;
}

/**
 * 获取用户信息并重新添加到缓存里面
 */
export async function userInfo() {
  let res = await getUserInfo();
  if (res.data.success) {
    storage.setUserInfo(res.data.result);
    return res.data.result;
  }
}

/**
 * 验证是否登录如果没登录则去登录
 * @param {*} val
 * @returns
 */
export function forceLogin() {
  let userInfo = storage.getUserInfo();
  if (!userInfo || !userInfo.userId) {
    // #ifdef MP-WEIXIN || MP-ALIPAY

    uni.navigateTo({
      url: "/pages/passport/mpLogin",
    });

    // #endif

    // #ifndef MP-WEIXIN || MP-ALIPAY

    uni.navigateTo({
      url: "/pages/passport/login",
    });

    //  #endif
  }
}

/**
 * 获取当前加载的页面对象
 * @param val
 */
export function getPages(val) {
  const pages = getCurrentPages(); //获取加载的页面
  const currentPage = pages[pages.length - 1]; //获取当前页面的对象
  const url = currentPage.route; //当前页面url

  return val ? currentPage : url;
}

/**
 * 跳转到登录页面
 */
export function navigateToLogin(type = "navigateTo", showTip = false) {
  /**
   * 此处进行条件编译判断
   * 微信小程序跳转到微信小程序登录页面
   * H5/App跳转到普通登录页面
   */
  let option = "";
  showTip && (option += "?showTip=1");
  // #ifdef MP-WEIXIN || MP-ALIPAY
  uni[type]({
    url: `/pages/passport/mpLogin${option}`,
  });
  // #endif
  // #ifndef MP-WEIXIN || MP-ALIPAY
  uni[type]({
    url: `/pages/passport/login${option}`,
  });
  //  #endif
}

/**
 * 服务状态列表
 */
export function serviceStatusList(val) {
  let statusList = {
    APPLY: "申请售后",
    PASS: "通过售后",
    REFUSE: "拒绝售后",
    BUYER_RETURN: "买家退货，待卖家收货",
    SELLER_RE_DELIVERY: "商家换货/补发",
    SELLER_CONFIRM: "卖家确认收货",
    SELLER_TERMINATION: "卖家终止售后",
    BUYER_CONFIRM: "买家确认收货",
    BUYER_CANCEL: "买家取消售后",
    WAIT_REFUND: "等待平台退款",
    COMPLETE: "完成售后",
  };
  return statusList[val];
}

/**
 * 订单状态列表
 */
export function orderStatusList(val) {
  let orderStatusList = {
    UNDELIVERED: "待发货",
    UNPAID: "未付款",
    PAID: "已付款",
    DELIVERED: "已发货",
    CANCELLED: "已取消",
    COMPLETED: "已完成",
    COMPLETE: "已完成",
    TAKE: "待核验",
  };
  return orderStatusList[val];
}

/**
 * 对象数组按某一key排序
 * @param [] array
 * @returns
 */
export function arraySort(array, key) {
  array.sort(compare(key));
}

/**
 * 将null转成0
 */
export function transNull(num) {
  if(num == null) num = 0;
  return num;
}

function compare(key) {
  return function (value1, value2) {
    var val1 = value1[key];
    var val2 = value2[key];
    return val1 - val2;
  };
}

/**
 * 折扣率转换  80 --> 8  85-->8.5
 */
export function unitDiscount(val) {
  let result = val
  if (!result) result = 0;
  if(result % 10 === 0)
  result = result /10
  return result;
}
