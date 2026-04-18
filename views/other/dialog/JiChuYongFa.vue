<template>
	<div>
		<div class="mb flex start gap10">
			<xBtn @click="openModal" preset="blue">基础弹窗</xBtn>
			<xBtn @click="openFullscreenModal" preset="green">支持全屏按钮</xBtn>
			<xBtn @click="openMinimizableModal" preset="orange">支持最小化按钮</xBtn>
		</div>
		<div class="mb">
			<xBtn 
				@click="restoreLastMinimized" 
				:disabled="!hasMinimizedModal" 
				preset="blue" 
				size="mini">
				恢复最近最小化的弹窗
			</xBtn>
		</div>
	</div>
</template>

<script lang="ts">
export default async function () {
	return {
		inject: ["APP"],
		data() {
			return {
				modalInstances: []
			};
		},
		computed: {
			hasMinimizedModal() {
				return this.modalInstances.some(vm => vm.dialog_class && vm.dialog_class.minimized);
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
			restoreLastMinimized() {
				const vm = [...this.modalInstances].reverse().find(vm => vm.dialog_class && vm.dialog_class.minimized);
				if (vm) {
					vm.restore();
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
