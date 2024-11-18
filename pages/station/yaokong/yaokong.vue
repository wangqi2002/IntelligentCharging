<template>
	<view class="wrapper">
		<view class="title-wrapper">
			<view class="title">遥控</view>
		</view>
		<view class="video-wrapper">
			<video class="video-card" src="/static/video.mp4"></video>
		</view>
		<view class="control-wrapper">
			<view class="control-btn control-top"></view>
			<view class="control-btn control-left"></view>
			<view class="control-btn control-bottom"></view>
			<view class="control-btn control-right"></view>
			<view class="control-round" style="background-color: #ffffff">
				<view class="control-round-up control-btn"></view>
				<view class="control-round-down control-btn"></view>
			</view>
			<view class="control-rotate">
				<view class="control-rotate-left control-rotate-btn">
					<img class="rotate-icon" src="/static/index/rotate-left.png" />
				</view>
				<view class="control-rotate-right control-rotate-btn">
					<img class="rotate-icon" src="/static/index/rotate-right.png" />
				</view>
			</view>
		</view>
		<view class="options-wrapper">
			<button class="guiwei option-btn">机器人归位</button>
			<button class="confirm option-btn">确认充电</button>
		</view>
	</view>
</template>
<script>
	import menuData from '@/config/menuData.js';

	export default {
		data() {
			return {};
		},
		async onLoad() {},
		onShow() {},
		onReady() {},
		mounted() {},
		methods: {}
	};
</script>

<style lang="scss">
	page {
		background-color: #f7f7f7;
	}

	.title-wrapper {
		position: fixed;
		top: 0;
		padding-top: calc(var(--status-bar-height) + 50rpx);
		height: calc(var(--status-bar-height) + 110rpx);
		width: 100%;
		z-index: 2;

		.title {
			font-family: 'Helvetica Neue', Helvetica, Arial, 'PingFang SC', 'Hiragino Sans GB', 'Heiti SC', 'Microsoft YaHei', 'WenQuanYi Micro Hei', sans-serif;
			font-size: $font-lg;
			text-align: center;
		}
	}

	.video-wrapper {
		width: 100%;
		padding: calc(110rpx + var(--status-bar-height)) 0 0;

		.video-card {
			width: 100%;
		}
	}

	.control-wrapper {
		cursor: pointer;
		position: relative;
		width: 550rpx;
		height: 550rpx;
		max-width: 600rpx;
		max-height: 600rpx;
		min-width: 300rpx;
		min-height: 300rpx;
		margin: 0 auto;
		border-radius: 50%;

		.control-btn {
			position: absolute;
			width: 38%;
			height: 38%;
			display: flex;
			align-items: center;
			justify-content: center;
			// border: 5rpx solid #78aee4;
			box-sizing: border-box;
			background-color: #78aee4;
			transition: all 0.3s linear;
		}

		.control-btn:active {
			color: black;
			background: #63a300;
		}

		.control-btn:after {
			content: '';
			position: absolute;
			width: 60%;
			height: 60%;
			z-index: 2;
		}

		.control-btn:before {
			content: '';
			position: relative;
			display: block;
			width: 30rpx;
			height: 30rpx;
			border-top: 10rpx solid #fff;
			border-right: 10rpx solid #fff;
			border-radius: 0 4rpx 0 0;
			box-sizing: border-box;
			z-index: 3;
		}

		.control-top {
			top: 0;
			left: 50%;
			transform: translateX(-50%) rotate(-45deg);
			border-radius: 4rpx 100% 4rpx 4rpx;
		}

		.control-top:before {
			transform: translate(30%, -25%);
		}

		.control-top:after {
			left: 0;
			bottom: 0;
			border-radius: 0 100% 0 0;
		}

		.control-bottom {
			left: 50%;
			bottom: 0;
			transform: translateX(-50%) rotate(45deg);
			border-radius: 4rpx 4rpx 100% 4rpx;
		}

		.control-bottom:before {
			transform: translate(25%, 25%) rotate(90deg);
		}

		.control-bottom:after {
			top: 0;
			left: 0;
			border-radius: 0 0 100% 0;
		}

		.control-left {
			top: 50%;
			left: 0;
			transform: translateY(-50%) rotate(45deg);
			border-radius: 4rpx 4rpx 4rpx 100%;
		}

		.control-left:before {
			transform: translate(-25%, 30%) rotate(180deg);
		}

		.control-left:after {
			right: 0;
			top: 0;
			border-radius: 0 0 0 100%;
		}

		.control-right {
			top: 50%;
			right: 0;
			transform: translateY(-50%) rotate(45deg);
			border-radius: 4rpx 100% 4rpx 4rpx;
		}

		.control-right:before {
			transform: translate(30%, -25%);
		}

		.control-right:after {
			left: 0;
			bottom: 0;
			border-radius: 0 100% 0 0;
		}

		.control-round {
			position: absolute;
			top: 50%;
			left: 50%;
			transform: translate(-50%, -50%);
			width: 280rpx;
			height: 280rpx;
			background: #fff;
			border-radius: 50%;

			.control-round-up {
				position: absolute;
				top: 35%;
				left: 50%;
				transform: translate(-50%, -50%);
				display: flex;
				justify-content: center;
				align-items: center;
				width: 140rpx;
				height: 70rpx;
				// border: 5rpx solid #fff;
				border-radius: 140rpx 140rpx 0 0;
			}

			.control-round-up:active {
				color: black;
				background: yellow;
			}

			.control-round-up:before {
				transform: translate(0, 50%) rotate(-45deg);
			}

			.control-round-down {
				position: absolute;
				top: 65%;
				left: 50%;
				transform: translate(-50%, -50%);
				display: flex;
				justify-content: center;
				align-items: center;
				width: 140rpx;
				height: 70rpx;
				border-radius: 0 0 140rpx 140rpx;
			}

			.control-round-down:active {
				color: black;
				background: yellow;
			}

			.control-round-down:before {
				transform: translate(0, -50%) rotate(135deg);
			}
		}

		.control-rotate {
			width: 100%;
			height: 160rpx;
			position: absolute;
			top: 90%;
			display: flex;
			justify-content: space-between;

			.control-rotate-btn {
				position: absolute;
				width: 160rpx;
				height: 160rpx;
				display: flex;
				align-items: center;
				justify-content: center;
				box-sizing: border-box;
				background-color: #78aee4;
				transition: all 0.3s linear;
				border-radius: 100%;

				.rotate-icon {
					width: 30%;
					height: 30%;
					position: absolute;
					top: 50%;
					left: 50%;
					transform: translate(-50%, -50%);
				}
			}

			.control-rotate-btn:active {
				color: black;
				background: #63a300;
			}

			.control-rotate-left {
				position: absolute;
				left: 0;
			}

			.control-rotate-right {
				position: absolute;
				right: 0;
			}
		}
	}

	.options-wrapper {
		width: 100%;
		height: 100rpx;
		position: absolute;
		bottom: 100rpx;
		display: flex;

		.option-btn {
			width: 250rpx;
			height: 100rpx;
			background-color: #78aee4;
			color: #fff;
			line-height: 110rpx;
			font-size: $font-sl;
		}
	}

	/* DarkMode 下的样式 start */
	@media (prefers-color-scheme: dark) {
		page {
			background-color: #121425;
		}
	}
</style>