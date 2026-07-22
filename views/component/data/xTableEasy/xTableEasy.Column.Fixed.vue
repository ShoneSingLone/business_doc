<template>
	<DocContentOfDemo class="x-table-easy-column-fixed">
		<xMd :md="mdTips" />
		<DemoAndCode
			title="左侧固定"
			path="@/views/component/data/xTableEasy/xTableEasy.Column.Fixed.Left.vue"
			unfold />
		<DemoAndCode
			title="右侧固定"
			path="@/views/component/data/xTableEasy/xTableEasy.Column.Fixed.Right.vue"
			unfold />
		<DemoAndCode
			title="两侧固定"
			path="@/views/component/data/xTableEasy/xTableEasy.Column.Fixed.Both.vue"
			unfold />
		<xMd :md="apiString" data-role="api" />
	</DocContentOfDemo>
</template>

<script lang="ts">
export default async function () {
	return {
		data() {
			return {
				mdTips: `
- 1、属性 \`scroll-width\` 为滚动区域的宽度
- 2、当外层容器宽度小于 \`scroll-width\` 值时，将会出现横向滚动条；当外层容器宽度大于 \`scroll-width\` 值时，将会跟随容器自适应；当 \`scroll-width=0\` 时，滚动条将根据列宽度决定
- 3、列宽可以不设置、或者设置为百分比、或者为像素值（px）
- 4、设置了 \`scroll-width\` 属性，列宽单位**强烈建议保持一致！**
- 5、通过 \`fixed: "left"\` 设置左列固定，通过 \`fixed: "right"\` 设置右列固定
`,
				apiString: `
## API

### 表格属性

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| scroll-width | 滚动区域宽度 | Number | \`0\` |

### 列配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| fixed | 是否固定列 | String | \`-\` |

**fixed 可选值**：
| 值 | 说明 |
|----|------|
| \`left\` | 左列固定 |
| \`right\` | 右列固定 |
`
			};
		}
	};
}
</script>

<style lang="less">
.x-table-easy-column-fixed {
}
</style>
