<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<xTableEasy
				border-y
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
				mdDoc: "自定义 footer 单元格渲染内容",
				columns: [
					{ field: "name", key: "name", title: "姓名", width: 120 },
					{ field: "department", key: "department", title: "部门", width: 150 },
					{
						field: "score",
						key: "score",
						title: "评分",
						width: 100,
						align: "center",
						renderFooterCell: ({ row, column }) => {
							return `<span style="color: ${row.score >= 90 ? "#67c23a" : "#f56c6c"}">${row.score}</span>`;
						}
					},
					{
						field: "bonus",
						key: "bonus",
						title: "奖金",
						width: 120,
						align: "right",
						renderFooterCell: ({ row, column }) => {
							return `<strong>¥${row.bonus.toLocaleString()}</strong>`;
						}
					}
				],
				tableData: [
					{ name: "张三", department: "研发一组", score: 95, bonus: 5000 },
					{ name: "李四", department: "质量保障", score: 88, bonus: 4000 },
					{ name: "王五", department: "产品中心", score: 91, bonus: 4500 }
				],
				footerData: [{ name: "汇总", department: "-", score: 274, bonus: 13500 }]
			};
		}
	});
}
</script>
<style lang="less"></style>
