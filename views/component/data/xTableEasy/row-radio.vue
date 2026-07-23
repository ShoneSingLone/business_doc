<template>
	<DocContentOfDemo class="x-table-easy-row-radio">
		<xMd :md="mdTips" />
		<div class="demo-controls">
			<span>当前选中: {{ selectedRow?.name || "无" }}</span>
		</div>
		<xTableEasy
			:columns="columns"
			:table-data="tableData"
			:radio-option="radioOption"
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
- 1、表格支持行单选功能
- 2、通过 radioOption 配置单选行为
- 3、同一时间只能选中一行
`,
				apiString: `
## API

### radioOption 配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| trigger | 触发方式 | String | 'row' |
| selectedRowKey | 选中的行key | String/Number | - |
| onChange | 选中状态变化事件 | Function(selectedRowKey, selectedRow) | - |
`,
				selectedRow: null,
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
				radioOption: {
					trigger: "row",
					onChange: (selectedRowKey, selectedRow) => {
						this.selectedRow = selectedRow;
					}
				}
			};
		}
	};
}
</script>

<style lang="less">
.x-table-easy-row-radio {
	.demo-controls {
		margin-bottom: 16px;
		padding: 12px;
		background-color: #f5f7fa;
		border-radius: 4px;
	}
}
</style>
