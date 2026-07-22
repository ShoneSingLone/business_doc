<template>
	<DocContentOfDemo class="x-table-easy-row-checkbox">
		<xMd :md="mdTips" />
		<div class="demo-controls">
			<span>已选择: {{ selectedRows.length }} 行</span>
			<xBtn @click="clearSelection">清除选择</xBtn>
			<xBtn @click="selectAll">全选</xBtn>
		</div>
		<xTableEasy
			:columns="columns"
			:table-data="tableData"
			:checkbox-option="checkboxOption"
			border-x
			border-y />
		<xMd :md="apiString" data-role="api" />
	</DocContentOfDemo>
</template>

<script lang="ts">
export default async function () {
	return {
		data() {
			return {
				mdTips: `
- 1、表格支持行多选功能
- 2、通过 checkboxOption 配置多选行为
- 3、支持自定义选中状态和禁用某些行
`,
				apiString: `
## API

### checkboxOption 配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| trigger | 触发方式 | String | 'row' |
| selectedRowKeys | 选中的行key | Array | [] |
| disabled | 是否禁用多选 | Function(row) | - |
| onChange | 选中状态变化事件 | Function(selectedRowKeys, selectedRows) | - |
`,
				selectedRows: [],
				columns: [
					{ field: "name", key: "name", title: "姓名", width: 120 },
					{ field: "department", key: "department", title: "部门", width: 150 },
					{ field: "position", key: "position", title: "岗位", width: 120 },
					{ field: "score", key: "score", title: "评分", width: 100, align: "center" }
				],
				tableData: [
					{
						id: 1,
						name: "张三",
						department: "研发一组",
						position: "前端开发",
						score: 95
					},
					{
						id: 2,
						name: "李四",
						department: "质量保障",
						position: "测试工程师",
						score: 88
					},
					{
						id: 3,
						name: "王五",
						department: "产品中心",
						position: "产品经理",
						score: 91
					},
					{ id: 4, name: "赵六", department: "研发二组", position: "后端开发", score: 84 }
				],
				checkboxOption: {
					trigger: "row",
					onChange: (selectedRowKeys, selectedRows) => {
						this.selectedRows = selectedRows;
					}
				}
			};
		},
		methods: {
			clearSelection() {
				this.selectedRows = [];
			},
			selectAll() {
				this.selectedRows = [...this.tableData];
			}
		}
	};
}
</script>

<style lang="less">
.x-table-easy-row-checkbox {
	.demo-controls {
		display: flex;
		gap: 16px;
		align-items: center;
		margin-bottom: 16px;
		padding: 12px;
		background-color: #f5f7fa;
		border-radius: 4px;
	}
}
</style>
