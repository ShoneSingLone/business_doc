# 23. 表头排序（header-sort）

## 23.1 功能说明

通过 `sort` 属性配置表头排序功能。

---

## 23.2 单条件排序

默认只支持单选排序。

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
        { field: "name", title: "姓名", width: 120, sort: true },
        { field: "age", title: "年龄", width: 80, sort: true }
      ],
      tableData: [...]
    };
  }
};
</script>
```

---

## 23.3 多条件排序

设置 `multiple-sort` 开启多条件排序。

---

## 23.4 始终排序

设置 `sort-always` 使排序始终生效。

---

## 23.5 API

### sort

排序配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| sort | 是否可排序 | Boolean | `false` |
| sortType | 默认排序类型 | String | - |
| multiple-sort | 是否支持多条件排序 | Boolean | `false` |

### 事件

| 事件名 | 说明 | 参数 |
|--------|------|------|
| sortChange | 排序状态改变 | `sortInfo` |

---

[返回模块索引](../10-module-design.md)