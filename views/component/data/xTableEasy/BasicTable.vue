<template>
	<DocContentOfDemo class="x-table-easy-basic">
		<xMd :md="mdTips" />
		<xTableEasy :columns="columns" :table-data="tableData" border-x border-y />
		<xMd :md="apiString" data-role="api" />
	</DocContentOfDemo>
</template>
<script lang="ts">
export default async function () {
	return {
		data() {
			return {
				mdTips: `
- 1、这是一个基础的 xTableEasy 表格示例，展示了最基本的表格功能。
- 2、通过 columns 配置列信息，通过 table-data 配置表格数据。
- 3、border-x 和 border-y 属性分别控制横向和纵向边框。
`,
				apiString: `
## API

### 基础表格属性

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| columns | 列配置数组 | Array | [] |
| table-data | 表格数据 | Array | [] |
| border-x | 是否显示横向边框 | Boolean | false |
| border-y | 是否显示纵向边框 | Boolean | false |
`,
				columns: [
					{ field: "name", key: "a", title: "Name", width: 100 },
					{ field: "date", key: "b", title: "Date", width: 150 },
					{ field: "hobby", key: "c", title: "Hobby", width: 200 },
					{ field: "address", key: "d", title: "Address", width: 300 }
				],
				tableData: [
					{
						name: "John",
						date: "1900-05-20",
						hobby: "coding",
						address: "No.1 Century Avenue, Shanghai"
					},
					{
						name: "Dickerson",
						date: "1910-06-20",
						hobby: "reading",
						address: "No.1 Century Avenue, Beijing"
					},
					{
						name: "Larsen",
						date: "2000-07-20",
						hobby: "swimming",
						address: "No.1 Century Avenue, Chongqing"
					},
					{
						name: "Geneva",
						date: "2010-08-20",
						hobby: "running",
						address: "No.1 Century Avenue, Xiamen"
					},
					{
						name: "Jami",
						date: "2020-09-20",
						hobby: "painting",
						address: "No.1 Century Avenue, Shenzhen"
					}
				]
			};
		}
	};
}
</script>
<style lang="less">
.x-table-easy-basic {
}
</style>
