﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿
<template>
	<DocContentOfDemo class="x-table-easy-cell-style">
		<xMd :md="mdTips" />
		<DemoAndCode
			title="表体单元格样式"
			path="@/views/component/data/xTableEasy/xTableEasy.Cell.Style.Base.vue"
			unfold />
		<DemoAndCode
			title="行样式（斑马纹、高亮）"
			path="@/views/component/data/xTableEasy/xTableEasy.Cell.Style.Row.vue"
			unfold />
		<DemoAndCode
			title="表头单元格样式"
			path="@/views/component/data/xTableEasy/xTableEasy.Cell.Style.Header.vue"
			unfold />
		<DemoAndCode
			title="表头行样式"
			path="@/views/component/data/xTableEasy/xTableEasy.Cell.Style.HeaderRow.vue"
			unfold />
		<DemoAndCode
			title="footer 单元格样式"
			path="@/views/component/data/xTableEasy/xTableEasy.Cell.Style.Footer.vue"
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
- 1、通过 cellStyleOption 属性自定义单元格样式
- 2、通过 rowStyleOption 属性设置行样式（斑马纹、高亮）
- 3、支持根据行、列、索引等条件动态设置样式
        `,
				apiString: `
## API

### cellStyleOption 配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| cellStyle | 表体单元格样式回调 | Function(row, column, rowIndex, colIndex) | - |
| headerCellStyle | 表头单元格样式回调 | Function(column, colIndex) | - |

### rowStyleOption 配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| hoverHighlight | 鼠标悬停高亮 | Boolean | true |
| clickHighlight | 点击高亮 | Boolean | true |
| stripe | 斑马纹 | Boolean | false |
        `
			};
		}
	};
}
</script>
<style lang="less">
.x-table-easy-cell-style {
}
</style>
