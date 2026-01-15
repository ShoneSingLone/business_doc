<template>
	<DocContentOfDemo>
		<xMd :md="descString" />
		<!-- 基础用法 -->
		<DemoAndCode title="基础用法" path="@/views/component/data/xTableEasy/JiChuYongFa.vue" />
		<DemoAndCode title="表格宽度" path="@/views/component/data/xTableEasy/BiaoGeKuanDu.vue" />
		<DemoAndCode title="表格高度" path="@/views/component/data/xTableEasy/BiaoGeGaoDu.vue" />
		<DemoAndCode
			title="表格边框"
			path="@/views/component/data/xTableEasy/BiaoGeBianKuang.vue" />

		<!-- 列相关 -->
		<DemoAndCode title="列宽设置" path="@/views/component/data/xTableEasy/LieKuanSheZhi.vue" />
		<DemoAndCode title="列宽拖动" path="@/views/component/data/xTableEasy/LieKuanTuoDong.vue" />
		<DemoAndCode title="列固定" path="@/views/component/data/xTableEasy/LieGuDing.vue" />
		<DemoAndCode title="列隐藏" path="@/views/component/data/xTableEasy/LieYinCang.vue" />

		<!-- 表头相关 -->
		<DemoAndCode title="表头固定" path="@/views/component/data/xTableEasy/BiaoTouGuDing.vue" />
		<DemoAndCode title="表头分组" path="@/views/component/data/xTableEasy/BiaoTouFenZu.vue" />
		<DemoAndCode title="表头隐藏" path="@/views/component/data/xTableEasy/BiaoTouYinCang.vue" />

		<!-- 数据处理 -->
		<DemoAndCode title="筛选" path="@/views/component/data/xTableEasy/ShaiXuan.vue" />
		<DemoAndCode
			title="筛选自定义"
			path="@/views/component/data/xTableEasy/ShaiXuanZiDingYi.vue" />
		<DemoAndCode title="排序" path="@/views/component/data/xTableEasy/PaiXu.vue" />

		<!-- 单元格相关 -->
		<DemoAndCode
			title="单元格对齐"
			path="@/views/component/data/xTableEasy/DanYuanGeDuiQi.vue" />
		<DemoAndCode
			title="单元格样式"
			path="@/views/component/data/xTableEasy/DanYuanGeYangShi.vue" />
		<DemoAndCode
			title="单元格自定义"
			path="@/views/component/data/xTableEasy/ZiDingYiDanYuanGeXuanRan.vue" />
		<DemoAndCode
			title="单元格合并"
			path="@/views/component/data/xTableEasy/DanYuanGeHeBing.vue" />

		<!-- 其他功能 -->
		<DemoAndCode title="操作列" path="@/views/component/data/xTableEasy/CaoZuoLie.vue" />
		<DemoAndCode
			title="单元格选择"
			path="@/views/component/data/xTableEasy/DaiYouXuanZeDeBiaoGe.vue" />
		<DemoAndCode title="虚拟滚动" path="@/views/component/data/xTableEasy/XuNiGunDong.vue" />
		<DemoAndCode
			title="单元格编辑"
			path="@/views/component/data/xTableEasy/DanYuanGeBianJi.vue" />
		<DemoAndCode
			title="行样式定制"
			path="@/views/component/data/xTableEasy/XingYangShiDingZhi.vue" />
		<DemoAndCode
			title="行展开"
			path="@/views/component/data/xTableEasy/examples/HangZhanKai.vue" />
	</DocContentOfDemo>
</template>
<script lang="ts">
export default async function () {
	const totalData = _.map(new Array(4000), (i, ii) => {
		return {
			id: ii,
			name: `name${ii}`,
			age: 18,
			sex: "男",
			phone: "13800000000",
			address: "上海市普陀区金沙江路 1518 弄"
		};
	});
	return {
		provide() {
			return {
				totalData
			};
		},
		data() {
			return {
				descString: `# xTableEasy 表格组件
xTableEasy 是一个基于 Vue 2.7 开发的高性能表格组件，提供了丰富的功能和良好的用户体验。

## 特性
- 支持虚拟滚动，高效渲染大数据
- 支持表头分组和多级表头
- 支持单元格选择和编辑
- 支持行样式定制和斑马纹
- 支持列固定和调整大小
- 支持表头排序和过滤
- 支持上下文菜单
- 支持单元格自动填充
- 支持行展开功能，查看详细信息

## 适用场景
xTableEasy 适用于各种中后台管理系统的表格展示场景，特别是需要处理大量数据的情况。
			`
			};
		}
	};
}
</script>
<style lang="less"></style>
