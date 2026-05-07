# 4. 单元格编辑（cell-edit）

## 4.1 功能说明

1. 通过 `edit-option` 属性配置单元格编辑功能
2. 通过 `columns` 对象设置 `edit=true` 允许编辑的列
3. 需要指定 `rowKeyFieldName` 属性

---

## 4.2 基础用法

开启单元格编辑功能，支持编辑校验回调。

**配置示例**：
```vue
<template>
  <xTableEasy
    :columns="columns"
    :table-data="tableData"
    rowKeyFieldName="rowKey"
    :edit-option="editOption" />
</template>
<script>
export default {
  data() {
    return {
      editOption: {
        beforeStartCellEditing: ({ row, column, cellValue }) => {
          if (row.rowKey === 0 && column.field === "name") {
            alert("You can't edit this cell.");
            return false;
          }
        },
        beforeCellValueChange: ({ row, column, changeValue }) => {
          if (column.field === "number" && !/^\d+$/.test(changeValue)) {
            alert("请输入数字");
            return false;
          }
        },
        afterCellValueChange: ({ row, column, changeValue }) => {
          console.log("Cell value changed:", changeValue);
        }
      },
      columns: [
        { field: "name", title: "姓名", edit: true },
        { field: "number", title: "数字", edit: true }
      ],
      tableData: [...]
    };
  }
};
</script>
```

**编辑流程说明**：
1. 单元格进入编辑状态前触发 `beforeStartCellEditing` 回调，返回 `false` 阻止进入编辑状态
2. 单元格停止编辑后触发 `beforeCellValueChange` 回调，返回 `false` 阻止编辑，还原为编辑前状态
3. 编辑成功后触发 `afterCellValueChange` 回调

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

通过实例方法控制编辑状态。

**配置示例**：
```vue
<template>
  <div>
    <button @click="startEditingCell(0, 'name')">编辑单元格0-0</button>
    <button @click="startEditingCell(2, 'hobby', '')">编辑并清空单元格</button>
    <xTableEasy
      ref="tableRef"
      :columns="columns"
      :table-data="tableData"
      rowKeyFieldName="rowKey"
      :edit-option="editOption" />
  </div>
</template>
<script>
export default {
  methods: {
    startEditingCell(rowKey, colKey, defaultValue) {
      this.$refs.tableRef.startEditingCell({ rowKey, colKey, defaultValue });
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
    :scroll-width="1600"
    :max-height="500"
    :columns="columns"
    :table-data="tableData"
    rowKeyFieldName="rowKey"
    :edit-option="editOption" />
</template>
<script>
export default {
  data() {
    return {
      editOption: {
        cellValueChange: ({ row, column }) => {
          console.log("Cell value changed");
        }
      },
      columns: [
        { field: "col1", title: "col1", width: 50, fixed: "left", edit: true },
        { field: "col2", title: "col2", edit: true },
        { field: "col3", title: "col3", width: 50, fixed: "right", edit: true }
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
  <div>
    <button @click="submit()">提交</button>
    <xTableEasy
      :columns="columns"
      :table-data="tableData"
      rowKeyFieldName="rowKey"
      :cell-selection-option="{ enable: false }" />
  </div>
</template>
<script>
export default {
  data() {
    return {
      submitData: [],
      columns: [
        { field: "name", title: "Name" },
        {
          field: "date",
          title: "Date",
          renderBodyCell: ({ row, column }, h) => {
            return (
              <el-date-picker
                size="small"
                value={row["date"]}
                on-input={val => {
                  row["date"] = val;
                  this.cellDataChange(row, column, val);
                }}
                type="date"
                value-format="yyyy-MM-dd"
                placeholder="选择日期"></el-date-picker>
            );
          }
        },
        {
          field: "gender",
          title: "Gender",
          renderBodyCell: ({ row, column }, h) => {
            return (
              <el-select
                size="small"
                value={row["gender"]}
                on-input={val => {
                  row["gender"] = val;
                  this.cellDataChange(row, column, val);
                }}
                placeholder="请选择">
                <el-option label="female" value="female"></el-option>
                <el-option label="male" value="male"></el-option>
              </el-select>
            );
          }
        }
      ],
      tableData: [...]
    };
  },
  methods: {
    submit() {
      alert(JSON.stringify(this.submitData));
    },
    cellDataChange(row, column, cellValue) {
      let currentCell = this.submitData.find(
        x => x.rowKey === row["rowKey"] && x.field === column.field
      );
      if (currentCell) {
        currentCell.value = cellValue;
      } else {
        this.submitData.push({
          rowKey: row["rowKey"],
          field: column.field,
          value: cellValue
        });
      }
    }
  }
};
</script>
```

**注意**：组件本身可能会和第三方库组件的快捷键冲突，此时可以通过 `cell-selection-option.enable = false` 禁用单元格选择功能。

---

## 4.7 API

### edit-option

编辑配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| beforeStartCellEditing | 进入编辑状态前回调，返回 false 阻止编辑 | Function | - |
| beforeCellValueChange | 值改变前回调，返回 false 阻止修改 | Function | - |
| afterCellValueChange | 值改变后回调 | Function | - |
| cellValueChange | 值改变回调 | Function | - |

**回调参数说明**：

| 参数 | 说明 | 类型 |
|------|------|------|
| row | 当前行数据 | Object |
| column | 当前列配置 | Object |
| cellValue | 当前单元格值 | Any |
| changeValue | 改变后的值 | Any |

### 列配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| edit | 是否可编辑 | Boolean | `false` |

### 实例方法

| 方法名 | 说明 | 参数 |
|--------|------|------|
| startEditingCell | 开始编辑指定单元格 | `{ rowKey, colKey, defaultValue }` |

---

[返回模块索引](../10-module-design.md)