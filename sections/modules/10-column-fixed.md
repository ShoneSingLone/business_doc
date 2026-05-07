# 10. 列固定（column-fixed）

## 10.1 功能说明

通过 `fixed` 属性配置列固定，支持左侧固定、右侧固定、两侧同时固定。

---

## 10.2 左侧固定

设置 `fixed: "left"` 将列固定在左侧。

**配置示例**：
```vue
<template>
  <xTableEasy :columns="columns" :table-data="tableData" />
</template>
<script>
export default {
  data() {
    return {
      columns: [
        { field: "name", title: "姓名", width: 120, fixed: "left" },
        { field: "age", title: "年龄", width: 80 },
        { field: "address", title: "地址", width: 300 }
      ],
      tableData: [...]
    };
  }
};
</script>
```

---

## 10.3 右侧固定

设置 `fixed: "right"` 将列固定在右侧。

---

## 10.4 两侧固定

同时设置左侧和右侧固定列。

---

## 10.5 自适应宽度

固定列支持自适应宽度。

---

## 10.6 API

### fixed

列固定配置

| 属性值 | 说明 |
|--------|------|
| left | 左侧固定 |
| right | 右侧固定 |

---

[返回模块索引](../10-module-design.md)