<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<xTableEasy
				:columns="columns"
				:table-data="tableData"
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
				mdDoc: "header 自定义单元格：通过 `renderHeaderCell` 函数自定义表头单元格渲染",
				columns: [
					{
						field: "name",
						key: "name",
						title: "Name",
						width: 150,
						renderHeaderCell: (column) => {
							return `<div style="color: #409eff; font-weight: bold;">${column.title} 🔍</div>`;
						}
					},
					{ field: "age", key: "age", title: "Age", width: 100, align: "center" },
					{ field: "hobby", key: "hobby", title: "Hobby", width: 200 }
				],
				tableData: [
					{ name: "John", age: 28, hobby: "coding" },
					{ name: "Dickerson", age: 32, hobby: "reading" },
					{ name: "Larsen", age: 25, hobby: "gaming" }
				]
			};
		}
	});
}
</script>
