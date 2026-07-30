<template>
	<div class="contextmenu-custom-demo">
		<xRow :gutter="50">
			<xCol :span="12">
				<div class="contextmenu-demo-box" v-xcontextmenu="customLabelMenus">
					<xBlock class="contextmenu-demo-trigger">自定义标签渲染</xBlock>
				</div>
			</xCol>
			<xCol :span="12">
				<div class="contextmenu-demo-box" v-xcontextmenu="headerFooterMenus">
					<xBlock class="contextmenu-demo-trigger">头部/尾部 + 自定义项</xBlock>
				</div>
			</xCol>
		</xRow>
	</div>
</template>
<script lang="ts">
export default async function () {
	return defineComponent({
		data() {
			const vm = this;
			return {
				/* 使用 renderLabel 给特定项添加标记 */
				customLabelMenus: {
					menus: [
						{
							id: "save",
							label: "保存",
							renderLabel: () => h("span", { style: "color: #409eff;font-weight:600;" }, "💾 保存")
						},
						{ id: "export", label: "导出", renderLabel: () => h("span", { style: "color: #67c23a;" }, "📤 导出为 CSV") },
						{ type: "divider" },
						{ id: "delete", label: "删除", disabled: true }
					],
					onNodeClick(item) {
						console.log("[xcontextmenu] clicked", item.id);
					}
				},
				/* 使用 renderHeader/renderFooter + item.render 完整自定义 */
				headerFooterMenus: {
					menus: [
						{
							id: "user-info",
							render: () =>
								h("div", { style: "display:flex;align-items:center;gap:8px;padding:4px 0;" }, [
									h("div", {
										style:
											"width:28px;height:28px;border-radius:50%;background:#409eff;color:#fff;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:600;"
									}, "U"),
									h("div", { style: "flex:1;" }, [
										h("div", { style: "font-weight:600;font-size:13px;" }, "用户名"),
										h("div", { style: "font-size:11px;color:#909399;" }, "在线")
									])
								])
						},
						{ type: "divider" },
						{ id: "settings", label: "设置" },
						{ id: "logout", label: "退出登录", renderLabel: () => h("span", { style: "color:#e74c3c;" }, "退出登录") }
					],
					renderHeader: () => h("div", { style: "text-align:center;color:#909399;font-size:11px;" }, "用户菜单"),
					renderFooter: () => h("div", { style: "text-align:center;color:#c0c4cc;font-size:11px;padding:2px 0;" }, "v1.0.0"),
					onNodeClick(item) {
						console.log("[xcontextmenu] clicked", item.id);
					}
				}
			};
		}
	});
}
</script>
<style lang="less">
.contextmenu-custom-demo {
}
</style>
