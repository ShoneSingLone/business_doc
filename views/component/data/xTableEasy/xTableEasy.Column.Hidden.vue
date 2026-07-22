<template>
	<DocContentOfDemo class="x-table-easy-column-hidden">
		<xMd :md="mdTips" />
		<DemoAndCode
			title="默认隐藏列"
			path="@/views/component/data/xTableEasy/xTableEasy.Column.Hidden.Default.vue"
			unfold />
		<DemoAndCode
			title="实例方法"
			path="@/views/component/data/xTableEasy/xTableEasy.Column.Hidden.Instance.vue"
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
- 1、通过 \`columnHiddenOption\` 实现列隐藏功能
- 2、支持通过实例方法控制列的隐藏与显示
`,
				apiString: `
## API

### columnHiddenOption

列隐藏配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| defaultHiddenColumnKeys | 默认隐藏的列 key 数组 | Array | \`[]\` |

### 实例方法

| 方法名 | 说明 | 参数 |
|--------|------|------|
| hideColumnsByKeys(keys) | 隐藏指定列 | keys: 列 key 数组 |
| showColumnsByKeys(keys) | 显示指定列 | keys: 列 key 数组 |
`
			};
		}
	};
}
</script>

<style lang="less">
.x-table-easy-column-hidden {
}
</style>
