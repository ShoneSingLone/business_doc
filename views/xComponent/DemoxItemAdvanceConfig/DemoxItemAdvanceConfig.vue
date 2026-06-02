<template>
	<DocContentOfDemo>
		<DemoAndCode
			title="基础用法 — itemType 模式"
			path="@/views/xComponent/DemoxItemAdvanceConfig/JiChuYongFa.vue"
			unfold />
		<DemoAndCode
			title="Slot 用法 — 独立 Wrapper 模式"
			path="@/views/xComponent/DemoxItemAdvanceConfig/SlotYongFa.vue"
			unfold />
		<xMd :md="apiString" data-role="api" />
	</DocContentOfDemo>
</template>

<script lang="ts">
export default async function () {
	return {
		data() {
			return {
				apiString: `### xItemAdvanceConfig

高级配置开关组件。展示一个 Switch 开关，打开后显示子控件区域，适用于"高级设置"等可折叠配置场景。

#### 使用方式

**方式一：作为 itemType 使用**

在 xItem configs 中指定 \`itemType: "xItemAdvanceConfig"\`，通过 \`subItems\` 配置子项：

\`\`\`js
{
  value: false,
  itemType: "xItemAdvanceConfig",
  label: "高级配置",
  subItems: [
    { value: "", label: "参数1", itemType: "xItemInput" },
    { value: "", label: "参数2", itemType: "xItemSelect", options: [...] }
  ]
}
\`\`\`

**方式二：独立 Wrapper 使用**

直接作为组件使用，通过 slot 传入子控件：

\`\`\`html
<xItemAdvanceConfig v-model="isOpen">
  <xItem :configs="form.child1" />
  <xItem :configs="form.child2" />
</xItemAdvanceConfig>
\`\`\`

#### Configs 属性

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| \`subItems\` | 子 xItem configs 数组（itemType 模式下） | Array | \`[]\` |
| \`required\` | 是否必填（为 true 时隐藏 Switch，强制展开） | Boolean | \`false\` |
| \`activeText\` | Switch 开启时的文本 | String | \`"开启"\` |
| \`inactiveText\` | Switch 关闭时的文本 | String | \`"关闭"\` |

#### Props（独立 Wrapper 模式）

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| \`v-model\` / \`value\` | 控制 Switch 开关状态 | Boolean | \`false\` |
| \`required\` | 是否必填 | Boolean | \`false\` |
`
			};
		}
	};
}
</script>

<style lang="less"></style>
