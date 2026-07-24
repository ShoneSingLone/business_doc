<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<xTableEasy
				:columns="columns"
				:table-data="tableData"
				:footer-data="footerData"
				border-x
				border-y />
		</div>
	</div>
</template>
<script lang="ts">
export default async function () {
	return defineComponent({
		data() {
			return {
				mdDoc: "footer 汇总自定义单元格：通过 `renderFooterCell` 函数自定义页脚单元格渲染",
				columns: [
					{
						field: "name",
						key: "name",
						title: "Name",
						width: 150,
						renderFooterCell: (row) => `<strong style="color: #e6a23c;">合计</strong>`
					},
					{
						field: "age",
						key: "age",
						title: "Age",
						width: 100,
						align: "center",
						renderFooterCell: (row) => `<span style="color: #f56c6c; font-weight: bold;">${row.age}</span>`
					},
					{ field: "hobby", key: "hobby", title: "Hobby", width: 200 }
				],
				tableData: [
					{ name: "John", age: 28, hobby: "coding" },
					{ name: "Dickerson", age: 32, hobby: "reading" },
					{ name: "Larsen", age: 25, hobby: "gaming" }
				],
				footerData: [
					{ name: "合计", age: 85, hobby: "" }
				]
			};
		}
	});
}
</script>
