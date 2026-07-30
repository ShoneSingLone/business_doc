<template>
	<div class="contextmenu-custom-demo">
		<xRow :gutter="50">
			<xCol :span="12">
				<div class="contextmenu-demo-box" v-xcontextmenu="customContent">
					<xBlock class="contextmenu-demo-trigger">content 完全自定义</xBlock>
				</div>
			</xCol>
		</xRow>
	</div>
</template>
<script lang="ts">
export default async function () {
	return defineComponent({
		data() {
			return {
				/* content 模式：不用 menus，自己和自己的渲染函数做决定 */
				customContent: {
					content: () =>
						h("div", [
							h("div", {
								style:
									"padding:8px 16px;background:#f0f5ff;font-size:12px;color:#409eff;border-bottom:1px solid #e4e7ed;"
							}, "当前选中：3 条"),
							h("div", { class: "x-contextmenu-item", onClick: () => console.log("批量删除") }, [
								h("xIcon", { icon: "_icon_delete", size: 14, style: "margin-right:8px" }),
								h("span", "批量删除")
							]),
							h("div", { class: "x-contextmenu-item", onClick: () => console.log("批量导出") }, [
								h("xIcon", { icon: "_icon_export", size: 14, style: "margin-right:8px" }),
								h("span", "批量导出")
							]),
							h("div", { class: "x-contextmenu-divider" }),
							h("div", {
								class: "x-contextmenu-item",
								style: "color:#e74c3c",
								onClick: () => console.log("清空回收站")
							}, "清空回收站")
						])
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
