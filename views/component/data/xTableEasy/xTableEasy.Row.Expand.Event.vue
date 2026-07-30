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
			<div class="event-log" v-if="eventLogs.length">
				<strong>事件日志：</strong>
				<div v-for="(log, i) in eventLogs" :key="i">{{ log }}</div>
			</div>
		</div>
	</div>
</template>
<script lang="ts">
export default async function () {
	return defineComponent({
		data() {
			return {
				mdDoc: "行展开事件：通过 `beforeExpandRowChange` 和 `afterExpandRowChange` 监听展开/折叠事件",
				eventLogs: [],
				expandOption: {
					enable: true,
					beforeExpandRowChange: ({ beforeExpandedRowKeys, row, rowIndex }) => {
						this.eventLogs.push(`[${new Date().toLocaleTimeString()}] beforeExpand: ${row.name}, 当前展开: [${beforeExpandedRowKeys}]`);
						return true;
					},
					afterExpandRowChange: ({ afterExpandedRowKeys, row, rowIndex }) => {
						this.eventLogs.push(`[${new Date().toLocaleTimeString()}] afterExpand: ${row.name}, 当前展开: [${afterExpandedRowKeys}]`);
					},
					render: (params, h) => {
						const { row } = params;
						return h("div", { style: { padding: "10px" } }, [
							h("strong", "展开内容："),
							h("span", ` ${row.name} 的详细信息`)
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
<style scoped>
.event-log {
	margin-top: 16px;
	padding: 12px;
	background-color: #f5f7fa;
	border-radius: 4px;
	font-size: 12px;
	max-height: 150px;
	overflow-y: auto;
}
</style>
