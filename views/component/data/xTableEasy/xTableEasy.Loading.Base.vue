<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<div class="demo-controls">
				<el-button type="primary" @click="loading = true">显示加载</el-button>
				<el-button @click="loading = false">隐藏加载</el-button>
			</div>
			<xTableEasy
				:columns="columns"
				:table-data="tableData"
				:loading="loading"
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
				mdDoc: "通过 loading 属性控制表格的加载状态",
				loading: false,
				columns: [
					{ field: "name", key: "a", title: "Name", width: 100 },
					{ field: "date", key: "b", title: "Tel", width: 200 },
					{ field: "hobby", key: "c", title: "Hobby", width: 300 },
					{ field: "address", key: "d", title: "Address", width: 400 }
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
<style scoped>
.demo-controls {
	margin-bottom: 16px;
	padding: 12px;
	background-color: #f5f7fa;
	border-radius: 4px;
	display: flex;
	gap: 12px;
}
</style>
