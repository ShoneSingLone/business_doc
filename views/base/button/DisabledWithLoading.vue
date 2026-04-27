<template>
	<div class="card-DisabledWithLoading">
		<xMd :md="mdTitle" />
		<div class="demo-container">
			<xMd :md="md1" />
			<xBtn 
				preset="primary" 
				:loading="true"
				:configs="{ disabled: '按钮处于禁用状态，无法点击' }"
			>
				禁用且加载中
			</xBtn>
			<p class="tip">提示：将鼠标悬停在这个按钮上，应该显示"按钮处于禁用状态，无法点击"的提示信息</p>
		</div>
		<div class="demo-container">
			<xMd :md="md2" />
			<xBtn 
				preset="danger"
				:loading="true"
				:configs="{ disabled: '权限不足，无法执行此操作' }"
			>
				删除
			</xBtn>
			<p class="tip">提示：将鼠标悬停在这个按钮上，应该显示"权限不足，无法执行此操作"的提示信息</p>
		</div>
	</div>
</template>
<script lang="ts">
export default async function () {
	return defineComponent({
		data() {
			return {
				mdTitle: "当按钮同时处于 disabled（string 类型）和 loading 状态时，鼠标 hover 应显示禁用提示信息。",
				md1: `#### 基础示例
disabled 为 string 类型，同时 loading 为 true，hover 显示提示信息`,
				md2: `#### 权限提示
显示权限相关的禁用提示`
			};
		}
	});
}
</script>
<style lang="less">
.card-DisabledWithLoading {
	.demo-container {
		margin-bottom: 24px;
		padding: 16px;
		border: 1px solid #ebeef5;
		border-radius: 4px;
		
		+ .demo-container {
			margin-top: 16px;
		}
		
		.tip {
			margin-top: 12px;
			color: #909399;
			font-size: 12px;
			line-height: 1.5;
		}
	}
}
</style>
