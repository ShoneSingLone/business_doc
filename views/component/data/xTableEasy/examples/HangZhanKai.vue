<template>
	<div class="example-container">
		<h3>行展开示例</h3>
		<div class="example-desc">
			展示如何使用表格的行展开功能，支持点击展开/折叠行，查看详细信息。
		</div>

		<!-- 操作按钮 -->
		<div class="example-actions">
			<el-button type="primary" @click="expandAll">展开所有</el-button>
			<el-button type="primary" @click="collapseAll">折叠所有</el-button>
			<el-button type="info" @click="toggleRandom">随机展开/折叠</el-button>
		</div>

		<!-- 表格组件 -->
		<x-table-easy
			:table-data="tableData"
			:columns="columns"
			:expand-option="expandOption"
			row-key-field-name="id"
			@row-expand="handleRowExpand"
			@row-collapse="handleRowCollapse"
			@expand-change="handleExpandChange">
			<!-- 展开内容插槽 -->
			<template #expand="{ row, rowIndex }">
				<div class="expand-content">
					<h4>行详细信息 #{{ rowIndex + 1 }}</h4>
					<div class="detail-item">
						<span class="label">ID:</span>
						<span class="value">{{ row.id }}</span>
					</div>
					<div class="detail-item">
						<span class="label">名称:</span>
						<span class="value">{{ row.name }}</span>
					</div>
					<div class="detail-item">
						<span class="label">年龄:</span>
						<span class="value">{{ row.age }}</span>
					</div>
					<div class="detail-item">
						<span class="label">地址:</span>
						<span class="value">{{ row.address }}</span>
					</div>
					<div class="detail-item">
						<span class="label">描述:</span>
						<span class="value">{{ row.description }}</span>
					</div>
					<div class="detail-actions">
						<el-button size="small" type="primary">编辑</el-button>
						<el-button size="small" type="danger">删除</el-button>
					</div>
				</div>
			</template>
		</x-table-easy>

		<!-- 事件日志 -->
		<div class="event-log">
			<h4>事件日志</h4>
			<div class="log-list">
				<div v-for="(log, index) in eventLogs" :key="index" class="log-item">
					<span class="log-time">{{ log.time }}</span>
					<span class="log-content">{{ log.content }}</span>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: "HangZhanKai",
	data() {
		return {
			// 展开配置
			expandOption: {
				enable: true
			},
			// 列配置
			columns: [
				{
					field: "name",
					title: "姓名",
					width: 120
				},
				{
					field: "age",
					title: "年龄",
					width: 80,
					align: "center"
				},
				{
					field: "gender",
					title: "性别",
					width: 80,
					align: "center"
				},
				{
					field: "email",
					title: "邮箱",
					width: 200
				},
				{
					field: "phone",
					title: "电话",
					width: 150
				}
			],
			// 表格数据
			tableData: [],
			// 事件日志
			eventLogs: []
		};
	},
	mounted() {
		this.initData();
	},
	methods: {
		// 初始化数据
		initData() {
			this.tableData = [];
			for (let i = 0; i < 20; i++) {
				this.tableData.push({
					id: i + 1,
					name: `用户${i + 1}`,
					age: Math.floor(Math.random() * 50) + 18,
					gender: Math.random() > 0.5 ? "男" : "女",
					email: `user${i + 1}@example.com`,
					phone: `138${Math.floor(Math.random() * 100000000)}`,
					address: `北京市朝阳区某某街道${Math.floor(Math.random() * 1000)}号`,
					description: `这是用户${i + 1}的详细描述，包含用户的基本信息和其他相关内容。用户${i + 1}是一位活跃的系统用户，经常使用系统的各项功能。`
				});
			}
		},

		// 展开所有行
		expandAll() {
			this.$refs.table.expandAllRows();
			this.addLog("展开所有行");
		},

		// 折叠所有行
		collapseAll() {
			this.$refs.table.collapseAllRows();
			this.addLog("折叠所有行");
		},

		// 随机展开/折叠行
		toggleRandom() {
			const randomIndex = Math.floor(Math.random() * this.tableData.length);
			const row = this.tableData[randomIndex];
			this.$refs.table.toggleRowExpand(row, randomIndex);
			this.addLog(`随机切换行 ${randomIndex + 1} 的展开状态`);
		},

		// 处理行展开事件
		handleRowExpand({ row, rowIndex }) {
			this.addLog(`行 ${rowIndex + 1} (${row.name}) 展开`);
		},

		// 处理行折叠事件
		handleRowCollapse({ row, rowIndex }) {
			this.addLog(`行 ${rowIndex + 1} (${row.name}) 折叠`);
		},

		// 处理展开状态变化事件
		handleExpandChange({ rowKey, expanded, row, rowIndex }) {
			this.addLog(
				`行 ${rowIndex + 1} (${row.name}) 展开状态变为: ${expanded ? "展开" : "折叠"}`
			);
		},

		// 添加日志
		addLog(content) {
			const now = new Date();
			const time = `${now.getHours().toString().padStart(2, "0")}:${now.getMinutes().toString().padStart(2, "0")}:${now.getSeconds().toString().padStart(2, "0")}`;
			this.eventLogs.unshift({ time, content });
			// 只保留最近20条日志
			if (this.eventLogs.length > 20) {
				this.eventLogs.pop();
			}
		}
	}
};
</script>

<style scoped>
.example-container {
	padding: 20px;
}

.example-desc {
	margin: 10px 0 20px;
	color: #666;
	font-size: 14px;
}

.example-actions {
	margin-bottom: 20px;
	display: flex;
	gap: 10px;
}

/* 展开内容样式 */
.expand-content {
	padding: 16px;
	background-color: #fafafa;
	border-radius: 4px;
	border: 1px solid #e8e8e8;
}

.expand-content h4 {
	margin: 0 0 16px;
	color: #333;
	font-size: 16px;
	font-weight: 500;
}

.detail-item {
	margin-bottom: 12px;
	display: flex;
	align-items: center;
}

.detail-item .label {
	width: 80px;
	font-weight: 500;
	color: #666;
}

.detail-item .value {
	flex: 1;
	color: #333;
}

.detail-actions {
	margin-top: 16px;
	display: flex;
	gap: 10px;
}

/* 事件日志样式 */
.event-log {
	margin-top: 20px;
	padding: 16px;
	background-color: #f5f7fa;
	border-radius: 4px;
}

.event-log h4 {
	margin: 0 0 16px;
	color: #333;
	font-size: 16px;
	font-weight: 500;
}

.log-list {
	max-height: 200px;
	overflow-y: auto;
	border: 1px solid #e8e8e8;
	border-radius: 4px;
	background-color: #fff;
}

.log-item {
	padding: 8px 12px;
	border-bottom: 1px solid #f0f0f0;
	font-size: 14px;
	display: flex;
	align-items: center;
}

.log-item:last-child {
	border-bottom: none;
}

.log-time {
	width: 80px;
	color: #999;
	font-size: 12px;
	margin-right: 12px;
}

.log-content {
	flex: 1;
	color: #666;
}
</style>
