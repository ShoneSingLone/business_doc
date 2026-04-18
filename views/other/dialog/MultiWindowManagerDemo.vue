<template>
	<div class="multi-window-manager-demo">
		<div class="mb flex start gap10">
			<xBtn @click="openWindow('win1')" preset="blue">打开窗口 1</xBtn>
			<xBtn @click="openWindow('win2')" preset="green">打开窗口 2</xBtn>
			<xBtn @click="openWindow('win3')" preset="orange">打开窗口 3</xBtn>
		</div>
		<div class="mb flex start gap10">
			<xBtn @click="toTop('win1')" :disabled="!isWin1Open || isWin1Minimized" size="mini">置顶窗口 1</xBtn>
			<xBtn @click="minimize('win1')" :disabled="!isWin1Open || isWin1Minimized" size="mini">最小化窗口 1</xBtn>
			<xBtn @click="restore('win1')" :disabled="!isWin1Open || !isWin1Minimized" size="mini">还原窗口 1</xBtn>
			<xBtn @click="close('win1')" :disabled="!isWin1Open" size="mini" preset="red">关闭窗口 1</xBtn>
		</div>
		<div class="mb flex start gap10">
			<xBtn @click="closeAll" preset="red">关闭所有窗口</xBtn>
		</div>
		<div class="mb flex start gap10 wrap" v-if="minimizedWindows.length > 0">
			<xBtn 
				v-for="win in minimizedWindows" 
				:key="win.id" 
				@click="restore(win.id)" 
				size="mini" 
				preset="blue">
				恢复窗口: {{win.id}}
			</xBtn>
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
			return {
				allWindows: []
			};
		},
		computed: {
			minimizedWindows() {
				return this.allWindows.filter(win => win.minimized);
			},
			isWin1Open() {
				return this.allWindows.some(win => win.id === 'win1');
			},
			isWin1Minimized() {
				return this.allWindows.some(win => win.id === 'win1' && win.minimized);
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
			refreshWindowsList() {
				const instances = _.$windowsManager.getAllInstances();
				this.allWindows = instances.map(vm => ({
					id: vm.id,
					minimized: !!(vm.dialog_class && vm.dialog_class.minimized)
				}));
			},
			async openWindow(id) {
				await _.$windowsManager.open({
					id: id,
					title: `窗口 - ${id}`,
					url: "@/views/other/WindowModify.vue",
					payload: {
						id: id
					}
				});
				this.refreshWindowsList();
			},
			toTop(id) {
				_.$windowsManager.toTop(id);
			},
			minimize(id) {
				_.$windowsManager.minimize(id);
				this.refreshWindowsList();
			},
			restore(id) {
				_.$windowsManager.restore(id);
				this.refreshWindowsList();
			},
			close(id) {
				_.$windowsManager.close(id);
				this.refreshWindowsList();
			},
			closeAll() {
				_.$windowsManager.closeAll();
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
