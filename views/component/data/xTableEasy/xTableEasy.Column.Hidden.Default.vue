<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<xTableEasy 
				:columns="columns" 
				:table-data="tableData" 
				:column-hidden-option="columnHiddenOption" 
				borderX borderY />
		</div>
	</div>
</template>

<script lang="ts">
export default async function () {
	return defineComponent({
		data() {
			return {
				mdDoc: "通过 `defaultHiddenColumnKeys` 属性设置默认隐藏的列",
				columnHiddenOption: {
					defaultHiddenColumnKeys: ["hobby", "name"]
				},
				columns: [
					{ field: "name", key: "name", title: "Name", width: 100 },
					{ field: "date", key: "date", title: "Date", width: 150 },
					{ field: "hobby", key: "hobby", title: "Hobby", width: 200 },
					{ field: "address", key: "address", title: "Address", width: 300 }
				],
				tableData: [
					{
						name: "John",
						date: "1900-05-20",
						hobby: "coding and coding repeat",
						address: "No.1 Century Avenue, Shanghai"
					},
					{
						name: "Dickerson",
						date: "1910-06-20",
						hobby: "coding and coding repeat",
						address: "No.1 Century Avenue, Beijing"
					},
					{
						name: "Larsen",
						date: "2000-07-20",
						hobby: "coding and coding repeat",
						address: "No.1 Century Avenue, Chongqing"
					},
					{
						name: "Geneva",
						date: "2010-08-20",
						hobby: "coding and coding repeat",
						address: "No.1 Century Avenue, Xiamen"
					},
					{
						name: "Jami",
						date: "2020-09-20",
						hobby: "coding and coding repeat",
						address: "No.1 Century Avenue, Shenzhen"
					}
				]
			};
		}
	});
}
</script>