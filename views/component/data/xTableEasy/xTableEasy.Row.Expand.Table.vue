<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<xTableEasy
				:columns="columns"
				:table-data="tableData"
				:expand-option="expandOption"
				:row-key-field-name="'name'"
				border-x
				border-y />
		</div>
	</div>
</template>
<script lang="ts">
export default async function () {
	return defineComponent({
		data() {
			return {
				mdDoc: "展开表格：展开行中嵌套显示子表格",
				expandOption: {
					enable: true,
					render: (params, h) => {
						const { row } = params;
						const subData = [
							{ id: 1, project: `${row.name}项目1`, status: "进行中", progress: "30%" },
							{ id: 2, project: `${row.name}项目2`, status: "已完成", progress: "60%" },
							{ id: 3, project: `${row.name}项目3`, status: "计划中", progress: "90%" }
						];
						return h("div", { style: { padding: "10px" } }, [
							h("strong", `${row.name}的项目列表：`),
							h("table", { style: { width: "100%", borderCollapse: "collapse", marginTop: "8px" } }, [
								h("tr", { style: { background: "#f5f7fa" } }, [
									h("th", { style: { padding: "6px", border: "1px solid #ebeef5", textAlign: "left" } }, "ID"),
									h("th", { style: { padding: "6px", border: "1px solid #ebeef5", textAlign: "left" } }, "项目"),
									h("th", { style: { padding: "6px", border: "1px solid #ebeef5", textAlign: "left" } }, "状态"),
									h("th", { style: { padding: "6px", border: "1px solid #ebeef5", textAlign: "left" } }, "进度")
								]),
								...subData.map(item =>
									h("tr", [
										h("td", { style: { padding: "6px", border: "1px solid #ebeef5" } }, String(item.id)),
										h("td", { style: { padding: "6px", border: "1px solid #ebeef5" } }, item.project),
										h("td", { style: { padding: "6px", border: "1px solid #ebeef5" } }, item.status),
										h("td", { style: { padding: "6px", border: "1px solid #ebeef5" } }, item.progress)
									])
								)
							])
						]);
					}
				},
				columns: [
					{ type: "expand", key: "expand", width: 50 },
					{ field: "name", key: "name", title: "Name", width: 100 },
					{ field: "date", key: "date", title: "Tel", width: 150 },
					{ field: "hobby", key: "hobby", title: "Hobby", width: 200 },
					{ field: "address", key: "address", title: "Address", width: 300 }
				],
				tableData: [
					{ name: "John", date: "1900-05-20", hobby: "coding", address: "Shanghai" },
					{ name: "Dickerson", date: "1910-06-20", hobby: "reading", address: "Beijing" },
					{ name: "Larsen", date: "2000-07-20", hobby: "gaming", address: "Chongqing" }
				]
			};
		}
	});
}
</script>
