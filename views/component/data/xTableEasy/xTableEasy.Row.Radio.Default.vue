<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<xTableEasy
				:columns="columns"
				:table-data="tableData"
				:radio-option="radioOption"
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
				mdDoc: "默认选中：通过 `defaultSelectedRowKey` 配置默认选中的行",
				radioOption: {
					defaultSelectedRowKey: 2,
					selectedRowChange: ({ row }) => {
						console.log("选中行:", row.name);
					}
				},
				columns: [
					{ type: "radio", key: "radio", width: 50 },
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
