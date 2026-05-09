<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<xTableEasy :columns="columns" :table-data="tableData" border-x border-y />
		</div>
	</div>
</template>
<script lang="ts">
export default async function () {
	return defineComponent({
		data() {
			return {
				mdDoc: "通过 columns 配置中的 render 函数来自定义单元格渲染内容",
				columns: [
					{ field: "name", key: "a", title: "Name", width: 120 },
					{
						field: "gender",
						key: "b",
						title: "Gender",
						width: 100,
						align: "center",
						render: (row, column, rowIndex, colIndex) => {
							return row.gender === "male"
								? '<span style="color: #1890ff;">男</span>'
								: '<span style="color: "#f50057;">女</span>';
						}
					},
					{
						field: "status",
						key: "c",
						title: "Status",
						width: 120,
						align: "center",
						render: (row, column, rowIndex, colIndex) => {
							const statusMap = {
								active: { text: "启用", color: "#52c41a" },
								inactive: { text: "禁用", color: "#ff4d4f" }
							};
							const status = statusMap[row.status] || statusMap.inactive;
							return `<span style="color: ${status.color};">${status.text}</span>`;
						}
					},
					{
						field: "action",
						key: "d",
						title: "Action",
						width: 150,
						align: "center",
						render: (row, column, rowIndex, colIndex) => {
							return `
								<el-button type="primary" size="small">编辑</el-button>
								<el-button type="danger" size="small">删除</el-button>
							`;
						}
					}
				],
				tableData: [
					{ name: "John", gender: "male", status: "active" },
					{ name: "Lili", gender: "female", status: "inactive" },
					{ name: "Tom", gender: "male", status: "active" }
				]
			};
		}
	});
}
</script>