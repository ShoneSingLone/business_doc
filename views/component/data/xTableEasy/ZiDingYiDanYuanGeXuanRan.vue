<template>
	<div class="card-ZiDingYiDanYuanGeXuanRan">
		<xMd :md="mdTips" />
		<xTableEasy
			:columns="columns"
			:table-data="tableData"
			:max-height="400"
			border-x
			border-y />
	</div>
</template>
<script lang="ts">
export default async function () {
	return defineComponent({
		data() {
			return {
				mdTips: `
- 1、通过配置 cellRenderer 函数，可以实现自定义单元格渲染。
- 2、支持返回 HTML 字符串进行富文本渲染。
- 3、可以实现状态标签、进度条、操作按钮等复杂效果。
`,
				tableData: [
					{
						id: 1,
						name: "张三",
						age: 18,
						sex: "男",
						phone: "13800000001",
						address: "上海市普陀区金沙江路 1518 弄",
						status: 1,
						score: 95
					},
					{
						id: 2,
						name: "李四",
						age: 20,
						sex: "女",
						phone: "13800000002",
						address: "上海市浦东新区张江高科技园区",
						status: 2,
						score: 88
					},
					{
						id: 3,
						name: "王五",
						age: 22,
						sex: "男",
						phone: "13800000003",
						address: "北京市海淀区中关村大街 1 号",
						status: 3,
						score: 76
					},
					{
						id: 4,
						name: "赵六",
						age: 25,
						sex: "女",
						phone: "13800000004",
						address: "广州市天河区天河路 385 号",
						status: 1,
						score: 92
					},
					{
						id: 5,
						name: "钱七",
						age: 28,
						sex: "男",
						phone: "13800000005",
						address: "深圳市南山区科技园南区",
						status: 2,
						score: 84
					}
				],
				columns: [
					{ field: "id", key: "id", title: "ID", width: 80, align: "center" },
					{ field: "name", key: "name", title: "姓名", width: 120, align: "left" },
					{ field: "age", key: "age", title: "年龄", width: 80, align: "center" },
					{
						field: "sex",
						key: "sex",
						title: "性别",
						width: 80,
						align: "center",
						cellRenderer: row =>
							row.sex === "男"
								? `<span style="color: blue;">${row.sex}</span>`
								: `<span style="color: pink;">${row.sex}</span>`
					},
					{
						field: "status",
						key: "status",
						title: "状态",
						width: 120,
						align: "center",
						cellRenderer: row => {
							const statusMap = {
								1: "<span style='color: green;'>正常</span>",
								2: "<span style='color: orange;'>待审核</span>",
								3: "<span style='color: red;'>已禁用</span>"
							};
							return statusMap[row.status] || "未知";
						}
					},
					{
						field: "score",
						key: "score",
						title: "分数",
						width: 150,
						align: "center",
						cellRenderer: row => {
							const score = row.score;
							let color = "red";
							if (score >= 90) color = "green";
							else if (score >= 80) color = "blue";
							else if (score >= 60) color = "orange";
							return `<div style="display: flex; align-items: center; justify-content: center;">
								<span style="color: ${color}; font-weight: bold;">${score}</span>
								<div style="width: 80px; height: 6px; background: #e0e0e0; margin-left: 8px; border-radius: 3px;">
									<div style="height: 100%; background: ${color}; width: ${score}%; border-radius: 3px;"></div>
								</div>
							</div>`;
						}
					},
					{
						field: "action",
						key: "action",
						title: "操作",
						width: 150,
						align: "center",
						cellRenderer: row => `<div style="display: flex; gap: 8px;">
							<button onclick="alert('编辑用户 ${row.name}')" style="padding: 4px 8px; background: #409eff; color: white; border: none; border-radius: 4px; cursor: pointer; font-size: 12px;">编辑</button>
							<button onclick="alert('删除用户 ${row.name}')" style="padding: 4px 8px; background: #f56c6c; color: white; border: none; border-radius: 4px; cursor: pointer; font-size: 12px;">删除</button>
						</div>`
					}
				]
			};
		}
	});
}
</script>
<style lang="less">
.card-ZiDingYiDanYuanGeXuanRan {
}
</style>
