﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿
<template>
	<DocContentOfDemo class="x-table-easy-virtual-scroll">
		<xMd :md="mdTips" />
		<DemoAndCode
			title="基础功能"
			path="@/views/component/data/xTableEasy/xTableEasy.Virtual.Scroll.Base.vue"
			unfold />
		<DemoAndCode
			title="结合行多选"
			path="@/views/component/data/xTableEasy/xTableEasy.Virtual.Scroll.Checkbox.vue"
			unfold />
		<DemoAndCode
			title="结合固定列"
			path="@/views/component/data/xTableEasy/xTableEasy.Virtual.Scroll.Fixed.vue"
			unfold />
		<DemoAndCode
			title="动态开启或关闭虚拟滚动"
			path="@/views/component/data/xTableEasy/xTableEasy.Virtual.Scroll.Toggle.vue"
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
- 1、通过 \`virtual-scroll-option\` 属性启用虚拟滚动
- 2、用于大数据量表格的性能优化
- 3、只渲染可见区域的单元格，减少DOM节点
- 4、支持结合行多选、固定列等功能
- 5、支持动态开启或关闭
- 6、【需求】2026-08-03 虚拟滚动 scroll 处理已内置 rAF 节流：一帧内多次 scroll 只执行一次可视行重算，滚动更顺滑（内部行为，无 API 变化）
        `,
				apiString: `
## API

### virtualScrollOption 配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| enable | 是否启用虚拟滚动 | Boolean | false |
| minRowHeight | 最小行高 | Number | 40 |
| bufferScale | 缓冲比例 | Number | 1 |

### 注意事项

- 虚拟滚动需要设置 \`max-height\` 属性
- 大数据量场景下建议启用虚拟滚动
- 支持动态开启或关闭
        `
			};
		}
	};
}
</script>
<style lang="less">
.x-table-easy-virtual-scroll {
}
</style>
