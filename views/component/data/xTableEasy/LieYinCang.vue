<template>
	<div class="card-LieYinCang">
		<xMd :md="mdTips" />
		<div class="column-control">
			<h4>列显示控制</h4>
			<div class="checkbox-group">
				<label v-for="column in columns" :key="column.field" class="checkbox-item">
					<input type="checkbox" v-model="visibleColumns[column.field]" @change="handleColumnVisibilityChange" />
					{{ column.title }}
				</label>
			</div>
		</div>
		<xTableEasy :columns="filteredColumns" :table-data="tableData" :max-height="300" border-x border-y />
	</div>
</template>
<script lang="ts">
export default async function () {
	return defineComponent({
		data() {
			return {
				mdTips: `
- 1、通过控制列的可见性配置，可以实现列的隐藏和显示功能。
- 2、通过 computed 属性过滤出可见的列配置。
- 3、可以将列的可见性配置保存到本地存储或后端。
`,
				tableData: [
					{ id: 1, name: "张三", age: 18, sex: "男", phone: "13800000001", email: "zhangsan@example.com", address: "上海市普陀区金沙江路 1518 弄" },
					{ id: 2, name: "李四", age: 20, sex: "女", phone: "13800000002", email: "lisi@example.com", address: "上海市浦东新区张江高科技园区" }
				],
				columns: [
					{ field: "id", key: "id", title: "ID", width: 80, align: "center" },
					{ field: "name", key: "name", title: "姓名", width: 120, align: "left" },
					{ field: "age", key: "age", title: "年龄", width: 80, align: "center" },
					{ field: "sex", key: "sex", title: "性别", width: 80, align: "center" },
					{ field: "phone", key: "phone", title: "电话号码", width: 150, align: "left" },
					{ field: "email", key: "email", title: "邮箱", width: 200, align: "left" },
					{ field: "address", key: "address", title: "地址", width: 250, align: "left" }
				],
				visibleColumns: { id: true, name: true, age: true, sex: true, phone: true, email: false, address: true }
			};
		},
		computed: {
			filteredColumns() {
				return this.columns.filter(column => this.visibleColumns[column.field]);
			}
		},
		methods: {
			handleColumnVisibilityChange() {
				console.log("列可见性变化", this.visibleColumns);
			}
		}
	});
}
</script>
<style lang="less">
.card-LieYinCang {
	.column-control {
		margin-bottom: 15px;
		padding: 12px;
		background-color: #f5f7fa;
		border-radius: 4px;
		
		h4 {
			margin: 0 0 10px 0;
			font-size: 14px;
			font-weight: 500;
		}
		
		.checkbox-group {
			display: flex;
			gap: 10px;
			flex-wrap: wrap;
		}
		
		.checkbox-item {
			display: flex;
			align-items: center;
			gap: 5px;
			cursor: pointer;
		}
	}
}
</style>