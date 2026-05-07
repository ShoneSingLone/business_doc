<template>
	<div class="card-DaiYouXuanZeDeBiaoGe">
		<xMd :md="mdTips" />
		<h4>Checkbox选择</h4>
		<xTableEasy :columns="columns" :table-data="tableData" :max-height="300" border-x border-y :checkbox-option="checkboxOption" row-key-field-name="id" />
		<h4>Radio选择</h4>
		<xTableEasy :columns="columns" :table-data="tableData" :max-height="300" border-x border-y :radio-option="radioOption" row-key-field-name="id" />
	</div>
</template>
<script lang="ts">
export default async function () {
	return defineComponent({
		data() {
			return {
				mdTips: `
- 1、表格支持行选择功能，包括多选(checkbox)和单选(radio)两种方式。
- 2、通过 checkbox-option 和 radio-option 配置选择行为。
- 3、支持选择状态变化回调。
`,
				tableData: [
					{ id: 1, name: "张三", age: 18, sex: "男", phone: "13800000001", address: "上海市普陀区金沙江路 1518 弄" },
					{ id: 2, name: "李四", age: 20, sex: "女", phone: "13800000002", address: "上海市浦东新区张江高科技园区" },
					{ id: 3, name: "王五", age: 22, sex: "男", phone: "13800000003", address: "北京市海淀区中关村大街 1 号" },
					{ id: 4, name: "赵六", age: 25, sex: "女", phone: "13800000004", address: "广州市天河区天河路 385 号" },
					{ id: 5, name: "钱七", age: 28, sex: "男", phone: "13800000005", address: "深圳市南山区科技园南区" }
				],
				columns: [
					{ field: "name", key: "name", title: "姓名", width: 120, align: "left" },
					{ field: "age", key: "age", title: "年龄", width: 80, align: "center" },
					{ field: "sex", key: "sex", title: "性别", width: 80, align: "center" },
					{ field: "phone", key: "phone", title: "电话号码", width: 150, align: "left" }
				],
				checkboxOption: {
					enable: true,
					selectedRowKeys: [],
					onChange: (selectedRowKeys, selectedRows) => { console.log("Checkbox选择变化:", selectedRowKeys, selectedRows); }
				},
				radioOption: {
					enable: true,
					selectedRowKey: null,
					onChange: (selectedRowKey, selectedRow) => { console.log("Radio选择变化:", selectedRowKey, selectedRow); }
				}
			};
		}
	});
}
</script>
<style lang="less">
.card-DaiYouXuanZeDeBiaoGe {
	h4 {
		margin: 15px 0 10px 0;
		font-size: 14px;
		font-weight: 500;
	}
}
</style>