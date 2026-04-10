<template>
	<DocContentOfDemo class="x-table-easy-cell-custom">
		<xMd :md="mdTips" />
		<xTableEasy :columns="columns" :table-data="tableData" border-x border-y />
		<xMd :md="apiString" data-role="api" />
	</DocContentOfDemo>
</template>

<script lang="ts">
export default async function () {
	return {
		data() {
			return {
				mdTips: `
- 1、通过列配置中的 \`renderBodyCell\` 可以自定义单元格内容渲染。
- 2、渲染函数会收到当前行、当前列、当前行索引等上下文信息。
- 3、当前示例同时演示文本徽标与简单进度条两种自定义渲染方式。
`,
				apiString: `
## API

### 列自定义渲染
| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| renderBodyCell | 自定义单元格渲染函数 | Function({ row, column, rowIndex }, h) | - |
`,
				columns: [
					{ field: "name", key: "name", title: "姓名", width: 140 },
					{ field: "role", key: "role", title: "岗位", width: 180 },
					{
						field: "status",
						key: "status",
						title: "状态",
						width: 120,
						align: "center",
						renderBodyCell: ({ row }, h) => {
							const statusMap = {
								active: { text: "启用", color: "#67c23a" },
								pending: { text: "待审核", color: "#e6a23c" },
								disabled: { text: "已禁用", color: "#f56c6c" }
							};
							const current = statusMap[row.status] || statusMap.disabled;
							return h(
								"span",
								{
									style: {
										display: "inline-block",
										padding: "2px 10px",
										borderRadius: "12px",
										color: "#fff",
										backgroundColor: current.color
									}
								},
								[current.text]
							);
						}
					},
					{
						field: "score",
						key: "score",
						title: "完成度",
						width: 220,
						renderBodyCell: ({ row }, h) => {
							return h("div", { class: "score-cell" }, [
								h("span", { class: "score-cell__label" }, [`${row.score}%`]),
								h("div", { class: "score-cell__track" }, [
									h("div", {
										class: "score-cell__bar",
										style: { width: `${row.score}%` }
									})
								])
							]);
						}
					}
				],
				tableData: [
					{ name: "张三", role: "前端开发", status: "active", score: 92 },
					{ name: "李四", role: "测试工程师", status: "pending", score: 76 },
					{ name: "王五", role: "产品经理", status: "disabled", score: 48 }
				]
			};
		}
	};
}
</script>

<style lang="less">
.x-table-easy-cell-custom {
	.score-cell {
		display: flex;
		align-items: center;
		gap: 8px;
	}

	.score-cell__label {
		width: 42px;
		text-align: right;
	}

	.score-cell__track {
		flex: 1;
		height: 8px;
		background-color: #ebeef5;
		border-radius: 4px;
		overflow: hidden;
	}

	.score-cell__bar {
		height: 100%;
		background-color: #409eff;
		border-radius: 4px;
	}
}
</style>
