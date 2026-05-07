<template>
	<DocContentOfDemo class="x-table-easy-loading">
		<xMd :md="mdTips" />
		<div class="demo-controls">
			<xBtn @click="startLoading">开始加载</xBtn>
			<xBtn @click="stopLoading">停止加载</xBtn>
		</div>
		<xTableEasy 
			:columns="columns" 
			:table-data="tableData" 
			:loading="isLoading"
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
- 1、表格支持加载状态显示
- 2、可自定义加载提示内容
- 3、常用于异步数据加载场景
`,
				apiString: `
## API

### 加载状态配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| loading | 是否显示加载状态 | Boolean | false |
| loadingText | 加载提示文本 | String | '加载中...' |
| loadingSlot | 自定义加载内容 | Slot | - |
`,
				isLoading: false,
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
			startLoading() {
				this.isLoading = true;
			},
			stopLoading() {
				this.isLoading = false;
			}
		}
	};
}
</script>

<style lang="less">
.x-table-easy-loading {
	.demo-controls {
		display: flex;
		gap: 12px;
		margin-bottom: 16px;
	}
}
</style>