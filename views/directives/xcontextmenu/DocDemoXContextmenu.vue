<template>
	<DocContentOfDemo class="doc-demo-xcontextmenu">
		<xMd
			:md="'# xContextmenu 右键菜单\n\n右键菜单指令，用于在元素上绑定右键菜单。\n\n## 何时使用\n\n`v-xcontextmenu` 指令用于为任意元素添加右键菜单功能，支持多级子菜单、禁用项、分割线。\n\n> 注：该指令由 `statics/common/ui-x/directives/xcontextmenu/` 提供基础能力，业务项目可自行覆盖菜单项样式。'" />
		<DemoAndCode
			title="基础用法"
			path="@/views/directives/xcontextmenu/JiChuYongFa.vue"
			unfold />
		<DemoAndCode
			title="子菜单"
			path="@/views/directives/xcontextmenu/ZiCaiDan.vue"
			unfold />
		<xMd :md="apiString" data-role="api" />
	</DocContentOfDemo>
</template>

<script lang="ts">
export default async function () {
	return {
		data() {
			return {
				apiString: [
					"### v-xcontextmenu 指令 API",
					"",
					"#### 指令值",
					"| 类型 | 说明 | 示例 |",
					"| :--- | :--- | :--- |",
					"| `Array` | 简写形式，直接传菜单项数组 | `v-xcontextmenu=\"menuItems\"` |",
					"| `Object` | 完整配置，支持 `menus` + `onNodeClick` 回调 | `v-xcontextmenu=\"{ menus, onNodeClick }\"` |",
					"",
					"#### 菜单项配置",
					"| 属性 | 类型 | 默认值 | 说明 |",
					"| :--- | :--- | :--- | :--- |",
					"| id | `string` | - | 唯一标识 |",
					"| label | `string` | - | 显示文本 |",
					"| icon | `string` | - | 图标名（当前面板尚未注册图标，仅作属性预留） |",
					"| disabled | `boolean` | `false` | 是否禁用 |",
					"| type | `string` | - | 设为 `'divider'` 渲染为分割线 |",
					"| children | `Array` | - | 子菜单项（支持递归嵌套） |",
					"",
					"#### 回调",
					"| 回调 | 参数 | 说明 |",
					"| :--- | :--- | :--- |",
					"| onNodeClick | `(item)` | 点击非子菜单项时触发 |"
				].join("\n")
			};
		}
	};
}
</script>
<style lang="less">
.doc-demo-xcontextmenu {
}
</style>
