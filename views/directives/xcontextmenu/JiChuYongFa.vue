<template>
	<xRow :gutter="50">
		<xCol :span="12">
			<div class="contextmenu-demo-box" v-xcontextmenu="basicMenus">
				<xBlock class="contextmenu-demo-trigger">右键点击此区域</xBlock>
			</div>
		</xCol>
		<xCol :span="12">
			<div class="contextmenu-demo-box" v-xcontextmenu="disabledMenus">
				<xBlock class="contextmenu-demo-trigger">包含禁用项</xBlock>
			</div>
		</xCol>
	</xRow>
</template>
<script lang="ts">
export default async function () {
	return defineComponent({
		data() {
			return {
				basicMenus: [
					{ id: "edit", label: "编辑" },
					{ id: "copy", label: "复制" },
					{ type: "divider" },
					{ id: "delete", label: "删除" }
				],
				disabledMenus: [
					{ id: "rename", label: "重命名" },
					{ id: "copy", label: "复制" },
					{ type: "divider" },
					{ id: "delete", label: "删除", disabled: true }
				]
			};
		}
	});
}
</script>
<style lang="less">
.contextmenu-demo-box {
	display: flex;
	justify-content: center;
	align-items: center;
	height: 120px;
	border: 1px dashed var(--el-border-color-lighter);
	border-radius: 8px;
	background: var(--color-surface-container);
}
.contextmenu-demo-trigger {
	cursor: context-menu;
	user-select: none;
}
</style>
