<template>
	<div class="mask-usage-demo">
		<div class="mb flex start gap10">
			<xBtn :configs="btnDefaultMask" />
			<xBtn :configs="btnClickableMask" />
			<xBtn :configs="btnNoMask" />
		</div>
		<xMd :md="tipsMd" />
	</div>
</template>

<script lang="ts">
export default async function () {
	return {
		data() {
			const vm = this;
			return {
				btnDefaultMask: {
					label: "默认遮罩 (不可点击关闭)",
					preset: "blue",
					onClick: vm.openDefaultMask
				},
				btnClickableMask: {
					label: "遮罩可点击关闭",
					preset: "green",
					onClick: vm.openClickableMask
				},
				btnNoMask: {
					label: "无遮罩 (可操作背景)",
					preset: "orange",
					onClick: vm.openNoMask
				},
				tipsMd: `
### 说明：
- **默认遮罩**：\`mask: true\`, \`closeOnClickMask: false\` (默认行为)。
- **可点击关闭**：显式设置 \`closeOnClickMask: true\`。
- **无遮罩**：\`mask: false\`，此时弹窗容器不会拦截鼠标事件，可以直接点击下方的按钮。
`
			};
		},
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
}
</style>
