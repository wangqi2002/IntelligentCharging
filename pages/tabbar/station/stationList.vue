<template>
	<view class="wrapper">
		<u-select v-model="selectCityVisible" :list="cityList" @confirm="citySelectConfirm"></u-select>
		<view
			class="title-wrapper"
			:style="{
				backgroundColor: theme === 'dark' ? '#222336' : '#fff',
				boxShadow: theme === 'dark' ? '0px 0px 1px 1px rgba(161, 161, 161, 0.25)' : '0px 0px 1px 1px rgba(232, 232, 232, 0.5)'
			}"
		>
			<view class="title">智能充电机器人</view>
		</view>
		<view class="top-wrapper">
			<view class="action-bar">
				<view class="button city" @click="selectCityVisible = true">
					{{ selectedCity.city || selectedCity.nation }}
				</view>
				<!-- 搜索框 -->
				<view class="search-bar">
					<view class="search-bar-box">
						<image class="search-span" src="/static/img/search.png" />
						<input type="text" value="" placeholder="请输入搜索内容" class="search-text" maxlength="10" focus />
						<button class="search-btn">搜索</button>
					</view>
				</view>
			</view>
		</view>
		<view class="swiper-wrap">
			<u-swiper
				:list="advertisingMap"
				duration="1000"
				interval="5000"
				:circular="true"
				:effect3d="true"
				img-mode="aspectFit"
				height="300"
				border-radius="40"
				bg-color="#D7DEEB"
			></u-swiper>
		</view>
		<view class="func-wrap">
			<view v-for="(func, findex) in funcList" :key="findex" class="func-card">
				<img class="func-img" :src="func.iconPath" />
				<view class="func-name">{{ func.text }}</view>
			</view>
		</view>
		<u-sticky :offset-top="offsetVal">
			<view class="filter-wrap">
				<view class="sort" v-for="(item, sindex) in menuData.sort" :key="sindex" @click="handleSort(item)">
					<view class="name">{{ item.text }}</view>
					<img class="icon" :src="item.isChanged ? (item.isUp ? item.iconPathUp : item.iconPathDown) : item.iconPath" alt="" />
				</view>
				<view class="sort filter" @click="handleFilter(menuData.filter)">
					<view class="name">{{ menuData.filter.text }}</view>
					<img class="icon" :src="menuData.filter.isChanged ? menuData.filter.selectedIconPath : menuData.filter.iconPath" alt="" />
				</view>
			</view>
		</u-sticky>
		<!-- 列表 -->
		<scroll-view scroll-y class="list">
			<view v-for="(station, cindex) in stationList" :key="cindex" class="station-card" @click="handleClick(station)">
				<view class="title">
					<view class="name">{{ station.info.stationName }}</view>
					<view class="tag">
						<img src="/static/map/location.png" alt />
						{{ station.userDistance + 'km' }}
					</view>
					<view class="tag nearest" v-if="station.nearest">最近</view>
				</view>
				<view class="address">
					{{ station.info.address }}
				</view>
				<view class="tags">
					<view v-for="(t, index) in station.tagList" :key="index" class="tag" style="margin: 10rpx 10rpx 0 0">{{ t.tagName }}</view>
				</view>
				<view class="bottom">
					<view class="left coupon-tag" style="position: relative">
						<text class="price">{{ station.currentPrice }}</text>
						<text class="unit">元/度</text>
					</view>
					<view class="right">
						<view class="label fast" v-if="station.totalFastGun > 0">空闲 {{ station.freeFastGun }}/{{ station.totalFastGun }}</view>
						<view class="label slow" v-if="station.totalGun - station.totalFastGun > 0">
							空闲
							{{ station.freeGun - station.freeFastGun }}/{{ station.totalGun - station.totalFastGun }}
						</view>
					</view>
				</view>
			</view>
			<u-empty v-if="stationList.length == 0" text=" " margin-top="100"></u-empty>
			<view style="height: 160rpx; text-align: center; padding-top: 10rpx"></view>
		</scroll-view>
	</view>
</template>
<script>
import menuData from '@/config/menuData.js';
import { stationP } from '@/config/virtualData.js';
import config from '@/config/config';
import * as API_Station from '@/api/station';
import { wxGeocoder } from '@/api/common';
import { getOrderList } from '@/api/order';
// const citySelector = requirePlugin('citySelector');

export default {
	data() {
		return {
			config,
			cityList: [...stationP.cities],
			selectCityVisible: false,
			selectedCity: {
				city: '',
				nation: ''
			},
			background: {
				backgroundColor: 'transparent'
			},
			id: 0, // 使用 marker点击事件 需要填写id
			title: 'map',
			mapLayerStyle: 1,
			mapStartLocation: {
				lat: 39.909,
				lon: 116.39742
			},
			mapCenterLocation: {
				lat: 39.909,
				lon: 116.39742
			},
			userLocation: {},
			stationList: [],
			currentPosition: {},
			showCurrent: true,
			lightColor: this.$lightColor,
			// 站点栏右侧滑动按钮
			options: [
				{
					text: '删除',
					style: {
						backgroundColor: this.$lightColor //高亮颜色
					}
				}
			],
			theme: '',
			scrollTop: 0, // 列表的滚动位置
			topWrapperBackground: 'red', // top-wrapper的背景色
			advertisingMap: [...stationP.swiperlist],
			funcList: [...stationP.funcList],
			menuData: {
				...menuData
			},
			offsetVal: 95
		};
	},
	async onLoad() {
		this.userLocation = this.mapStartLocation;
	},
	// 从城市选择器插件返回后，在页面的onShow生命周期函数中能够调用插件接口，获取cityInfo结果对象
	onShow() {
		this.getCenterLanLat();

		// this.getStationList();
		if (uni.getSystemInfoSync().platform == 'devtools') {
			this.getStationList();
		}
	},
	// onUnload() {
	//   // 页面卸载时清空插件数据，防止再次进入页面，getCity返回的是上次的结果
	//   citySelector.clearCity();
	// },
	onReady() {
		// 检查深浅模式，确定地图样式
		let _this = this;
		uni.getSystemInfo({
			success: function (res) {
				console.log('getSystemInfo:', res);
				_this.theme = res.hostTheme || 'light';
				_this.mapLayerStyle = _this.theme === 'dark' ? 2 : 1;
			}
		});
	},
	mounted() {
		// #ifdef MP-WEIXIN
		this.offsetVal = 210;
		uni.showShareMenu({
			withShareTicket: true
		});
		// #endif
	},
	methods: {
		confirm() {
			console.log('hello,is me');
		},

		/**
		 * 获取站点数据
		 */
		async getStationList() {
			let _this = this;
			uni.showLoading({
				title: '加载中'
			});

			let userLocation = {
				userLat: this.userLocation.lat,
				userLon: this.userLocation.lon
			};
			let query = Object.assign({}, userLocation, this.mapCenterLocation, {
				isDetail: 1
			});

			//处理搜索半径
			if (query.keywd == null || query.keywd == '') {
				delete query.keywd;
				query.radius = 100;
			} else {
				//关键字不为空时，半径为零
				query.radius = 0;
			}
			let response = await API_Station.getStations(query);
			if (true) {
				// if (response && response.data && response.data.code === 200) {
				uni.stopPullDownRefresh();
				_this.stationList = stationP.stations; //测试数据

				// _this.stationList = response.data.data;
				// 计算站点与用户位置的距离
				_this.calUserDistance();

				_this.stationList.forEach((station, index) => {
					// 将站点放入marker数组
					let labelContent = `￥${station.currentPrice}\n`;
					labelContent += station.totalFastGun > 0 ? `快${station.freeFastGun}/${station.totalFastGun} ` : ' ';
					labelContent += station.totalGun - station.totalFastGun > 0 ? `慢${station.freeGun - station.freeFastGun}/${station.totalGun - station.totalFastGun}` : '';
					station.latitude = Number(Number(station.lat).toFixed(5));
					station.longitude = Number(Number(station.lon).toFixed(5));
					station.labelContent = labelContent;
				});
			}
			uni.hideLoading();
		},
		onListScroll(e) {
			this.scrollTop = e.detail.scrollTop; // 更新滚动位置
			if (this.scrollTop > 100) {
				this.topWrapperBackground = '#ffffff'; // 当滚动位置超过100时，修改top-wrapper的背景为红色
			} else {
				this.topWrapperBackground = 'transparent'; // 否则将top-wrapper的背景设置为透明
			}
		},
		calUserDistance() {
			this.stationList.forEach((p, i) => {
				const lon = Number(p.lon);
				const lat = Number(p.lat);
				// this.$set(p, 'userDistance', Number(p.userDistance).toFixed(2))
				let userDistance = Math.round(this.$options.filters.calcDistance(this.userLocation.lon, this.userLocation.lat, lon, lat) / 100) / 10;
				this.$set(p, 'userDistance', userDistance);
			});
			// 按用户距离排序
			this.$options.filters.arraySort(this.stationList, 'userDistance');
			// 将第一个地点标为最近
			if (this.stationList.length > 0) {
				this.stationList[0].nearest = true;
			}
		},
		// 获取用户当前位置
		getUserLocation() {
			let _this = this;

			_this.userLocation.lat = stationP.mapStartLocation.lat; //测试数据
			_this.userLocation.lon = stationP.mapStartLocation.lon;
			_this.calUserDistance();
			_this.mapStartLocation = Object.assign(_this.userLocation, {});

			/* uni.getLocation({
					type: 'gcj02', // 默认为 wgs84 返回 gps 坐标，gcj02 返回可用于 wx.openLocation 的坐标
					success: (res) => {
						//赋值经纬度
						_this.$set(_this.userLocation, 'lat', parseFloat(res.latitude))
						_this.$set(_this.userLocation, 'lon', parseFloat(res.longitude))
						_this.calUserDistance()
						_this.mapStartLocation = Object.assign(_this.userLocation, {})
					},
					fail: function(res) {
						console.log(res)
					},
				})*/
		},
		async getCenterLanLat() {
			let _this = this;

			_this.userLocation.lat = stationP.mapCenterLocation.lat; //测试数据
			_this.userLocation.lon = stationP.mapCenterLocation.lon;
			_this.mapCenterLocation = stationP.mapCenterLocation;
			_this.selectedCity = stationP.selectedCity;
			await _this.getStationList();

			/* uni.getLocation({
					success: function(res) {
						const lat = parseFloat(res.latitude)
						const lon = parseFloat(res.longitude)
						_this.userLocation.lat = lat
						_this.userLocation.lon = lon
						_this.mapCenterLocation.lat = lat
						_this.mapCenterLocation.lon = lon

						// 逆解析获取当前城市
						wxGeocoder(`${lat},${lon}`).then(res => {
							if (res.data.result) {
								_this.selectedCity = res.data.result.address_component
							}
						})
						_this.getStationList()
					},

					fail: function(res) {
						console.log(res)
					}

				}) */
		},
		handleSort(item) {
			if (item.isChanged == false && item.isUp == false) {
				item.isChanged = true;
				item.isUp = false;
				return;
			} else if (item.isChanged == true && item.isUp == false) {
				item.isChanged = true;
				item.isUp = true;
				return;
			} else if (item.isChanged == true && item.isUp == true) {
				item.isChanged = false;
				item.isUp = false;
				return;
			}
		},
		handleFilter(item) {
			item.isChanged = !item.isChanged;
		},
		handleClick(item) {
			if (item.stationStatus == 50) {
				// uni.navigateTo({
				//   url: `/pages/station/index?id=${item.stationId}&d=${item.distance}`,
				// });
				uni.navigateTo({
					url: `/pages/station/index?id=100&d=5`
				});
			} else {
				uni.showToast({
					title: '站点未开放',
					duration: 2000,
					icon: 'none'
				});
			}
		},
		/**
		 * 跳转
		 */
		navigateTo(url) {
			uni.navigateTo({
				url
			});
		},
		citySelectConfirm(e) {
			let _this = this;
			let location = e[0].value;
			let cityName = e[0].label;
			this.$set(this.mapCenterLocation, 'lat', location.latitude);
			this.$set(this.mapCenterLocation, 'lon', location.longitude);
			this.selectedCity = {
				city: cityName
			};
			this.getStationList();
		}
	}
};
</script>

<style scoped lang="scss">
@import './stationList.scss';
</style>

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
