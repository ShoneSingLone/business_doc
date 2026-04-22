<template>
	<div>
		<div class="mb flex start gap10">
			<xBtn :configs="btnOpenBase" />
			<xBtn :configs="btnOpenFullscreen" />
			<xBtn :configs="btnToggleMinimizable" />
		</div>
	</div>
</template>

<script lang="ts">
export default async function () {
	return {
		inject: ["APP"],
		data() {
			const vm = this;
			return {
				modalInstances: [],
				btnOpenBase: {
					label: "基础弹窗",
					preset: "blue",
					onClick: vm.openModal
				},
				btnOpenFullscreen: {
					label: "支持全屏按钮",
					preset: "green",
					onClick: vm.openFullscreenModal
				}
			};
		},
		computed: {
			hasMinimizedModal() {
				return this.modalInstances.some(vm => vm.isMinimized);
			},
			btnToggleMinimizable() {
				const vm = this;
				const hasInstance = this.modalInstances.length > 0;
				let label = "打开支持最小化的弹窗";
				let preset = "orange";

				if (hasInstance) {
					label = this.hasMinimizedModal ? "恢复最近最小化的弹窗" : "最小化最近的弹窗";
					preset = "blue";
				}

				return {
					label,
					preset,
					onClick: hasInstance ? vm.toggleLastModal : vm.openMinimizableModal
				};
			}
		},
		methods: {
			async openModal() {
				const vm = await _.$openModal({
					title: "基础弹窗",
					url: "@/views/other/WindowModify.vue",
					payload: {}
				});
				this.registerInstance(vm);
			},
			async openFullscreenModal() {
				const vm = await _.$openModal(
					{
						title: "全屏弹窗示例",
						url: "@/views/other/WindowModify.vue",
						payload: {}
					},
					{
						fullscreen: true
					}
				);
				this.registerInstance(vm);
			},
			async openMinimizableModal() {
				const vm = await _.$openModal(
					{
						title: "最小化弹窗示例",
						url: "@/views/other/WindowModify.vue",
						payload: {}
					},
					{
						minimizable: true
					}
				);
				this.registerInstance(vm);
			},
			registerInstance(vm) {
				this.modalInstances.push(vm);
				vm.$on("hook:beforeDestroy", () => {
					this.modalInstances = this.modalInstances.filter(i => i !== vm);
				});
			},
			toggleLastModal() {
				const minimizedVm = [...this.modalInstances]
					.reverse()
					.find(vm => vm.isMinimized);
				if (minimizedVm) {
					minimizedVm.restore();
				} else {
					const lastVm = _.last(this.modalInstances);
					if (lastVm) {
						lastVm.minimize();
					}
				}
			}
		}
	};
}
</script>

<style lang="less">
.gap10 {
	gap: 10px;
}
</style>
