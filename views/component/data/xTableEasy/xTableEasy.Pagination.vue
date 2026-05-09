<template>
  <DocContentOfDemo class="x-table-easy-pagination">
    <xMd :md="mdTips" />
    <DemoAndCode title="分页功能" path="@/views/component/data/xTableEasy/xTableEasy.Pagination.Base.vue" unfold />
    <xMd :md="apiString" data-role="api" />
  </DocContentOfDemo>
</template>
<script lang="ts">
export default async function () {
  return {
    data() {
      return {
        mdTips: `
- 1、通过 \`pagination\` 属性配置分页功能
- 2、可以设置当前页码、每页条数、总数等
- 3、支持 \`@page-change\` 事件监听页面变化
        `,
        apiString: `
## API

### pagination 配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| currentPage | 当前页码 | Number | 1 |
| pageSize | 每页条数 | Number | 10 |
| total | 数据总条数 | Number | 0 |

### 事件

| 事件名 | 说明 | 参数 |
|--------|------|------|
| page-change | 页码改变时触发 | (page: Number) |
        `
      };
    }
  };
}
</script>
<style lang="less">
.x-table-easy-pagination {
}
</style>