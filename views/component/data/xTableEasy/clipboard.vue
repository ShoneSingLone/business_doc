<template>
	<DocContentOfDemo class="x-table-easy-clipboard">
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
- 1、clipboard功能说明待补充
- 2、具体使用方式待补充
- 3、注意事项待补充
`,
				apiString: `
## API

### clipboard相关配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| - | - | - | - |
`,
				columns: [
					{ field: "id", key: "id", title: "ID", width: 80, align: "center" },
					{ field: "name", key: "name", title: "名称", width: 120 },
					{ field: "description", key: "description", title: "描述", width: 300 }
				],
				tableData: [
					{ id: 1, name: "示例数据1", description: "这是一条示例数据" },
					{ id: 2, name: "示例数据2", description: "这是另一条示例数据" },
					{ id: 3, name: "示例数据3", description: "这是第三条示例数据" }
				]
			};
		}
	};
}
</script>

<style lang="less">
.x-table-easy-clipboard {
}
</style>
