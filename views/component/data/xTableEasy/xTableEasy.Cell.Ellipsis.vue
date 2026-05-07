<template>
	<DocContentOfDemo class="x-table-easy-cell-ellipsis">
		<xMd :md="mdTips" />
		<div class="demo-controls">
			<xSwitch v-model="enableEllipsis" active-text="启用省略" />
			<xSwitch v-model="enableMultiline" active-text="多行省略" />
		</div>
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
- 1、通过配置列的 \`ellipsis\` 属性实现单元格内容省略
- 2、单行省略会在内容超出时显示省略号
- 3、多行省略可通过设置 \`lineClamp\` 属性实现
`,
				apiString: `
## API

### 列配置中的省略相关属性

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| ellipsis | 是否启用省略 | Boolean | false |
| lineClamp | 多行省略时显示的行数 | Number | 1 |
| tooltip | 鼠标悬停时是否显示完整内容 | Boolean | true |
`,
				enableEllipsis: true,
				enableMultiline: false,
				columns: [
					{ field: "id", key: "id", title: "ID", width: 80, align: "center" },
					{ 
						field: "name", 
						key: "name", 
						title: "姓名", 
						width: 120,
						ellipsis: true 
					},
					{ 
						field: "description", 
						key: "description", 
						title: "描述", 
						width: 200,
						ellipsis: true,
						lineClamp: 2 
					},
					{ field: "status", key: "status", title: "状态", width: 100, align: "center" }
				],
				tableData: [
					{ 
						id: 1, 
						name: "张三", 
						description: "这是一段非常长的描述文本，用于测试单元格内容省略功能，当内容超出列宽时会自动显示省略号", 
						status: "正常" 
					},
					{ 
						id: 2, 
						name: "李四", 
						description: "这是一段较长的描述文本用于测试省略功能", 
						status: "正常" 
					},
					{ 
						id: 3, 
						name: "王五", 
						description: "短描述", 
						status: "正常" 
					}
				]
			};
		},
		computed: {
			computedColumns() {
				return this.columns.map(col => ({
					...col,
					ellipsis: this.enableEllipsis && col.ellipsis,
					lineClamp: this.enableMultiline ? (col.lineClamp || 2) : 1
				}));
			}
		}
	};
}
</script>

<style lang="less">
.x-table-easy-cell-ellipsis {
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