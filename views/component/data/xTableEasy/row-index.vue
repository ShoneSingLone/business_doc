<template>
	<DocContentOfDemo class="x-table-easy-row-index">
		<xMd :md="mdTips" />
		<xTableEasy :columns="columns" :table-data="tableData" border-x border-y />
		<xMd :md="apiString" data-role="api" />
	</DocContentOfDemo>
</template>

<script lang="ts">
export default async function () {
	return {
		data() {
			return {
				mdTips: `
- 1、表格支持自动生成行序号
- 2、通过 type: "index" 配置序号列
- 3、支持自定义序号起始值
`,
				apiString: `
## API

### 序号列配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| type | 列类型，设为 "index" 表示序号列 | String | - |
| width | 列宽度 | Number | 60 |
| indexMethod | 自定义序号生成函数 | Function(rowIndex) | - |
`,
				columns: [
					{ type: "index", key: "index", title: "序号", width: 60, align: "center" },
					{ field: "name", key: "name", title: "姓名", width: 120 },
					{ field: "department", key: "department", title: "部门", width: 150 },
					{ field: "score", key: "score", title: "评分", width: 100, align: "center" }
				],
				tableData: [
					{ id: 1, name: "张三", department: "研发一组", score: 95 },
					{ id: 2, name: "李四", department: "质量保障", score: 88 },
					{ id: 3, name: "王五", department: "产品中心", score: 91 },
					{ id: 4, name: "赵六", department: "研发二组", score: 84 }
				]
			};
		}
	};
}
</script>

<style lang="less">
.x-table-easy-row-index {
}
</style>
