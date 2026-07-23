# 25. 加载状态（loading）

## 25.1 功能说明

通过 `loading` 属性控制表格加载状态。

---

## 25.2 基础用法

显示加载状态。

**配置示例**：

```vue
<template>
	<xTableEasy :loading="loading" :columns="columns" :table-data="tableData" />
</template>
<script>
export default {
  data() {
    return {
      loading: true,
      columns: [...],
      tableData: []
    };
  },
  mounted() {
    setTimeout(() => {
      this.loading = false;
      this.tableData = [...];
    }, 2000);
  }
};
</script>
```

---

## 25.3 API

### loading

加载状态

| 属性    | 说明             | 类型    | 默认值  |
| ------- | ---------------- | ------- | ------- |
| loading | 是否显示加载状态 | Boolean | `false` |

---

[返回模块索引](../10-module-design.md)
