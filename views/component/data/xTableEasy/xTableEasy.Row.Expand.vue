<template>
	<DocContentOfDemo class="x-table-easy-row-expand">
		<xMd :md="mdTips" />
		<xTableEasy
			:columns="columns"
			:table-data="tableData"
			row-key-field-name="id"
			:expand-option="expandOption"
			border-x
			border-y />
		<xMd :md="apiString" data-role="api" />
	</DocContentOfDemo>
</template>

<script lang="ts">
export default async function () {
	return {
		data() {
			return {
				mdTips: `
- 1、通过增加 \`type: "expand"\` 的列，可以为表格启用行展开入口。
- 2、通过 \`expandOption.render\` 返回展开区域内容，支持使用 \`h\` 函数生成任意节点。
- 3、当前示例使用默认的图标触发展开，适合先验证主链路是否可用。
`,
				apiString: `
## API

### expandOption
| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| render | 展开区域渲染函数，参数为当前行上下文 | Function({ row, column, rowIndex }, h) | - |
| trigger | 触发展开的方式，可选 icon / cell / row | String | icon |
| defaultExpandAllRows | 是否默认展开全部行 | Boolean | false |
| defaultExpandedRowKeys | 默认展开的行 key 列表 | Array | [] |
`,
				columns: [
					{ field: "expand", key: "expand", title: "", width: 60, type: "expand" },
					{ field: "name", key: "name", title: "姓名", width: 140 },
					{ field: "role", key: "role", title: "岗位", width: 180 },
					{ field: "city", key: "city", title: "城市", width: 140 },
					{ field: "score", key: "score", title: "评分", width: 100, align: "center" }
				],
				tableData: [
					{
						id: 1,
						name: "张三",
						role: "前端开发",
						city: "上海",
						score: 95,
						description: "负责控制台核心页面开发与组件封装。"
					},
					{
						id: 2,
						name: "李四",
						role: "测试工程师",
						city: "北京",
						score: 89,
						description: "负责自动化测试与质量保障流程建设。"
					},
					{
						id: 3,
						name: "王五",
						role: "产品经理",
						city: "深圳",
						score: 92,
						description: "负责需求设计、版本推进和跨团队协调。"
					}
				],
				// 用最小配置先验证行展开能力，后续再继续补更多触发方式与受控场景
				expandOption: {
					render: ({ row }, h) => {
						return h("div", { class: "expand-panel" }, [
							h("div", { class: "expand-panel__title" }, `成员：${row.name}`),
							h("div", `岗位：${row.role}`),
							h("div", `城市：${row.city}`),
							h("div", `说明：${row.description}`)
						]);
					}
				}
			};
		}
	};
}
</script>

<style lang="less">
.x-table-easy-row-expand {
	.expand-panel {
		padding: 12px 16px;
		line-height: 1.8;
		background-color: #fafafa;
	}

	.expand-panel__title {
		font-weight: 600;
		color: #303133;
	}
}
</style>
