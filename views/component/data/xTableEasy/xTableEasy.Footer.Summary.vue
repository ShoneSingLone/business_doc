<template>
	<DocContentOfDemo class="x-table-easy-footer-summary">
		<xMd :md="mdTips" />
		<DemoAndCode
			title="footer 基础功能"
			path="@/views/component/data/xTableEasy/xTableEasy.Footer.Summary.Base.vue"
			unfold />
		<DemoAndCode
			title="footer 列合并"
			path="@/views/component/data/xTableEasy/xTableEasy.Footer.Summary.CellSpan.vue"
			unfold />
		<DemoAndCode
			title="自定义 footer 单元格"
			path="@/views/component/data/xTableEasy/xTableEasy.Footer.Summary.CustomCell.vue"
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
- 1、footer 汇总允许对表格数据进行汇总展示
- 2、\`footerData\` 为 footer 汇总数据，数据结构与 \`tableData\` 保持一致
`,
				apiString: `
## API

### footerData 配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| footerData | 页脚汇总数据 | Array | [] |

### renderFooterCell（列配置）

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| renderFooterCell | 自定义 footer 单元格渲染函数 | Function({row, column, rowIndex}) | - |
`
			};
		}
	};
}
</script>

<style lang="less">
.x-table-easy-footer-summary {
}
</style>
