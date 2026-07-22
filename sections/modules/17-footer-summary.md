# 17. 页脚汇总（footer-summary）

## 17.1 功能说明

1. footer 汇总，允许对表格数据进行汇总展示
2. `footerData` 为 footer 汇总数据。数据结构与 `tableData` 保持一致

---

## 17.2 基础功能

默认汇总数据固定在底部。

**配置示例**：

```vue
<template>
	<xTableEasy
		border-y
		fixed-header
		:max-height="300"
		:columns="columns"
		:table-data="tableData"
		:footer-data="footerData"
		row-key-field-name="rowKey" />
</template>
<script>
export default {
	data() {
		return {
			columns: [
				{ field: "name", key: "a", title: "Name", align: "center" },
				{ field: "date", key: "b", title: "Date", align: "left" },
				{ field: "hobby", key: "c", title: "Hobby", align: "center" },
				{ field: "address", key: "d", title: "Address", align: "left" }
			],
			tableData: [],
			footerData: []
		};
	},
	methods: {
		initTableData() {
			let data = [];
			for (let i = 0; i < 15; i++) {
				data.push({
					rowKey: i,
					name: i,
					date: i,
					hobby: i,
					address: i
				});
			}
			this.tableData = data;
		},
		initFooterData() {
			this.footerData = [
				{
					rowKey: 0,
					name: "平均值",
					date: 213,
					hobby: 355,
					address: 189
				},
				{
					rowKey: 1,
					name: "汇总值",
					date: 1780,
					hobby: 890,
					address: 2988
				}
			];
		}
	},
	created() {
		this.initTableData();
		this.initFooterData();
	}
};
</script>
```

---

## 17.3 自定义单元格

通过 `renderFooterCell` 自定义 footer 单元格内容。

**配置示例**：

```vue
<template>
	<xTableEasy border-y :columns="columns" :table-data="tableData" :footer-data="footerData" />
</template>
<script>
export default {
  data() {
    return {
      columns: [
        { field: "name", title: "Name" },
        {
          field: "amount",
          title: "Amount",
          renderFooterCell: ({ row, column, rowIndex }, h) => {
            return (
              <span style="color:red;font-weight:bold;">
                Total: {row.amount}
              </span>
            );
          }
        }
      ],
      tableData: [...],
      footerData: [{ rowKey: 0, name: "合计", amount: 1000 }]
    };
  }
};
</script>
```

---

## 17.4 单元格样式

自定义 footer 单元格样式。

**配置示例**：

```vue
<template>
	<xTableEasy border-y :columns="columns" :table-data="tableData" :footer-data="footerData" />
</template>
<script>
export default {
  data() {
    return {
      columns: [...],
      tableData: [...],
      footerData: [
        {
          rowKey: 0,
          name: {
            text: "汇总",
            style: {
              color: "#1890ff",
              fontWeight: "bold"
            }
          },
          date: 100,
          hobby: 200,
          address: 300
        }
      ]
    };
  }
};
</script>
```

---

## 17.5 单元格合并

通过 `span` 属性设置单元格合并。

**配置示例**：

```vue
<template>
	<xTableEasy border-y :columns="columns" :table-data="tableData" :footer-data="footerData" />
</template>
<script>
export default {
  data() {
    return {
      columns: [...],
      tableData: [...],
      footerData: [
        {
          rowKey: 0,
          name: {
            text: "合并单元格",
            span: {
              rowspan: 2,
              colspan: 2
            }
          },
          date: "数据1",
          hobby: "数据2",
          address: "数据3"
        }
      ]
    };
  }
};
</script>
```

---

## 17.6 固定页脚

footer 固定在底部，不会随滚动而移动。

**配置示例**：

```vue
<template>
	<xTableEasy
		border-y
		fixed-header
		fixed-footer
		:max-height="300"
		:columns="columns"
		:table-data="tableData"
		:footer-data="footerData" />
</template>
<script>
export default {
  data() {
    return {
      columns: [...],
      tableData: [...],
      footerData: [...]
    };
  }
};
</script>
```

---

## 17.7 结合列固定

在固定列中使用 footer。

**配置示例**：

```vue
<template>
	<xTableEasy
		border-y
		:scroll-width="1200"
		style="width:900px"
		:columns="columns"
		:table-data="tableData"
		:footer-data="footerData" />
</template>
<script>
export default {
  data() {
    return {
      columns: [
        { field: "name", title: "Name", fixed: "left" },
        { field: "date", title: "Date" },
        { field: "hobby", title: "Hobby" },
        { field: "address", title: "Address", fixed: "right" }
      ],
      tableData: [...],
      footerData: [...],
    };
  }
};
</script>
```

---

## 17.8 虚拟滚动

虚拟滚动模式下的汇总。

**配置示例**：

```vue
<template>
	<xTableEasy
		border-y
		virtual-scroll
		:max-height="300"
		:columns="columns"
		:table-data="tableData"
		:footer-data="footerData" />
</template>
<script>
export default {
  data() {
    return {
      columns: [...],
      tableData: [...],
      footerData: [...]
    };
  }
};
</script>
```

---

## 17.9 API

### 表格属性

| 属性         | 说明            | 类型    | 默认值  |
| ------------ | --------------- | ------- | ------- |
| footer-data  | footer 汇总数据 | Array   | []      |
| fixed-footer | 是否固定 footer | Boolean | `false` |

### 列配置

| 属性             | 说明                  | 类型     | 默认值 |
| ---------------- | --------------------- | -------- | ------ |
| renderFooterCell | footer 单元格渲染函数 | Function | -      |

### footerData 数据结构

footer 数据支持以下两种格式：

**简单格式**：

```javascript
{
  rowKey: 0,
  field1: "value1",
  field2: "value2"
}
```

**对象格式（支持样式和合并）**：

```javascript
{
  rowKey: 0,
  field1: {
    text: "显示文本",
    style: { color: "#1890ff" },
    span: { rowspan: 2, colspan: 2 }
  }
}
```

**对象格式属性**：| 属性 | 说明 | 类型 | |------|------|------| | text | 显示文本 | String | | style | 自定义样式 |
Object | | span | 单元格合并配置 | Object |

### 事件

| 事件名               | 说明           | 参数                     |
| -------------------- | -------------- | ------------------------ |
| on-footer-row-click  | 汇总行点击     | `event`, `row`, `column` |
| on-footer-cell-click | 汇总单元格点击 | `event`, `row`, `column` |

---

[返回模块索引](../10-module-design.md)
