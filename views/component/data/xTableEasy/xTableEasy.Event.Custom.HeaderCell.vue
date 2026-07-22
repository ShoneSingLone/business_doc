<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<div class="event-log">
				<ul>
					<li v-for="(log, index) in eventLogs" :key="index">
						{{ log.time }} - {{ log.message }}
					</li>
				</ul>
			</div>
			<xTableEasy
				:columns="columns"
				:table-data="tableData"
				border-x
				border-y
				@on-header-cell-click="handleHeaderCellClick" />
		</div>
	</div>
</template>
<script lang="ts">
export default async function () {
	return defineComponent({
		data() {
			return {
				mdDoc: "header 单元格事件：监听表头单元格点击事件",
				eventLogs: [],
				columns: [
					{ field: "name", key: "name", title: "姓名", width: 120 },
					{ field: "department", key: "department", title: "部门", width: 150 },
					{ field: "score", key: "score", title: "评分", width: 100, align: "center" }
				],
				tableData: [
					{ name: "张三", department: "研发一组", score: 95 },
					{ name: "李四", department: "质量保障", score: 88 },
					{ name: "王五", department: "产品中心", score: 91 }
				]
			};
		},
		methods: {
			addLog(message) {
				const now = new Date();
				const time = `${now.getHours().toString().padStart(2, "0")}:${now.getMinutes().toString().padStart(2, "0")}:${now.getSeconds().toString().padStart(2, "0")}`;
				this.eventLogs.unshift({ time, message });
				if (this.eventLogs.length > 5) {
					this.eventLogs.pop();
				}
			},
			handleHeaderCellClick({ column, columnIndex }) {
				this.addLog(`点击表头 [列${columnIndex + 1}]: ${column.title}`);
			}
		}
	});
}
</script>
<style lang="less">
.event-log {
	margin-bottom: 12px;
	padding: 8px;
	background-color: #f5f7fa;
	border-radius: 4px;
	max-height: 100px;
	overflow-y: auto;

	ul {
		list-style: none;
		padding: 0;
		margin: 0;

		li {
			padding: 3px 0;
			font-size: 12px;
			color: #f56c6c;
		}
	}
}
</style>
