<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<xTableEasy
				:columns="columns"
				:table-data="tableData"
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
				mdDoc: "通过 `cellStyleOption.headerCellStyle` 自定义表头单元格样式",
				cellStyleOption: {
					headerCellStyle: (column, colIndex) => {
						if (column.field === "age") {
							return {
								backgroundColor: "#e6f7ff",
								color: "#1890ff",
								fontWeight: "bold"
							};
						}
						return {};
					}
				},
				columns: [
					{ field: "name", key: "a", title: "Name", width: 150 },
					{ field: "age", key: "b", title: "Age", width: 100, align: "center" },
					{ field: "date", key: "c", title: "Tel", width: 200 },
					{ field: "hobby", key: "d", title: "Hobby", width: 300 }
				],
				tableData: [
					{ name: "John", age: 28, date: "1900-05-20", hobby: "coding" },
					{ name: "Dickerson", age: 32, date: "1910-06-20", hobby: "reading" },
					{ name: "Larsen", age: 25, date: "2000-07-20", hobby: "gaming" }
				]
			};
		}
	});
}
</script>
