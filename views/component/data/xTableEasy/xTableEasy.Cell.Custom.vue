<template>
  <DocContentOfDemo class="x-table-easy-cell-custom">
    <xMd :md="mdTips" />
    <DemoAndCode title="自定义单元格" path="@/views/component/data/xTableEasy/xTableEasy.Cell.Custom.Base.vue" unfold />
    <xMd :md="apiString" data-role="api" />
  </DocContentOfDemo>
</template>
<script lang="ts">
export default async function () {
  return {
    data() {
      return {
        mdTips: `
- 1、通过 columns 配置中的 \`render\` 函数自定义表体单元格渲染
- 2、通过 columns 配置中的 \`renderHeaderCell\` 函数自定义表头单元格渲染
- 3、可以渲染任意HTML内容，包括按钮、输入框等交互元素
- 4、支持条件渲染和自定义样式
        `,
        apiString: `
## API

### 列配置

| 属性 | 说明 | 类型 |
|------|------|------|
| render | 表体单元格渲染函数 | Function(row, column, rowIndex, colIndex) |
| renderHeaderCell | 表头单元格渲染函数 | Function(column) |

### render 函数参数

| 参数 | 说明 | 类型 |
|------|------|------|
| row | 当前行数据 | Object |
| column | 当前列配置 | Object |
| rowIndex | 行索引 | Number |
| colIndex | 列索引 | Number |

### renderHeaderCell 函数参数

| 参数 | 说明 | 类型 |
|------|------|------|
| column | 当前列配置 | Object |

### 使用示例

**表体单元格自定义（带按钮）**：
\`\`\`javascript
render: (row, column, rowIndex, colIndex) => {
  return \`
    <el-button type="primary" size="small">编辑</el-button>
    <el-button type="danger" size="small">删除</el-button>
  \`;
}
\`\`\`

**表头单元格自定义（带输入框）**：
\`\`\`javascript
renderHeaderCell: (column) => {
  return \`<input type="text" placeholder="搜索" style="width:90%;" />\`;
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