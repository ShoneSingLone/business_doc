<template>
	<DocContentOfDemo class="x-table-easy-table-border">
		<xMd :md="mdTips" />
		<DemoAndCode
			title="完整边框（横向和纵向）"
			path="@/views/component/data/xTableEasy/xTableEasy.TableBorder.AutoBorder.vue"
			unfold />
		<DemoAndCode
			title="只显示横向边框"
			path="@/views/component/data/xTableEasy/xTableEasy.TableBorder.HorizontalBorder.vue"
			unfold />
		<DemoAndCode
			title="只显示纵向边框"
			path="@/views/component/data/xTableEasy/xTableEasy.TableBorder.VerticalBorder.vue"
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
- 1、通过配置 borderX 属性，可以显示表格的纵向边框
- 2、通过配置 borderY 属性，可以显示表格的横向边框
- 3、同时配置 borderX 和 borderY，可以显示完整的表格边框
- 4、borderAround 属性可以显示表格的外边框
`,
				apiString: ``
			};
		}
	};
}
</script>

<style lang="less">
.x-table-easy-table-border {
}
</style>
