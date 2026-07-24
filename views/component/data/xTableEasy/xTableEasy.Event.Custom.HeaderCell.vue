<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<div class="event-log" v-if="eventLogs.length">
				<strong>事件日志：</strong>
				<div v-for="(log, i) in eventLogs" :key="i">{{ log }}</div>
			</div>
			<xTableEasy
				:columns="columns"
				:table-data="tableData"
				:event-custom-option="eventCustomOption"
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
				mdDoc: "header 单元格事件：通过 `eventCustomOption.headerCellEvents` 自定义表头单元格的点击事件",
				eventLogs: [],
				eventCustomOption: {
					headerCellEvents: ({ column, rowIndex }) => {
						return {
							click: (e) => {
								const log = `[${new Date().toLocaleTimeString()}] 表头单元格点击: ${column.title}`;
								this.eventLogs.unshift(log);
								if (this.eventLogs.length > 5) this.eventLogs.pop();
							}
						};
					}
				},
				columns: [
					{ field: "name", key: "name", title: "Name", width: 150 },
					{ field: "age", key: "age", title: "Age", width: 100, align: "center" },
					{ field: "hobby", key: "hobby", title: "Hobby", width: 200 }
				],
				tableData: [
					{ name: "John", age: 28, hobby: "coding" },
					{ name: "Dickerson", age: 32, hobby: "reading" },
					{ name: "Larsen", age: 25, hobby: "gaming" }
				]
			};
		}
	});
}
</script>
<style scoped>
.event-log {
	margin-bottom: 12px;
	padding: 8px;
	background-color: #f5f7fa;
	border-radius: 4px;
	max-height: 100px;
	overflow-y: auto;
	font-size: 12px;
	color: #f56c6c;
}
</style>
