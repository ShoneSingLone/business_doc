<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<xTableEasy
				:columns="columns"
				:table-data="tableData"
				:row-style-option="rowStyleOption"
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
				mdDoc: "通过 rowStyleOption 属性自定义行样式",
				rowStyleOption: {
					rowStyle: (row, rowIndex) => {
						if (rowIndex % 2 === 0) {
							return {
								backgroundColor: "#f9f9f9"
							};
						}
						if (row.age > 30) {
							return {
								color: "#ff4d4f"
							};
						}
						return {};
					}
				},
				columns: [
					{ field: "name", key: "a", title: "Name", width: 100 },
					{ field: "age", key: "b", title: "Age", width: 100, align: "center" },
					{ field: "date", key: "c", title: "Tel", width: 200 },
					{ field: "hobby", key: "d", title: "Hobby", width: 300 }
				],
				tableData: [
					{ name: "John", age: 28, date: "1900-05-20", hobby: "coding" },
					{ name: "Dickerson", age: 32, date: "1910-06-20", hobby: "coding" },
					{ name: "Larsen", age: 25, date: "2000-07-20", hobby: "coding" },
					{ name: "Geneva", age: 35, date: "2010-08-20", hobby: "coding" },
					{ name: "Jami", age: 26, date: "2020-09-20", hobby: "coding" }
				]
			};
		}
	});
}
</script>