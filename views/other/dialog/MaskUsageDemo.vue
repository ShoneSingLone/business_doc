<template>
	<div class="mask-usage-demo">
		<div class="mb flex start gap10">
			<xBtn @click="openDefaultMask" preset="blue">默认遮罩 (不可点击关闭)</xBtn>
			<xBtn @click="openClickableMask" preset="green">遮罩可点击关闭</xBtn>
			<xBtn @click="openNoMask" preset="orange">无遮罩 (可操作背景)</xBtn>
		</div>
		<div class="tips-box">
			<p>说明：</p>
			<ul>
				<li><b>默认遮罩</b>：`mask: true`, `closeOnClickMask: false` (默认行为)。</li>
				<li><b>可点击关闭</b>：显式设置 `closeOnClickMask: true`。</li>
				<li><b>无遮罩</b>：`mask: false`，此时弹窗容器不会拦截鼠标事件，可以直接点击下方的按钮。</li>
			</ul>
		</div>
	</div>
</template>

<script lang="ts">
export default async function () {
	return {
		methods: {
			async openDefaultMask() {
				await _.$openModal({
					title: "默认遮罩弹窗",
					url: "@/views/other/WindowModify.vue",
					mask: true // 默认即为 true
				});
			},
			async openClickableMask() {
				await _.$openModal({
					title: "点击遮罩可关闭",
					url: "@/views/other/WindowModify.vue",
					mask: true,
					closeOnClickMask: true
				});
			},
			async openNoMask() {
				await _.$openModal({
					title: "无遮罩弹窗",
					url: "@/views/other/WindowModify.vue",
					mask: false
				});
			}
		}
	};
}
</script>

<style lang="less">
.mask-usage-demo {
	.gap10 {
		gap: 10px;
	}
	.tips-box {
		padding: 10px;
		background: #f0f9eb;
		border-left: 4px solid #67c23a;
		margin-top: 10px;
		font-size: 13px;
		color: #606266;
		ul {
			margin: 5px 0 0 20px;
			padding: 0;
		}
	}
}
</style>
