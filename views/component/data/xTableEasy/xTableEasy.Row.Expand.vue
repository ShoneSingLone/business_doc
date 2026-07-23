﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿
<template>
	<DocContentOfDemo class="x-table-easy-row-expand">
		<xMd :md="mdTips" />
		<DemoAndCode
			title="行展开"
			path="@/views/component/data/xTableEasy/xTableEasy.Row.Expand.Base.vue"
			unfold />
		<DemoAndCode
			title="默认展开配置"
			path="@/views/component/data/xTableEasy/xTableEasy.Row.Expand.Default.vue"
			unfold />
		<DemoAndCode
			title="展开表格"
			path="@/views/component/data/xTableEasy/xTableEasy.Row.Expand.Table.vue"
			unfold />
		<DemoAndCode
			title="行展开事件"
			path="@/views/component/data/xTableEasy/xTableEasy.Row.Expand.Event.vue"
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
- 1、通过 \`expand-option\` 属性配置行展开功能
- 2、支持自定义展开内容的渲染
- 3、展开行可以显示更多详细信息
- 4、支持默认展开、展开事件监听等功能
        `,
				apiString: `
## API

### expandOption 配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| enable | 是否启用行展开 | Boolean | false |
| render | 展开内容渲染函数 | Function(row, rowIndex) | - |
| defaultExpandedRowKeys | 默认展开的行 key 数组 | Array | [] |
| beforeExpandRowChange | 展开前回调 | Function({beforeExpandedRowKeys, row, rowIndex}) | - |
| afterExpandRowChange | 展开后回调 | Function({afterExpandedRowKeys, row, rowIndex}) | - |
        `
			};
		}
	};
}
</script>
<style lang="less">
.x-table-easy-row-expand {
}
</style>
