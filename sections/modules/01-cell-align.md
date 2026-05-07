# 1. 单元格对齐（cell-align）

## 1.1 功能说明

通过 `column` 对象的 `align` 属性设置单元格内容的水平对齐方式。

---

## 1.2 基础用法

支持三种对齐方式：左对齐、居中对齐、右对齐。

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
        { field: "name", title: "姓名", align: "left" },
        { field: "age", title: "年龄", align: "center" },
        { field: "score", title: "分数", align: "right" }
      ],
      tableData: [...]
    };
  }
};
</script>
```

---

## 1.3 API

### align

单元格对齐方式

| 属性值 | 说明 | 适用场景 |
|--------|------|---------|
| left | 左对齐 | 文本类型数据 |
| center | 居中对齐 | 状态类数据、标题 |
| right | 右对齐 | 数字类型数据 |

---

[返回模块索引](../10-module-design.md)