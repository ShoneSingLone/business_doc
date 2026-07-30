<template>
	<div class="contextmenu-custom-demo">
		<xRow :gutter="50">
			<xCol :span="12">
				<div class="contextmenu-demo-box" v-xcontextmenu="customContent">
					<xBlock class="contextmenu-demo-trigger">content 完全自定义</xBlock>
				</div>
			</xCol>
			<xCol :span="12">
				<div class="contextmenu-demo-box" v-xcontextmenu="scrollableContent">
					<xBlock class="contextmenu-demo-trigger">可滚动内容（滚动内部不关闭）</xBlock>
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
				},
				/* content 模式 + 可滚动列表：内部滚动不关闭菜单 */
				scrollableContent: {
					content: () =>
						h("div", { style: "width:200px;" }, [
							h("div", {
								style: "padding:6px 12px;font-size:11px;color:#909399;border-bottom:1px solid #e4e7ed;"
							}, "通知中心（滚动查看全部）"),
							h("div", { style: "max-height:180px;overflow-y:auto;" }, [
								h("div", { class: "x-contextmenu-item", style: "font-size:12px;", onClick: () => console.log("通知 1") }, "通知消息第 1 条"),
								h("div", { class: "x-contextmenu-item", style: "font-size:12px;", onClick: () => console.log("通知 2") }, "通知消息第 2 条"),
								h("div", { class: "x-contextmenu-item", style: "font-size:12px;", onClick: () => console.log("通知 3") }, "通知消息第 3 条"),
								h("div", { class: "x-contextmenu-item", style: "font-size:12px;", onClick: () => console.log("通知 4") }, "通知消息第 4 条"),
								h("div", { class: "x-contextmenu-item", style: "font-size:12px;", onClick: () => console.log("通知 5") }, "通知消息第 5 条")
							]),
							h("div", {
								style: "padding:6px 12px;font-size:11px;color:#c0c4cc;text-align:center;border-top:1px solid #e4e7ed;cursor:pointer;",
								onClick: () => console.log("查看全部")
							}, "查看全部通知")
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
