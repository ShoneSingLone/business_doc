<template>
	<div class="doc-demo-testcomponent">
		<h1>TestComponent 组件</h1>
		<div class="doc-content">
			<h2>目录</h2>
			<ul class="doc-menu">
				<li><a href="#basic-usage">基础用法</a></li>
				<li><a href="#attributes">属性</a></li>
				<li><a href="#events">事件</a></li>
			</ul>

			<h2 id="basic-usage">基础用法</h2>
			<p>以下是 TestComponent 组件的基础使用方法：</p>
			<xPageContent>
				<JiChuYongFa />
			</xPageContent>

			<h2 id="attributes">属性</h2>
			<table class="doc-table">
				<thead>
					<tr>
						<th>属性名</th>
						<th>类型</th>
						<th>默认值</th>
						<th>说明</th>
					</tr>
				</thead>
				<tbody>
					<!-- 这里将自动生成属性说明 -->
				</tbody>
			</table>

			<h2 id="events">事件</h2>
			<table class="doc-table">
				<thead>
					<tr>
						<th>事件名</th>
						<th>参数</th>
						<th>说明</th>
					</tr>
				</thead>
				<tbody>
					<!-- 这里将自动生成事件说明 -->
				</tbody>
			</table>
		</div>
	</div>
</template>

<script lang="ts">
export default async function () {
	return {
		components: {
			JiChuYongFa: () => _.$importVue("@/views/component/base/TestComponent/JiChuYongFa.vue")
		}
	};
}
</script>

<style lang="less">
.doc-demo-testcomponent {
	padding: 20px;

	h1 {
		font-size: 24px;
		margin-bottom: 20px;
		color: #333;
	}

	h2 {
		font-size: 20px;
		margin-top: 30px;
		margin-bottom: 15px;
		color: #666;
	}

	.doc-menu {
		list-style: none;
		padding: 0;
		margin-bottom: 30px;

		li {
			margin: 10px 0;

			a {
				color: #409eff;
				text-decoration: none;

				&:hover {
					text-decoration: underline;
				}
			}
		}
	}

	.doc-table {
		width: 100%;
		border-collapse: collapse;
		margin: 20px 0;

		th,
		td {
			border: 1px solid #eaeaea;
			padding: 10px;
			text-align: left;
		}

		th {
			background-color: #f5f7fa;
			font-weight: bold;
		}
	}
}
</style>
