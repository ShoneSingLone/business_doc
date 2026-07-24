﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿
<template>
	<DocContentOfDemo class="x-table-easy-cell-autofill">
		<xMd :md="mdTips" />
		<DemoAndCode
			title="基本用法"
			path="@/views/component/data/xTableEasy/xTableEasy.Cell.Autofill.Base.vue"
			unfold />
		<DemoAndCode
			title="自动填充方向"
			path="@/views/component/data/xTableEasy/xTableEasy.Cell.Autofill.Direction.vue"
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
- 1、通过 cellAutofillOption 属性启用自动填充功能
- 2、选中单元格后拖动右下角填充柄进行填充
- 3、支持数字序列、日期序列等智能填充
        `,
				apiString: `
## API

### cellAutofillOption 配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| enable | 是否启用自动填充 | Boolean | false |

### 支持的填充类型

| 类型 | 说明 | 示例 |
|------|------|------|
| 复制填充 | 重复复制选中内容 | 1, 1, 1 |
| 数字序列 | 自动递增数字 | 1, 2, 3 |
| 日期序列 | 自动递增日期 | 2024-01-01, 2024-01-02 |
| 文本序列 | 自动递增序号 | Item 1, Item 2 |
        `
			};
		}
	};
}
</script>
<style lang="less">
.x-table-easy-cell-autofill {
}
</style>
