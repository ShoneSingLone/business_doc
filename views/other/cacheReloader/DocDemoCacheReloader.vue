<template>
	<DocContentOfDemo class="DemoCacheReloader">
		<xMd :md="md" />
		<DemoAndCode
			title="基础用法：检测到新版本时弹出"
			path="@/views/other/cacheReloader/JiChuYongFa.vue"
			unfold />
		<DemoAndCode
			title="自定义更新亮点（changelog）"
			path="@/views/other/cacheReloader/ZiDingYiGengXinLiangDian.vue"
			unfold />
		<DemoAndCode
			title="倒计时自动重载"
			path="@/views/other/cacheReloader/DaoJiShiZiDongZhongZai.vue"
			unfold />
		<DemoAndCode
			title="指令式调用 _.$cacheReloader"
			path="@/views/other/cacheReloader/ZhiLingShiDiaoYong.vue"
			unfold />
		<xMd :md="apiString" data-role="api" />
	</DocContentOfDemo>
</template>

<script lang="ts">
export default async function () {
	return {
		data() {
			return {
				md: `## xCacheReloader 缓存更新浮窗

右下角浮窗组件，用于在前端项目发布新版本后提示用户"本次更新了什么"，并提供"立即体验 / 重新加载"按钮，**实际完成的工作就是清除前端缓存并重新加载资源**。

### 何时使用

- 前端项目使用 IndexedDB / localStorage 缓存了 .vue 源码、静态资源（本项目 \`seed.js\` 已内置该机制）
- 发版后需要告知用户新增功能或修复的重要 Bug
- 相比顶部提示条，右下角浮窗更具现代感，且能承载更丰富的信息（如更新日志）

### 工作原理

1. 组件挂载后比较 \`window.APP_VERSION\` 与 \`_.$idb.get("APP_VERSION")\`
2. 版本不一致 → 浮窗弹出，展示更新亮点
3. 用户点击"立即体验" → \`_.$idb.clear()\` 清空缓存 → \`location.reload(true)\` 重新加载
4. 可配置为倒计时后自动消失，或持续悬浮直至用户响应

> 组件路径：\`/common/ui-x/common/xCacheReloader.vue\`
> 图标建议：\`refresh\` / \`icon_refresh\`
`,
				apiString: `### Props

| 参数            | 说明                                                                   | 类型            | 可选值                 | 默认值        |
|-----------------|------------------------------------------------------------------------|-----------------|------------------------|---------------|
| version         | 当前版本号，默认读取 \`window.APP_VERSION\`                             | string          | —                      | APP_VERSION   |
| changelog       | 更新亮点列表，每一项为字符串或 \`{ text, type }\`                       | array           | —                      | []            |
| title           | 浮窗标题                                                               | string          | —                      | "发现新版本"   |
| buttonText      | 主按钮文案                                                             | string          | —                      | "立即体验"    |
| dismissText     | 次按钮（忽略）文案，为空则不显示                                       | string          | —                      | "稍后"        |
| countdown       | 倒计时秒数，到 0 自动触发重载；传 0 表示不自动重载                      | number          | —                      | 0             |
| autoDismiss     | 倒计时结束后是否自动消失（不重载）                                     | boolean         | —                      | false         |
| position        | 浮窗位置                                                               | string          | bottom-right/top-right | bottom-right  |
| icon            | 自定义图标名                                                           | string          | —                      | "refresh"     |
| clearStorageKeys| 需要同步清除的 localStorage key 列表                                   | array           | —                      | []            |
| onBeforeReload  | 重载前的钩子，支持 async，返回 false 可取消重载                        | function        | —                      | —             |
| onReload        | 执行清缓存+重载后的回调（重载前同步执行）                              | function        | —                      | —             |
| onDismiss       | 用户点击"稍后"的回调                                                   | function        | —                      | —             |

### Methods（通过 ref 调用）

| 方法名        | 说明                                   |
|---------------|----------------------------------------|
| show()        | 手动弹出浮窗                           |
| dismiss()     | 关闭浮窗（不重载）                     |
| reload()      | 立即执行清缓存 + 重载                  |

### Events

| 事件名   | 说明                 | 回调参数 |
|----------|----------------------|----------|
| show     | 浮窗显示时触发       | —        |
| dismiss  | 浮窗关闭时触发       | —        |
| reload   | 执行清缓存+重载时触发 | —        |

### 指令式 API

除标签式使用外，还提供全局工具函数：

\`\`\`javascript
_.$cacheReloader({
  version: "1.2.0",
  changelog: ["新增导出功能", "修复登录闪烁问题"],
  buttonText: "立即体验",
  countdown: 10
});
\`\`\`
`
			};
		}
	};
}
</script>

<style lang="less"></style>
