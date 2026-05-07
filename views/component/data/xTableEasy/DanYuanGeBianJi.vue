<template>
	<div class="card-DanYuanGeBianJi">
		<xMd :md="mdTips" />
		<xTableEasy :columns="columns" :table-data="tableData" :max-height="400" border-x border-y row-key-field-name="id" :edit-option="editOption" />
	</div>
</template>
<script lang="ts">
export default async function () {
	return defineComponent({
		data() {
			return {
				mdTips: `
- 1、通过配置 edit-option，可以实现单元格的编辑功能。
- 2、支持多种编辑类型：text、number、select、switch。
- 3、可配置编辑回调函数进行数据校验和保存。
`,
				tableData: [
					{ id: 1, name: "张三", age: 18, sex: "男", phone: "13800000001", email: "zhangsan@example.com", score: 95, status: 1 },
					{ id: 2, name: "李四", age: 20, sex: "女", phone: "13800000002", email: "lisi@example.com", score: 88, status: 2 }
				],
				columns: [
					{ field: "id", key: "id", title: "ID", width: 80, align: "center" },
					{ field: "name", key: "name", title: "姓名", width: 120, align: "left", edit: true },
					{ field: "age", key: "age", title: "年龄", width: 80, align: "center", edit: true, editType: "number", editOption: { min: 0, max: 120, step: 1 } },
					{ field: "sex", key: "sex", title: "性别", width: 80, align: "center", edit: true, editType: "select", editOption: { options: [{ value: "男", label: "男" }, { value: "女", label: "女" }] } },
					{ field: "phone", key: "phone", title: "电话号码", width: 150, align: "left", edit: true },
					{ field: "email", key: "email", title: "邮箱", width: 200, align: "left", edit: true },
					{ field: "score", key: "score", title: "分数", width: 100, align: "center", edit: true, editType: "number", editOption: { min: 0, max: 100, step: 1 } },
					{
						field: "status",
						key: "status",
						title: "状态",
						width: 120,
						align: "center",
						edit: true,
						editType: "switch",
						cellRenderer: (row) => row.status === 1 ? "<span style='color: green;'>启用</span>" : "<span style='color: red;'>禁用</span>"
					}
				],
				editOption: {
					enable: true,
					mode: "dblclick",
					beforeEdit: (row, column) => { console.log("编辑前", { row, column }); return true; },
					onEditing: (row, column, value) => { console.log("编辑中", { row, column, value }); },
					afterEdit: (row, column, oldValue, newValue) => { console.log("编辑完成", { row, column, oldValue, newValue }); }
				}
			};
		}
	});
}
</script>
<style lang="less">
.card-DanYuanGeBianJi {
}
</style>