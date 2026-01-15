<template>
	<div>
		<h3>虚拟滚动 (4000 条数据)</h3>
		<p>虚拟滚动可以高效渲染大量数据，只渲染可视区域内的数据行，提升性能。</p>
		<xTableEasy
			:columns="columns"
			:tableData="tableData"
			:maxHeight="500"
			borderX
			borderY
			rowKeyFieldName="id"
			:virtualScrollOption="virtualScrollOption" />
	</div>
</template>
<script lang="ts">
export default async function () {
	// 生成大量测试数据
	const generateTestData = () => {
		const data = [];
		for (let i = 0; i < 4000; i++) {
			data.push({
				id: i + 1,
				name: `用户${i + 1}`,
				age: 18 + Math.floor(Math.random() * 30),
				sex: Math.random() > 0.5 ? "男" : "女",
				phone: `1380000${String(i).padStart(4, "0")}`,
				address: `上海市浦东新区张江高科技园区 ${i + 1} 号`,
				status: Math.floor(Math.random() * 3) + 1,
				score: Math.floor(Math.random() * 100) + 1
			});
		}
		return data;
	};

	return {
		data() {
			return {
				// 表格数据
				tableData: generateTestData(),
				// 列配置
				columns: [
					{
						colKey: "id",
						field: "id",
						title: "ID",
						width: 100,
						align: "center"
					},
					{
						colKey: "name",
						field: "name",
						title: "姓名",
						width: 120,
						align: "left"
					},
					{
						colKey: "age",
						field: "age",
						title: "年龄",
						width: 80,
						align: "center"
					},
					{
						colKey: "sex",
						field: "sex",
						title: "性别",
						width: 80,
						align: "center"
					},
					{
						colKey: "phone",
						field: "phone",
						title: "电话号码",
						width: 150,
						align: "left"
					},
					{
						colKey: "address",
						field: "address",
						title: "地址",
						width: 250,
						align: "left"
					},
					{
						colKey: "status",
						field: "status",
						title: "状态",
						width: 120,
						align: "center",
						cellRenderer: (row, column, rowIndex, colIndex) => {
							const statusMap = {
								1: "<span style='color: green;'>正常</span>",
								2: "<span style='color: orange;'>待审核</span>",
								3: "<span style='color: red;'>已禁用</span>"
							};
							return statusMap[row.status] || "未知";
						}
					},
					{
						colKey: "score",
						field: "score",
						title: "分数",
						width: 100,
						align: "center"
					}
				],
				// 虚拟滚动配置
				virtualScrollOption: {
					enable: true,
					bufferScale: 1, // 缓冲比例
					minRowHeight: 40, // 最小行高
					scrolling: (
						startRowIndex,
						visibleStartIndex,
						visibleEndIndex,
						visibleAboveCount,
						visibleBelowCount
					) => {
						console.log("虚拟滚动数据范围:", {
							startRowIndex,
							visibleStartIndex,
							visibleEndIndex,
							visibleAboveCount,
							visibleBelowCount
						});
					}
				}
			};
		}
	};
}
</script>
<style lang="less">
h3 {
	margin: 0 0 10px 0;
	font-size: 16px;
	font-weight: 500;
}

p {
	margin: 0 0 15px 0;
	color: #606266;
	font-size: 14px;
}
</style>
