# 8. 单元格样式（cell-style）

## 8.1 功能说明

通过 `cellStyle` 或 `cell-style` 属性自定义单元格样式。

---

## 8.2 表体单元格样式

自定义表体单元格样式。

**配置示例**：
```vue
<template>
  <xTableEasy :columns="columns" :table-data="tableData" :cell-style="cellStyle" />
</template>
<script>
export default {
  data() {
    return {
      columns: [...],
      tableData: [...]
    };
  },
  methods: {
    cellStyle({ row, column, rowIndex, columnIndex }) {
      if (column.field === 'score') {
        if (row.score >= 80) {
          return { color: '#27ae60', fontWeight: 'bold' };
        }
      }
    }
  }
};
</script>
```

---

## 8.3 表体行样式

自定义表体行样式。

---

## 8.4 表头单元格样式

自定义表头单元格样式。

---

## 8.5 表头行样式

自定义表头行样式。

---

## 8.6 API

### cellStyle

列级别单元格样式

| 属性 | 说明 | 类型 |
|------|------|------|
| cellStyle | 单元格样式 | Object/Function |

### cell-style

表格级别单元格样式函数

| 参数 | 说明 | 类型 |
|------|------|------|
| row | 当前行数据 | Object |
| column | 当前列配置 | Object |
| rowIndex | 行索引 | Number |
| columnIndex | 列索引 | Number |

### row-style

行样式函数

| 参数 | 说明 | 类型 |
|------|------|------|
| row | 当前行数据 | Object |
| rowIndex | 行索引 | Number |

---

[返回模块索引](../10-module-design.md)