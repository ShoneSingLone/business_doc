<template>
	<div class="advance-configs-demo">
		<div class="mb flex start gap10">
			<xBtn :configs="btnNoCenter" />
			<xBtn :configs="btnResponsive" />
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
				btnNoCenter: {
					label: "禁用自动居中 (跟随级联)",
					preset: "blue",
					onClick: vm.openNoCenter
				},
				btnResponsive: {
					label: "开启响应式全屏",
					preset: "green",
					onClick: vm.openResponsive
				},
				tipsMd: `
### 说明：
- **禁用自动居中**：设置 \`center: false\`。此时窗口将不会强制在视口中心弹出，而是保持初始定义的坐标（或遵循级联策略）。
- **响应式全屏**：设置 \`responsiveMaximize: true\`（默认阈值 768px）或指定数值。当浏览器宽度缩小至阈值以下时，窗口会自动切换为全屏。
`
			};
		},
		methods: {
			async openNoCenter() {
				// 模拟 ModalManager 的级联效果，手动给一个偏移
				const count = _.$ModalManager.getAllInstances().length;
				await _.$openModal({
					title: "非居中弹窗",
					url: "@/views/other/WindowModify.vue",
					style: {
						left: 50 + count * 20,
						top: 50 + count * 20
					}
				}, {
					center: false
				});
			},
			async openResponsive() {
				await _.$openModal({
					title: "响应式全屏弹窗",
					url: "@/views/other/WindowModify.vue",
				}, {
					responsiveMaximize: 600 // 演示用，设为 600px
				});
				_.$msg("请尝试缩小浏览器窗口至 600px 以下观察效果");
			}
		}
	};
}
</script>

<style lang="less">
.advance-configs-demo {
	.gap10 {
		gap: 10px;
	}
}
</style>
