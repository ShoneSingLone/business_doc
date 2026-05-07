# 3. 自定义单元格（cell-custom）

## 3.1 功能说明

通过 `render` 或 `formatter` 属性自定义单元格内容。

---

## 3.2 表体单元格自定义

使用 `render` 函数自定义表体单元格内容。

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
        { field: "name", title: "姓名" },
        { 
          field: "status", 
          title: "状态",
          render: (row, column, cellValue) => {
            const statusMap = { 0: '禁用', 1: '启用' };
            return `<span style="color:${cellValue === 1 ? 'green' : 'red'}">${statusMap[cellValue]}</span>`;
          }
        }
      ],
      tableData: [...]
    };
  }
};
</script>
```

---

## 3.3 表头单元格自定义

使用 `renderHeader` 函数自定义表头单元格内容。

---

## 3.4 更多自定义方式

支持自定义样式、事件处理等。

---

## 3.5 API

### 列配置

| 属性 | 说明 | 类型 |
|------|------|------|
| render | 表体单元格渲染函数 | Function |
| renderHeader | 表头单元格渲染函数 | Function |
| formatter | 单元格内容格式化函数 | Function |

---

[返回模块索引](../10-module-design.md)