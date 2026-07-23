﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿
<template>
	<DocContentOfDemo class="x-table-easy-row-style">
		<xMd :md="mdTips" />
		<DemoAndCode
			title="自定义行样式"
			path="@/views/component/data/xTableEasy/xTableEasy.Row.Style.Base.vue"
			unfold />
		<DemoAndCode
			title="斑马纹"
			path="@/views/component/data/xTableEasy/xTableEasy.Row.Style.Stripe.vue"
			unfold />
		<DemoAndCode
			title="行 hover 高亮"
			path="@/views/component/data/xTableEasy/xTableEasy.Row.Style.Hover.vue"
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
- 1、通过 \`rowStyleOption\` 属性自定义行样式
- 2、支持斑马纹、hover 高亮、click 高亮
- 3、支持根据行数据动态设置样式
        `,
				apiString: `
## API

### rowStyleOption 配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| rowStyle | 行样式回调函数 | Function(row, rowIndex) | - |
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
.x-table-easy-row-style {
}
</style>
