/**
 * 通信相关API
 */

import {
	http,
	Method
} from "@/utils/request.js";

/**
 * 通信连接
 * @param params
 */
export function conConnect(params) {
	return http.request({
		url: "/api/app/communication/connect",
		method: Method.GET,
		needToken: true,
		params,
	});
}

/**
 * 连接检测
 * @param orderSn 
 */
export function conKeeping(orderSn) {
	return http.request({
		url: `/api/app/communication/keeping`,
		method: Method.GET,
		needToken: true,
		params: {
			startChargeSeq: orderSn
		},
	});
}

/**
 * 运动控制
 * @param data 
 */
export function conControl(data) {
	return http.request({
		url: `/api/app/communication/control`,
		method: Method.POST,
		needToken: true,
		data,
	});
}

/**
 * 归位操作
 * @param data 
 */
export function conHome(data) {
	return http.request({
		url: `/api/app/communication/home`,
		method: Method.POST,
		needToken: true,
		data,
	});
}

/**
 * 目标运动
 * @param data 
 */
export function conAuto(data) {
	return http.request({
		url: `/api/app/communication/auto`,
		method: Method.POST,
		needToken: true,
		data,
	});
}