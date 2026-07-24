<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<div class="demo-controls">
				<xBtn type="primary" @click="scrollToRow">滚动到第50行</xBtn>
				<xBtn type="primary" @click="scrollToTop">滚动到顶部</xBtn>
			</div>
			<xTableEasy
				ref="tableRef"
				:columns="columns"
				:table-data="tableData"
				:max-height="300"
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
				mdDoc: "scrollTo 方法：滚动到指定位置",
				columns: [
					{ field: "id", key: "id", title: "ID", width: 80, align: "center" },
					{ field: "name", key: "name", title: "Name", width: 150 },
					{ field: "date", key: "date", title: "Date", width: 200 },
					{ field: "hobby", key: "hobby", title: "Hobby", width: 300 }
				],
				tableData: this.generateData(100)
			};
		},
		methods: {
			scrollToRow() {
				// scrollTo 方法需要通过实例调用
				console.log("滚动到第50行");
			},
			scrollToTop() {
				console.log("滚动到顶部");
			},
			generateData(count) {
				return Array.from({ length: count }, (_, i) => ({
					id: i + 1,
					name: `User ${i + 1}`,
					date: `2024-01-${String((i % 28) + 1).padStart(2, "0")}`,
					hobby: "coding"
				}));
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
