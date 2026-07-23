<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<xTableEasy
				style="width: 600px"
				:scroll-width="1200"
				:columns="columns"
				:table-data="tableData"
				:edit-option="editOption"
				:row-key-field-name="'name'"
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
				mdDoc: "结合固定列：编辑功能与列固定同时使用",
				editOption: {
					enable: true,
					afterEditCell: ({ row, column, value, oldValue }) => {
						console.log(`编辑完成: ${column.field} 从 "${oldValue}" 改为 "${value}"`);
					}
				},
				columns: [
					{ field: "name", key: "name", title: "Name", width: 120, fixed: "left", edit: true },
					{ field: "age", key: "age", title: "Age", width: 80, align: "center", edit: true },
					{ field: "date", key: "date", title: "Tel", width: 150, edit: true },
					{ field: "hobby", key: "hobby", title: "Hobby", width: 200 },
					{ field: "address", key: "address", title: "Address", width: 300 }
				],
				tableData: [
					{ name: "John", age: 28, date: "1900-05-20", hobby: "coding", address: "Shanghai" },
					{ name: "Dickerson", age: 32, date: "1910-06-20", hobby: "reading", address: "Beijing" },
					{ name: "Larsen", age: 25, date: "2000-07-20", hobby: "gaming", address: "Chongqing" },
					{ name: "Geneva", age: 35, date: "2010-08-20", hobby: "sports", address: "Xiamen" },
					{ name: "Jami", age: 26, date: "2020-09-20", hobby: "music", address: "Shenzhen" }
				]
			};
		}
	});
}
</script>
