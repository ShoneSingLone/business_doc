# 8. 单元格样式（cell-style）

## 8.1 功能说明

**配置要点**：
1. 通过配置对象 `cell-style-option` 设置单元格的样式
2. 支持通过回调函数动态设置符合条件的单元格 class
3. `<style>` 标签不可以使用 `scoped` 属性
4. 也可以通过 `renderBodyCell`、`renderHeaderCell`、`renderFooterCell` 等实现单元格样式的自定义功能

---

## 8.2 表体单元格样式

通过 `bodyCellClass` 回调函数设置表体单元格样式。

**配置示例**：
```vue
<template>
  <xTableEasy
    :columns="columns"
    :table-data="tableData"
    :cell-style-option="cellStyleOption" />
  <style>
    .highlight-cell {
      background-color: #fff7e6;
      color: #d46b08;
    }
  </style>
</template>
<script>
export default {
  data() {
    return {
      cellStyleOption: {
        bodyCellClass: ({ row, column, rowIndex }) => {
          if (column.field === "score") {
            if (row.score >= 80) {
              return "highlight-cell";
            }
          }
        }
      },
      columns: [
        { field: "name", title: "姓名" },
        { field: "score", title: "分数" }
      ],
      tableData: [...]
    };
  }
};
</script>
```

---

## 8.3 表体行样式

通过 `bodyRowClass` 回调函数设置表体行样式。

**配置示例**：
```vue
<template>
  <xTableEasy
    :columns="columns"
    :table-data="tableData"
    :cell-style-option="cellStyleOption" />
  <style>
    .highlight-row {
      background-color: #f6ffed;
    }
  </style>
</template>
<script>
export default {
  data() {
    return {
      cellStyleOption: {
        bodyRowClass: ({ row, rowIndex }) => {
          if (row.status === "success") {
            return "highlight-row";
          }
        }
      },
      columns: [...],
      tableData: [...]
    };
  }
};
</script>
```

---

## 8.4 表头单元格样式

通过 `headerCellClass` 回调函数设置表头单元格样式。

**配置示例**：
```vue
<template>
  <xTableEasy
    :columns="columns"
    :table-data="tableData"
    :cell-style-option="cellStyleOption" />
  <style>
    .header-required {
      color: #f5222d;
      font-weight: bold;
    }
  </style>
</template>
<script>
export default {
  data() {
    return {
      cellStyleOption: {
        headerCellClass: ({ column, rowIndex }) => {
          if (column.required) {
            return "header-required";
          }
        }
      },
      columns: [
        { field: "name", title: "姓名", required: true },
        { field: "age", title: "年龄" }
      ],
      tableData: [...]
    };
  }
};
</script>
```

---

## 8.5 表头行样式

通过 `headerRowClass` 回调函数设置表头行样式。

**配置示例**：
```vue
<template>
  <xTableEasy
    :columns="columns"
    :table-data="tableData"
    :cell-style-option="cellStyleOption" />
  <style>
    .custom-header-row {
      background-color: #f0f5ff;
    }
  </style>
</template>
<script>
export default {
  data() {
    return {
      cellStyleOption: {
        headerRowClass: ({ rowIndex }) => {
          if (rowIndex === 0) {
            return "custom-header-row";
          }
        }
      },
      columns: [...],
      tableData: [...]
    };
  }
};
</script>
```

---

## 8.6 页脚单元格样式

通过 `footerCellClass` 回调函数设置页脚单元格样式。

**配置示例**：
```vue
<template>
  <xTableEasy
    :columns="columns"
    :table-data="tableData"
    :footer-data="footerData"
    :cell-style-option="cellStyleOption" />
  <style>
    .footer-total {
      font-weight: bold;
      color: #1890ff;
    }
  </style>
</template>
<script>
export default {
  data() {
    return {
      cellStyleOption: {
        footerCellClass: ({ row, column, rowIndex }) => {
          if (column.field === "total") {
            return "footer-total";
          }
        }
      },
      columns: [...],
      tableData: [...],
      footerData: [...]
    };
  }
};
</script>
```

---

## 8.7 API

### cell-style-option

单元格样式配置

| 属性 | 说明 | 类型 |
|------|------|------|
| bodyCellClass | 表体单元格 class 回调函数 | Function |
| bodyRowClass | 表体行 class 回调函数 | Function |
| headerCellClass | 表头单元格 class 回调函数 | Function |
| headerRowClass | 表头行 class 回调函数 | Function |
| footerCellClass | 页脚单元格 class 回调函数 | Function |
| footerRowClass | 页脚行 class 回调函数 | Function |

### bodyCellClass 参数

| 参数 | 说明 | 类型 |
|------|------|------|
| row | 当前行数据 | Object |
| column | 当前列配置 | Object |
| rowIndex | 行索引 | Number |

### bodyRowClass 参数

| 参数 | 说明 | 类型 |
|------|------|------|
| row | 当前行数据 | Object |
| rowIndex | 行索引 | Number |

### headerCellClass 参数

| 参数 | 说明 | 类型 |
|------|------|------|
| column | 当前列配置 | Object |
| rowIndex | 行索引 | Number |

### headerRowClass 参数

| 参数 | 说明 | 类型 |
|------|------|------|
| rowIndex | 行索引 | Number |

---

[返回模块索引](../10-module-design.md)