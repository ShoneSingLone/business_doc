﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿<template>
	<DocContentOfDemo class="x-table-easy-header-fixed">
		<xMd :md="mdTips" />
		<DemoAndCode title="表头固定" path="@/views/component/data/xTableEasy/xTableEasy.Header.Fixed.Base.vue" unfold />
		<xMd :md="apiString" data-role="api" />
	</DocContentOfDemo>
</template>
<script lang="ts">
export default async function () {
	return {
		data() {
			return {
				mdTips: `
- 1、通过设置 fixedHeader 属性为 true 来实现表头固定
- 2、配合 maxHeight 属性使用，当内容超过高度时出现滚动条
- 3、表头会固定在顶部，方便用户查看列标题
        `,
				apiString: `
## API

### 表头固定配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| fixedHeader | 是否固定表头 | Boolean | false |
| maxHeight | 表格最大高度 | Number/String | - |

### 注意事项

- fixedHeader 需要配合 maxHeight 使用
- 当表格内容高度超过 maxHeight 时才会出现滚动条
- 表头固定后，表格会自动添加阴影效果区分表头和内容
        `
			};
		}
	};
}
</script>
<style lang="less">
.x-table-easy-header-fixed {
}
</style>
