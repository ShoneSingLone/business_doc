# 7. 右键菜单（contextmenu）

## 7.1 功能说明

1. 有些操作可以通过右键菜单更方便的完成。比如单元格编辑功能，可以通过右键操作很方便的插入行或者移除行
2. 当然你也可以自定义右键菜单功能

---

## 7.2 右键菜单清单

### header 右键菜单清单

| 功能 | 类型 |
|------|------|
| 分割线 | `SEPARATOR` |
| 剪切 | `CUT` |
| 拷贝 | `COPY` |
| 清空列 | `EMPTY_COLUMN` |
| 左列冻结至该列 | `LEFT_FIXED_COLUMN_TO` |
| 右列冻结至该列 | `RIGHT_FIXED_COLUMN_TO` |
| 取消左列冻结至该列 | `CANCEL_LEFT_FIXED_COLUMN_TO` |
| 取消右列冻结至该列 | `CANCEL_RIGHT_FIXED_COLUMN_TO` |

### body 右键菜单清单

| 功能 | 类型 |
|------|------|
| 分割线 | `SEPARATOR` |
| 剪切 | `CUT` |
| 拷贝 | `COPY` |
| 在上方插入行 | `INSERT_ROW_ABOVE` |
| 在下方插入行 | `INSERT_ROW_BELOW` |
| 删除行 | `REMOVE_ROW` |
| 清空行 | `EMPTY_ROW` |
| 清空单元格 | `EMPTY_CELL` |

---

## 7.3 基础用法

右键表格区域查看效果。

**配置示例**：
```vue
<template>
  <xTableEasy
    :max-height="350"
    :scroll-width="1600"
    row-key-field-name="rowKey"
    :fixed-header="true"
    :columns="columns"
    :table-data="tableData"
    :contextmenu-body-option="contextmenuBodyOption"
    :contextmenu-header-option="contextmenuHeaderOption" />
</template>
<script>
export default {
  data() {
    return {
      // contextmenu header option
      contextmenuHeaderOption: {
        beforeShow: ({ isWholeColSelection, selectionRangeKeys, selectionRangeIndexes }) => {
          console.log("---contextmenu header beforeShow--");
        },
        afterMenuClick: ({ type, selectionRangeKeys, selectionRangeIndexes }) => {
          console.log("---contextmenu header afterMenuClick--");
        },
        contextmenus: [
          { type: "CUT" },
          { type: "COPY" },
          { type: "SEPARATOR" },
          { type: "EMPTY_COLUMN" },
          { type: "SEPARATOR" },
          { type: "LEFT_FIXED_COLUMN_TO" },
          { type: "CANCEL_LEFT_FIXED_COLUMN_TO" },
          { type: "RIGHT_FIXED_COLUMN_TO" },
          { type: "CANCEL_RIGHT_FIXED_COLUMN_TO" }
        ]
      },
      // contextmenu body option
      contextmenuBodyOption: {
        beforeShow: ({ isWholeRowSelection, selectionRangeKeys, selectionRangeIndexes }) => {
          console.log("---contextmenu body beforeShow--");
        },
        afterMenuClick: ({ type, selectionRangeKeys, selectionRangeIndexes }) => {
          console.log("---contextmenu body afterMenuClick--");
        },
        contextmenus: [
          { type: "CUT" },
          { type: "COPY" },
          { type: "SEPARATOR" },
          { type: "INSERT_ROW_ABOVE" },
          { type: "INSERT_ROW_BELOW" },
          { type: "SEPARATOR" },
          { type: "REMOVE_ROW" },
          { type: "EMPTY_ROW" },
          { type: "EMPTY_CELL" }
        ]
      },
      columns: [...],
      tableData: [...]
    };
  }
};
</script>
```

---

## 7.4 自定义右键菜单

支持自定义右键菜单项，包括子菜单。

**配置示例**：
```vue
<template>
  <xTableEasy
    :scroll-width="1600"
    :max-height="350"
    row-key-field-name="rowKey"
    :fixed-header="true"
    :columns="columns"
    :table-data="tableData"
    :contextmenu-body-option="contextmenuBodyOption"
    :contextmenu-header-option="contextmenuHeaderOption" />
</template>
<script>
export default {
  data() {
    return {
      contextmenuBodyOption: {
        contextmenus: [
          { type: "CUT" },
          { type: "COPY" },
          { type: "SEPARATOR" },
          {
            type: "custom-empty-row",
            label: "empty row(custom)"
          },
          {
            type: "customType1",
            label: "custom menu",
            children: [
              {
                label: "menu5-1",
                type: "menu5-1-type",
                children: [
                  { label: "menu5-1-1", type: "menu5-1-1-type" },
                  { label: "menu5-2-2", type: "menu5-2-2-type" }
                ]
              },
              { label: "menu5-2", disabled: true },
              { type: "SEPARATOR" },
              { label: "menu5-3", type: "menu5-3-type" }
            ]
          }
        ]
      },
      columns: [...],
      tableData: [...]
    };
  }
};
</script>
```

---

## 7.5 API

### contextmenuHeaderOption

表头右键菜单配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| beforeShow | 菜单显示前回调 | Function | - |
| afterMenuClick | 菜单点击后回调 | Function | - |
| contextmenus | 菜单项数组 | Array | [] |

**contextmenus 配置项**：
| 属性 | 说明 | 类型 |
|------|------|------|
| type | 菜单类型 | String |
| label | 菜单显示文本 | String |
| disabled | 是否禁用 | Boolean |
| children | 子菜单数组 | Array |

**beforeShow 回调参数**：
| 参数 | 说明 | 类型 |
|------|------|------|
| isWholeColSelection | 是否整列选中 | Boolean |
| selectionRangeKeys | 选中范围的键 | Object |
| selectionRangeIndexes | 选中范围的索引 | Object |

**afterMenuClick 回调参数**：
| 参数 | 说明 | 类型 |
|------|------|------|
| type | 菜单类型 | String |
| selectionRangeKeys | 选中范围的键 | Object |
| selectionRangeIndexes | 选中范围的索引 | Object |

### contextmenuBodyOption

表体右键菜单配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| beforeShow | 菜单显示前回调 | Function | - |
| afterMenuClick | 菜单点击后回调 | Function | - |
| contextmenus | 菜单项数组 | Array | [] |

**contextmenus 配置项**：
| 属性 | 说明 | 类型 |
|------|------|------|
| type | 菜单类型 | String |
| label | 菜单显示文本 | String |
| disabled | 是否禁用 | Boolean |
| children | 子菜单数组 | Array |

**beforeShow 回调参数**：
| 参数 | 说明 | 类型 |
|------|------|------|
| isWholeRowSelection | 是否整行选中 | Boolean |
| selectionRangeKeys | 选中范围的键 | Object |
| selectionRangeIndexes | 选中范围的索引 | Object |

**afterMenuClick 回调参数**：
| 参数 | 说明 | 类型 |
|------|------|------|
| type | 菜单类型 | String |
| selectionRangeKeys | 选中范围的键 | Object |
| selectionRangeIndexes | 选中范围的索引 | Object |

---

[返回模块索引](../10-module-design.md)