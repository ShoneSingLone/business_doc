<template>
	<DocContentOfDemo class="x-table-easy-table-width">
		<xMd :md="mdTips" />
		<h4>固定宽度</h4>
		<xTableEasy
			:columns="columns"
			:table-data="tableData"
			:max-height="300"
			:scroll-width="800"
			border-x
			border-y />
		<h4>百分比宽度</h4>
		<xTableEasy
			:columns="columns"
			:table-data="tableData"
			:max-height="300"
			:scroll-width="'100%'"
			border-x
			border-y />
		<xMd :md="apiString" data-role="api" />
	</DocContentOfDemo>
</template>
<script lang="ts">
export default async function () {
	return {
		data() {
			return {
				mdTips: `
- 1、通过配置 scroll-width 属性，可以设置表格的宽度。
- 2、支持像素值和百分比两种单位。
- 3、当内容超过宽度时会显示水平滚动条。
`,
				apiString: `
## API

### 表格宽度配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| scroll-width | 表格宽度 | Number/String | - |
`,
				tableData: [
					{
						id: 1,
						name: "张三",
						age: 18,
						sex: "男",
						phone: "13800000001",
						address: "上海市普陀区金沙江路 1518 弄"
					},
					{
						id: 2,
						name: "李四",
						age: 20,
						sex: "女",
						phone: "13800000002",
						address: "上海市浦东新区张江高科技园区"
					}
				],
				columns: [
					{ field: "id", key: "id", title: "ID", width: 80, align: "center" },
					{ field: "name", key: "name", title: "姓名", width: 120, align: "left" },
					{ field: "age", key: "age", title: "年龄", width: 80, align: "center" },
					{ field: "sex", key: "sex", title: "性别", width: 80, align: "center" },
					{ field: "phone", key: "phone", title: "电话号码", width: 150, align: "left" },
					{ field: "address", key: "address", title: "地址", width: 250, align: "left" }
				]
			};
		}
	};
}
</script>
<style lang="less">
.x-table-easy-table-width {
	h4 {
		margin: 15px 0 10px 0;
		font-size: 14px;
		font-weight: 500;
	}
}
</style>
