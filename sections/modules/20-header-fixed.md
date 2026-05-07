# 20. 表头固定（header-fixed）

## 20.1 功能说明

通过 `fixed-header` 属性固定表头，滚动时表头保持可见。

---

## 20.2 基础用法

启用表头固定功能。

**配置示例**：
```vue
<template>
  <xTableEasy :columns="columns" :table-data="tableData" fixed-header :max-height="300" />
</template>
<script>
export default {
  data() {
    return {
      columns: [...],
      tableData: [...]
    };
  }
};
</script>
```

---

## 20.3 禁用表头固定

设置 `fixed-header: false` 禁用表头固定。

---

## 20.4 多级表头固定

支持多级表头的固定。

---

## 20.5 API

### fixed-header

表头固定配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| fixed-header | 是否固定表头 | Boolean | `false` |
| max-height | 表格最大高度 | String/Number | - |

---

[返回模块索引](../10-module-design.md)