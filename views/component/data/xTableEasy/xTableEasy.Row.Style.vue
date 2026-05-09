<template>
  <DocContentOfDemo class="x-table-easy-row-style">
    <xMd :md="mdTips" />
    <DemoAndCode title="行样式" path="@/views/component/data/xTableEasy/xTableEasy.Row.Style.Base.vue" />
    <xMd :md="apiString" data-role="api" />
  </DocContentOfDemo>
</template>
<script lang="ts">
export default async function () {
  return {
    data() {
      return {
        mdTips: `
- 1、通过 \`rowStyleOption\` 属性自定义行样式
- 2、支持根据行数据动态设置样式
- 3、可实现斑马纹、高亮等效果
        `,
        apiString: `
## API

### rowStyleOption 配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| rowStyle | 行样式回调函数 | Function(row, rowIndex) | - |

### 返回值

回调函数应返回一个样式对象
        `
      };
    }
  };
}
</script>
<style lang="less">
.x-table-easy-row-style {
}
</style>