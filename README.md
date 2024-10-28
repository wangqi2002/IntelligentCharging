## 智充

### 快速开始

#### 阅读文档

`uni-app` https://uniapp.dcloud.net.cn/api/

`vue2` https://v2.cn.vuejs.org/

`uView v1` https://v1.uviewui.com/

#### 环境

HBuilderX

### 技术栈

本项目技术栈为 `uni-app` + `scss` + `ES2015` + `uView` 提前学习和了解这些知识将帮助你更好地上手我们的项目。

### 目录结构

```
├── api  // 接口
├── components  // 组件
├── config  // 配置文件
├── pages  // 页面
├── static  // 静态资源
├── store  // vuex
├── utils  // 工具类
├── uview-ui  // uview
├── App.vue  // 入口页面
├── main.js  // 入口文件
├── manifest.json  // hbulider配置文件
├── pages.json  // 路由配置文件
├── uni.scss  // 全局样式
└── vue.config.js  // vue配置文件
```

### 运行

#### 运行在微信小程序

1.需要保证本地要有`微信开发者工具` https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html

2.在`hbulider`中点击`运行`->`运行到小程序模拟器`->`微信开发者工具` 运行的时候需要配置小程序的`appid`，配置完成后即可运行


### 项目配置/开发

#### config配置
在根目录`config`下的`config`设置中配置了一些默认的配置，可以根据自己的需求进行修改

```
const name = "奥升"; //全局商城name
const schemeName = "Orise"; //唤醒app需要的schemeName
export default {
  name: name,
  customerServiceMobile: "", //默认客服电话
  customerServiceEmail: "", //默认客服邮箱
  /**
   * 如需更换主题请修改此处以及uni.scss中的全局颜色
   */
  mainColor: "#ff3c2a", // 主题色
  lightColor: "#ff6b35", // 高亮主题色
  aiderLightColor: "#ff9f28", // 辅助高亮颜色
};

```
#### 组件
在根目录`components`下的`components`设置中配置了一些默认的组件，可以根据自己的需求进行修改

#### 页面
在`pages`文件夹写入或修改页面代码，在`pages.json`中去配置页面路由，具体配置可以参考`pages.json` 或参考uni-app的文档

在微信小程序中默认启用分包操作，如果需要在微信小程序中使用分包，需要在`pages.json`中配置分包路径，具体配置可以参考`pages.json` 或参考uni-app的文档

#### 主题
1.现在`config`中设置主题色

2.在`uni.scss`中设置全局颜色

3.替换项目中一些icon以及图片的颜色

