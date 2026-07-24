<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<xTableEasy
				:columns="columns"
				:table-data="tableData"
				:cell-span-option="cellSpanOption"
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
				mdDoc: "body 列合并：同一行的多个单元格合并为一个",
				cellSpanOption: {
					cellSpan: ({ row, column, rowIndex, colIndex }) => {
						// 第一行的 name 列跨 2 列
						if (rowIndex === 0 && column.field === "name") {
							return { rowspan: 1, colspan: 2 };
						}
						// 第一行的 age 列被合并，隐藏
						if (rowIndex === 0 && column.field === "age") {
							return { rowspan: 0, colspan: 0 };
						}
						return { rowspan: 1, colspan: 1 };
					}
				},
				columns: [
					{ field: "name", key: "name", title: "Name", width: 150 },
					{ field: "age", key: "age", title: "Age", width: 100, align: "center" },
					{ field: "hobby", key: "hobby", title: "Hobby", width: 200 },
					{ field: "address", key: "address", title: "Address", width: 300 }
				],
				tableData: [
					{ name: "John & Dickerson", age: 28, hobby: "coding", address: "Shanghai" },
					{ name: "Larsen", age: 25, hobby: "gaming", address: "Beijing" },
					{ name: "Geneva", age: 35, hobby: "sports", address: "Chongqing" }
				]
			};
		}
	});
}
</script>
