﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿
<template>
	<DocContentOfDemo class="x-table-easy-data-empty">
		<xMd :md="mdTips" />
		<DemoAndCode
			title="空数据状态"
			path="@/views/component/data/xTableEasy/xTableEasy.Data.Empty.Base.vue"
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
- 1、当表格数据为空时显示空数据提示
- 2、通过 \`empty-text\` 属性自定义空数据提示文本
- 3、可以配合 \`v-if\` 或数据判断来控制空状态显示
        `,
				apiString: `
## API

### 空数据配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| empty-text | 空数据提示文本 | String | 暂无数据 |
        `
			};
		}
	};
}
</script>
<style lang="less">
.x-table-easy-data-empty {
}
</style>
