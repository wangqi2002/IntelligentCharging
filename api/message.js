/**
 * 站内消息相关API
 */

import {http,Method} from '@/utils/request.js';
const request = http.request

/**
 * 获取微信消息订阅
 * @param params
 * @returns {AxiosPromise}
 */
export function getWeChatMpMessage() { 
  return http.request({
    url: 'passport/connect/miniProgram/subscribeMessage',
    method: Method.GET
  });
}

/**
 * 获取消息列表
 * @param params
 * @returns {AxiosPromise}
 */
export function getMessages(params) {
  params = params || {};
  params.pageSize = params.pageSize || 5;
  return http.request({
    url: 'members/member-nocice-logs',
    method: Method.GET,
    needToken: true,
    params,
  });
}


/**
 * 标记消息为已读
 * @param ids
 */
export function messageMarkAsRead(ids) {
  return http.request({
    url: `members/member-nocice-logs/${ids}/read`,
    method: Method.PUT,
    needToken: true,
  });
}

//读取站内消息
export function editMessages(message_id,params){
  return http.request({
    url:`/message/member/${message_id}`,
    method:Method.PUT,
    needToken:true,
    params
  })
}
//获取站内消息
export function messages(params) {
  return http.request({
    url: "/message/member",
    method: Method.GET,
    needToken: true,
    params,
  });
}

/**
 * @param appType
 * @returns {AxiosPromise}
 * 
 */	
 export function getAppVersion(appType) {
  return http.request({
    url: `/other/appVersion/${appType}`,
    method: Method.GET,
    type:"manager"
  });
}