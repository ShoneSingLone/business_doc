<template>
	<div class="card-BiaoTouFenZu">
		<xMd :md="mdTips" />
		<xTableEasy :columns="columns" :table-data="tableData" :max-height="400" border-x border-y />
	</div>
</template>
<script lang="ts">
export default async function () {
	return defineComponent({
		data() {
			return {
				mdTips: `
- 1、通过配置 columns 的 children 属性，可以创建多级表头。
- 2、分组列本身不直接绑定字段，最终渲染的数据列仍然是最末级叶子列。
- 3、建议为每个叶子列设置稳定的 key 和宽度，避免分组表头布局错乱。
`,
				tableData: [
					{ id: 1, name: "张三", age: 18, sex: "男", phone: "13800000001", email: "zhangsan@example.com", address: "上海市普陀区金沙江路 1518 弄", status: 1, score: 95, rank: 1 },
					{ id: 2, name: "李四", age: 20, sex: "女", phone: "13800000002", email: "lisi@example.com", address: "上海市浦东新区张江高科技园区", status: 2, score: 88, rank: 2 },
					{ id: 3, name: "王五", age: 22, sex: "男", phone: "13800000003", email: "wangwu@example.com", address: "北京市海淀区中关村大街 1 号", status: 3, score: 76, rank: 3 },
					{ id: 4, name: "赵六", age: 25, sex: "女", phone: "13800000004", email: "zhaoliu@example.com", address: "广州市天河区天河路 385 号", status: 1, score: 92, rank: 4 },
					{ id: 5, name: "钱七", age: 28, sex: "男", phone: "13800000005", email: "qianqi@example.com", address: "深圳市南山区科技园南区", status: 2, score: 84, rank: 5 }
				],
				columns: [
					{ field: "id", key: "id", title: "ID", width: 80, align: "center" },
					{
						title: "基本信息",
						children: [
							{ field: "name", key: "name", title: "姓名", width: 120, align: "left" },
							{ field: "age", key: "age", title: "年龄", width: 80, align: "center" },
							{ field: "sex", key: "sex", title: "性别", width: 80, align: "center" }
						]
					},
					{
						title: "联系方式",
						children: [
							{ field: "phone", key: "phone", title: "电话号码", width: 150, align: "left" },
							{ field: "email", key: "email", title: "邮箱", width: 200, align: "left" },
							{ field: "address", key: "address", title: "地址", width: 250, align: "left" }
						]
					},
					{
						title: "学习信息",
						children: [
							{
								field: "status",
								key: "status",
								title: "状态",
								width: 120,
								align: "center",
								cellRenderer: (row) => {
									const statusMap = { 1: "<span style='color: green;'>正常</span>", 2: "<span style='color: orange;'>待审核</span>", 3: "<span style='color: red;'>已禁用</span>" };
									return statusMap[row.status] || "未知";
								}
							},
							{
								title: "成绩信息",
								children: [
									{ field: "score", key: "score", title: "分数", width: 100, align: "center" },
									{ field: "rank", key: "rank", title: "排名", width: 80, align: "center" }
								]
							}
						]
					}
				]
			};
		}
	});
}
</script>
<style lang="less">
.card-BiaoTouFenZu {
}
</style>