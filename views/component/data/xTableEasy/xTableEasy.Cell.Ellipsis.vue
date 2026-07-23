<template>
	<DocContentOfDemo class="x-table-easy-cell-ellipsis">
		<xMd :md="mdTips" />
		<DemoAndCode
			title="超出换行"
			path="@/views/component/data/xTableEasy/xTableEasy.Cell.Ellipsis.Base.vue"
			unfold />
		<DemoAndCode
			title="省略显示"
			path="@/views/component/data/xTableEasy/xTableEasy.Cell.Ellipsis.Ellipsis.vue"
			unfold />
		<DemoAndCode
			title="多行省略"
			path="@/views/component/data/xTableEasy/xTableEasy.Cell.Ellipsis.EllipsisLine.vue"
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
- 1、通过 column 的 \`ellipsis\` 属性设置超出显示省略
- 2、通过 \`lineClamp\` 设置内容超出多少行开始出现省略
`,
				apiString: `
## API

### 列配置中的省略相关属性

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| ellipsis | 是否启用省略 | Boolean | false |
| lineClamp | 多行省略时显示的行数 | Number | 1 |
| tooltip | 鼠标悬停时是否显示完整内容 | Boolean | true |
`
			};
		}
	};
}
</script>

<style lang="less">
.x-table-easy-cell-ellipsis {
}
</style>
