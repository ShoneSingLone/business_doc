<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<xTableEasy
				:columns="columns"
				:table-data="tableData"
				:event-custom-option="eventCustomOption"
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
				mdDoc: "header 行事件自定义：通过 `eventCustomOption.headerRowEvents` 自定义表头行的鼠标事件",
				eventLogs: [],
				eventCustomOption: {
					headerRowEvents: ({ rowIndex }) => {
						return {
							mouseenter: (e) => {
								this.eventLogs.push(`[${new Date().toLocaleTimeString()}] header row ${rowIndex} mouseenter`);
								if (this.eventLogs.length > 5) this.eventLogs.shift();
							},
							mouseleave: (e) => {
								this.eventLogs.push(`[${new Date().toLocaleTimeString()}] header row ${rowIndex} mouseleave`);
								if (this.eventLogs.length > 5) this.eventLogs.shift();
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
	margin-top: 16px;
	padding: 12px;
	background-color: #f5f7fa;
	border-radius: 4px;
	font-size: 12px;
	max-height: 150px;
	overflow-y: auto;
}
</style>
