const sortMenu = [{
	text: "综合",
	iconPath: "/static/img/sort0.png",
	iconPathUp: "/static/img/sort1.png",
	iconPathDown: "/static/img/sort2.png",
	isChanged:false,
	isUp:false
}, {
	text: "距离",
	iconPath: "/static/img/sort0.png",
	iconPathUp: "/static/img/sort1.png",
	iconPathDown: "/static/img/sort2.png",
	isChanged:false,
	isUp:false
}, {
	text: "价格",
	iconPath: "/static/img/sort0.png",
	iconPathUp: "/static/img/sort1.png",
	iconPathDown: "/static/img/sort2.png",
	isChanged:false,
	isUp:false
}];
const filterMenu = {
	text: "筛选",
	iconPath: "/static/index/arrow-down-1.png",
	selectedIconPath: "/static/index/arrow-up.png",
	isChanged:false,
};
let menuData = {
	sort: sortMenu,
	filter: filterMenu
}
export default menuData;