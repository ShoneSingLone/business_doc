<template>
  <DocContentOfDemo class="x-table-easy-cell-align">
    <xMd :md="mdTips" />
    <DemoAndCode title="单元格对齐" path="@/views/component/data/xTableEasy/xTableEasy.Cell.Align.Base.vue" unfold />
    <xMd :md="apiString" data-role="api" />
  </DocContentOfDemo>
</template>
<script lang="ts">
export default async function () {
  return {
    data() {
      return {
        mdTips: `
- 1、通过 columns 配置中的 align 属性控制单元格对齐
- 2、支持左对齐、居中对齐、右对齐三种方式
- 3、对齐方式同时作用于表头和表体单元格
        `,
        apiString: `
## API

### 列配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| align | 单元格对齐方式 | String | 'left' |

### align 可选值

| 值 | 说明 |
|----|------|
| left | 左对齐 |
| center | 居中对齐 |
| right | 右对齐 |

### 示例

\`\`\`javascript
{
  field: "name",
  key: "a",
  title: "姓名",
  align: "center"
}
\`\`\`
        `
      };
    }
  };
}
</script>
<style lang="less">
.x-table-easy-cell-align {
}
</style>