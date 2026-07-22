<template>
	<div class="card-BiaoTouGuDing">
		<xMd :md="mdTips" />
		<h4>固定表头</h4>
		<xTableEasy
			:columns="columns"
			:table-data="tableData"
			:max-height="300"
			fixed-header
			border-x
			border-y />
		<h4>不固定表头</h4>
		<xTableEasy
			:columns="columns"
			:table-data="tableData"
			:max-height="300"
			:fixed-header="false"
			border-x
			border-y />
		<h4>同时固定表头和表尾</h4>
		<xTableEasy
			:columns="columns"
			:table-data="tableData"
			:footer-data="footerData"
			:max-height="300"
			fixed-header
			fixed-footer
			border-x
			border-y />
	</div>
</template>
<script lang="ts">
export default async function () {
	const generateTestData = () => {
		const data = [];
		for (let i = 0; i < 30; i++) {
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

	return defineComponent({
		data() {
			return {
				mdTips: `
- 1、通过配置 fixed-header 属性，可以实现表头的固定功能。
- 2、当表格内容滚动时，表头保持可见。
- 3、同时支持固定表尾功能。
`,
				tableData: generateTestData(),
				footerData: [{ id: "合计", name: "", age: 0, sex: "", phone: "", address: "" }],
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
	});
}
</script>
<style lang="less">
.card-BiaoTouGuDing {
	h4 {
		margin: 15px 0 10px 0;
		font-size: 14px;
		font-weight: 500;
	}
}
</style>
