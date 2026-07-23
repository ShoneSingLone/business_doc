import os

# 定义所有模块内容
modules = {
    '01-cell-align.md': '''# 1. 单元格对齐（cell-align）

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

[返回模块索引](../10-module-design.md)''',
    
    '02-cell-autofill.md': '''# 2. 单元格自动填充（cell-autofill）

## 2.1 功能说明

**配置要点**：
1. 通过 `cell-autofill` 属性开启自动填充功能
2. 支持拖拽填充单元格数据
3. 自动识别序列模式（数字、日期等）

---

## 2.2 基础用法

启用自动填充功能。

---

## 2.3 功能特点

- 支持数字序列填充
- 支持日期序列填充
- 支持复制填充
- 支持自定义填充方向

---

## 2.4 快捷键支持

| 快捷键 | 说明 |
|--------|------|
| Ctrl+拖动 | 强制复制填充 |
| Shift+拖动 | 强制序列填充 |

---

## 2.5 API

### cell-autofill 相关配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| cell-autofill | 是否启用自动填充 | Boolean | `false` |

---

[返回模块索引](../10-module-design.md)''',

    '03-cell-custom.md': '''# 3. 自定义单元格（cell-custom）

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

[返回模块索引](../10-module-design.md)''',

    '04-cell-edit.md': '''# 4. 单元格编辑（cell-edit）

## 4.1 功能说明

**配置要点**：
1. 通过 `editOption` 属性配置编辑功能
2. 通过在 `columns` 设置 `edit` 属性开启该列编辑
3. 双击单元格进入编辑状态

---

## 4.2 基础用法

开启单元格编辑功能。

---

## 4.3 快捷键支持

支持常用编辑快捷键：
- Enter：确认编辑
- Esc：取消编辑
- Tab：切换到下一个单元格

---

## 4.4 实例方法

通过实例方法控制编辑状态：
- `startEdit(rowKey, columnKey)`：开始编辑指定单元格
- `stopEdit()`：停止当前编辑

---

## 4.5 结合列固定

在固定列中使用编辑功能。

---

## 4.6 结合 Element UI

使用 Element UI 组件作为编辑器。

---

## 4.7 API

### editOption

编辑配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| trigger | 触发方式 | String | `dblclick` |
| mode | 编辑模式 | String | `cell` |

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

[返回模块索引](../10-module-design.md)''',

    '05-cell-ellipsis.md': '''# 5. 单元格省略（cell-ellipsis）

## 5.1 功能说明

**配置要点**：
1. 通过 `ellipsis` 属性开启省略功能
2. 单行省略：内容超出宽度时显示省略号
3. 多行省略：内容超出指定行数时显示省略号

---

## 5.2 单行省略

默认单行省略，鼠标悬停显示完整内容。

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
        { field: "name", title: "姓名", width: 100 },
        { field: "address", title: "地址", width: 200, ellipsis: true }
      ],
      tableData: [...]
    };
  }
};
</script>
```

---

## 5.3 多行省略

设置 `ellipsisLine` 属性指定显示行数。

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
        { field: "desc", title: "描述", width: 300, ellipsis: true, ellipsisLine: 3 }
      ],
      tableData: [...]
    };
  }
};
</script>
```

---

## 5.4 API

### ellipsis 相关配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| ellipsis | 是否启用省略 | Boolean | `false` |
| ellipsisLine | 多行省略行数 | Number | `1` |

---

[返回模块索引](../10-module-design.md)''',

    '06-cell-selection.md': '''# 6. 单元格选择（cell-selection）

## 6.1 功能说明

**配置要点**：
1. 通过 `cell-selection` 属性开启单元格选择功能
2. 支持单选、多选、范围选择
3. 支持快捷键操作

---

## 6.2 基础用法

启用单元格选择功能。

---

## 6.3 禁用选择

通过 `disabled` 函数控制某些单元格不可选择。

---

## 6.4 快捷键支持

| 快捷键 | 说明 |
|--------|------|
| Ctrl+点击 | 多选 |
| Shift+点击 | 范围选择 |
| Ctrl+C | 复制选中内容 |

---

## 6.5 实例方法

| 方法名 | 说明 |
|--------|------|
| getSelectedCells() | 获取选中的单元格 |
| clearSelection() | 清除选择 |

---

## 6.6 API

### cell-selection 相关配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| cell-selection | 是否启用单元格选择 | Boolean | `false` |

---

[返回模块索引](../10-module-design.md)''',

    '07-cell-span.md': '''# 7. 单元格合并（cell-span）

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

[返回模块索引](../10-module-design.md)''',

    '08-cell-style.md': '''# 8. 单元格样式（cell-style）

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

[返回模块索引](../10-module-design.md)''',

    '09-clipboard.md': '''# 9. 剪贴板（clipboard）

## 9.1 功能说明

**配置要点**：
1. 通过 `clipboard` 属性开启剪贴板功能
2. 支持复制选中的单元格内容
3. 支持带表头复制

---

## 9.2 基础用法

启用剪贴板功能。

---

## 9.3 功能特点

- 支持选中单元格自动复制
- 支持带表头复制
- 支持快捷键 Ctrl+C

---

## 9.4 API

### clipboard 相关配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| clipboard | 是否启用剪贴板 | Boolean | `false` |
| clipboard-with-header | 是否包含表头 | Boolean | `false` |

---

[返回模块索引](../10-module-design.md)''',

    '10-column-fixed.md': '''# 10. 列固定（column-fixed）

## 10.1 功能说明

通过 `fixed` 属性配置列固定，支持左侧固定、右侧固定、两侧同时固定。

---

## 10.2 左侧固定

设置 `fixed: "left"` 将列固定在左侧。

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
        { field: "name", title: "姓名", width: 120, fixed: "left" },
        { field: "age", title: "年龄", width: 80 },
        { field: "address", title: "地址", width: 300 }
      ],
      tableData: [...]
    };
  }
};
</script>
```

---

## 10.3 右侧固定

设置 `fixed: "right"` 将列固定在右侧。

---

## 10.4 两侧固定

同时设置左侧和右侧固定列。

---

## 10.5 自适应宽度

固定列支持自适应宽度。

---

## 10.6 API

### fixed

列固定配置

| 属性值 | 说明 |
|--------|------|
| left | 左侧固定 |
| right | 右侧固定 |

---

[返回模块索引](../10-module-design.md)''',

    '11-column-hidden.md': '''# 11. 列隐藏（column-hidden）

## 11.1 功能说明

通过 `hidden` 属性控制列的显示和隐藏。

---

## 11.2 默认隐藏

设置 `hidden: true` 默认隐藏列。

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
        { field: "id", title: "ID", width: 80 },
        { field: "name", title: "姓名", width: 120 },
        { field: "secret", title: "敏感信息", width: 150, hidden: true }
      ],
      tableData: [...]
    };
  }
};
</script>
```

---

## 11.3 动态控制

通过函数动态控制列的显示和隐藏。

---

## 11.4 实例方法

| 方法名 | 说明 |
|--------|------|
| showColumn(columnKey) | 显示指定列 |
| hideColumn(columnKey) | 隐藏指定列 |

---

## 11.5 API

### hidden

列隐藏配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| hidden | 是否隐藏 | Boolean/Function | `false` |

---

[返回模块索引](../10-module-design.md)''',

    '12-column-resize.md': '''# 12. 列宽调整（column-resize）

## 12.1 功能说明

通过 `resizable` 属性开启列宽拖拽调整功能。

---

## 12.2 基础用法

启用列宽调整功能。

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
        { field: "name", title: "姓名", width: 120, resizable: true },
        { field: "age", title: "年龄", width: 80, resizable: true }
      ],
      tableData: [...]
    };
  }
};
</script>
```

---

## 12.3 禁用调整

通过 `resizable: false` 禁用某列的宽度调整。

---

## 12.4 API

### resizable

列宽调整配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| resizable | 是否可调整 | Boolean | `false` |
| minWidth | 最小宽度 | Number | - |
| maxWidth | 最大宽度 | Number | - |

---

[返回模块索引](../10-module-design.md)''',

    '13-column-width.md': '''# 13. 列宽（column-width）

## 13.1 功能说明

通过 `width` 属性设置列宽度，支持像素值、百分比和自动宽度。

---

## 13.2 不设置宽度

不设置宽度时，列宽度自动适应内容。

---

## 13.3 像素宽度

设置固定像素宽度。

**配置示例**：`width: 120`

---

## 13.4 百分比宽度

设置百分比宽度。

**配置示例**：`width: "20%"`

---

## 13.5 长文本处理

处理超长文本时的宽度设置。

---

## 13.6 API

### width

列宽度配置

| 属性 | 说明 | 类型 |
|------|------|------|
| width | 列宽度（像素或百分比） | Number/String |
| minWidth | 最小宽度 | Number |
| maxWidth | 最大宽度 | Number |

---

[返回模块索引](../10-module-design.md)''',

    '14-contextmenu.md': '''# 14. 右键菜单（contextmenu）

## 14.1 功能说明

有些操作可以通过右键菜单更方便的完成。比如单元格编辑功能，可以通过右键操作很方便的插入行或者移除行。当然你也可以自定义右键菜单功能。

---

## 14.2 右键菜单清单

### 14.2.1 header 右键菜单清单

| 功能 | 类型 |
| :----------------- | :----------------------------- |
| 分割线 | `SEPARATOR` |
| 剪切 | `CUT` |
| 拷贝 | `COPY` |
| 清空列 | `EMPTY_COLUMN` |
| 左列冻结至该列 | `LEFT_FIXED_COLUMN_TO` |
| 右列冻结至该列 | `RIGHT_FIXED_COLUMN_TO` |
| 取消左列冻结至该列 | `CANCEL_LEFT_FIXED_COLUMN_TO` |
| 取消右列冻结至该列 | `CANCEL_RIGHT_FIXED_COLUMN_TO` |

### 14.2.2 body 右键菜单清单

| 功能 | 类型 |
| :----------- | :----------------- |
| 分割线 | `SEPARATOR` |
| 剪切 | `CUT` |
| 拷贝 | `COPY` |
| 在上方插入行 | `INSERT_ROW_ABOVE` |
| 在下方插入行 | `INSERT_ROW_BELOW` |
| 删除行 | `REMOVE_ROW` |
| 清空行 | `EMPTY_ROW` |
| 清空单元格 | `EMPTY_CELL` |

---

## 14.3 基础用法

右键表格区域查看效果。你可以根据需要进行组合使用。

**基本配置**：
- 通过 `contextmenu-header-option` 配置表头右键菜单
- 通过 `contextmenu-body-option` 配置表体右键菜单
- 每个配置包含 `beforeShow`、`afterMenuClick` 和 `contextmenus` 三个主要属性

---

## 14.4 自定义右键菜单

支持自定义右键菜单功能，包括：
- 自定义菜单项标签
- 嵌套子菜单
- 禁用菜单项
- 自定义菜单类型

---

## 14.5 API

### 14.5.1 contextmenuHeaderOption

header 右键菜单配置

| 属性 | 说明 | 类型 |
|------|------|------|
| beforeShow | 菜单显示前回调，可修改菜单配置 | Function |
| afterMenuClick | 菜单点击后回调 | Function |
| contextmenus | 菜单项配置数组 | Array |

**contextmenus 菜单项配置**：
| 属性 | 说明 | 类型 |
|------|------|------|
| type | 菜单类型 | String |
| label | 自定义标签 | String |
| disabled | 是否禁用 | Boolean |
| children | 子菜单 | Array |

### 14.5.2 contextmenuBodyOption

body 右键菜单配置

| 属性 | 说明 | 类型 |
|------|------|------|
| beforeShow | 菜单显示前回调，可修改菜单配置 | Function |
| afterMenuClick | 菜单点击后回调 | Function |
| contextmenus | 菜单项配置数组 | Array |

**contextmenus 菜单项配置**：
| 属性 | 说明 | 类型 |
|------|------|------|
| type | 菜单类型 | String |
| label | 自定义标签 | String |
| disabled | 是否禁用 | Boolean |
| children | 子菜单 | Array |

---

[返回模块索引](../10-module-design.md)''',

    '15-data-empty.md': '''# 15. 空数据（data-empty）

## 15.1 功能说明

通过 `empty-text` 或 `empty-component` 属性配置空数据状态。

---

## 15.2 基础用法

显示空数据提示。

**配置示例**：
```vue
<template>
  <xTableEasy :columns="columns" :table-data="tableData" empty-text="暂无数据" />
</template>
<script>
export default {
  data() {
    return {
      columns: [...],
      tableData: []
    };
  }
};
</script>
```

---

## 15.3 API

### 空数据配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| empty-text | 空数据提示文字 | String | `暂无数据` |
| empty-component | 自定义空数据组件 | Component | - |

---

[返回模块索引](../10-module-design.md)''',

    '16-event-custom.md': '''# 16. 自定义事件（event-custom）

## 16.1 功能说明

支持自定义事件处理，包括表头行、表头单元格、表体行、表体单元格的点击事件。

---

## 16.2 表头行点击事件

通过 `on-header-row-click` 监听表头行点击事件。

---

## 16.3 表头单元格点击事件

通过 `on-header-cell-click` 监听表头单元格点击事件。

---

## 16.4 表体行点击事件

通过 `on-body-row-click` 监听表体行点击事件。

---

## 16.5 表体单元格点击事件

通过 `on-body-cell-click` 监听表体单元格点击事件。

---

## 16.6 API

### 事件

| 事件名 | 说明 | 参数 |
|--------|------|------|
| on-header-row-click | 表头行点击 | `event`, `row`, `column` |
| on-header-cell-click | 表头单元格点击 | `event`, `row`, `column` |
| on-body-row-click | 表体行点击 | `event`, `row`, `column` |
| on-body-cell-click | 表体单元格点击 | `event`, `row`, `column` |

---

[返回模块索引](../10-module-design.md)''',

    '17-footer-summary.md': '''# 17. 页脚汇总（footer-summary）

## 17.1 功能说明

通过 `summaryOption` 属性配置页脚汇总功能，支持求和、平均值等统计计算。

---

## 17.2 基础用法

配置页脚汇总行。

---

## 17.3 自定义单元格

自定义汇总单元格内容。

---

## 17.4 单元格样式

自定义汇总单元格样式。

---

## 17.5 单元格合并

汇总行单元格合并。

---

## 17.6 固定页脚

固定页脚行。

---

## 17.7 结合列固定

在固定列中显示汇总。

---

## 17.8 虚拟滚动

虚拟滚动模式下的汇总。

---

## 17.9 API

### summaryOption

汇总配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| summaryMethod | 汇总计算方法 | Function | - |

### 事件

| 事件名 | 说明 | 参数 |
|--------|------|------|
| on-footer-row-click | 汇总行点击 | `event`, `row`, `column` |
| on-footer-cell-click | 汇总单元格点击 | `event`, `row`, `column` |

---

[返回模块索引](../10-module-design.md)''',

    '18-header-filter.md': '''# 18. 表头筛选（header-filter）

## 18.1 功能说明

通过 `column` 对象的 `filter` 属性设置筛选功能，支持单条件筛选和多条件筛选。

**配置要点**：
1. 通过 `column` 对象的 `filter` 属性设置筛选功能
2. `filterList` 设置筛选条件，包含 `label`、`value`、`selected` 三个属性
3. `isMultiple` 开启筛选项多选，默认为 false
4. `filterConfirm` 筛选确认函数
5. `filterReset` 筛选重置函数

---

## 18.2 单条件筛选

默认只支持单选筛选，点击表头筛选图标即可打开筛选下拉框。

**特点**：
- 只能选择一个选项
- 适合互斥的筛选条件
- 简单直观

---

## 18.3 多条件筛选

设置 `isMultiple: true` 开启多选模式。

**特点**：
- 可选择多个选项
- 适合组合筛选条件
- 当筛选框内容很多时，可通过 `maxHeight` 属性设置筛选框的最大高度

---

## 18.4 混合使用

根据不同的业务场景，任意搭配使用单条件筛选和多条件筛选。

**特点**：
- 不同列可配置不同筛选模式
- 通过 `selected: true` 设置默认选中的项
- 支持组合筛选逻辑

---

## 18.5 自定义图标

`filterIcon` 回调函数，支持返回自定义的图标。

**特点**：
- 可自定义筛选图标
- 支持使用内置图标或第三方图标库

---

## 18.6 API

### filter

表头筛选配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| filterList | 筛选条件列表 | Array | - |
| isMultiple | 是否多选 | Boolean | `false` |
| maxHeight | 筛选框最大高度 | Number | - |
| filterConfirm | 筛选确认回调 | Function | - |
| filterReset | 筛选重置回调 | Function | - |
| filterIcon | 自定义筛选图标 | Function | - |

**filterList 项配置**：
| 属性 | 说明 | 类型 |
|------|------|------|
| value | 值 | Any |
| label | 显示标签 | String |
| selected | 是否选中 | Boolean |

---

[返回模块索引](../10-module-design.md)''',

    '19-header-filter-custom.md': '''# 19. 自定义表头筛选（header-filter-custom）

## 19.1 功能说明

通过 `filterCustom` 属性配置自定义筛选组件。

---

## 19.2 单条件筛选

使用自定义组件实现单条件筛选。

---

## 19.3 自定义图标

自定义筛选图标。

---

## 19.4 API

### filterCustom

自定义筛选配置

| 属性 | 说明 | 类型 |
|------|------|------|
| filterCustom | 自定义筛选组件 | Component |

---

[返回模块索引](../10-module-design.md)''',

    '20-header-fixed.md': '''# 20. 表头固定（header-fixed）

## 20.1 功能说明

通过 `fixed-header` 属性固定表头，滚动时表头保持可见。

---

## 20.2 基础用法

启用表头固定功能。

**配置示例**：
```vue
<template>
  <xTableEasy :columns="columns" :table-data="tableData" fixed-header :max-height="300" />
</template>
<script>
export default {
  data() {
    return {
      columns: [...],
      tableData: [...]
    };
  }
};
</script>
```

---

## 20.3 禁用表头固定

设置 `fixed-header: false` 禁用表头固定。

---

## 20.4 多级表头固定

支持多级表头的固定。

---

## 20.5 API

### fixed-header

表头固定配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| fixed-header | 是否固定表头 | Boolean | `false` |
| max-height | 表格最大高度 | String/Number | - |

---

[返回模块索引](../10-module-design.md)''',

    '21-header-grouping.md': '''# 21. 表头分组（header-grouping）

## 21.1 功能说明

通过 `columns` 配置实现表头分组功能。

---

## 21.2 基础用法

配置多级表头分组。

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
        { field: "name", title: "姓名", width: 120 },
        {
          title: "成绩",
          children: [
            { field: "math", title: "数学", width: 100 },
            { field: "chinese", title: "语文", width: 100 }
          ]
        }
      ],
      tableData: [...]
    };
  }
};
</script>
```

---

## 21.3 分组表头与固定列

结合列固定功能使用表头分组。

---

## 21.4 API

### columns

表头分组配置

| 属性 | 说明 | 类型 |
|------|------|------|
| title | 分组标题 | String |
| children | 子列配置 | Array |

---

[返回模块索引](../10-module-design.md)''',

    '22-header-hidden.md': '''# 22. 表头隐藏（header-hidden）

## 22.1 功能说明

通过 `show-header` 属性控制表头的显示和隐藏。

---

## 22.2 基础用法

隐藏表头。

**配置示例**：
```vue
<template>
  <xTableEasy :columns="columns" :table-data="tableData" :show-header="false" />
</template>
<script>
export default {
  data() {
    return {
      columns: [...],
      tableData: [...]
    };
  }
};
</script>
```

---

## 22.3 API

### show-header

表头显示配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| show-header | 是否显示表头 | Boolean | `true` |

---

[返回模块索引](../10-module-design.md)''',

    '23-header-sort.md': '''# 23. 表头排序（header-sort）

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

[返回模块索引](../10-module-design.md)''',

    '24-instance-methods.md': '''# 24. 实例方法（instance-methods）

## 24.1 功能说明

表格提供了一些实例方法供外部调用。

---

## 24.2 滚动到指定位置

### 24.2.1 滚动到指定坐标

使用 `scrollTo(x, y)` 方法滚动到指定坐标。

### 24.2.2 滚动到指定行

使用 `scrollToRowKey(rowKey)` 方法滚动到指定行。

### 24.2.3 滚动到指定列

使用 `scrollToColKey(colKey)` 方法滚动到指定列。

---

## 24.3 API

### 实例方法

| 方法名 | 说明 | 参数 |
|--------|------|------|
| scrollTo(x, y) | 滚动到指定坐标 | `x`: 水平位置, `y`: 垂直位置 |
| scrollToRowKey(rowKey) | 滚动到指定行 | `rowKey`: 行标识 |
| scrollToColKey(colKey) | 滚动到指定列 | `colKey`: 列标识 |

---

[返回模块索引](../10-module-design.md)''',

    '25-loading.md': '''# 25. 加载状态（loading）

## 25.1 功能说明

通过 `loading` 属性控制表格加载状态。

---

## 25.2 基础用法

显示加载状态。

**配置示例**：
```vue
<template>
  <xTableEasy :loading="loading" :columns="columns" :table-data="tableData" />
</template>
<script>
export default {
  data() {
    return {
      loading: true,
      columns: [...],
      tableData: []
    };
  },
  mounted() {
    setTimeout(() => {
      this.loading = false;
      this.tableData = [...];
    }, 2000);
  }
};
</script>
```

---

## 25.3 API

### loading

加载状态

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| loading | 是否显示加载状态 | Boolean | `false` |

---

[返回模块索引](../10-module-design.md)''',

    '26-operation-column.md': '''# 26. 操作列（operation-column）

## 26.1 功能说明

通过 `render` 属性配置操作列，添加操作按钮。

---

## 26.2 基础用法

添加操作列。

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
        { field: "name", title: "姓名", width: 120 },
        { 
          title: "操作", 
          width: 200,
          render: (row) => {
            return `
              <button onclick="edit(${row.id})">编辑</button>
              <button onclick="del(${row.id})">删除</button>
            `;
          }
        }
      ],
      tableData: [...]
    };
  },
  methods: {
    edit(id) {
      console.log('编辑:', id);
    },
    del(id) {
      console.log('删除:', id);
    }
  }
};
</script>
```

---

## 26.3 API

### render

操作列渲染函数

| 参数 | 说明 | 类型 |
|------|------|------|
| row | 当前行数据 | Object |
| column | 当前列配置 | Object |
| rowIndex | 行索引 | Number |

---

[返回模块索引](../10-module-design.md)''',

    '27-pagination.md': '''# 27. 分页（pagination）

## 27.1 功能说明

**注意事项**：
1. 表格组件和分页组件是分开的
2. 示例为模拟数据，通常分页需要结合后端服务
3. 数据量很大但不想使用分页时，可以使用虚拟滚动

---

## 27.2 基础分页

结合分页组件实现基础分页功能。

---

## 27.3 带多选的分页

分页时保持多选状态。

---

## 27.4 API

### pagination

分页配置（通常使用独立的分页组件）

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| pageSize | 每页条数 | Number | `10` |
| currentPage | 当前页码 | Number | `1` |
| total | 总条数 | Number | `0` |

---

[返回模块索引](../10-module-design.md)''',

    '28-row-checkbox.md': '''# 28. 行多选（row-checkbox）

## 28.1 功能说明

**配置要点**：
1. 通过 `checkboxOption` 属性开启多选功能
2. 通过在 `columns` 设置 `type=checkbox` 作为多选的列
3. 设置 `rowKeyFieldName` 属性对应行数据的列名
4. `selectedRowChange` 行改变事件，接收 3 个参数：`row`、`isSelected`、`selectedRowKeys`
5. `selectedAllChange` 全选事件，接收 2 个参数：`isSelected`、`selectedRowKeys`

---

## 28.2 基础用法

通过设置 `checkboxOption` 和 `type=checkbox` 列开启多选功能。

---

## 28.3 默认选中

通过 `selectedRowKeys` 设置默认选中的行。

---

## 28.4 禁用行选中

通过 `disabled` 函数控制某些行不可选中。

---

## 28.5 点击行选中

设置 `checkStrictly=false`，点击行即可选中。

---

## 28.6 自定义列位置

将多选列放在任意位置。

---

## 28.7 隐藏全选框

设置 `hideDefaultCheckbox` 隐藏全选框。

---

## 28.8 API

### checkboxOption

多选配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| selectedRowKeys | 默认选中的行 key 数组 | Array | - |
| disabled | 禁用选中的函数 | Function | - |
| checkStrictly | 是否严格模式（仅点击 checkbox 选中） | Boolean | `true` |
| hideDefaultCheckbox | 是否隐藏全选框 | Boolean | `false` |

### 事件

| 事件名 | 说明 | 参数 |
|--------|------|------|
| selectedRowChange | 行选中状态改变 | `row`, `isSelected`, `selectedRowKeys` |
| selectedAllChange | 全选状态改变 | `isSelected`, `selectedRowKeys` |

---

[返回模块索引](../10-module-design.md)''',

    '29-row-expand.md': '''# 29. 行展开（row-expand）

## 29.1 功能说明

**配置要点**：
1. 通过 `expandOption` 属性配置展开行功能
2. 通过在 `columns` 设置 `type=expand` 展开的列
3. 设置 `rowKeyFieldName` 属性对应行数据的列名
4. `render` 函数允许自定义展开内容，支持 jsx 语法

---

## 29.2 基础用法

通过 `expandOption` 和 `type=expand` 列开启行展开功能。

---

## 29.3 默认展开

通过 `expandedRowKeys` 设置默认展开的行。

---

## 29.4 自定义触发方式

设置 `trigger` 属性自定义展开触发方式（click/dblclick）。

---

## 29.5 控制展开

通过 API 控制行的展开和收起。

---

## 29.6 展开事件

监听展开和收起事件。

---

## 29.7 展开表格

在展开区域内嵌表格。

---

## 29.8 展开图表

在展开区域内嵌图表。

---

## 29.9 自定义展开列位置

将展开列放在任意位置。

---

## 29.10 条件展开

通过 `expandable` 函数控制哪些行可以展开。

---

## 29.11 API

### expandOption

展开配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| expandedRowKeys | 默认展开的行 key 数组 | Array | - |
| trigger | 触发方式 | String | `click` |
| expandable | 是否可展开的函数 | Function | - |
| render | 自定义展开内容 | Function | - |

### 事件

| 事件名 | 说明 | 参数 |
|--------|------|------|
| expandChange | 展开状态改变 | `row`, `expanded` |

---

[返回模块索引](../10-module-design.md)''',

    '30-row-index.md': '''# 30. 行序号（row-index）

## 30.1 功能说明

通过 `indexOption` 属性配置行序号功能。

---

## 30.2 基础用法

显示行序号。

---

## 30.3 排名模式

从大到小排序并显示排名。

---

## 30.4 API

### indexOption

序号配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| type | 序号类型 | String | `index` |
| start | 起始序号 | Number | `1` |

---

[返回模块索引](../10-module-design.md)''',

    '31-row-radio.md': '''# 31. 行单选（row-radio）

## 31.1 功能说明

**配置要点**：
1. 通过 `radioOption` 属性开启单选功能
2. 通过在 `columns` 设置 `type=radio` 作为单选的列
3. 设置 `rowKeyFieldName` 属性对应行数据的列名

---

## 31.2 基础用法

通过设置 `radioOption` 和 `type=radio` 列开启单选功能。

---

## 31.3 默认选中

通过 `selectedRowKey` 设置默认选中的行。

---

## 31.4 禁用行选中

通过 `disabled` 函数控制某些行不可选中。

---

## 31.5 点击行选中

设置 `checkStrictly=false`，点击行即可选中。

---

## 31.6 自定义列位置

将单选列放在任意位置。

---

## 31.7 API

### radioOption

单选配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| selectedRowKey | 默认选中的行 key | Any | - |
| disabled | 禁用选中的函数 | Function | - |
| checkStrictly | 是否严格模式（仅点击 radio 选中） | Boolean | `true` |

### 事件

| 事件名 | 说明 | 参数 |
|--------|------|------|
| selectedRowChange | 行选中状态改变 | `row`, `isSelected`, `selectedRowKey` |

---

[返回模块索引](../10-module-design.md)''',

    '32-row-style.md': '''# 32. 行样式（row-style）

## 32.1 功能说明

通过 `rowStyle` 属性自定义行样式。

---

## 32.2 斑马纹效果

通过 `rowStyle` 函数实现斑马纹效果。

**配置示例**：
```vue
<template>
  <xTableEasy :columns="columns" :table-data="tableData" :row-style="rowStyle" />
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
    rowStyle({ rowIndex }) {
      return rowIndex % 2 === 0 
        ? { backgroundColor: '#f8f9fa' } 
        : { backgroundColor: '#ffffff' };
    }
  }
};
</script>
```

---

## 32.3 鼠标悬停高亮

鼠标悬停时高亮行。

---

## 32.4 点击高亮

点击行时高亮。

---

## 32.5 API

### rowStyle

行样式函数

| 参数 | 说明 | 类型 |
|------|------|------|
| row | 当前行数据 | Object |
| rowIndex | 行索引 | Number |

---

[返回模块索引](../10-module-design.md)''',

    '33-table-border.md': '''# 33. 表格边框（table-border）

## 33.1 功能说明

通过 `border` 属性配置表格边框样式。

---

## 33.2 无边框

默认无边框样式。

---

## 33.3 内边框

只显示内部边框。

---

## 33.4 外边框

只显示外边框。

---

## 33.5 全部边框

显示全部边框。

---

## 33.6 纵向边框

只显示纵向边框。

---

## 33.7 横向边框

只显示横向边框。

---

## 33.8 圆角边框

设置圆角边框。

---

## 33.9 API

### border

边框配置

| 属性值 | 说明 |
|--------|------|
| none | 无边框 |
| around | 外边框 |
| inside | 内边框 |
| all | 全部边框 |
| x | 横向边框 |
| y | 纵向边框 |

---

[返回模块索引](../10-module-design.md)''',

    '34-table-height.md': '''# 34. 表格高度（table-height）

## 34.1 功能说明

**配置要点**：
1. 表格高度可以设置固定值。如：`style="height:300px;"`
2. 表格高度可以设置动态值。如：`style="height:calc(100vh - 210px)"`

---

## 34.2 自动高度

表格高度随内容自动调整。

---

## 34.3 固定高度

设置固定像素高度。

**配置示例**：`style="height:300px;"`

---

## 34.4 动态高度（calc css 函数）

使用 calc 函数动态计算高度。

**配置示例**：`style="height:calc(100vh - 210px);"`

---

## 34.5 API

### 表格高度设置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| style | 表格样式，可设置 height 属性 | Object/String | - |
| max-height | 最大高度 | String/Number | - |

---

[返回模块索引](../10-module-design.md)''',

    '36-virtual-scroll.md': '''# 36. 虚拟滚动（virtual-scroll）

## 36.1 功能说明

通过 `virtualScrollOption` 属性配置虚拟滚动，用于处理大数据量表格的性能优化。

---

## 36.2 基础用法

开启虚拟滚动功能。

---

## 36.3 动态启用

根据数据量动态启用虚拟滚动。

---

## 36.4 结合行展开

虚拟滚动模式下使用行展开功能。

---

## 36.5 结合行多选

虚拟滚动模式下使用多选功能。

---

## 36.6 结合行单选

虚拟滚动模式下使用单选功能。

---

## 36.7 结合列固定

虚拟滚动模式下使用列固定功能。

---

## 36.8 结合懒加载

虚拟滚动模式下实现懒加载。

---

## 36.9 API

### virtualScrollOption

虚拟滚动配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| enable | 是否启用 | Boolean | `false` |
| estimatedRowHeight | 预估行高 | Number | `40` |

---

[返回模块索引](../10-module-design.md)'''
}

# 写入所有模块文件
directory = r'e:\ghca_code\m2o\statics\business_doc\sections\modules'
for filename, content in modules.items():
    filepath = os.path.join(directory, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Created: {filename}')

print('All modules created successfully!')
