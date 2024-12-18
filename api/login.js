import {
	http
} from "@/utils/request.js";

import api from "@/config/api.js";

/**
 * 通过短信重置密码
 * @param  mobile
 */
export function resetByMobile(params) {
	return http.request({
		url: `/api/app/user/resetByMobile`,
		method: "POST",
		params,
	});
}

/**
 * 账号密码登陆
 * @params  password
 * @params  username
 */
export function userLogin(params) {
	return http.request({
		method: "POST",
		url: `/api/app/user/accountLogin`,
		data: params,
		header: {
			"content-type": "application/json",
		},
	})
}


/**
 * 发送验证码
 * @param  mobile
 */
export function sendMobile(params) {
	return http.request({
		url: `/api/app/user/sendCode`,
		method: "GET",
		data: params,
		header: {
			"content-type": "application/json",
		},
	});
}

/**
 * 短信登录
 * @param  mobile
 * @param  smsCode
 */
export function smsLogin(params, clientType) {
	return http.request({
		url: `/api/app/user/smsLogin`,
		method: "POST",
		data: params,
		header: {
			"content-type": "application/json",
			clientType: clientType,
		},
	});
}

/**
 * 修改密码
 * @param  newPassword
 * @param  password
 */

export function modifyPass(params) {
	return http.request({
		url: `/api/app/user/modifyPass`,
		method: "PUT",
		params,
	});
}

/**
 * 刷新token
 */
export function refreshTokenFn(refresh_token) {
	return http.request({
		url: `/api/app/user/refresh/${refresh_token}`,
		method: "GET",
	});
}

// 获取密码状态
export function logout() {
	return http.request({
		url: '/api/app/user/logout',
		method: "POST",
		needToken: true,
	})
}