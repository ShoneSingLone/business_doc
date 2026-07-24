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
				mdDoc: "body 行合并：同一列的多个单元格合并为一个",
				cellSpanOption: {
					cellSpan: ({ row, column, rowIndex, colIndex }) => {
						// 第一列的前三行合并
						if (colIndex === 0 && rowIndex < 3) {
							return { rowspan: 3, colspan: 1 };
						}
						// 被合并覆盖的单元格隐藏
						if (colIndex === 0 && rowIndex >= 3 && rowIndex < 5) {
							return { rowspan: 0, colspan: 0 };
						}
						return { rowspan: 1, colspan: 1 };
					}
				},
				columns: [
					{ field: "category", key: "category", title: "分类", width: 120 },
					{ field: "name", key: "name", title: "Name", width: 150 },
					{ field: "age", key: "age", title: "Age", width: 100, align: "center" },
					{ field: "hobby", key: "hobby", title: "Hobby", width: 200 }
				],
				tableData: [
					{ category: "前端", name: "John", age: 28, hobby: "coding" },
					{ category: "前端", name: "Dickerson", age: 32, hobby: "reading" },
					{ category: "前端", name: "Larsen", age: 25, hobby: "gaming" },
					{ category: "后端", name: "Geneva", age: 35, hobby: "sports" },
					{ category: "后端", name: "Jami", age: 26, hobby: "music" }
				]
			};
		}
	});
}
</script>
