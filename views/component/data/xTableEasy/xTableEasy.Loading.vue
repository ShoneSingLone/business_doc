<template>
  <DocContentOfDemo class="x-table-easy-loading">
    <xMd :md="mdTips" />
    <DemoAndCode title="加载状态" path="@/views/component/data/xTableEasy/xTableEasy.Loading.Base.vue" unfold />
    <xMd :md="apiString" data-role="api" />
  </DocContentOfDemo>
</template>
<script lang="ts">
export default async function () {
  return {
    data() {
      return {
        mdTips: `
- 1、通过 \`loading\` 属性控制表格的加载状态
- 2、\`loading\` 为 \`true\` 时显示加载动画
- 3、常用于数据加载时的loading效果
        `,
        apiString: `
## API

### 加载状态配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| loading | 是否显示加载状态 | Boolean | false |
        `
      };
    }
  };
}
</script>
<style lang="less">
.x-table-easy-loading {
}
</style>