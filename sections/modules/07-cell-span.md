# 7. 单元格合并（cell-span）

## 7.1 功能说明

通过 `span-method` 属性配置单元格合并。

---

## 7.2 跨行合并

通过 `rowspan` 实现跨行合并。

**配置示例**：
```vue
<template>
  <xTableEasy :columns="columns" :table-data="tableData" :span-method="spanMethod" />
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
    spanMethod({ row, column, rowIndex, columnIndex }) {
      if (columnIndex === 0) {
        if (rowIndex % 2 === 0) {
          return { rowspan: 2, colspan: 1 };
        } else {
          return { rowspan: 0, colspan: 0 };
        }
      }
    }
  }
};
</script>
```

---

## 7.3 跨列合并

通过 `colspan` 实现跨列合并。

---

## 7.4 自定义合并内容

自定义合并单元格的显示内容。

---

## 7.5 API

### span-method

合并方法

| 参数 | 说明 | 类型 |
|------|------|------|
| row | 当前行数据 | Object |
| column | 当前列配置 | Object |
| rowIndex | 行索引 | Number |
| columnIndex | 列索引 | Number |

**返回值**：
| 属性 | 说明 | 类型 |
|------|------|------|
| rowspan | 跨行数 | Number |
| colspan | 跨列数 | Number |

---

[返回模块索引](../10-module-design.md)