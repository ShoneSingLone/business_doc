<template>
	<DocContentOfDemo class="x-table-easy-header-group">
		<xMd :md="mdTips" />
		<xTableEasy :columns="columns" :table-data="tableData" border-x border-y />
		<xMd :md="apiString" data-role="api" />
	</DocContentOfDemo>
</template>

<script lang="ts">
export default async function () {
	return {
		data() {
			return {
				mdTips: `
- 1、通过列配置中的 \`children\` 属性可以实现多级表头。
- 2、分组列本身不直接绑定字段，最终渲染的数据列仍然是最末级叶子列。
- 3、建议为每个叶子列设置稳定的 \`key\` 和宽度，避免分组表头布局错乱。
`,
				apiString: `
## API

### 分组表头相关列配置
| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| title | 当前表头标题 | String | - |
| key | 当前列唯一标识 | String | - |
| children | 子列数组，用于声明分组表头 | Array | - |
| width | 叶子列宽度 | Number/String | - |
| align | 表头与单元格对齐方式 | String | left |
`,
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
						age: 27,
						gender: "女",
						phone: "13800000002",
						email: "lisi@example.com",
						score: 91,
						rank: 2
					},
					{
						id: 3,
						name: "王五",
						age: 29,
						gender: "男",
						phone: "13800000003",
						email: "wangwu@example.com",
						score: 86,
						rank: 3
					}
				]
			};
		}
	};
}
</script>

<style lang="less">
.x-table-easy-header-group {
}
</style>
