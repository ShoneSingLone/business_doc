<template>
	<DocContentOfDemo class="x-table-easy-row-checkbox">
		<xMd :md="mdTips" />
		<DemoAndCode
			title="基础功能"
			path="@/views/component/data/xTableEasy/xTableEasy.Row.Checkbox.Base.vue"
			unfold />
		<DemoAndCode
			title="默认选中"
			path="@/views/component/data/xTableEasy/xTableEasy.Row.Checkbox.Default.vue"
			unfold />
		<DemoAndCode
			title="禁止选中"
			path="@/views/component/data/xTableEasy/xTableEasy.Row.Checkbox.Disabled.vue"
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
- 1、表格支持行多选功能，通过 checkbox 列实现
- 2、通过 checkboxOption 配置多选行为和事件回调
- 3、支持默认选中、禁止选中等功能
`,
				apiString: `
## API

### checkboxOption 配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| trigger | 触发方式，可选 row / cell | String | 'row' |
| selectedRowKeys | 选中的行 key 数组 | Array | [] |
| defaultSelectedRowKeys | 默认选中的行 key 数组 | Array | [] |
| disableSelectedRowKeys | 禁止选中的行 key 数组 | Array | [] |
| selectedRowChange | 选中状态变化事件 | Function({row, isSelected, selectedRowKeys}) | - |
| selectedAllChange | 全选状态变化事件 | Function({isSelected, selectedRowKeys}) | - |

### 列配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| type | 列类型，设为 "checkbox" | String | - |
| width | 列宽度 | Number | 50 |
`
			};
		}
	};
}
</script>

<style lang="less">
.x-table-easy-row-checkbox {
}
</style>
