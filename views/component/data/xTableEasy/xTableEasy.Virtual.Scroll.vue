<template>
	<DocContentOfDemo class="x-table-easy-virtual-scroll">
		<xMd :md="mdTips" />
		<xTableEasy
			:columns="columns"
			:table-data="tableData"
			:max-height="360"
			row-key-field-name="id"
			:virtual-scroll-option="virtualScrollOption"
			border-x
			border-y />
		<xMd :md="apiString" data-role="api" />
	</DocContentOfDemo>
</template>

<script lang="ts">
export default async function () {
	const createTableData = total => {
		const result = [];
		for (let i = 0; i < total; i++) {
			result.push({
				id: i + 1,
				name: `用户${i + 1}`,
				department: `研发${(i % 5) + 1}组`,
				age: 20 + (i % 12),
				score: 60 + (i % 40)
			});
		}
		return result;
	};

	return {
		data() {
			return {
				mdTips: `
- 1、开启虚拟滚动后，组件只渲染当前可视区域附近的数据行。
- 2、虚拟滚动必须配合 \`maxHeight\` 和 \`rowKeyFieldName\` 使用。
- 3、当数据量较大时，这种方式可以显著减少 DOM 数量并提升滚动性能。
`,
				apiString: `
## API

### virtualScrollOption
| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|------|
| enable | 是否开启虚拟滚动 | Boolean | false |
| bufferScale | 预渲染缓冲比例 | Number | 1 |
| minRowHeight | 最小行高，用于估算可视区行数 | Number | 40 |
| scrolling | 滚动过程回调，参数为范围信息对象 | Function | - |
`,
				columns: [
					{ field: "id", key: "id", title: "ID", width: 80, align: "center" },
					{ field: "name", key: "name", title: "姓名", width: 160 },
					{ field: "department", key: "department", title: "部门", width: 180 },
					{ field: "age", key: "age", title: "年龄", width: 100, align: "center" },
					{ field: "score", key: "score", title: "得分", width: 100, align: "center" }
				],
				tableData: createTableData(2000),
				// 先保留最小配置，优先验证当前虚拟滚动主链路
				virtualScrollOption: {
					enable: true,
					bufferScale: 1,
					minRowHeight: 40
				}
			};
		}
	};
}
</script>

<style lang="less">
.x-table-easy-virtual-scroll {
}
</style>
