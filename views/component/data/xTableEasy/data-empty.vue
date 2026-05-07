<template>
	<DocContentOfDemo class="x-table-easy-data-empty">
		<xMd :md="mdTips" />
		<xTableEasy 
			:columns="columns" 
			:table-data="tableData" 
			border-x 
			border-y 
			:empty-text="emptyText" />
		<xMd :md="apiString" data-role="api" />
	</DocContentOfDemo>
</template>

<script lang="ts">
export default async function () {
	return {
		data() {
			return {
				mdTips: `
- 1、当表格数据为空时，会显示空数据提示
- 2、支持自定义空数据提示文本
- 3、支持自定义空数据渲染内容
`,
				apiString: `
## API

### 空数据相关配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| emptyText | 空数据提示文本 | String | '暂无数据' |
| emptySlot | 自定义空数据内容 | Slot | - |
`,
				emptyText: '暂无数据',
				columns: [
					{ field: "id", key: "id", title: "ID", width: 80, align: "center" },
					{ field: "name", key: "name", title: "姓名", width: 120 },
					{ field: "department", key: "department", title: "部门", width: 150 },
					{ field: "status", key: "status", title: "状态", width: 100, align: "center" }
				],
				tableData: []
			};
		}
	};
}
</script>

<style lang="less">
.x-table-easy-data-empty {
}
</style>