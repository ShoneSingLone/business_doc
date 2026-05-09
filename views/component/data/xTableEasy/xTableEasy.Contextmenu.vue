<template>
  <DocContentOfDemo class="x-table-easy-contextmenu">
    <xMd :md="mdTips" />
    <DemoAndCode title="右键菜单" path="@/views/component/data/xTableEasy/xTableEasy.Contextmenu.Base.vue" />
    <xMd :md="apiString" data-role="api" />
  </DocContentOfDemo>
</template>
<script lang="ts">
export default async function () {
  return {
    data() {
      return {
        mdTips: `
- 1、通过 contextmenuBodyOption 属性配置右键菜单
- 2、支持自定义菜单项和点击事件
- 3、右键点击表格行时显示菜单
        `,
        apiString: `
## API

### contextmenuBodyOption 配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| contextmenus | 菜单项数组 | Array | [] |

### contextmenus 项配置

| 属性 | 说明 | 类型 |
|------|------|------|
| label | 菜单项显示文本 | String |
| action | 点击菜单项时的回调函数 | Function(row, rowIndex) |
| disabled | 是否禁用 | Boolean/Function |
| children | 子菜单数组 | Array |
        `
      };
    }
  };
}
</script>
<style lang="less">
.x-table-easy-contextmenu {
}
</style>