# 4. 单元格编辑（cell-edit）

## 4.1 功能说明

1. 通过 `editOption` 属性配置单元格编辑功能
2. 通过 `columns` 对象设置 `edit=true` 允许编辑的列

---

## 4.2 基础用法

开启单元格编辑功能。

**配置示例**：
```vue
<template>
  <xTableEasy
    :columns="columns"
    :table-data="tableData"
    :edit-option="editOption" />
</template>
<script>
export default {
  data() {
    return {
      editOption: {
        trigger: 'click',
        mode: 'cell'
      },
      columns: [
        { field: "name", title: "姓名", edit: true },
        { field: "age", title: "年龄", edit: true },
        { field: "score", title: "分数", edit: true }
      ],
      tableData: [...]
    };
  }
};
</script>
```

---

## 4.3 快捷键

可编辑单元格支持以下快捷键（参考 excel 快捷键）：

| 功能 | 快捷键 |
|------|--------|
| 活动单元格进入编辑状态 | `F2` |
| 停止编辑状态，并停留在当前单元格 | `Ctrl` + `Enter` |
| 单元格内文本换行 | `Alt` + `Enter` |
| 清空活动单元格内容 | `Delete` |
| 清空活动单元格内容，并进入编辑状态 | `BackSpace` |
| 清空活动单元格内容并填入空格 | `Space` |
| 停止编辑状态并向下移动活动单元格 | `Enter` |
| 停止编辑状态并向上移动活动单元格 | `Shift` + `Enter` |
| 停止编辑状态并向右移动活动单元格 | `Tab` |
| 停止编辑状态并向左移动活动单元格 | `Shift` + `Tab` |
| 支持在可编辑单元格直接输入文本并进入编辑状态 | - |
| 支持长文本输入时，编辑框自动伸缩功能 | - |

---

## 4.4 实例方法

通过实例方法控制编辑状态：

| 方法名 | 说明 | 参数 |
|--------|------|------|
| startEdit(rowKey, columnKey) | 开始编辑指定单元格 | `rowKey`: 行标识, `columnKey`: 列标识 |
| stopEdit() | 停止当前编辑 | 无 |

**使用示例**：
```vue
<template>
  <xTableEasy
    ref="tableRef"
    :columns="columns"
    :table-data="tableData"
    :edit-option="editOption" />
</template>
<script>
export default {
  methods: {
    editCell(rowKey, columnKey) {
      this.$refs.tableRef.startEdit(rowKey, columnKey);
    },
    stopEditCell() {
      this.$refs.tableRef.stopEdit();
    }
  }
};
</script>
```

---

## 4.5 结合列固定

在固定列中使用编辑功能。

**配置示例**：
```vue
<template>
  <xTableEasy
    :columns="columns"
    :table-data="tableData"
    :edit-option="editOption" />
</template>
<script>
export default {
  data() {
    return {
      editOption: {
        trigger: 'click'
      },
      columns: [
        { field: "name", title: "姓名", fixed: "left", edit: true },
        { field: "age", title: "年龄", edit: true },
        { field: "score", title: "分数", fixed: "right", edit: true }
      ],
      tableData: [...]
    };
  }
};
</script>
```

---

## 4.6 结合 Element UI

使用 Element UI 组件作为编辑器。

**配置示例**：
```vue
<template>
  <xTableEasy
    :columns="columns"
    :table-data="tableData"
    :edit-option="editOption" />
</template>
<script>
export default {
  data() {
    return {
      editOption: {
        trigger: 'click',
        customEditCell: ({ row, column, rowIndex, columnIndex }) => {
          if (column.field === 'status') {
            return {
              component: 'el-select',
              props: {
                value: row[column.field],
                options: [
                  { label: '启用', value: 1 },
                  { label: '禁用', value: 0 }
                ]
              },
              event: {
                change: (value) => {
                  row[column.field] = value;
                }
              }
            };
          }
        }
      },
      columns: [
        { field: "name", title: "姓名", edit: true },
        { field: "status", title: "状态", edit: true }
      ],
      tableData: [...]
    };
  }
};
</script>
```

---

## 4.7 API

### editOption

编辑配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| trigger | 触发方式 | String | `dblclick` |
| mode | 编辑模式 | String | `cell` |
| customEditCell | 自定义编辑器函数 | Function | - |

### 列配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| edit | 是否可编辑 | Boolean | `false` |
| editType | 编辑器类型 | String | `input` |
| editOptions | 下拉选项（当 editType 为 select 时） | Array | - |

### 事件

| 事件名 | 说明 | 参数 |
|--------|------|------|
| editStart | 开始编辑 | `row`, `column` |
| editEnd | 结束编辑 | `row`, `column`, `value` |

---

[返回模块索引](../10-module-design.md)