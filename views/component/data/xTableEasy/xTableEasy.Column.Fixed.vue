<template>
	<DocContentOfDemo class="x-table-easy-column-fixed">
		<xMd :md="mdTips" />

		<h3>左列固定</h3>
		<xTableEasy
			style="width: 600px"
			:scroll-width="900"
			border-y
			:columns="leftFixedColumns"
			:table-data="tableData" />

		<h3>右列固定</h3>
		<xTableEasy
			style="width: 600px"
			:scroll-width="900"
			border-y
			:columns="rightFixedColumns"
			:table-data="tableData" />

		<h3>左右列同时固定</h3>
		<xTableEasy
			style="width: 600px"
			:scroll-width="900"
			border-y
			:columns="bothFixedColumns"
			:table-data="tableData" />

		<xMd :md="apiString" data-role="api" />
	</DocContentOfDemo>
</template>
</template>

<script lang="ts">
export default async function () {
	return {
		data() {
			return {
				mdTips: `
- 1、属性 \`scroll-width\` 为滚动区域的宽度
- 2、当外层容器宽度小于 \`scroll-width\` 值时，将会出现横向滚动条；当外层容器宽度大于 \`scroll-width\` 值时，将会跟随容器自适应；当 \`scroll-width=0\` 时，滚动条将根据列宽度决定
- 3、列宽可以不设置、或者设置为百分比、或者为像素值（px）
- 4、设置了 \`scroll-width\` 属性，列宽单位**强烈建议保持一致！**
- 5、通过 \`fixed: "left"\` 设置左列固定，通过 \`fixed: "right"\` 设置右列固定
`,
				apiString: `
## API

### 表格属性

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| scroll-width | 滚动区域宽度 | Number | \`0\` |

### 列配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| fixed | 是否固定列 | String | \`-\` |

**fixed 可选值**：
| 值 | 说明 |
|----|------|
| \`left\` | 左列固定 |
| \`right\` | 右列固定 |
`,
				leftFixedColumns: [
					{ field: "col1", key: "a", title: "固定列1", fixed: "left", width: 120 },
					{ field: "col2", key: "b", title: "固定列2", fixed: "left", width: 120 },
					{ field: "col3", key: "c", title: "普通列3", width: 150 },
					{ field: "col4", key: "d", title: "普通列4", width: 150 },
					{ field: "col5", key: "e", title: "普通列5", width: 150 },
					{ field: "col6", key: "f", title: "普通列6", width: 150 }
				],
				rightFixedColumns: [
					{ field: "col1", key: "a", title: "普通列1", width: 150 },
					{ field: "col2", key: "b", title: "普通列2", width: 150 },
					{ field: "col3", key: "c", title: "普通列3", width: 150 },
					{ field: "col4", key: "d", title: "普通列4", width: 150 },
					{ field: "col5", key: "e", title: "固定列5", fixed: "right", width: 120 },
					{ field: "col6", key: "f", title: "固定列6", fixed: "right", width: 120 }
				],
				bothFixedColumns: [
					{ field: "col1", key: "a", title: "左固定1", fixed: "left", width: 120 },
					{ field: "col2", key: "b", title: "左固定2", fixed: "left", width: 120 },
					{ field: "col3", key: "c", title: "普通列3", width: 150 },
					{ field: "col4", key: "d", title: "普通列4", width: 150 },
					{ field: "col5", key: "e", title: "右固定5", fixed: "right", width: 120 },
					{ field: "col6", key: "f", title: "右固定6", fixed: "right", width: 120 }
				],
				tableData: Array.from({ length: 10 }, (_, i) => ({
					col1: `数据${i + 1}-1`,
					col2: `数据${i + 1}-2`,
					col3: `数据${i + 1}-3`,
					col4: `数据${i + 1}-4`,
					col5: `数据${i + 1}-5`,
					col6: `数据${i + 1}-6`
				}))
			};
		}
	};
}
</script>

<style lang="less">
.x-table-easy-column-fixed {
	h3 {
		margin: 20px 0 10px;
		font-size: 14px;
		font-weight: 600;
		color: #303133;
	}
}
</style>