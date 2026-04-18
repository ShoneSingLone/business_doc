<template>
	<DocContentOfDemo class="dropdown-demo">
		<xMd :md="md" />
		<DemoAndCode title="基础用法" path="@/views/other/dialog/JiChuYongFa.vue" unfold />
		<DemoAndCode title="多窗口管理" path="@/views/other/dialog/MultiWindowManagerDemo.vue" unfold />
		<xMd :md="apiString" data-role="api" />
	</DocContentOfDemo>
</template>

<script lang="ts">
export default async function () {
	return {
		data() {
			return {
				md: "基于`Vue-popper`开发，支持多窗口生命周期管理、层级置顶、最小化还原及状态记忆。",
				apiString: `### _.$windowsManager API
| 方法 | 说明 | 参数 | 返回值 |
|------|------|------|--------|
| open(config) | 打开或激活窗口 | config: WindowConfig | Promise<WindowInstance> |
| close(windowId) | 关闭指定窗口 | windowId: string | void |
| closeAll() | 关闭所有窗口 | - | void |
| minimize(windowId) | 最小化窗口 | windowId: string | void |
| restore(windowId) | 还原窗口 | windowId: string | void |
| maximize(windowId) | 最大化窗口 | windowId: string | void |
| toTop(windowId) | 置顶窗口 | windowId: string | void |
| getInstance(windowId) | 获取窗口实例 | windowId: string | WindowInstance |

### Attributes
| 参数 | 说明 | 类型 | 可选值 | 默认值 |
|------|------|------|--------|--------|
| windowId | 窗口唯一标识，用于单例管理和 DOM 查找 | string | - | - |
| modal | 是否显示遮罩（锁定背景）。在 windowsManager 中默认为 false | boolean | true/false | false |
| onCancel | 取消按钮点击事件，返回为 \`真值\` 则不会关闭 modal | Function | - | - |
`
			};
		}
	};
}
</script>

<style lang="less">
.popover-demo {
}
</style>
