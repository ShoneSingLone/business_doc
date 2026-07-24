<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<div class="demo-controls">
				<xBtn type="primary" @click="sortByAge">按年龄排序</xBtn>
				<xBtn type="primary" @click="sortByScore">按成绩排序</xBtn>
				<xBtn type="info" @click="resetSort">重置</xBtn>
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
				mdDoc: "多字段排序：同时对多个字段进行排序",
				sortOption: {
					multipleSort: true,
					sortChange: sortColumns => {
						console.log("sortColumns:", sortColumns);
					}
				},
				originalData: [
					{ name: "John", age: 25, score: 90, hobby: "coding" },
					{ name: "Dickerson", age: 20, score: 85, hobby: "reading" },
					{ name: "Larsen", age: 25, score: 95, hobby: "gaming" },
					{ name: "Geneva", age: 30, score: 88, hobby: "sports" },
					{ name: "Jami", age: 20, score: 92, hobby: "music" }
				],
				sortedData: [],
				columns: [
					{ field: "name", key: "a", title: "Name", width: 120 },
					{
						field: "age",
						key: "b",
						title: "Age",
						width: 100,
						align: "center",
						sortBy: ""
					},
					{
						field: "score",
						key: "c",
						title: "Score",
						width: 100,
						align: "center",
						sortBy: ""
					},
					{ field: "hobby", key: "d", title: "Hobby", width: 200 }
				]
			};
		},
		mounted() {
			this.sortedData = [...this.originalData];
		},
		methods: {
			sortByAge() {
				const col = this.columns.find(c => c.field === "age");
				if (col.sortBy === "asc") {
					this.sortedData = [...this.sortedData].sort((a, b) => b.age - a.age);
					col.sortBy = "desc";
				} else {
					this.sortedData = [...this.sortedData].sort((a, b) => a.age - b.age);
					col.sortBy = "asc";
				}
				this.columns = [...this.columns];
			},
			sortByScore() {
				const col = this.columns.find(c => c.field === "score");
				if (col.sortBy === "asc") {
					this.sortedData = [...this.sortedData].sort((a, b) => b.score - a.score);
					col.sortBy = "desc";
				} else {
					this.sortedData = [...this.sortedData].sort((a, b) => a.score - b.score);
					col.sortBy = "asc";
				}
				this.columns = [...this.columns];
			},
			resetSort() {
				this.sortedData = [...this.originalData];
				this.columns.forEach(c => {
					c.sortBy = "";
				});
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
