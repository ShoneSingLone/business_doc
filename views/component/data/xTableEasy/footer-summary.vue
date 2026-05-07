<template>
	<DocContentOfDemo class="x-table-easy-footer-summary">
		<xMd :md="mdTips" />
		<xTableEasy 
			:columns="columns" 
			:table-data="tableData" 
			border-x 
			border-y
			:summary-option="summaryOption" />
		<xMd :md="apiString" data-role="api" />
	</DocContentOfDemo>
</template>

<script lang="ts">
export default async function () {
	return {
		data() {
			return {
				mdTips: `
- 1、表格支持页脚汇总行功能
- 2、可自定义汇总计算逻辑
- 3、支持多种汇总类型（求和、平均值、计数等）
`,
				apiString: `
## API

### summaryOption 配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| render | 汇总行渲染函数 | Function | - |
| fixed | 是否固定汇总行 | Boolean | false |
`,
				columns: [
					{ field: "id", key: "id", title: "ID", width: 80, align: "center" },
					{ field: "name", key: "name", title: "姓名", width: 120 },
					{ field: "department", key: "department", title: "部门", width: 150 },
					{ field: "score", key: "score", title: "评分", width: 100, align: "center" },
					{ field: "bonus", key: "bonus", title: "奖金", width: 120, align: "right" }
				],
				tableData: [
					{ id: 1, name: "张三", department: "研发一组", score: 95, bonus: 5000 },
					{ id: 2, name: "李四", department: "质量保障", score: 88, bonus: 4000 },
					{ id: 3, name: "王五", department: "产品中心", score: 91, bonus: 4500 },
					{ id: 4, name: "赵六", department: "研发二组", score: 84, bonus: 3800 }
				],
				summaryOption: {
					render: (data, h) => {
						const totalBonus = data.reduce((sum, item) => sum + item.bonus, 0);
						const avgScore = Math.round(data.reduce((sum, item) => sum + item.score, 0) / data.length);
						return h("tr", [
							h("td", { attrs: { colspan: 3 }, style: { textAlign: "right", fontWeight: "bold" } }, "汇总"),
							h("td", { style: { textAlign: "center", fontWeight: "bold" } }, avgScore),
							h("td", { style: { textAlign: "right", fontWeight: "bold" } }, `¥${totalBonus.toLocaleString()}`)
						]);
					}
				}
			};
		}
	};
}
</script>

<style lang="less">
.x-table-easy-footer-summary {
}
</style>