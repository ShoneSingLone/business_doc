<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<xTableEasy
				border-y
				:max-height="300"
				:columns="columns"
				:table-data="tableData"
				:footer-data="footerData"
				:cell-span-option="cellSpanOption" />
		</div>
	</div>
</template>
<script lang="ts">
export default async function () {
	return defineComponent({
		data() {
			return {
				mdDoc: "footer 列合并：设置汇总第1行的评分列和奖金列合并",
				cellSpanOption: {
					footerCellSpan: this.footerCellSpan
				},
				columns: [
					{ field: "name", key: "name", title: "姓名", width: 120, align: "center" },
					{
						field: "department",
						key: "department",
						title: "部门",
						width: 150,
						align: "left"
					},
					{ field: "score", key: "score", title: "评分", width: 100, align: "center" },
					{ field: "bonus", key: "bonus", title: "奖金", width: 120, align: "right" }
				],
				tableData: [],
				footerData: []
			};
		},
		created() {
			this.initTableData();
			this.initFooterData();
		},
		methods: {
			footerCellSpan({ row, column, rowIndex }) {
				if (rowIndex === 0) {
					if (column.field === "score") {
						return { rowspan: 1, colspan: 2 };
					} else if (column.field === "bonus") {
						return { rowspan: 0, colspan: 0 };
					}
				}
			},
			initTableData() {
				this.tableData = [
					{ name: "张三", department: "研发一组", score: 95, bonus: 5000 },
					{ name: "李四", department: "质量保障", score: 88, bonus: 4000 },
					{ name: "王五", department: "产品中心", score: 91, bonus: 4500 }
				];
			},
			initFooterData() {
				const totalBonus = this.tableData.reduce((sum, item) => sum + item.bonus, 0);
				const avgScore = Math.round(
					this.tableData.reduce((sum, item) => sum + item.score, 0) /
						this.tableData.length
				);
				this.footerData = [
					{ name: "合并演示", department: "跨列展示", score: "合并单元格示例", bonus: 0 },
					{ name: "汇总值", department: "-", score: "-", bonus: totalBonus }
				];
			}
		}
	});
}
</script>
<style lang="less"></style>
