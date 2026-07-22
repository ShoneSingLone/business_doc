<template>
	<DocContentOfDemo class="x-table-easy-table-height">
		<xMd :md="mdTips" />
		<h4>固定高度</h4>
		<xTableEasy
			:columns="columns"
			:table-data="tableData"
			:max-height="300"
			border-x
			border-y />
		<h4>自适应高度</h4>
		<xTableEasy :columns="columns" :table-data="tableData" border-x border-y />
		<h4>百分比高度</h4>
		<div
			style="height: 300px; border: 1px solid #e8e8e8; padding: 10px; box-sizing: border-box">
			<xTableEasy
				:columns="columns"
				:table-data="tableData"
				:max-height="'100%'"
				border-x
				border-y />
		</div>
		<xMd :md="apiString" data-role="api" />
	</DocContentOfDemo>
</template>
<script lang="ts">
export default async function () {
	const generateTestData = () => {
		const data = [];
		for (let i = 0; i < 20; i++) {
			data.push({
				id: i + 1,
				name: `用户${i + 1}`,
				age: 18 + Math.floor(Math.random() * 30),
				sex: Math.random() > 0.5 ? "男" : "女",
				phone: `138000000${String(i).padStart(2, "0")}`,
				address: `上海市浦东新区张江高科技园区 ${i + 1} 号`
			});
		}
		return data;
	};

	return {
		data() {
			return {
				mdTips: `
- 1、通过配置 max-height 属性，可以设置表格的最大高度。
- 2、当内容超过最大高度时会显示滚动条。
- 3、支持像素值、百分比和自适应三种方式。
`,
				apiString: `
## API

### 表格高度配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| max-height | 最大高度 | Number/String | - |
`,
				tableData: generateTestData(),
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
.x-table-easy-table-height {
	h4 {
		margin: 15px 0 10px 0;
		font-size: 14px;
		font-weight: 500;
	}
}
</style>
