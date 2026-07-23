<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<xTableEasy
				style="width: 600px"
				:scroll-width="1200"
				:columns="columns"
				:table-data="tableData"
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
				mdDoc: "表头分组结合固定列：通过 `fixed: \"left\"` 或 `fixed: \"right\"` 设置固定列，同时使用 `children` 实现分组表头",
				columns: [
					{
						key: "fixedInfo",
						title: "固定信息",
						fixed: "left",
						children: [
							{ field: "id", key: "id", title: "ID", width: 80, align: "center", fixed: "left" },
							{ field: "name", key: "name", title: "姓名", width: 120, fixed: "left" }
						]
					},
					{
						key: "basicInfo",
						title: "基本信息",
						children: [
							{ field: "age", key: "age", title: "年龄", width: 100, align: "center" },
							{ field: "gender", key: "gender", title: "性别", width: 100, align: "center" }
						]
					},
					{
						key: "contactInfo",
						title: "联系方式",
						children: [
							{ field: "phone", key: "phone", title: "手机号", width: 160 },
							{ field: "email", key: "email", title: "邮箱", width: 220 }
						]
					},
					{
						key: "scoreInfo",
						title: "成绩信息",
						children: [
							{ field: "score", key: "score", title: "成绩", width: 120, align: "center" },
							{ field: "rank", key: "rank", title: "排名", width: 100, align: "center" }
						]
					},
					{
						key: "fixedAction",
						title: "操作",
						fixed: "right",
						children: [
							{ field: "action", key: "action", title: "操作", width: 100, align: "center", fixed: "right" }
						]
					}
				],
				tableData: [
					{ id: 1, name: "张三", age: 25, gender: "男", phone: "13800000001", email: "zhangsan@example.com", score: 95, rank: 1, action: "编辑" },
					{ id: 2, name: "李四", age: 27, gender: "女", phone: "13800000002", email: "lisi@example.com", score: 91, rank: 2, action: "编辑" },
					{ id: 3, name: "王五", age: 29, gender: "男", phone: "13800000003", email: "wangwu@example.com", score: 86, rank: 3, action: "编辑" },
					{ id: 4, name: "赵六", age: 31, gender: "女", phone: "13800000004", email: "zhaoliu@example.com", score: 82, rank: 4, action: "编辑" },
					{ id: 5, name: "钱七", age: 28, gender: "男", phone: "13800000005", email: "qianqi@example.com", score: 88, rank: 5, action: "编辑" }
				]
			};
		}
	});
}
</script>
