<template>
  <DocContentOfDemo class="x-table-easy-cell-custom">
    <xMd :md="mdTips" />
    <DemoAndCode title="自定义单元格" path="@/views/component/data/xTableEasy/xTableEasy.Cell.Custom.Base.vue" />
    <xMd :md="apiString" data-role="api" />
  </DocContentOfDemo>
</template>
<script lang="ts">
export default async function () {
  return {
    data() {
      return {
        mdTips: `
- 1、通过 columns 配置中的 \`render\` 函数自定义单元格渲染
- 2、可以渲染任意HTML内容
- 3、支持条件渲染和自定义样式
        `,
        apiString: `
## API

### 列配置中的 render 函数

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| render | 单元格渲染函数 | Function(row, column, rowIndex, colIndex) | - |

### render 函数返回值

返回 HTML 字符串，例如：
\`\`\`javascript
render: (row, column, rowIndex, colIndex) => {
  return \`<span style="color: #ff4d4f;">\${row.name}</span>\`;
}
\`\`\`
        `
      };
    }
  };
}
</script>
<style lang="less">
.x-table-easy-cell-custom {
}
</style>