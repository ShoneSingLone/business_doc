<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<div class="demo-controls">
				<el-input v-model="filterKeyword" placeholder="输入姓名搜索" style="width: 200px">
					<el-button
						slot="append"
						icon="el-icon-search"
						@click="handleFilter"></el-button>
				</el-input>
				<el-button type="info" @click="resetFilter">重置</el-button>
			</div>
			<xTableEasy
				:columns="columns"
				:table-data="filteredData"
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
				mdDoc: "1、通过外部筛选控件实现表格数据的筛选\n2、可以根据业务需求自定义筛选逻辑和筛选控件\n3、筛选后的数据直接传递给 table-data 属性",
				filterKeyword: "",
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
				columns: [
					{ field: "name", key: "a", title: "Name", width: 150 },
					{ field: "tel", key: "b", title: "Tel", width: 200 },
					{ field: "hobby", key: "c", title: "Hobby", width: 300 },
					{ field: "address", key: "d", title: "Address", width: 400 }
				]
			};
		},
		computed: {
			filteredData() {
				if (!this.filterKeyword) {
					return this.originalData;
				}
				return this.originalData.filter(item => {
					return item.name.toLowerCase().includes(this.filterKeyword.toLowerCase());
				});
			}
		},
		methods: {
			handleFilter() {
				// 筛选逻辑已在 computed 中实现
			},
			resetFilter() {
				this.filterKeyword = "";
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
