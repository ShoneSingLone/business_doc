<template>
	<DocContentOfDemo class="x-table-easy-header-group">
		<xMd :md="mdTips" />
		<DemoAndCode
			title="表头分组"
			path="@/views/component/data/xTableEasy/xTableEasy.Header.Group.Base.vue" />
		<xMd :md="apiString" data-role="api" />
	</DocContentOfDemo>
</template>
<script lang="ts">
export default async function () {
	return {
		data() {
			return {
				mdTips: `
- 1、通过列配置中的 \`children\` 属性可以实现多级表头
- 2、分组列本身不直接绑定字段，最终渲染的数据列仍然是最末级叶子列
- 3、建议为每个叶子列设置稳定的 \`key\` 和宽度，避免分组表头布局错乱
        `,
				apiString: `
## API

### 分组表头相关列配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| title | 当前表头标题 | String | - |
| key | 当前列唯一标识 | String | - |
| children | 子列数组，用于声明分组表头 | Array | - |
| width | 叶子列宽度 | Number/String | - |
| align | 表头与单元格对齐方式 | String | left |
        `
			};
		}
	};
}
</script>
<style lang="less">
.x-table-easy-header-group {
}
</style>
