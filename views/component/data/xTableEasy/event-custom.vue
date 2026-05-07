<template>
	<DocContentOfDemo class="x-table-easy-event-custom">
		<xMd :md="mdTips" />
		<div class="event-log">
			<h3>事件日志</h3>
			<ul>
				<li v-for="(log, index) in eventLogs" :key="index" :class="log.type">
					{{ log.time }} - {{ log.message }}
				</li>
			</ul>
		</div>
		<xTableEasy 
			:columns="columns" 
			:table-data="tableData" 
			border-x 
			border-y
			@on-body-cell-click="handleBodyCellClick"
			@on-body-row-click="handleBodyRowClick"
			@on-header-cell-click="handleHeaderCellClick" />
		<xMd :md="apiString" data-role="api" />
	</DocContentOfDemo>
</template>

<script lang="ts">
export default async function () {
	return {
		data() {
			return {
				mdTips: `
- 1、表格支持多种自定义事件监听
- 2、可监听单元格点击、行点击、表头点击等事件
- 3、事件参数包含当前行、列、索引等信息
`,
				apiString: `
## API

### 自定义事件

| 事件名 | 说明 | 参数 |
|--------|------|------|
| on-body-cell-click | 单元格点击事件 | { row, column, rowIndex, columnIndex } |
| on-body-row-click | 行点击事件 | { row, rowIndex } |
| on-header-cell-click | 表头点击事件 | { column, columnIndex } |
| on-header-row-click | 表头行点击事件 | { columns } |
`,
				eventLogs: [],
				columns: [
					{ field: "id", key: "id", title: "ID", width: 80, align: "center" },
					{ field: "name", key: "name", title: "姓名", width: 120 },
					{ field: "department", key: "department", title: "部门", width: 150 },
					{ field: "score", key: "score", title: "评分", width: 100, align: "center" }
				],
				tableData: [
					{ id: 1, name: "张三", department: "研发一组", score: 95 },
					{ id: 2, name: "李四", department: "质量保障", score: 88 },
					{ id: 3, name: "王五", department: "产品中心", score: 91 }
				]
			};
		},
		methods: {
			addLog(type, message) {
				const now = new Date();
				const time = `${now.getHours().toString().padStart(2, '0')}:${now.getMinutes().toString().padStart(2, '0')}:${now.getSeconds().toString().padStart(2, '0')}`;
				this.eventLogs.unshift({ time, type, message });
				if (this.eventLogs.length > 10) {
					this.eventLogs.pop();
				}
			},
			handleBodyCellClick({ row, column }) {
				this.addLog('cell', `单元格点击: ${column.title} = ${row[column.field]}`);
			},
			handleBodyRowClick({ row }) {
				this.addLog('row', `行点击: ${row.name}`);
			},
			handleHeaderCellClick({ column }) {
				this.addLog('header', `表头点击: ${column.title}`);
			}
		}
	};
}
</script>

<style lang="less">
.x-table-easy-event-custom {
	.event-log {
		margin-bottom: 16px;
		padding: 12px;
		background-color: #f5f7fa;
		border-radius: 4px;
		max-height: 200px;
		overflow-y: auto;
		
		h3 {
			margin: 0 0 10px 0;
			font-size: 14px;
			font-weight: 600;
		}
		
		ul {
			list-style: none;
			padding: 0;
			margin: 0;
			
			li {
				padding: 4px 0;
				font-size: 12px;
				
				&.cell { color: #409eff; }
				&.row { color: #67c23a; }
				&.header { color: #f56c6c; }
			}
		}
	}
}
</style>