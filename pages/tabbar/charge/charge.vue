<template>
  <view class="wrapper">
	charging
  </view>
</template>
<script>
import config from '@/config/config'
import * as API_Station from "@/api/station";
import { wxGeocoder } from "@/api/common";
import { mpScan } from "@/utils/tools.js";
import { getOrderList } from "@/api/order";
// const citySelector = requirePlugin('citySelector');

export default {
  onHide() {
    this.isHide = true;
  },
  data() {
    return {
      config,
      cityList: [
        {
          label: "上海市",
          value: { latitude: 31.230525, longitude: 121.473667 },
        },
        {
          label: "北京市",
          value: { latitude: 39.905023, longitude: 116.384502 },
        },
      ],
      id: 0, // 使用 marker点击事件 需要填写id
      title: 'map',
      userLocation: {},
      stationList: [],
      currentPosition: {},
      showCurrent: true,
      connectorId: null,
      showChargingBtn: false,
      isHide: false,
      theme: "",
      scrollTop: 0, // 列表的滚动位置
      topWrapperBackground: 'red', // top-wrapper的背景色
    };
  },
  async onLoad() {
    this.userLocation = this.mapStartLocation
  },
  onShow() {
    this.updateChargingBtn()
    this.isHide = false;
    this.shouldGetCenterLanLat = false;
    this.getCenterLanLat()
  },
  onReady() {
    // 检查深浅模式，确定地图样式
    let _this = this
  },
  mounted() {
    // #ifdef MP-WEIXIN
    uni.showShareMenu({
      withShareTicket: true
    });
    // #endif
  },
  methods: {
    handleClick(item) {
      if (item.stationStatus == 50) {
        uni.navigateTo({
          url: `/pages/station/index?id=${item.stationId}&d=${item.distance}`,
        });
      } else {
        uni.showToast({
          title: "站点未开放",
          duration: 2000,
          icon: "none",
        });
      }
    },
  },
};
</script>

<style lang="scss">
page {
  background-color: #f7f7f7;
}
/* DarkMode 下的样式 start */
@media (prefers-color-scheme: dark) {
  page {
    background-color: #121425;
  }
}
</style>