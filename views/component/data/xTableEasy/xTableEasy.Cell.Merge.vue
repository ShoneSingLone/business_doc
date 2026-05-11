﻿<template>
  <DocContentOfDemo class="x-table-easy-cell-merge">
    <xMd :md="mdTips" />
    <DemoAndCode title="单元格合并" path="@/views/component/data/xTableEasy/xTableEasy.Cell.Merge.Base.vue" unfold />
    <xMd :md="apiString" data-role="api" />
  </DocContentOfDemo>
</template>
<script lang="ts">
export default async function () {
  return {
    data() {
      return {
        mdTips: `
- 1、通过 cellSpanOption 属性实现单元格合并
- 2、支持跨行合并(rowspan)和跨列合并(colspan)
- 3、合并后的单元格会占据多个单元格位置
        `,
        apiString: `
## API

### cellSpanOption 配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| cellSpan | 单元格合并回调函数 | Function(row, column, rowIndex, colIndex) | - |

### 返回值格式

\`\`\`javascript
{
  rowspan: 2,  // 跨行数，0 表示隐藏当前单元格
  colspan: 1   // 跨列数，0 表示隐藏当前单元格
}
\`\`\`

### 注意事项

- 返回 {rowspan: 0, colspan: 0} 表示隐藏该单元格
- 被合并覆盖的单元格需要返回 {colspan: 0} 或 {rowspan: 0}
        `
      };
    }
  };
}
</script>
<style lang="less">
.x-table-easy-cell-merge {
}
</style>