﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿
<template>
	<DocContentOfDemo class="x-table-easy-clipboard">
		<xMd :md="mdTips" />
		<DemoAndCode
			title="剪贴板功能"
			path="@/views/component/data/xTableEasy/xTableEasy.Clipboard.Base.vue"
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
- 1、通过 cellSelectionOption 启用单元格选择功能
- 2、选中单元格后可以复制内容到剪贴板
- 3、支持按 Ctrl+C 快捷键复制
        `,
				apiString: `
## API

### cellSelectionOption 配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| enable | 是否启用单元格选择 | Boolean | false |

### 快捷键

| 快捷键 | 说明 |
|--------|------|
| Ctrl+C | 复制选中的单元格内容 |
| Ctrl+X | 剪切选中的单元格内容 |
        `
			};
		}
	};
}
</script>
<style lang="less">
.x-table-easy-clipboard {
}
</style>
