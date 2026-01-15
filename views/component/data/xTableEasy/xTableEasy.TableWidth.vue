<template>
	<DocContentOfDemo class="x-table-easy-table-width">
		<xMd :md="mdTips" />
		<DemoAndCode
			title="表格自动宽度"
			path="@/views/component/data/xTableEasy/xTableEasy.TableWidth.AutoWidth.vue"
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
- 1、表格宽度可以设置固定值。如：\`style="width:900px;"\`
- 2、表格宽度可以设置动态值。如：\`style="width:calc(100vh - 210px)"\` 或者 \`style="width:80%"\`
`,
				apiString: ``
			};
		}
	};
}
</script>

<style lang="less">
.x-table-easy-table-width {
}
</style>
