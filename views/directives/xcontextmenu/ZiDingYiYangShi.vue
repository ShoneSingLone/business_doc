<template>
	<xRow :gutter="50">
		<xCol :span="12">
			<div class="contextmenu-demo-box">
				<xBlock
					class="contextmenu-demo-trigger contextmenu-demo-trigger--danger"
					v-xcontextmenu="dangerMenus">
					危险操作菜单
				</xBlock>
			</div>
		</xCol>
		<xCol :span="12">
			<div class="contextmenu-demo-box">
				<xBlock
					class="contextmenu-demo-trigger contextmenu-demo-trigger--round"
					v-xcontextmenu="roundMenus">
					圆角样式菜单
				</xBlock>
			</div>
		</xCol>
	</xRow>
</template>
<script lang="ts">
export default async function () {
	return defineComponent({
		data() {
			return {
				dangerMenus: [
					{ id: "lock", label: "锁定", icon: "_lock" },
					{ id: "archive", label: "归档", icon: "_archive" },
					{ id: "divider", divider: true },
					{ id: "delete", label: "永久删除", icon: "_delete" }
				],
				roundMenus: [
					{ id: "share", label: "分享", icon: "_share" },
					{ id: "favorite", label: "收藏", icon: "star" },
					{ id: "export", label: "导出", icon: "_download" }
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
	&--danger {
		color: var(--color-error);
	}
	&--round {
		border-radius: 20px;
		padding: 8px 20px;
		background: var(--color-surface-variant);
	}
}
</style>
