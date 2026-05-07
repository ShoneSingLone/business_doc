<template>
	<div class="card-JiChuYongFa">
		<xMd :md="mdTips" />
		<xTableEasy :columns="columns" :table-data="tableData" :max-height="400" border-x border-y />
	</div>
</template>
<script lang="ts">
export default async function () {
	return defineComponent({
		data() {
			return {
				mdTips: `
- 1、基础用法展示了 xTableEasy 的核心能力。
- 2、通过 columns 配置列信息，包括标题、宽度、对齐方式等。
- 3、通过 table-data 传入表格数据，支持动态数据绑定。
`,
				tableData: [
					{ id: 1, name: "张三", age: 18, sex: "男", phone: "13800000001", address: "上海市普陀区金沙江路 1518 弄" },
					{ id: 2, name: "李四", age: 20, sex: "女", phone: "13800000002", address: "上海市浦东新区张江高科技园区" },
					{ id: 3, name: "王五", age: 22, sex: "男", phone: "13800000003", address: "北京市海淀区中关村大街 1 号" },
					{ id: 4, name: "赵六", age: 25, sex: "女", phone: "13800000004", address: "广州市天河区天河路 385 号" },
					{ id: 5, name: "钱七", age: 28, sex: "男", phone: "13800000005", address: "深圳市南山区科技园南区" }
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
.card-JiChuYongFa {
}
</style>