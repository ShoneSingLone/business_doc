<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<xTableEasy
				:columns="columns"
				:table-data="tableData"
				:cell-autofill-option="cellAutofillOption"
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
				mdDoc: "自动填充方向：通过 `beforeAutofill` 回调可以控制填充方向和行为",
				cellAutofillOption: {
					enable: true,
					beforeAutofill: ({ direction, cellSelectionRangeData, nextCurrentCell, nextNormalEndCell }) => {
						console.log("填充方向:", direction);
						console.log("选区:", cellSelectionRangeData);
						return true; // 返回 true 允许填充
					},
					afterAutofill: ({ direction, cellSelectionRangeData }) => {
						console.log("填充完成:", direction);
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
					{ name: "Larsen", age: 25, date: "2000-07-20", hobby: "gaming" },
					{ name: "Geneva", age: 35, date: "2010-08-20", hobby: "sports" }
				]
			};
		}
	});
}
</script>
