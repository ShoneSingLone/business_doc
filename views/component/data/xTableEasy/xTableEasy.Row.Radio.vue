<template>
	<DocContentOfDemo class="x-table-easy-row-radio">
		<xMd :md="mdTips" />
		<DemoAndCode
			title="基础功能"
			path="@/views/component/data/xTableEasy/xTableEasy.Row.Radio.Base.vue"
			unfold />
		<DemoAndCode
			title="默认选中"
			path="@/views/component/data/xTableEasy/xTableEasy.Row.Radio.Default.vue"
			unfold />
		<DemoAndCode
			title="禁用选择"
			path="@/views/component/data/xTableEasy/xTableEasy.Row.Radio.Disabled.vue"
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
- 1、表格支持行单选功能，通过 radio 列实现
- 2、通过 radioOption 配置单选行为和事件回调
- 3、支持默认选中、禁用选择等功能
`,
				apiString: `
## API

### radioOption 配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| trigger | 触发方式，可选 row / cell | String | 'row' |
| selectedRowKey | 当前选中的行 key | String/Number | - |
| defaultSelectedRowKey | 默认选中的行 key | String/Number | - |
| disabledRowKeys | 禁用选择的行 key 数组 | Array | [] |
| selectedRowChange | 选中状态变化事件 | Function({row}) | - |

### 列配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| type | 列类型，设为 "radio" | String | - |
| width | 列宽度 | Number | 50 |
`
			};
		}
	};
}
</script>

<style lang="less">
.x-table-easy-row-radio {
}
</style>
