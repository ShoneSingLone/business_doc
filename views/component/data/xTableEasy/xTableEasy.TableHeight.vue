<template>
	<DocContentOfDemo class="x-table-easy-table-height">
		<xMd :md="mdTips" />
		<DemoAndCode
			title="表格自动高度"
			path="@/views/component/data/xTableEasy/xTableEasy.TableHeight.AutoHeight.vue"
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
- 1、表格高度可以设置固定值。如：maxHeight: 500
- 2、表格高度可以设置动态值。如：maxHeight: 'calc(100vh - 210px)'
- 3、不设置maxHeight时，表格会根据内容自动调整高度
`,
				apiString: ``
			};
		}
	};
}
</script>

<style lang="less">
.x-table-easy-table-height {
}
</style>