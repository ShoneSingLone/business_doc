<template>
	<DocContentOfDemo class="x-table-easy-column-width">
		<xMd :md="mdTips" />
		<DemoAndCode
			title="列宽设置"
			path="@/views/component/data/xTableEasy/xTableEasy.ColumnWidth.Setting.vue"
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
- 1、通过在 columns 配置中设置 width 属性来定义列宽
- 2、宽度可以是数字（像素）或字符串（支持百分比等）
- 3、不设置 width 时，列会自动分配宽度
`,
				apiString: ``
			};
		}
	};
}
</script>

<style lang="less">
.x-table-easy-column-width {
}
</style>