﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿
<template>
	<DocContentOfDemo class="x-table-easy-instance-methods">
		<xMd :md="mdTips" />
		<DemoAndCode
			title="实例方法"
			path="@/views/component/data/xTableEasy/xTableEasy.Instance.Methods.Base.vue"
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
- 1、通过表格实例可以调用多种方法
- 2、支持滚动到指定行、清除选择、获取选中行等
- 3、通过 \`ref\` 获取表格实例后调用方法
        `,
				apiString: `
## API

### 实例方法

| 方法名 | 说明 | 参数 |
|--------|------|------|
| scrollToRow | 滚动到指定行 | (rowIndex: Number) |
| clearRowSelection | 清除行选中 | - |
| getRowSelection | 获取选中的行 | - |
| clearCellSelectionCurrentCell | 清除单元格选中 | - |
        `
			};
		}
	};
}
</script>
<style lang="less">
.x-table-easy-instance-methods {
}
</style>
