<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<xTableEasy :columns="columns" :table-data="tableData" border-x border-y />
		</div>
	</div>
</template>
<script lang="ts">
export default async function () {
	return defineComponent({
		data() {
			return {
				mdDoc: "通过列配置中的 children 属性可以实现多级表头",
				columns: [
					{ field: "id", key: "id", title: "ID", width: 80, align: "center" },
					{
						key: "basicInfo",
						title: "基本信息",
						children: [
							{ field: "name", key: "name", title: "姓名", width: 120 },
							{
								field: "age",
								key: "age",
								title: "年龄",
								width: 100,
								align: "center"
							},
							{
								field: "gender",
								key: "gender",
								title: "性别",
								width: 100,
								align: "center"
							}
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
							{
								field: "score",
								key: "score",
								title: "成绩",
								width: 120,
								align: "center"
							},
							{
								field: "rank",
								key: "rank",
								title: "排名",
								width: 100,
								align: "center"
							}
						]
					}
				],
				tableData: [
					{
						id: 1,
						name: "张三",
						age: 25,
						gender: "男",
						phone: "13800000001",
						email: "zhangsan@example.com",
						score: 95,
						rank: 1
					},
					{
						id: 2,
						name: "李四",
						age: