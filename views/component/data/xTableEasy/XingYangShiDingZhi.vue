<template>
	<div class="card-XingYangShiDingZhi">
		<xMd :md="mdTips" />
		<xTableEasy :columns="columns" :table-data="tableData" :max-height="400" border-x border-y row-key-field-name="id" :row-style-option="rowStyleOption" />
	</div>
</template>
<script lang="ts">
export default async function () {
	return defineComponent({
		data() {
			return {
				mdTips: `
- 1、通过配置 row-style-option，可以实现行样式的定制。
- 2、支持斑马纹、悬停高亮和点击高亮三种基础样式。
- 3、支持自定义行样式和行类名，实现条件样式。
`,
				tableData: [
					{ id: 1, name: "张三", age: 18, sex: "男", phone: "13800000001", address: "上海市普陀区金沙江路 1518 弄", score: 95, status: 1 },
					{ id: 2, name: "李四", age: 20, sex: "女", phone: "13800000002", address: "上海市浦东新区张江高科技园区", score: 88, status: 2 },
					{ id: 3, name: "王五", age: 22, sex: "男", phone: "13800000003", address: "北京市海淀区中关村大街 1 号", score: 76, status: 3 }
				],
				columns: [
					{ field: "id", key: "id", title: "ID", width: 80, align: "center" },
					{ field: "name", key: "name", title: "姓名", width: 120, align: "left" },
					{ field: "age", key: "age", title: "年龄", width: 80, align: "center" },
					{ field: "sex", key: "sex", title: "性别", width: 80, align: "center" },
					{ field: "phone", key: "phone", title: "电话号码", width: 150, align: "left" },
					{ field: "address", key: "address", title: "地址", width: 250, align: "left" },
					{ field: "score", key: "score", title: "分数", width: 100, align: "center" }
				],
				rowStyleOption: {
					stripe: true,
					hoverHighlight: true,
					clickHighlight: true,
					rowStyle: (row) => {
						if (row.score >= 90) return { backgroundColor: "rgba(72, 187, 120, 0.1)" };
						if (row.score >= 80) return { backgroundColor: "rgba(64, 158, 255, 0.1)" };
						if (row.score >= 60) return { backgroundColor: "rgba(250, 173, 20, 0.1)" };
						return { backgroundColor: "rgba(245, 108, 108, 0.1)" };
					},
					rowClass: (row) => ({
						"row-high-score": row.score >= 90,
						"row-middle-score": row.score >= 80 && row.score < 90,
						"row-low-score": row.score < 60
					})
				}
			};
		}
	});
}
</script>
<style lang="less">
.card-XingYangShiDingZhi {
	:deep(.x-table-easy) {
		.row-high-score td {
			font-weight: bold;
			color: #67c23a;
		}
		.row-middle-score td {
			font-weight: bold;
			color: #409eff;
		}
		.row-low-score td {
			font-weight: bold;
			color: #f56c6c;
		}
	}
}
</style>