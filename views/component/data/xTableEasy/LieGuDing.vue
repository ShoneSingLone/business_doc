<template>
	<div class="card-LieGuDing">
		<xMd :md="mdTips" />
		<h4>固定左侧列</h4>
		<xTableEasy
			:columns="columns"
			:table-data="tableData"
			:max-height="300"
			:scroll-width="1000"
			border-x
			border-y />
		<h4>固定右侧列</h4>
		<xTableEasy
			:columns="columns2"
			:table-data="tableData"
			:max-height="300"
			:scroll-width="1000"
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
- 1、通过配置列的 fixed 属性，可以实现列的固定功能。
- 2、支持固定左侧列（fixed: "left"）和固定右侧列（fixed: "right"）。
- 3、固定列在水平滚动时保持可见。
`,
				tableData: [
					{
						id: 1,
						name: "张三",
						age: 18,
						sex: "男",
						phone: "13800000001",
						email: "zhangsan@example.com",
						address: "上海市普陀区金沙江路 1518 弄",
						status: 1
					},
					{
						id: 2,
						name: "李四",
						age: 20,
						sex: "女",
						phone: "13800000002",
						email: "lisi@example.com",
						address: "上海市浦东新区张江高科技园区",
						status: 2
					}
				],
				columns: [
					{
						field: "id",
						key: "id",
						title: "ID",
						width: 80,
						align: "center",
						fixed: "left"
					},
					{
						field: "name",
						key: "name",
						title: "姓名",
						width: 120,
						align: "left",
						fixed: "left"
					},
					{ field: "age", key: "age", title: "年龄", width: 80, align: "center" },
					{ field: "sex", key: "sex", title: "性别", width: 80, align: "center" },
					{ field: "phone", key: "phone", title: "电话号码", width: 150, align: "left" },
					{ field: "email", key: "email", title: "邮箱", width: 200, align: "left" },
					{ field: "address", key: "address", title: "地址", width: 300, align: "left" },
					{ field: "status", key: "status", title: "状态", width: 100, align: "center" }
				],
				columns2: [
					{ field: "id", key: "id", title: "ID", width: 80, align: "center" },
					{ field: "name", key: "name", title: "姓名", width: 120, align: "left" },
					{ field: "age", key: "age", title: "年龄", width: 80, align: "center" },
					{ field: "sex", key: "sex", title: "性别", width: 80, align: "center" },
					{ field: "phone", key: "phone", title: "电话号码", width: 150, align: "left" },
					{ field: "email", key: "email", title: "邮箱", width: 200, align: "left" },
					{ field: "address", key: "address", title: "地址", width: 300, align: "left" },
					{
						field: "status",
						key: "status",
						title: "状态",
						width: 100,
						align: "center",
						fixed: "right"
					}
				]
			};
		}
	});
}
</script>
<style lang="less">
.card-LieGuDing {
	h4 {
		margin: 15px 0 10px 0;
		font-size: 14px;
		font-weight: 500;
	}
}
</style>
