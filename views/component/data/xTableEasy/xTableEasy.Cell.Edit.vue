﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿
<template>
	<DocContentOfDemo class="x-table-easy-cell-edit">
		<xMd :md="mdTips" />
		<DemoAndCode
			title="基本用法"
			path="@/views/component/data/xTableEasy/xTableEasy.Cell.Edit.Base.vue"
			unfold />
		<DemoAndCode
			title="结合固定列"
			path="@/views/component/data/xTableEasy/xTableEasy.Cell.Edit.Fixed.vue"
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
- 1、通过 editOption 属性启用单元格编辑功能
- 2、双击或单击单元格进入编辑模式
- 3、支持与固定列结合使用
        `,
				apiString: `
## API

### editOption 配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| enable | 是否启用编辑 | Boolean | false |
| editMode | 编辑触发方式 | String('click'/'dblclick') | 'dblclick' |
| afterEditCell | 编辑完成回调 | Function({row, column, value, oldValue}) | - |

### 列配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| edit | 是否可编辑 | Boolean | false |
| editRender | 自定义编辑渲染函数 | Function | - |
        `
			};
		}
	};
}
</script>
<style lang="less">
.x-table-easy-cell-edit {
}
</style>
