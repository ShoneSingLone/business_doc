<template>
	<DocContentOfDemo class="x-table-easy-pagination">
		<xMd :md="mdTips" />
		<xTableEasy 
			:columns="columns" 
			:table-data="displayData" 
			border-x 
			border-y />
		<div class="pagination-wrapper">
			<xPagination
				:total="total"
				:page-size="pageSize"
				:current-page="currentPage"
				@current-change="handlePageChange" />
		</div>
		<xMd :md="apiString" data-role="api" />
	</DocContentOfDemo>
</template>

<script lang="ts">
export default async function () {
	return {
		data() {
			return {
				mdTips: `
- 1、表格支持与分页组件配合使用
- 2、通过控制显示的数据实现分页效果
- 3、支持自定义分页大小和当前页码
`,
				apiString: `
## API

### 分页相关配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| total | 总记录数 | Number | 0 |
| pageSize | 每页显示条数 | Number | 10 |
| currentPage | 当前页码 | Number | 1 |
`,
				currentPage: 1,
				pageSize: 10,
				total: 100,
				columns: [
					{ field: "id", key: "id", title: "ID", width: 80, align: "center" },
					{ field: "name", key: "name", title: "姓名", width: 120 },
					{ field: "department", key: "department", title: "部门", width: 150 },
					{ field: "score", key: "score", title: "评分", width: 100, align: "center" }
				],
				allData: Array.from({ length: 100 }, (_, i) => ({
					id: i + 1,
					name: `用户${i + 1}`,
					department: `部门${(i % 5) + 1}`,
					score: 60 + Math.floor(Math.random() * 40)
				}))
			};
		},
		computed: {
			displayData() {
				const start = (this.currentPage - 1) * this.pageSize;
				const end = start + this.pageSize;
				return this.allData.slice(start, end);
			}
		},
		methods: {
			handlePageChange(page) {
				this.currentPage = page;
			}
		}
	};
}
</script>

<style lang="less">
.x-table-easy-pagination {
	.pagination-wrapper {
		margin-top: 16px;
		display: flex;
		justify-content: center;
	}
}
</style>