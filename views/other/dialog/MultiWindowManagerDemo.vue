<template>
	<div class="multi-window-manager-demo">
		<div class="mb flex start gap10">
			<xBtn @click="openWindow('win1')" preset="blue">打开窗口 1</xBtn>
			<xBtn @click="openWindow('win2')" preset="green">打开窗口 2</xBtn>
			<xBtn @click="openWindow('win3')" preset="orange">打开窗口 3</xBtn>
		</div>
		<div class="mb flex start gap10">
			<xBtn @click="toTop('win1')" size="mini">置顶窗口 1</xBtn>
			<xBtn @click="minimize('win1')" size="mini">最小化窗口 1</xBtn>
			<xBtn @click="restore('win1')" size="mini">还原窗口 1</xBtn>
			<xBtn @click="close('win1')" size="mini" preset="red">关闭窗口 1</xBtn>
		</div>
		<div class="mb flex start gap10">
			<xBtn @click="closeAll" preset="red">关闭所有窗口</xBtn>
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
		methods: {
			async openWindow(id) {
				await _.$windowsManager.open({
					id: id,
					title: `窗口 - ${id}`,
					url: "@/views/other/WindowModify.vue",
					payload: {
						id: id
					}
				});
			},
			toTop(id) {
				_.$windowsManager.toTop(id);
			},
			minimize(id) {
				_.$windowsManager.minimize(id);
			},
			restore(id) {
				_.$windowsManager.restore(id);
			},
			close(id) {
				_.$windowsManager.close(id);
			},
			closeAll() {
				_.$windowsManager.closeAll();
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
