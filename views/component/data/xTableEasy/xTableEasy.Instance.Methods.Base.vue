<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<div class="demo-controls">
				<el-button type="primary" @click="scrollToRow">滚动到第5行</el-button>
				<el-button @click="clearSelection">清除选择</el-button>
				<el-button @click="getSelectedRows">获取选中行</el-button>
			</div>
			<xTableEasy
				ref="tableRef"
				:columns="columns"
				:table-data="tableData"
				:checkbox-option="checkboxOption"
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
				mdDoc: "通过表格实例方法可以实现滚动、选中、清除等操作",
				checkboxOption: {
					enable: true
				},
				columns: [
					{ field: "name", key: "a", title: "Name", width: 100 },
					{ field: "date", key: "b", title: "Tel", width: 200 },
					{ field: "hobby", key: "c", title: "Hobby", width: 300 },
					{ field: "address", key: "d", title: "Address", width: 400 }
				],
				tableData: [
					{ name: "John", date: "1900-05-20", hobby: "coding", address: "Shanghai" },
					{ name: "Dickerson", date: "1910-06-20", hobby: "coding", address: "Beijing" },
					{ name: "Larsen", date: "2000-07-20", hobby: "coding", address: "Chongqing" },
					{ name: "Geneva", date: "2010-08-20", hobby: "coding", address: "Xiamen" },
					{ name: "Jami", date: "2020-09-20", hobby: "coding", address: "Shenzhen" }
				]
			};
		},
		methods: {
			scrollToRow() {
				this.$refs.table.scrollToRow(4);
			},
			clearSelection() {
				this.$refs.table.clearRowSelection();
			},
			getSelectedRows() {
				const selected = this.$refs.table.getRowSelection();
				console.log("Selected rows:", selected);
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
	gap: 12px;
}
</style>