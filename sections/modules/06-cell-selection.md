# 6. 单元格选择（cell-selection）

## 6.1 功能说明

**配置要点**：

1. 通过 `cell-selection-option` 属性配置单元格选择功能
2. 需要指定 `rowKeyFieldName` 属性
3. 支持单选、多选、范围选择
4. 支持快捷键操作
5. 开启单元格选择会禁用文本选择（`user-select:none`）

---

## 6.2 基础用法

启用单元格选择功能。

**配置示例**：

```vue
<template>
	<xTableEasy
		:columns="columns"
		:table-data="tableData"
		rowKeyFieldName="rowKey"
		:cell-selection-option="cellSelectionOption" />
</template>
<script>
export default {
  data() {
    return {
      cellSelectionOption: {
        enable: true
      },
      columns: [...],
      tableData: [...]
    };
  }
};
</script>
```

---

## 6.3 禁用选择

通过 `cell-selection-option.enable = false` 关闭单元格选择功能。

**配置示例**：

```vue
<template>
	<xTableEasy
		:columns="columns"
		:table-data="tableData"
		rowKeyFieldName="rowKey"
		:cell-selection-option="{ enable: false }" />
</template>
```

---

## 6.4 快捷键支持

单元格选择支持以下快捷键（参考 excel 快捷键）：

| 功能               | 快捷键            |
| ------------------ | ----------------- |
| 向上移动活动单元格 | `↑`               |
| 向右移动活动单元格 | `→`               |
| 向下移动活动单元格 | `↓`               |
| 向左移动活动单元格 | `←`               |
| 向下移动活动单元格 | `Enter`           |
| 向上移动活动单元格 | `Shift` + `Enter` |
| 向右移动活动单元格 | `Tab`             |
| 向左移动活动单元格 | `Shift` + `Tab`   |

---

## 6.5 单选实例方法

通过实例方法设置单元格选中。

**配置示例**：

```vue
<template>
	<div>
		<button @click="setCellSelection(2, 'col5')">选中第3行第5列</button>
		<xTableEasy ref="tableRef" :columns="columns" :table-data="tableData" rowKeyFieldName="rowKey" />
	</div>
</template>
<script>
export default {
	methods: {
		setCellSelection(rowKey, colKey) {
			this.$refs.tableRef.setCellSelection({ rowKey, colKey });
		}
	}
};
</script>
```

---

## 6.6 区域选择实例方法

通过实例方法设置区域单元格选中。

**配置示例**：

```vue
<template>
	<div>
		<button @click="setAllCellSelection()">单元格全选</button>
		<button @click="setRangeCellSelection()">区域选择</button>
		<xTableEasy ref="tableRef" :columns="columns" :table-data="tableData" rowKeyFieldName="rowKey" />
	</div>
</template>
<script>
export default {
	methods: {
		setAllCellSelection() {
			this.$refs.tableRef.setAllCellSelection();
		},
		setRangeCellSelection() {
			this.$refs.tableRef.setRangeCellSelection({
				startRowKey: 3,
				startColKey: "col2",
				endRowKey: 5,
				endColKey: "col4",
				isScrollToStartCell: true
			});
		}
	}
};
</script>
```

---

## 6.7 API

### cell-selection-option

单元格选择配置

| 属性   | 说明               | 类型    | 默认值 |
| ------ | ------------------ | ------- | ------ |
| enable | 是否启用单元格选择 | Boolean | `true` |

### 实例方法

| 方法名                | 说明             | 参数                                                                      |
| --------------------- | ---------------- | ------------------------------------------------------------------------- |
| setCellSelection      | 设置单选单元格   | `{ rowKey, colKey }`                                                      |
| setAllCellSelection   | 设置全选         | 无                                                                        |
| setRangeCellSelection | 设置区域选择     | `{ startRowKey, startColKey, endRowKey, endColKey, isScrollToStartCell }` |
| getSelectedCells      | 获取选中的单元格 | 无                                                                        |
| clearSelection        | 清除选择         | 无                                                                        |

---

[返回模块索引](../10-module-design.md)
