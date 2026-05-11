﻿<template>
  <DocContentOfDemo class="x-table-easy-action-column">
    <xMd :md="mdTips" />
    <DemoAndCode title="操作列" path="@/views/component/data/xTableEasy/xTableEasy.Action.Column.Base.vue" unfold />
    <xMd :md="apiString" data-role="api" />
  </DocContentOfDemo>
</template>
<script lang="ts">
export default async function () {
  return {
    data() {
      return {
        mdTips: `
- 1、通过在 columns 中配置 render 函数实现操作列
- 2、支持自定义按钮、链接等操作元素
- 3、操作按钮可以绑定点击事件处理业务逻辑
        `,
        apiString: `
## API

### 列配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| render | 自定义渲染函数 | Function(row, column, rowIndex, colIndex) | - |

### render 函数

\`\`\`javascript
render: (row, column, rowIndex, colIndex) => {
  return \`
    <el-button type="primary" size="small" @click="handleEdit('\${rowIndex}')">编辑</el-button>
    <el-button type="danger" size="small" @click="handleDelete('\${rowIndex}')">删除</el-button>
  \`;
}
\`\`\`

### 注意事项

- render 函数返回 HTML 字符串
- 需要使用模板字符串绑定事件处理函数
- 事件处理函数定义在组件的 methods 中
        `
      };
    }
  };
}
</script>
<style lang="less">
.x-table-easy-action-column {
}
</style>