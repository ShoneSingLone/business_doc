<template>
	<div class="multi-window-manager-demo">
		<div class="mb flex start gap10">
			<xBtn :configs="btnOpenWin1" />
			<xBtn :configs="btnOpenWin2" />
			<xBtn :configs="btnOpenWin3" />
		</div>
		<div class="mb flex start gap10">
			<xBtn :configs="btnToTopWin1" />
			<xBtn :configs="btnToggleWin1" />
			<xBtn :configs="btnCloseWin1" />
		</div>
		<div class="mb flex start gap10">
			<xBtn @click="closeAll" preset="red">关闭所有窗口</xBtn>
		</div>
		<div class="mb flex start gap10 wrap" v-if="minimizedWindows.length > 0">
			<xBtn v-for="win in minimizedWindows" :key="win.id" :configs="getRestoreBtnConfigs(win.id)" />
		</div>
		<div class="mb" v-else>
			<xBtn disabled size="mini">暂无最小化窗口</xBtn>
		</div>
		<div class="tips-box">
			<p>提示：支持快捷键操作（需窗口获得焦点）：</p>
			<ul>
				<li><b>Ctrl + M</b>: 最小化当前置顶窗口</li>
				<li><b>Ctrl + W</b>: 关闭当前置顶窗口</li>
			</ul>
		</div>
	</div>
</template>

<script lang="ts">
export default async function () {
	return {
		data() {
			const vm = this;
			return {
				allWindows: [],
				btnOpenWin1: {
					label: "打开窗口 1",
					preset: "blue",
					onClick: () => vm.openWindow("win1")
				},
				btnOpenWin2: {
					label: "打开窗口 2",
					preset: "green",
					onClick: () => vm.openWindow("win2")
				},
				btnOpenWin3: {
					label: "打开窗口 3",
					preset: "orange",
					onClick: () => vm.openWindow("win3")
				}
			};
		},
		computed: {
			minimizedWindows() {
				return this.allWindows.filter(win => win.minimized);
			},
			isWin1Open() {
				return this.allWindows.some(win => win.id === "win1");
			},
			isWin1Minimized() {
				return this.allWindows.some(win => win.id === "win1" && win.minimized);
			},
			btnToTopWin1() {
				return {
					label: "置顶窗口 1",
					size: "mini",
					disabled: !this.isWin1Open || this.isWin1Minimized,
					onClick: () => this.toTop("win1")
				};
			},
			btnToggleWin1() {
				return {
					label: this.isWin1Minimized ? "还原窗口 1" : "最小化窗口 1",
					size: "mini",
					disabled: !this.isWin1Open,
					onClick: () => this.toggleWindow("win1")
				};
			},
			btnCloseWin1() {
				return {
					label: "关闭窗口 1",
					size: "mini",
					preset: "red",
					disabled: !this.isWin1Open,
					onClick: () => this.close("win1")
				};
			}
		},
		mounted() {
			this.timer = setInterval(() => {
				this.refreshWindowsList();
			}, 500);
		},
		beforeDestroy() {
			clearInterval(this.timer);
		},
		methods: {
			getRestoreBtnConfigs(id) {
				return {
					label: `恢复窗口: ${id}`,
					size: "mini",
					preset: "blue",
					onClick: () => this.restore(id)
				};
			},
			refreshWindowsList() {
				const instances = _.$ModalManager.getAllInstances();
				this.allWindows = instances.map(vm => ({
					id: vm.id,
					minimized: !!(vm.dialog_class && vm.dialog_class.minimized)
				}));
			},
			async openWindow(id) {
				await _.$ModalManager.open({
					id: id,
					title: `窗口 - ${id}`,
					url: "@/views/other/WindowModify.vue",
					payload: {
						id: id
					},
					modalConfigs: {
						keyboard: true
					}
				});
				this.refreshWindowsList();
			},
			toTop(id) {
				_.$ModalManager.toTop(id);
			},
			toggleWindow(id) {
				const win = this.allWindows.find(w => w.id === id);
				if (win) {
					if (win.minimized) {
						_.$ModalManager.restore(id);
					} else {
						_.$ModalManager.minimize(id);
					}
					this.refreshWindowsList();
				}
			},
			minimize(id) {
				_.$ModalManager.minimize(id);
				this.refreshWindowsList();
			},
			restore(id) {
				_.$ModalManager.restore(id);
				this.refreshWindowsList();
			},
			close(id) {
				_.$ModalManager.close(id);
				this.refreshWindowsList();
			},
			closeAll() {
				_.$ModalManager.closeAll();
				this.refreshWindowsList();
			}
		}
	};
}
</script>

<style lang="less">
.multi-window-manager-demo {
	.gap10 {
		gap: 10px;
	}
	.tips-box {
		padding: 10px;
		background: #f8f9fa;
		border-left: 4px solid #007bff;
		margin-top: 10px;
		font-size: 13px;
		ul {
			margin: 5px 0 0 20px;
			padding: 0;
		}
	}
}
</style>
