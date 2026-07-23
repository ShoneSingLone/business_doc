<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<div class="demo-controls">
				<el-button type="primary" @click="sortByName">按姓名排序</el-button>
				<el-button type="primary" @click="sortByTel">按电话排序</el-button>
				<el-button type="info" @click="resetSort">重置顺序</el-button>
			</div>
			<xTableEasy
				:columns="columns"
				:table-data="sortedData"
				:sort-option="sortOption"
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
				mdDoc: "1、表格支持通过外部排序逻辑实现表头排序\n2、点击表头或使用按钮触发排序\n3、排序后的数据重新传递给表格组件",
				sortOption: {
					sortChange: (sortColumns) => {
						console.log("sortColumns:", sortColumns);
					}
				},
				originalData: [
					{
						name: "John",
						tel: "1900-05-20",
						hobby: "coding and coding repeat",
						address: "No.1 Century Avenue, Shanghai"
					},
					{
						name: "Dickerson",
						tel: "1910-06-20",
						hobby: "coding and coding repeat",
						address: "No.1 Century Avenue, Beijing"
					},
					{
						name: "Larsen",
						tel: "2000-07-20",
						hobby: "coding and coding repeat",
						address: "No.1 Century Avenue, Chongqing"
					},
					{
						name: "Geneva",
						tel: "2010-08-20",
						hobby: "coding and coding repeat",
						address: "No.1 Century Avenue, Xiamen"
					},
					{
						name: "Jami",
						tel: "2020-09-20",
						hobby: "coding and coding repeat",
						address: "No.1 Century Avenue, Shenzhen"
					}
				],
				sortedData: [],
				columns: [
					{ field: "name", key: "a", title: "Name", width: 150, align: "center", sortBy: "" },
					{ field: "tel", key: "b", title: "Tel", width: 200, align: "center", sortBy: "" },
					{ field: "hobby", key: "c", title: "Hobby", width: 300 },
					{ field: "address", key: "d", title: "Address", width: 400 }
				]
			};
		},
		mounted() {
			this.sortedData = [...this.originalData];
		},
		methods: {
			sortByName() {
				const col = this.columns.find(c => c.field === "name");
				if (col.sortBy === "asc") {
					this.sortedData = [...this.sortedData].sort((a, b) => b.name.localeCompare(a.name));
					col.sortBy = "desc";
				} else {
					this.sortedData = [...this.sortedData].sort((a, b) => a.name.localeCompare(b.name));
					col.sortBy = "asc";
				}
				this.columns = [...this.columns];
			},
			sortByTel() {
				const col = this.columns.find(c => c.field === "tel");
				if (col.sortBy === "asc") {
					this.sortedData = [...this.sortedData].sort((a, b) => b.tel.localeCompare(a.tel));
					col.sortBy = "desc";
				} else {
					this.sortedData = [...this.sortedData].sort((a, b) => a.tel.localeCompare(b.tel));
					col.sortBy = "asc";
				}
				this.columns = [...this.columns];
			},
			resetSort() {
				this.sortedData = [...this.originalData];
				this.columns.forEach(c => { c.sortBy = ""; });
				this.columns = [...this.columns];
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
	align-items: center;
	gap: 12px;
}
</style>
