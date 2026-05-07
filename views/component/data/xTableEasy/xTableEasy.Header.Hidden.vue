<template>
  <DocContentOfDemo class="x-table-easy-header-hidden">
    <xMd :md="mdTips" />
    <DemoAndCode title="表头隐藏" path="xTableEasy.Header.Hidden.Base.vue" />
    <xMd :md="apiString" data-role="api" />
  </DocContentOfDemo>
</template>
<script lang="ts">
export default async function () {
  return {
    data() {
      return {
        mdTips: `
- 1、通过设置 showHeader 属性控制表头显示与隐藏
- 2、showHeader 为 true 时显示表头，为 false 时隐藏表头
- 3、适用于只需要展示数据列表的场景
        `,
        apiString: `
## API

### 表头配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| showHeader | 是否显示表头 | Boolean | true |

### 示例

\`\`\`javascript
<xTableEasy
  :columns="columns"
  :table-data="tableData"
  :showHeader="showHeader"
  borderX
  borderY />
\`\`\`
        `
      };
    }
  };
}
</script>
<style lang="less">
.x-table-easy-header-hidden {
}
</style>