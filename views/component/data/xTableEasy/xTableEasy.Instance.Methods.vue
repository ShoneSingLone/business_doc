<template>
	<DocContentOfDemo class="x-table-easy-instance-methods">
		<xMd :md="mdTips" />
		<div class="demo-controls">
			<xBtn @click="scrollToTop">滚动到顶部</xBtn>
			<xBtn @click="scrollToRow(2)">滚动到第3行</xBtn>
			<xBtn @click="scrollToColumn('name')">滚动到姓名列</xBtn>
		</div>
		<xTableEasy 
			ref="tableRef"
			:columns="columns" 
			:table-data="tableData" 
			:max-height="300"
			border-x 
			border-y />
		<xMd :md="apiString" data-role="api" />
	</DocContentOfDemo>
</template>

<script lang="ts">
export default async function () {
	return {
		data() {
			return {
				mdTips: `
- 1、表格提供多种实例方法用于操作表格
- 2、需要通过 ref 获取表格实例
- 3、支持滚动到指定行、列等操作
`,
				apiString: `
## API

### 实例方法

| 方法名 | 说明 | 参数 |
|--------|------|------|
| scrollTo | 滚动到指定位置 | { rowIndex, columnIndex } |
| scrollToRowKey | 滚动到指定行key | rowKey |
| scrollToColKey | 滚动到指定列key | colKey |
| scrollToTop | 滚动到顶部 | - |
| clearSelection | 清除选中状态 | - |
`,
				columns: [
					{ field: "id", key: "id", title: "ID", width: 80, align: "center" },
					{ field: "name", key: "name", title: "姓名", width: 120 },
					{ field: "department", key: "department", title: "部门", width: 150 },
					{ field: "position", key: "position", title: "岗位", width: 120 },
					{ field: "city", key: "city", title: "城市", width: 100 },
					{ field: "score", key: "score", title: "评分", width: 100, align: "center" }
				],
				tableData: Array.from({ length: 50 }, (_, i) => ({
					id: i + 1,
					name: `用户${i + 1}`,
					department: `部门${(i % 5) + 1}`,
					position: ["前端开发", "后端开发", "测试", "产品", "设计"][i % 5],
					city: ["北京", "上海", "广州", "深圳", "杭州"][i % 5],
					score: 60 + Math.floor(Math.random() * 40)
				}))
			};
		},
		methods: {
			scrollToTop() {
				this.$refs.tableRef.scrollToTop();
			},
			scrollToRow(index) {
				this.$refs.tableRef.scrollTo({ rowIndex: index });
			},
			scrollToColumn(key) {
				this.$refs.tableRef.scrollToColKey(key);
			}
		}
	};
}
</script>

<style lang="less">
.x-table-easy-instance-methods {
	.demo-controls {
		display: flex;
		gap: 12px;
		margin-bottom: 16px;
	}
}
</style>