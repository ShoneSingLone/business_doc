﻿<template>
  <DocContentOfDemo class="x-table-easy-virtual-scroll">
    <xMd :md="mdTips" />
    <DemoAndCode title="虚拟滚动" path="@/views/component/data/xTableEasy/xTableEasy.Virtual.Scroll.Base.vue" unfold />
    <xMd :md="apiString" data-role="api" />
  </DocContentOfDemo>
</template>
<script lang="ts">
export default async function () {
  return {
    data() {
      return {
        mdTips: `
- 1、通过 \`virtual-scroll-option\` 属性启用虚拟滚动
- 2、用于大数据量表格的性能优化
- 3、只渲染可见区域的单元格，减少DOM节点
        `,
        apiString: `
## API

### virtualScrollOption 配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| enable | 是否启用虚拟滚动 | Boolean | false |

### 注意事项

- 虚拟滚动会改变表格的滚动行为
- 确保表格有固定的高度（maxHeight）
- 大数据量场景下建议启用虚拟滚动
        `
      };
    }
  };
}
</script>
<style lang="less">
.x-table-easy-virtual-scroll {
}
</style>