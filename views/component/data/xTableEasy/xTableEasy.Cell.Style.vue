<template>
  <DocContentOfDemo class="x-table-easy-cell-style">
    <xMd :md="mdTips" />
    <DemoAndCode title="单元格样式" path="@/views/component/data/xTableEasy/xTableEasy.Cell.Style.Base.vue" />
    <xMd :md="apiString" data-role="api" />
  </DocContentOfDemo>
</template>
<script lang="ts">
export default async function () {
  return {
    data() {
      return {
        mdTips: `
- 1、通过 cellStyleOption 属性自定义单元格样式
- 2、支持根据行、列、索引等条件动态设置样式
- 3、可实现斑马纹、高亮等效果
        `,
        apiString: `
## API

### cellStyleOption 配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| cellStyle | 单元格样式回调函数 | Function(row, column, rowIndex, colIndex) | - |
| rowStyle | 行样式回调函数 | Function(row, rowIndex) | - |

### 返回值

回调函数应返回一个样式对象，例如：
\`\`\`javascript
{
  backgroundColor: '#f9f9f9',
  color: '#ff4d4f',
  fontWeight: 'bold'
}
\`\`\`
        `
      };
    }
  };
}
</script>
<style lang="less">
.x-table-easy-cell-style {
}
</style>