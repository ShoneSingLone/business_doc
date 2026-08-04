<template>
	<div class="cache-reloader-ZhiLing">
		<xMd
			md="无需在 template 中声明，直接调用全局工具函数 `_.$cacheReloader(options)` 即可弹出浮窗。适合在检测到新版本的入口逻辑（如 seed.js、App.vue mounted）中调用。" />
		<div class="mt">
			<xBtn :configs="cpt_btn_call" />
			<xBtn :configs="cpt_btn_call_countdown" />
		</div>
	</div>
</template>

<script lang="ts">
export default async function () {
	return defineComponent({
		computed: {
			/* 【需求】指令式调用：直接弹窗，不占 template 位置；演示用 onBeforeReload 拦截 reload */
			cpt_btn_call() {
				return {
					label: "_.$cacheReloader({...})",
					preset: "blue",
					onClick: () => {
						_.$cacheReloader({
							version: "1.0.0",
							title: "指令式调用",
							changelog: ["通过 _.$cacheReloader 弹出"],
							buttonText: "立即体验",
							onBeforeReload: () => {
								_.$notify({
									title: "演示拦截",
									message: "已拦截 reload"
								});
								return false;
							}
						});
					}
				};
			},
			cpt_btn_call_countdown() {
				return {
					label: "带倒计时的指令式调用",
					preset: "plain",
					onClick: () => {
						_.$cacheReloader({
							version: "1.0.0",
							title: "5 秒后自动更新",
							countdown: 5,
							changelog: ["倒计时结束自动 reload"],
							buttonText: "立即更新",
							onBeforeReload: () => {
								_.$notify({
									title: "演示拦截",
									message: "已拦截 reload"
								});
								return false;
							}
						});
					}
				};
			}
		}
	});
}
</script>

<style lang="less">
.cache-reloader-ZhiLing {
	.mt {
		margin-top: 12px;
	}
}
</style>
