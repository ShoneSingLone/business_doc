<template>
	<div class="contextmenu-sub-demo">
		<xRow :gutter="50">
			<xCol :span="12">
				<div class="contextmenu-demo-box" v-xcontextmenu="subMenus">
					<xBlock class="contextmenu-demo-trigger">右键体验子菜单</xBlock>
				</div>
			</xCol>
			<xCol :span="12">
				<div class="contextmenu-demo-box" v-xcontextmenu="nestedMenus">
					<xBlock class="contextmenu-demo-trigger">多级嵌套</xBlock>
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
				subMenus: [
					{ id: "open", label: "打开" },
					{
						id: "new",
						label: "新建",
						children: [
							{ id: "new-file", label: "新建文件" },
							{ id: "new-folder", label: "新建文件夹" }
						]
					},
					{ type: "divider" },
					{ id: "delete", label: "删除" }
				],
				nestedMenus: [
					{ id: "view", label: "查看" },
					{
						id: "sort",
						label: "排序方式",
						children: [
							{ id: "sort-name", label: "按名称" },
							{ id: "sort-date", label: "按日期" },
							{ id: "sort-size", label: "按大小" }
						]
					},
					{
						id: "group",
						label: "分组方式",
						children: [
							{ id: "group-type", label: "按类型" },
							{
								id: "group-more",
								label: "更多",
								children: [
									{ id: "group-author", label: "按作者" },
									{ id: "group-tag", label: "按标签" }
								]
							}
						]
					}
				]
			};
		}
	});
}
</script>
<style lang="less">
.contextmenu-sub-demo {
}
</style>
