# 11. 列隐藏（column-hidden）

## 11.1 功能说明

通过 `hidden` 属性控制列的显示和隐藏。

---

## 11.2 默认隐藏

设置 `hidden: true` 默认隐藏列。

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
        { field: "id", title: "ID", width: 80 },
        { field: "name", title: "姓名", width: 120 },
        { field: "secret", title: "敏感信息", width: 150, hidden: true }
      ],
      tableData: [...]
    };
  }
};
</script>
```

---

## 11.3 动态控制

通过函数动态控制列的显示和隐藏。

---

## 11.4 实例方法

| 方法名 | 说明 |
|--------|------|
| showColumn(columnKey) | 显示指定列 |
| hideColumn(columnKey) | 隐藏指定列 |

---

## 11.5 API

### hidden

列隐藏配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| hidden | 是否隐藏 | Boolean/Function | `false` |

---

[返回模块索引](../10-module-design.md)