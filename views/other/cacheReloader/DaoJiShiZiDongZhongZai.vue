<template>
	<div class="cache-reloader-DaoJiShi">
		<xMd
			md="设置 countdown 后，浮窗右下角会显示倒计时，到 0 自动触发清缓存+重载。本演示为避免实际刷新页面，使用 onBeforeReload 钩子拦截重载，仅打印日志。" />
		<div class="mt">
			<xBtn :configs="cpt_btn_show" />
		</div>

		<!-- 【需求】倒计时自动重载：countdown > 0 时自动倒计时，到 0 触发 reload -->
		<xCacheReloader
			v-if="showReloader"
			ref="reloader"
			version="3.0.0"
			title="紧急安全更新"
			buttonText="立即更新"
			:countdown="10"
			:changelog="['修复安全漏洞 CVE-XXXX-XXXX', '建议立即更新']"
			:onBeforeReload="onBeforeReload"
			@reload="onReload"
			@dismiss="onDismiss" />
	</div>
</template>

<script lang="ts">
export default async function () {
	return defineComponent({
		data() {
			return {
				showReloader: false
			};
		},
		computed: {
			cpt_btn_show() {
				return {
					label: "弹出 10 秒倒计时浮窗",
					preset: "blue",
					onClick: () => {
						this.showReloader = true;
						this.$nextTick(() => {
							this.$refs.reloader && this.$refs.reloader.show();
						});
					}
				};
			}
		},
		methods: {
			/* 【需求】演示用：拦截真实重载，仅打印日志，避免刷新演示页 */
			onBeforeReload() {
				console.log("[xCacheReloader 演示] onBeforeReload：已拦截实际 location.reload");
				_.$notify({
					title: "演示拦截",
					message: "已拦截 location.reload，实际使用时请移除 onBeforeReload"
				});
				this.showReloader = false;
				return false;
			},
			onReload() {
				console.log("[xCacheReloader 演示] onReload 触发");
			},
			onDismiss() {
				this.showReloader = false;
			}
		}
	});
}
</script>

<style lang="less">
.cache-reloader-DaoJiShi {
	.mt {
		margin-top: 12px;
	}
}
</style>
