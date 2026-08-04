<template>
	<div class="cache-reloader-JiChuYongFa">
		<xMd
			md='点击按钮模拟检测到新版本，右下角将弹出更新浮窗。点击"立即体验"会清空 IndexedDB 缓存并重新加载页面。' />
		<div class="mt">
			<xBtn :configs="cpt_btn_show" />
			<xBtn :configs="cpt_btn_toggle_version" />
		</div>

		<!-- 【需求】基础用法：右下角浮窗提示用户清除缓存并重新加载 -->
		<xCacheReloader
			v-if="showReloader"
			ref="reloader"
			:version="cpt_mock_version"
			title="发现新版本"
			buttonText="立即体验"
			:changelog="['优化了首屏加载速度', '修复了部分浏览器下表格错位的问题']"
			@dismiss="onDismiss" />
	</div>
</template>

<script lang="ts">
export default async function () {
	return defineComponent({
		data() {
			return {
				showReloader: false,
				mockVersion: ""
			};
		},
		computed: {
			/* 模拟一个与当前 APP_VERSION 不同的版本号 */
			cpt_mock_version() {
				return this.mockVersion || "2.0." + (Date.now() % 100);
			},
			cpt_btn_show() {
				return {
					label: "模拟发现新版本",
					preset: "blue",
					onClick: () => {
						this.showReloader = true;
						this.$nextTick(() => {
							this.$refs.reloader && this.$refs.reloader.show();
						});
					}
				};
			},
			cpt_btn_toggle_version() {
				return {
					label: "切换模拟版本（当前：" + this.cpt_mock_version + "）",
					preset: "plain",
					onClick: () => {
						this.mockVersion = "2.0." + Math.floor(Math.random() * 1000);
					}
				};
			}
		},
		methods: {
			onDismiss() {
				/* 演示用：用户点击"稍后"时仅移除组件 */
				this.showReloader = false;
			}
		}
	});
}
</script>

<style lang="less">
.cache-reloader-JiChuYongFa {
	.mt {
		margin-top: 12px;
	}
}
</style>
