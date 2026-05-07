<template>
  <DocContentOfDemo class="x-table-easy-sort">
    <xMd :md="mdTips" />
    <DemoAndCode title="表头排序" path="xTableEasy.Sort.Base.vue" />
    <xMd :md="apiString" data-role="api" />
  </DocContentOfDemo>
</template>
<script lang="ts">
export default async function () {
  return {
    data() {
      return {
        mdTips: `
- 1、表格支持通过外部排序逻辑实现表头排序
- 2、点击表头或使用按钮触发排序
- 3、排序后的数据重新传递给表格组件
        `,
        apiString: `
## API

### 排序实现方式

通过在外部实现排序逻辑，然后将排序后的数据传递给表格组件。

### 示例代码

\`\`\`javascript
// 按姓名排序
sortByName() {
  this.sortedData = [...this.sortedData].sort((a, b) => {
    return a.name.localeCompare(b.name);
  });
}

// 按日期排序
sortByDate() {
  this.sortedData = [...this.sortedData].sort((a, b) => {
    return new Date(a.date) - new Date(b.date);
  });
}
\`\`\`
        `
      };
    }
  };
}
</script>
<style lang="less">
.x-table-easy-sort {
}
</style>