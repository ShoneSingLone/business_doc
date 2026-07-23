# 15. 空数据（data-empty）

## 15.1 功能说明

通过 `empty-text` 或 `empty-component` 属性配置空数据状态。

---

## 15.2 基础用法

显示空数据提示。

**配置示例**：

```vue
<template>
	<xTableEasy :columns="columns" :table-data="tableData" empty-text="暂无数据" />
</template>
<script>
export default {
  data() {
    return {
      columns: [...],
      tableData: []
    };
  }
};
</script>
```

---

## 15.3 API

### 空数据配置

| 属性            | 说明             | 类型      | 默认值     |
| --------------- | ---------------- | --------- | ---------- |
| empty-text      | 空数据提示文字   | String    | `暂无数据` |
| empty-component | 自定义空数据组件 | Component | -          |

---

[返回模块索引](../10-module-design.md)
