<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<xTableEasy
				:columns="columns"
				:table-data="tableData"
				:footer-data="footerData"
				:cell-style-option="cellStyleOption"
				borderX
				borderY />
		</div>
	</div>
</template>
<script lang="ts">
export default async function () {
	return defineComponent({
		data() {
			return {
				mdDoc: "footer 单元格样式：通过 `cellStyleOption.footerCellStyle` 自定义页脚单元格样式",
				cellStyleOption: {
					footerCellStyle: (row, column, rowIndex, colIndex) => {
						if (column.field === "age") {
							return {
								backgroundColor: "#fdf6ec",
								color: "#e6a23c",
								fontWeight: "bold"
							};
						}
						return {};
					}
				},
				columns: [
					{ field: "name", key: "name", title: "Name", width: 150 },
					{ field: "age", key: "age", title: "Age", width: 100, align: "center" },
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
