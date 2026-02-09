<template>
	<DocContentOfDemo class="x-table-easy-column-width-dragging">
		<xMd :md="mdDoc" />
		<DemoAndCode
			title="列宽拖动"
			path="@/views/component/data/xTableEasy/xTableEasy.ColumnWidth.Dragging.Basic.vue"
			unfold />
		<DemoAndCode
			title="禁用列宽拖动"
			path="@/views/component/data/xTableEasy/xTableEasy.ColumnWidth.Dragging.Disable.vue"
			unfold />
	</DocContentOfDemo>
</template>

<script lang="ts">
export default async function () {
	return {
		data() {
			return {
				mdDoc: `- 1、当存在大文本时，列宽调整将会很有用
- 2、通过 \`columnWidthResizeOption\` 设置列宽拖动功能
- 3、建议设置 \`scroll-width=0\`，那么当列宽总和大于容器宽度时，将会出横向滚动条
- 4、通过 \`column.width\` 设置列的默认宽度，如果所有列宽总和小于容器宽度，列宽度将会自适应`
			};
		}
	};
}
</script>

<style lang="less">
.x-table-easy-column-width-dragging {
}
</style>
