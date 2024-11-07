/**
 * 交易相关API
 */
import { http, Method } from "@/utils/request.js";
import { encodeURL } from "@/api/common";
import api from "../config/api";

/**
 * 获取充电站列表
 * @param 
 */
export function getStations(params) {
  let path = "/mp/v1/geo/geoStationList";
  const url = encodeURL(path, params);
  return http.request({
    url: url,
    method: "get",
  });
}

/**
 * 获取充电站详情
 * @param stationId 充电站id
 */
export function getStation(stationId) {
  return http.request({
    url: '/mp/v1/station/' + stationId,
    method: Method.GET,
  });
}

/**
 * 获取充电接口详情
 * @param connectorId 充电接口id
 */
export function getConnector(params) {
  return http.request({
    url: '/mp/v1/charge/order/prepareOrderInfo',
    method: Method.GET,
    params: params,
  });
}
