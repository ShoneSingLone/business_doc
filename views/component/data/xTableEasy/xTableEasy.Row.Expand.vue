<template>
  <DocContentOfDemo class="x-table-easy-row-expand">
    <xMd :md="mdTips" />
    <DemoAndCode title="行展开" path="@/views/component/data/xTableEasy/xTableEasy.Row.Expand.Base.vue" />
    <xMd :md="apiString" data-role="api" />
  </DocContentOfDemo>
</template>
<script lang="ts">
export default async function () {
  return {
    data() {
      return {
        mdTips: `
- 1、通过 \`expand-option\` 属性配置行展开功能
- 2、支持自定义展开内容的渲染
- 3、展开行可以显示更多详细信息
        `,
        apiString: `
## API

### expandOption 配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| enable | 是否启用行展开 | Boolean | false |
| render | 展开内容渲染函数 | Function(row, rowIndex) | - |
        `
      };
    }
  };
}
</script>
<style lang="less">
.x-table-easy-row-expand {
}
</style>