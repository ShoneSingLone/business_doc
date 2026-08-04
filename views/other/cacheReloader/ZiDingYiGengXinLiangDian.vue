<template>
	<div class="cache-reloader-ZiDingYi">
		<xMd
			md="changelog 支持字符串数组，也支持带 type 的对象数组（type 会影响每一项前面的圆点颜色：success/warning/error/info）。" />
		<div class="mt">
			<xBtn :configs="cpt_btn_show" />
		</div>

		<!-- 【需求】自定义更新亮点：通过 changelog 传入更新日志，type 控制每项颜色 -->
		<xCacheReloader
			v-if="showReloader"
			ref="reloader"
			version="1.5.0"
			title="v1.5.0 更新公告"
			buttonText="立即体验"
			dismissText="稍后再说"
			:changelog="changelog"
			:clearStorageKeys="['_doc_app_theme']"
			@dismiss="onDismiss" />
	</div>
</template>

<script lang="ts">
export default async function () {
	return defineComponent({
		data() {
			return {
				showReloader: false,
				/* 演示用：结构化 changelog */
				changelog: [
					{ text: "新增批量导出功能", type: "success" },
					{ text: "优化了大表格的渲染性能", type: "info" },
					{ text: "已知问题：IE 下仍有部分样式不兼容", type: "warning" }
				]
			};
		},
		computed: {
			cpt_btn_show() {
				return {
					label: "弹出自定义 changelog",
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
			onDismiss() {
				this.showReloader = false;
			}
		}
	});
}
</script>

<style lang="less">
.cache-reloader-ZiDingYi {
	.mt {
		margin-top: 12px;
	}
}
</style>
