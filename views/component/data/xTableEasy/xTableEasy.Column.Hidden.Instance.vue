<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<div class="demo-controls">
				<el-button @click="hideColumns(['name'])" type="primary" size="small">隐藏 Name 列</el-button>
				<el-button @click="hideColumns(['date'])" type="primary" size="small">隐藏 Date 列</el-button>
				<el-button @click="hideColumns(['hobby'])" type="primary" size="small">隐藏 Hobby 列</el-button>
				<el-button @click="showColumns(['name','date','hobby'])" type="success" size="small">显示所有列</el-button>
			</div>
			<xTableEasy 
				ref="tableRef"
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
				mdDoc: "通过实例方法 `hideColumnsByKeys(keys)` 和 `showColumnsByKeys(keys)` 控制列的显示与隐藏",
				columnHiddenOption: {
					defaultHiddenColumnKeys: []
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
		},
		methods: {
			hideColumns(keys) {
				this.$refs["tableRef"].hideColumnsByKeys(keys);
			},
			showColumns(keys) {
				this.$refs["tableRef"].showColumnsByKeys(keys);
			}
		}
	});
}
</script>

<style scoped>
.demo-controls {
	margin-bottom: 16px;
	padding: 12px;
	background-color: #f5f7fa;
	border-radius: 4px;
	display: flex;
	gap: 8px;
}
</style>