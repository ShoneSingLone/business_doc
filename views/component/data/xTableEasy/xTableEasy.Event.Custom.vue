<template>
	<DocContentOfDemo class="x-table-easy-event-custom">
		<xMd :md="mdTips" />
		<DemoAndCode
			title="body 单元格事件"
			path="@/views/component/data/xTableEasy/xTableEasy.Event.Custom.BodyCell.vue"
			unfold />
		<DemoAndCode
			title="body 行事件"
			path="@/views/component/data/xTableEasy/xTableEasy.Event.Custom.BodyRow.vue"
			unfold />
		<DemoAndCode
			title="header 单元格事件"
			path="@/views/component/data/xTableEasy/xTableEasy.Event.Custom.HeaderCell.vue"
			unfold />
		<xMd :md="apiString" data-role="api" />
	</DocContentOfDemo>
</template>

<script lang="ts">
export default async function () {
	return {
		data() {
			return {
				mdTips: `
- 1、\`eventCustomOption\` 配置自定义事件
- 2、支持 body、header、footer 行和列事件自定义
- 3、支持多种事件类型：click、dblclick、contextmenu、mouseenter、mouseleave 等
`,
				apiString: `
## API

### 自定义事件

| 事件名 | 说明 | 参数 |
|--------|------|------|
| on-body-cell-click | 单元格点击事件 | { row, column, rowIndex, columnIndex } |
| on-body-row-click | 行点击事件 | { row, rowIndex } |
| on-header-cell-click | 表头点击事件 | { column, columnIndex } |
| on-header-row-click | 表头行点击事件 | { columns } |
| on-footer-cell-click | 页脚单元格点击事件 | { row, column, rowIndex, columnIndex } |
| on-footer-row-click | 页脚行点击事件 | { row, rowIndex } |
`
			};
		}
	};
}
</script>

<style lang="less">
.x-table-easy-event-custom {
}
</style>
