﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿
<template>
	<DocContentOfDemo class="x-table-easy-sort">
		<xMd :md="mdTips" />
		<DemoAndCode
			title="单字段排序"
			path="@/views/component/data/xTableEasy/xTableEasy.Sort.Base.vue"
			unfold />
		<DemoAndCode
			title="多字段排序"
			path="@/views/component/data/xTableEasy/xTableEasy.Sort.Multi.vue"
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
- 1、表格支持通过外部排序逻辑实现表头排序
- 2、点击表头或使用按钮触发排序
- 3、排序后的数据重新传递给表格组件
- 4、支持单字段排序和多字段排序
        `,
				apiString: `
## API

### sortOption 配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| multipleSort | 是否启用多字段排序 | Boolean | false |
| sortChange | 排序变化回调 | Function(sortColumns) | - |

### 列配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| sortBy | 排序状态 | String | '' |

**sortBy 可选值**：
| 值 | 说明 |
|----|------|
| 'asc' | 升序 |
| 'desc' | 降序 |
| '' | 不排序 |
        `
			};
		}
	};
}
</script>
<style lang="less">
.x-table-easy-sort {
}
</style>
