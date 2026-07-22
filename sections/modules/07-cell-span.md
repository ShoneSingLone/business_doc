# 7. 单元格合并（cell-span）

## 7.1 功能说明

**配置要点**：

1. 通过配置对象 `cell-span-option` 设置合并单元格
2. 通过 `bodyCellSpan` 方法设置表体单元格合并
3. 通过 `footerCellSpan` 方法设置页脚单元格合并
4. 属性 `colspan` 指定合并的列数；属性 `rowspan` 指定合并的行数
5. 需要指定不需要渲染的列，设置 `colspan`、`rowspan` 的值为 0 即可
6. 默认合并后的内容，是渲染的单元格的内容。若要自定义单元格内容，可以结合 `renderBodyCell` 实现

---

## 7.2 跨行合并

通过 `rowspan` 实现跨行合并。

**配置示例**：

```vue
<template>
	<xTableEasy
		:columns="columns"
		:table-data="tableData"
		:border-around="true"
		:border-x="true"
		:border-y="true"
		:cell-span-option="cellSpanOption" />
</template>
<script>
export default {
	data() {
		return {
			cellSpanOption: {
				bodyCellSpan: this.bodyCellSpan
			},
			columns: [
				{ field: "name", title: "姓名", width: 200 },
				{ field: "date", title: "日期", width: 200 },
				{ field: "hobby", title: "爱好", width: 200 },
				{ field: "address", title: "地址" }
			],
			tableData: [
				{ name: "John", date: "1900-05-20", hobby: "coding", address: "Shanghai" },
				{ name: "Dickerson", date: "1910-06-20", hobby: "coding", address: "Beijing" },
				{ name: "Larsen", date: "2000-07-20", hobby: "coding", address: "Chongqing" },
				{ name: "Geneva", date: "2010-08-20", hobby: "coding", address: "Xiamen" },
				{ name: "Jami", date: "2020-09-20", hobby: "coding", address: "Shenzhen" }
			]
		};
	},
	methods: {
		bodyCellSpan({ row, column, rowIndex }) {
			if (column.field === "name") {
				if (rowIndex === 1) {
					return {
						rowspan: 2,
						colspan: 1
					};
				} else if (rowIndex === 2) {
					return {
						rowspan: 0,
						colspan: 0
					};
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

**配置示例**：

```vue
<template>
	<xTableEasy
		:columns="columns"
		:table-data="tableData"
		:border-around="true"
		:border-x="true"
		:border-y="true"
		:cell-span-option="cellSpanOption" />
</template>
<script>
export default {
  data() {
    return {
      cellSpanOption: {
        bodyCellSpan: this.bodyCellSpan
      },
      columns: [
        { field: "name", title: "姓名", width: 200 },
        { field: "date", title: "日期", width: 200 },
        { field: "hobby", title: "爱好", width: 200 },
        { field: "address", title: "地址" }
      ],
      tableData: [...]
    };
  },
  methods: {
    bodyCellSpan({ row, column, rowIndex }) {
      if (rowIndex === 1) {
        if (column.field === "date") {
          return {
            rowspan: 1,
            colspan: 2
          };
        } else if (column.field === "hobby") {
          return {
            rowspan: 0,
            colspan: 0
          };
        }
      }
    }
  }
};
</script>
```

---

## 7.4 自定义合并内容

通过 `renderBodyCell` 自定义合并单元格的显示内容。

**配置示例**：

```vue
<template>
	<xTableEasy :columns="columns" :table-data="tableData" :cell-span-option="cellSpanOption" />
</template>
<script>
export default {
  data() {
    return {
      cellSpanOption: {
        bodyCellSpan: this.bodyCellSpan
      },
      columns: [
        {
          field: "name",
          title: "姓名",
          renderBodyCell: ({ row, column, rowIndex }, h) => {
            if (rowIndex === 1 && column.field === "name") {
              return <span style="color:#1890ff;">合并内容</span>;
            }
            return row[column.field];
          }
        },
        { field: "date", title: "日期" },
        { field: "hobby", title: "爱好" },
        { field: "address", title: "地址" }
      ],
      tableData: [...]
    };
  },
  methods: {
    bodyCellSpan({ row, column, rowIndex }) {
      if (column.field === "name") {
        if (rowIndex === 1) {
          return { rowspan: 2, colspan: 1 };
        } else if (rowIndex === 2) {
          return { rowspan: 0, colspan: 0 };
        }
      }
    }
  }
};
</script>
```

---

## 7.5 页脚单元格合并

通过 `footerCellSpan` 方法设置页脚单元格合并。

**配置示例**：

```vue
<template>
	<xTableEasy
		:columns="columns"
		:table-data="tableData"
		:footer-data="footerData"
		:cell-span-option="cellSpanOption" />
</template>
<script>
export default {
  data() {
    return {
      cellSpanOption: {
        footerCellSpan: this.footerCellSpan
      },
      columns: [
        { field: "name", title: "姓名" },
        { field: "amount", title: "金额" },
        { field: "total", title: "总计" }
      ],
      tableData: [...],
      footerData: [
        { name: "合计", amount: "", total: "1000" }
      ]
    };
  },
  methods: {
    footerCellSpan({ row, column, rowIndex }) {
      if (rowIndex === 0) {
        if (column.field === "name") {
          return { rowspan: 1, colspan: 2 };
        } else if (column.field === "amount") {
          return { rowspan: 0, colspan: 0 };
        }
      }
    }
  }
};
</script>
```

---

## 7.6 API

### cell-span-option

单元格合并配置

| 属性           | 说明               | 类型     |
| -------------- | ------------------ | -------- |
| bodyCellSpan   | 表体单元格合并方法 | Function |
| footerCellSpan | 页脚单元格合并方法 | Function |

### bodyCellSpan 参数

| 参数     | 说明       | 类型   |
| -------- | ---------- | ------ |
| row      | 当前行数据 | Object |
| column   | 当前列配置 | Object |
| rowIndex | 行索引     | Number |

### footerCellSpan 参数

| 参数     | 说明           | 类型   |
| -------- | -------------- | ------ |
| row      | 当前页脚行数据 | Object |
| column   | 当前列配置     | Object |
| rowIndex | 页脚行索引     | Number |

### 返回值

| 属性    | 说明                 | 类型   |
| ------- | -------------------- | ------ |
| rowspan | 跨行数，0 表示不渲染 | Number |
| colspan | 跨列数，0 表示不渲染 | Number |

---

[返回模块索引](../10-module-design.md)
