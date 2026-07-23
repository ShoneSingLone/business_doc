<template>
	<DocContentOfDemo>
		<DemoAndCode
			title="基础用法 — Slot 模式"
			path="@/views/xComponent/DemoxItemAdvanceWrapper/JiChuYongFa.vue"
			unfold />
		<DemoAndCode
			title="必填模式 — 强制展开"
			path="@/views/xComponent/DemoxItemAdvanceWrapper/BiTianMoShi.vue"
			unfold />
		<DemoAndCode
			title="自定义 Label"
			path="@/views/xComponent/DemoxItemAdvanceWrapper/ZiDingYiLabel.vue"
			unfold />
		<xMd :md="apiString" data-role="api" />
	</DocContentOfDemo>
</template>

<script lang="ts">
export default async function () {
	return {
		data() {
			return {
				apiString: `### xItemAdvanceWrapper

高级设置包裹组件。展示一个"高级设置" Switch 开关，打开后通过 **slot** 展示子控件区域，自带 xItem 风格的 label 对齐。

> 与 \`xItemAdvanceConfig\` 的区别：本组件是**纯 Wrapper**，不可作为 itemType 使用；始终通过 slot 传入子内容，灵活性更高。

#### 使用方式

\`\`\`html
<xItemAdvanceWrapper>
	<xItem :configs="form.param1" />
	<xItem :configs="form.param2" />
</xItemAdvanceWrapper>
\`\`\`

#### Props

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| \`checked\` | 初始展开状态 | Boolean | \`false\` |
| \`required\` | 是否必填（为 true 时隐藏 Switch，强制展开） | Boolean | \`false\` |
`
			};
		}
	};
}
</script>

<style lang="less"></style>
