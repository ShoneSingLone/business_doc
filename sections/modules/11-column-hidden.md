# 11. 列隐藏（column-hidden）

## 11.1 功能说明

- 1、通过 `columnHiddenOption` 实现列隐藏功能
- 2、支持通过实例方法控制列的隐藏与显示

---

## 11.2 默认隐藏列

通过 `defaultHiddenColumnKeys` 属性设置默认隐藏的列。

**配置示例**：
```vue
<template>
	<xTableEasy :columns="columns" :table-data="tableData" :column-hidden-option="columnHiddenOption" />
</template>
<script>
export default {
	data() {
		return {
			columnHiddenOption: {
				defaultHiddenColumnKeys: ["hobby", "name"]
			},
			columns: [
				{ field: "name", key: "name", title: "Name" },
				{ field: "date", key: "date", title: "Date" },
				{ field: "hobby", key: "hobby", title: "Hobby" },
				{ field: "address", key: "address", title: "Address" }
			],
			tableData: [...]
		};
	}
};
</script>
```

---

## 11.3 实例方法

通过实例方法动态控制列的显示与隐藏。

**配置示例**：
```vue
<template>
	<div>
		<button @click="hideColumns(['col1'])">隐藏 col1 列</button>
		<button @click="showColumns(['col1'])">显示 col1 列</button>
		<xTableEasy
			ref="tableRef"
			:columns="columns"
			:table-data="tableData"
			:column-hidden-option="columnHiddenOption" />
	</div>
</template>
<script>
export default {
	data() {
		return {
			columnHiddenOption: {
				defaultHiddenColumnKeys: ["col8"]
			},
			columns: [...],
			tableData: [...]
		};
	},
	methods: {
		hideColumns(keys) {
			this.$refs["tableRef"].hideColumnsByKeys(keys);
		},
		showColumns(keys) {
			this.$refs["tableRef"].showColumnsByKeys(keys);
		}
	}
};
</script>
```

---

## 11.4 API

### columnHiddenOption

列隐藏配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| defaultHiddenColumnKeys | 默认隐藏的列 key 数组 | Array | `[]` |

### 实例方法

| 方法名 | 说明 | 参数 |
|--------|------|------|
| hideColumnsByKeys(keys) | 隐藏指定列 | keys: 列 key 数组 |
| showColumnsByKeys(keys) | 显示指定列 | keys: 列 key 数组 |

---

[返回模块索引](../10-module-design.md)