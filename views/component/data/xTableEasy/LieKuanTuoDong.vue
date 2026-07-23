<template>
	<div class="card-LieKuanTuoDong">
		<xMd :md="mdTips" />
		<xTableEasy
			:columns="columns"
			:table-data="tableData"
			:max-height="300"
			border-x
			border-y />
	</div>
</template>
<script lang="ts">
export default async function () {
	return defineComponent({
		data() {
			return {
				mdTips: `
- 1、通过拖动列之间的分隔线，可以调整列的宽度。
- 2、拖动时会显示实时的宽度变化。
- 3、调整后的列宽会自动适配表格布局。
`,
				tableData: [
					{
						id: 1,
						name: "张三",
						age: 18,
						sex: "男",
						phone: "13800000001",
						address: "上海市普陀区金沙江路 1518 弄"
					},
					{
						id: 2,
						name: "李四",
						age: 20,
						sex: "女",
						phone: "13800000002",
						address: "上海市浦东新区张江高科技园区"
					}
				],
				columns: [
					{ field: "id", key: "id", title: "ID", width: 80, align: "center" },
					{ field: "name", key: "name", title: "姓名", width: 120, align: "left" },
					{ field: "age", key: "age", title: "年龄", width: 80, align: "center" },
					{ field: "sex", key: "sex", title: "性别", width: 80, align: "center" },
					{ field: "phone", key: "phone", title: "电话号码", width: 150, align: "left" },
					{ field: "address", key: "address", title: "地址", width: 250, align: "left" }
				]
			};
		}
	});
}
</script>
<style lang="less">
.card-LieKuanTuoDong {
}
</style>
