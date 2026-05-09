<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<h4>一、表体单元格自定义（含操作按钮）</h4>
			<xTableEasy :columns="bodyColumns" :table-data="bodyTableData" border-x border-y />
			<h4>二、表头单元格自定义（含搜索输入框）</h4>
			<xTableEasy :columns="headerColumns" :table-data="headerTableData" border-x border-y />
		</div>
	</div>
</template>
<script lang="ts">
export default async function () {
	return defineComponent({
		data() {
			return {
				searchText: "",
				mdDoc: "通过 columns 配置中的 render（表体）和 renderHeaderCell（表头）函数来自定义单元格渲染内容",
				bodyColumns: [
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
								: '<span style="color: #f50057;">女</span>';
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
				bodyTableData: [
					{ name: "John", gender: "male", status: "active" },
					{ name: "Lili", gender: "female", status: "inactive" },
					{ name: "Tom", gender: "male", status: "active" }
				],
				headerColumns: [
					{
						field: "name",
						key: "a",
						title: "Name",
						width: 180,
						align: "center",
						renderHeaderCell: (column) => {
							return `
								<input 
									type="text" 
									placeholder="搜索名称" 
									style="width:90%;padding:4px;border:1px solid #d9d9d9;border-radius:4px;"
									oninput="this.parentNode.parentNode.parentNode.parentNode.parentNode.__vue__.$data.searchText = this.value"
								/>
							`;
						}
					},
					{
						field: "date",
						key: "b",
						title: "Date",
						width: 150,
						renderHeaderCell: (column) => {
							return `<span style="color:#1890ff;font-weight:bold;">${column.title}</span>`;
						}
					},
					{ field: "address", key: "c", title: "Address", width: 200 }
				],
				headerTableData: [
					{ name: "张三", date: "2024-01-01", address: "北京市朝阳区" },
					{ name: "李四", date: "2024-01-02", address: "上海市浦东新区" },
					{ name: "王五", date: "2024-01-03", address: "广州市天河区" }
				]
			};
		}
	});
}
</script>