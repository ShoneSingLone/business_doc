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
					render: (row) => {
						const hobbies = ["coding", "reading", "gaming", "sports", "music"];
						const subData = Array.from({ length: 3 }, (_, i) => ({
							id: i + 1,
							project: `${row.name}项目${i + 1}`,
							status: ["进行中", "已完成", "计划中"][i],
							progress: `${(i + 1) * 30}%`
						}));
						return `<div style="padding: 10px;">
							<strong>${row.name}的项目列表：</strong>
							<table style="width:100%;border-collapse:collapse;margin-top:8px;">
								<tr style="background:#f5f7fa;">
									<th style="padding:6px;border:1px solid #ebeef5;text-align:left;">ID</th>
									<th style="padding:6px;border:1px solid #ebeef5;text-align:left;">项目</th>
									<th style="padding:6px;border:1px solid #ebeef5;text-align:left;">状态</th>
									<th style="padding:6px;border:1px solid #ebeef5;text-align:left;">进度</th>
								</tr>
								${subData.map(item => `<tr>
									<td style="padding:6px;border:1px solid #ebeef5;">${item.id}</td>
									<td style="padding:6px;border:1px solid #ebeef5;">${item.project}</td>
									<td style="padding:6px;border:1px solid #ebeef5;">${item.status}</td>
									<td style="padding:6px;border:1px solid #ebeef5;">${item.progress}</td>
								</tr>`).join('')}
							</table>
						</div>`;
					}
				},
				columns: [
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
