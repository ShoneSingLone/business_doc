<template>
	<div class="card-LieKuanSheZhi">
		<xMd :md="mdTips" />
		<h4>像素宽度</h4>
		<xTableEasy :columns="columnsPx" :table-data="tableData" border-x border-y />
		<h4>百分比宽度</h4>
		<xTableEasy :columns="columnsPercent" :table-data="tableData" :max-height="300" border-x border-y />
		<h4>不设置宽度（自动分配）</h4>
		<xTableEasy :columns="columnsAuto" :table-data="tableData" border-x border-y />
	</div>
</template>
<script lang="ts">
export default async function () {
	return defineComponent({
		data() {
			return {
				mdTips: `
- 1、通过配置列的 width 属性，可以设置列的宽度。
- 2、支持像素值、百分比和不设置（自动分配）三种方式。
- 3、合理设置列宽可以优化表格的显示效果。
`,
				tableData: [
					{ id: 1, name: "张三", age: 18, sex: "男", phone: "13800000001", address: "上海市普陀区金沙江路 1518 弄" },
					{ id: 2, name: "李四", age: 20, sex: "女", phone: "13800000002", address: "上海市浦东新区张江高科技园区" }
				],
				columnsPx: [
					{ field: "id", key: "id", title: "ID", width: 80, align: "center" },
					{ field: "name", key: "name", title: "姓名", width: 120, align: "left" },
					{ field: "age", key: "age", title: "年龄", width: 80, align: "center" },
					{ field: "sex", key: "sex", title: "性别", width: 80, align: "center" },
					{ field: "phone", key: "phone", title: "电话号码", width: 150, align: "left" },
					{ field: "address", key: "address", title: "地址", width: 250, align: "left" }
				],
				columnsPercent: [
					{ field: "id", key: "id", title: "ID", width: "10%", align: "center" },
					{ field: "name", key: "name", title: "姓名", width: "15%", align: "left" },
					{ field: "age", key: "age", title: "年龄", width: "10%", align: "center" },
					{ field: "sex", key: "sex", title: "性别", width: "10%", align: "center" },
					{ field: "phone", key: "phone", title: "电话号码", width: "20%", align: "left" },
					{ field: "address", key: "address", title: "地址", width: "35%", align: "left" }
				],
				columnsAuto: [
					{ field: "id", key: "id", title: "ID", align: "center" },
					{ field: "name", key: "name", title: "姓名", align: "left" },
					{ field: "age", key: "age", title: "年龄", align: "center" },
					{ field: "sex", key: "sex", title: "性别", align: "center" },
					{ field: "phone", key: "phone", title: "电话号码", align: "left" },
					{ field: "address", key: "address", title: "地址", align: "left" }
				]
			};
		}
	});
}
</script>
<style lang="less">
.card-LieKuanSheZhi {
	h4 {
		margin: 15px 0 10px 0;
		font-size: 14px;
		font-weight: 500;
	}
}
</style>