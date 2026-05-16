﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿<template>
  <DocContentOfDemo class="x-table-easy-cell-selection">
    <xMd :md="mdTips" />
    <DemoAndCode title="单元格选择" path="@/views/component/data/xTableEasy/xTableEasy.Cell.Selection.Base.vue" unfold />
    <xMd :md="apiString" data-role="api" />
  </DocContentOfDemo>
</template>
<script lang="ts">
export default async function () {
  return {
    data() {
      return {
        mdTips: `
- 1、通过 cellSelectionOption 属性启用单元格选择功能
- 2、支持单击选中、拖拽选择、Shift+点击范围选择
- 3、选中的单元格会高亮显示
        `,
        apiString: `
## API

### cellSelectionOption 配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| enable | 是否启用单元格选择 | Boolean | false |
| trigger | 触发方式 | String('click'/'cell') | 'click' |

### 实例方法

| 方法名 | 说明 |
|--------|------|
| clearCellSelectionCurrentCell | 清除当前选中状态 |
| getSelectedCells | 获取选中的单元格信息 |

### 快捷键

| 快捷键 | 说明 |
|--------|------|
| Ctrl+A | 全选所有单元格 |
| Delete/Backspace | 删除选中内容 |
        `
      };
    }
  };
}
</script>
<style lang="less">
.x-table-easy-cell-selection {
}
</style>