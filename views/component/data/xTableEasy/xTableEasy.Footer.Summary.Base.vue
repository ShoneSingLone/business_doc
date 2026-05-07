<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<xTableEasy 
				border-y 
				:max-height="300"
				:columns="columns" 
				:table-data="tableData"
				:footer-data="footerData" />
		</div>
	</div>
</template>
<script lang="ts">
export default async function () {
	return defineComponent({
		data() {
			return {
				mdDoc: 'footer 汇总功能，默认汇总数据固定在底部显示',
				columns: [
					{ field: "name", key: "name", title: "姓名", width: 120, align: "center" },
					{ field: "department", key: "department", title: "部门", width: 150, align: "left" },
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
			initTableData() {
				this.tableData = [
					{ name: "张三", department: "研发一组", score: 95, bonus: 5000 },
					{ name: "李四", department: "质量保障", score: 88, bonus: 4000 },
					{ name: "王五", department: "产品中心", score: 91, bonus: 4500 },
					{ name: "赵六", department: "研发二组", score: 84, bonus: 3800 }
				];
			},
			initFooterData() {
				const totalBonus = this.tableData.reduce((sum, item) => sum + item.bonus, 0);
				const avgScore = Math.round(this.tableData.reduce((sum, item) => sum + item.score, 0) / this.tableData.length);
				this.footerData = [
					{ name: "平均值", department: "-", score: avgScore, bonus: Math.round(totalBonus / this.tableData.length) },
					{ name: "汇总值", department: "-", score: "-", bonus: totalBonus }
				];
			}
		}
	});
}
</script>
<style lang="less"></style>
