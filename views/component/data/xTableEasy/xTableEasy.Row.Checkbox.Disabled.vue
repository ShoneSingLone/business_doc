<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<xTableEasy
				:columns="columns"
				:table-data="tableData"
				:checkbox-option="checkboxOption"
				:row-key-field-name="'id'"
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
				mdDoc: "禁止选中：通过 `disableSelectedRowKeys` 禁止选中指定行",
				checkboxOption: {
					disableSelectedRowKeys: [2, 4],
					selectedRowChange: ({ row, isSelected, selectedRowKeys }) => {
						console.log("选中变化:", row.name, isSelected);
					}
				},
				columns: [
					{ type: "checkbox", key: "checkbox", width: 50 },
					{ field: "name", key: "name", title: "Name", width: 150 },
					{ field: "age", key: "age", title: "Age", width: 100, align: "center" },
					{ field: "hobby", key: "hobby", title: "Hobby", width: 200 }
				],
				tableData: [
					{ id: 1, name: "John", age: 28, hobby: "coding" },
					{ id: 2, name: "Dickerson", age: 32, hobby: "reading" },
					{ id: 3, name: "Larsen", age: 25, hobby: "gaming" },
					{ id: 4, name: "Geneva", age: 35, hobby: "sports" },
					{ id: 5, name: "Jami", age: 26, hobby: "music" }
				]
			};
		}
	});
}
</script>
