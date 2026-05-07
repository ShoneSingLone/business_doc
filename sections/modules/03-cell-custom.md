# 3. 自定义单元格（cell-custom）

## 3.1 功能说明

通过 `renderBodyCell` 和 `renderHeaderCell` 属性自定义单元格内容，支持 JSX 语法。

---

## 3.2 body 自定义单元格

通过 `renderBodyCell` 属性自定义表体单元格内容。

**配置示例**：
```vue
<template>
  <xTableEasy style="width:100%" :columns="columns" :table-data="tableData" />
</template>
<script>
export default {
  data() {
    return {
      columns: [
        {
          field: "",
          key: "a",
          title: "#",
          align: "center",
          renderBodyCell: ({ row, column, rowIndex }, h) => {
            return (
              <span style="color:#1890ff;">
                {++rowIndex}
              </span>
            );
          }
        },
        {
          field: "name",
          key: "b",
          title: "Name"
        },
        {
          field: "",
          key: "c",
          title: "Action",
          renderBodyCell: ({ row, column, rowIndex }, h) => {
            return (
              <span>
                <button onClick={() => this.editRow(rowIndex)}>Edit</button>
                <button onClick={() => this.deleteRow(rowIndex)}>Delete</button>
              </span>
            );
          }
        }
      ],
      tableData: [...]
    };
  },
  methods: {
    editRow(rowIndex) {
      alert(`Edit row: ${rowIndex}`);
    },
    deleteRow(rowIndex) {
      this.tableData.splice(rowIndex, 1);
    }
  }
};
</script>
```

**renderBodyCell 参数**：
| 参数 | 说明 | 类型 |
|------|------|------|
| row | 当前行数据 | Object |
| column | 当前列配置 | Object |
| rowIndex | 行索引 | Number |

---

## 3.3 header 自定义单元格

通过 `renderHeaderCell` 属性自定义表头单元格内容。

**配置示例**：
```vue
<template>
  <xTableEasy style="width:100%" :columns="columns" :table-data="tableData" />
</template>
<script>
export default {
  data() {
    return {
      searchText: "",
      columns: [
        {
          field: "name",
          key: "a",
          title: "Name",
          align: "center",
          renderHeaderCell: ({ column }, h) => {
            return (
              <input
                value={this.searchText}
                onInput={(e) => { this.searchText = e.target.value; }}
                style="width:90%"
                placeholder="请输入名称关键字"
              />
            );
          }
        },
        {
          field: "date",
          key: "b",
          title: "Date",
          renderHeaderCell: ({ column }, h) => {
            return (
              <span style="color:#1890ff;">
                {column.title}
              </span>
            );
          }
        }
      ],
      tableData: [...]
    };
  }
};
</script>
```

**renderHeaderCell 参数**：
| 参数 | 说明 | 类型 |
|------|------|------|
| column | 当前列配置 | Object |

---

## 3.4 更多自定义方式

### 3.4.1 分组表头中使用

`renderHeaderCell` 在表头分组中同样适用。

### 3.4.2 自定义样式

可以在渲染函数中使用内联样式或 CSS 类名。

### 3.4.3 事件处理

支持在渲染函数中绑定事件处理函数。

---

## 3.5 API

### 列配置

| 属性 | 说明 | 类型 |
|------|------|------|
| renderBodyCell | 表体单元格渲染函数 | Function |
| renderHeaderCell | 表头单元格渲染函数 | Function |

---

[返回模块索引](../10-module-design.md)