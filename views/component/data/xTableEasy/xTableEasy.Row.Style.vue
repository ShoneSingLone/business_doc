<template>
	<DocContentOfDemo class="x-table-easy-row-style">
		<xMd :md="mdTips" />
		<div class="demo-controls">
			<xSwitch v-model="enableStripe" active-text="斑马纹" />
			<xSwitch v-model="enableHoverHighlight" active-text="悬停高亮" />
			<xSwitch v-model="enableClickHighlight" active-text="点击高亮" />
		</div>
		<xTableEasy
			:columns="columns"
			:table-data="tableData"
			row-key-field-name="id"
			:row-style-option="cpt_row_style_option"
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
- 1、当前版本已经支持 \`stripe\`、\`hoverHighlight\`、\`clickHighlight\` 三类基础行样式能力。
- 2、这些能力通过 \`rowStyleOption\` 统一控制，适合表格基础视觉增强场景。
- 3、如果后续继续移植更复杂的行样式能力，再补充更细粒度的示例。
`,
				apiString: `
## API

### rowStyleOption
| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| stripe | 是否启用斑马纹 | Boolean | false |
| hoverHighlight | 是否启用悬停高亮 | Boolean | true |
| clickHighlight | 是否启用点击高亮 | Boolean | true |
`,
				enableStripe: true,
				enableHoverHighlight: true,
				enableClickHighlight: true,
				columns: [
					{ field: "id", key: "id", title: "ID", width: 80, align: "center" },
					{ field: "name", key: "name", title: "姓名", width: 140 },
					{ field: "role", key: "role", title: "角色", width: 160 },
					{ field: "department", key: "department", title: "部门", width: 180 },
					{ field: "score", key: "score", title: "评分", width: 100, align: "center" }
				],
				tableData: [
					{ id: 1, name: "张三", role: "前端开发", department: "研发一组", score: 95 },
					{ id: 2, name: "李四", role: "测试工程师", department: "质量保障", score: 88 },
					{ id: 3, name: "王五", role: "产品经理", department: "产品中心", score: 91 },
					{ id: 4, name: "赵六", role: "后端开发", department: "研发二组", score: 84 }
				]
			};
		},
		computed: {
			cpt_row_style_option() {
				return {
					stripe: this.enableStripe,
					hoverHighlight: this.enableHoverHighlight,
					clickHighlight: this.enableClickHighlight
				};
			}
		}
	};
}
</script>

<style lang="less">
.x-table-easy-row-style {
	.demo-controls {
		display: flex;
		gap: 16px;
		margin-bottom: 16px;
		padding: 12px;
		background-color: #f5f7fa;
		border-radius: 4px;
	}
}
</style>
