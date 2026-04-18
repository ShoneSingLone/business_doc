<template>
	<DocContentOfDemo class="dropdown-demo">
		<xMd :md="md" />
		<DemoAndCode title="基础用法" path="@/views/other/dialog/JiChuYongFa.vue" unfold />
		<DemoAndCode title="遮罩与交互" path="@/views/other/dialog/MaskUsageDemo.vue" unfold />
		<DemoAndCode title="多窗口管理" path="@/views/other/dialog/MultiWindowManagerDemo.vue" unfold />
		<xMd :md="apiString" data-role="api" />
	</DocContentOfDemo>
</template>

<script lang="ts">
export default async function () {
	return {
		data() {
			return {
				md: `基于 \`Vue-popper\` 开发，支持多窗口生命周期管理、层级置顶、最小化还原及状态记忆。

### 弹窗实例管理 (Instance Management)
当使用 \`_.$openModal\` 打开弹窗时，它会返回一个指向该弹窗 Vue 实例的 **Promise**。你可以通过保存这个实例句柄，在业务代码中灵活控制弹窗的状态：

1. **获取实例**：\`const vm = await _.$openModal(...)\`
2. **状态监测**：通过 \`vm.dialog_class.minimized\` 判断窗口是否处于最小化状态。
3. **手动控制**：
    - \`vm.minimize()\`：将窗口最小化。
    - \`vm.restore()\`：将最小化或全屏的窗口还原。
    - \`vm.closeModal()\`：关闭并销毁窗口。
4. **生命周期监听**：使用 \`vm.$on('hook:beforeDestroy', callback)\` 来清理业务逻辑中保存的引用，防止内存泄漏。

> 若需更强大的自动化管理（如单例控制、自动记忆位置等），建议直接使用 **_.$windowsManager** 模块。
`,
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

### 默认行为一览 (Default Behavior)
| 属性 | \`_.$openModal\` (基础) | \`_.$windowsManager\` (管理) |
| :--- | :--- | :--- |
| **\`mask\` (遮罩)** | **\`true\`** (锁定背景) | **\`false\`** (不锁定背景) |
| **\`fullscreen\` (全屏)** | **隐藏图标** | **显示图标** (初始不全屏) |
| **\`minimizable\` (最小化)** | **隐藏图标** | **显示图标** (初始不最小化) |
| **\`resize\` (调整大小)** | **\`false\`** | **\`true\`** |
| **\`keyboard\` (快捷键)** | **\`false\`** | **\`false\`** |

### Attributes
| 参数 | 说明 | 类型 | 可选值 | 默认值 |
|------|------|------|--------|--------|
| windowId | 窗口唯一标识，用于单例管理和 DOM 查找 | string | - | - |
| mask | 是否显示遮罩（锁定背景）。在 \`_.$openModal\` 中默认为 true，在 \`_.$windowsManager\` 中默认为 false | boolean | true/false | true |
| closeOnClickMask | 是否可以通过点击遮罩层关闭窗口。默认为 false | boolean | true/false | false |
| fullscreen | 控制全屏按钮。**字段存在**即显示按钮，**值**决定初始是否全屏。在 \`_.$openModal\` 中默认隐藏，在 \`_.$windowsManager\` 中默认显示且初始不全屏 | boolean | true/false | - |
| minimizable | 控制最小化按钮。**值为 true** 即显示按钮。在 \`_.$openModal\` 中默认隐藏，在 \`_.$windowsManager\` 中默认显示 | boolean | true/false | - |
| resize | 是否允许从右下角自由调整窗口大小。在 \`_.$openModal\` 中默认 false，在 \`_.$windowsManager\` 中默认 true | boolean | true/false | - |
| keyboard | 是否开启键盘快捷键（Ctrl+W 关闭，Ctrl+M 最小化）。默认全都不开启 | boolean | true/false | false |
| onCancel | 取消按钮点击事件，返回为 \`真值\` 则不会关闭 modal | Function | - | - |

> **提示：逻辑解耦说明**
> - **全屏控制 (fullscreen)**：只要 \`modalConfigs\` 中定义了该键，就会显示图标；字段的布尔值决定初始状态。
> - **最小化控制 (minimizable)**：仅当 \`modalConfigs.minimizable === true\` 时显示图标，且窗口初始始终为常规状态（不为最小化）。

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
