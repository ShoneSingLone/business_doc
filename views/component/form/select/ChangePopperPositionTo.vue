<template>
	<div class="test-must-set-popper-append-to-body">
		<h2>changePopperPositionTo 测试页面</h2>

		<div class="test-controls">
			<xBtn @click="testAppendToBody">测试：移动到 body (appendToBody)</xBtn>
			<xBtn @click="testAppendToSelf">测试：移回组件内 (非 appendToBody)</xBtn>
			<xBtn @click="checkStatus">检查当前状态</xBtn>
		</div>

		<div class="test-result">
			<h3>测试结果：</h3>
			<xMd :md="testResult" />
		</div>

		<div class="test-select">
			<h3>测试用 Select 组件：</h3>
			<xSelect ref="testSelect" v-model="selectValue" placeholder="请选择" :filterable="true">
				<xOption
					v-for="item in options"
					:key="item.value"
					:label="item.label"
					:value="item.value" />
			</xSelect>
		</div>

		<div class="test-info">
			<h3>状态说明：</h3>
			<ul>
				<li>appendToBody 模式：select 根元素有 <code>is-append-to-body</code> 类</li>
				<li>非 appendToBody 模式：select 根元素有 <code>is-append-to-self</code> 类</li>
			</ul>
		</div>
	</div>
</template>

<script lang="ts">
export default async function () {
	return {
		mounted() {
			(async () => {
				await _.$ensure(() => this.$refs.testSelect?.$el);
				this.testResult = `\`\`\` ${this.$refs.testSelect.$el.outerHTML} \`\`\``;
			})();
		},
		data() {
			return {
				testResult: "",
				selectValue: "",
				options: [
					{ value: 1, label: "选项 1" },
					{ value: 2, label: "选项 2" },
					{ value: 3, label: "选项 3" },
					{ value: 4, label: "选项 4" },
					{ value: 5, label: "选项 5" }
				]
			};
		},
		methods: {
			testAppendToBody() {
				const selectVm = this.$refs.testSelect;
				if (!selectVm) {
					this.testResult = "错误：无法获取 select 组件实例";
					return;
				}

				selectVm.changePopperPositionTo("body");

				this.testResult = `\`\`\` ${this.$refs.testSelect.$el.outerHTML} \`\`\``;
			},

			testAppendToSelf() {
				const selectVm = this.$refs.testSelect;
				if (!selectVm) {
					this.testResult = "错误：无法获取 select 组件实例";
					return;
				}

				selectVm.changePopperPositionTo("other");
				this.testResult = `\`\`\` ${this.$refs.testSelect.$el.outerHTML} \`\`\``;
			},

			checkStatus() {
				const selectVm = this.$refs.testSelect;
				if (!selectVm) {
					this.testResult = "错误：无法获取 select 组件实例";
					return;
				}

				const selectEl = selectVm.$el;
				const hasAppendToBodyClass = $(selectEl).hasClass("is-append-to-body");
				const hasAppendToSelfClass = $(selectEl).hasClass("is-append-to-self");
				const popper = selectVm.$refs.popper;
				const popperElm = popper ? popper.popperElm || popper.$el : null;
				const isInBody = popperElm ? popperElm.parentNode === document.body : "未知";

				this.testResult = `\`\`\` ${this.$refs.testSelect.$el.outerHTML} \`\`\``;
			}
		}
	};
}
</script>

<style lang="less">
.test-must-set-popper-append-to-body {
	padding: 20px;

	.test-controls {
		margin-bottom: 20px;

		.xBtn {
			margin-right: 10px;
		}
	}

	.test-result {
		margin-bottom: 20px;
		padding: 15px;
		background-color: #f5f7fa;
		border-radius: 4px;

		pre {
			white-space: pre-wrap;
			word-wrap: break-word;
			font-family: "Courier New", monospace;
			font-size: 13px;
			line-height: 1.5;
		}
	}

	.test-select {
		margin-bottom: 20px;
		max-width: 300px;
	}

	.test-info {
		ul {
			list-style: disc;
			margin-left: 20px;

			li {
				margin-bottom: 8px;

				code {
					background-color: #f0f0f0;
					padding: 2px 6px;
					border-radius: 3px;
					font-family: "Courier New", monospace;
				}
			}
		}
	}
}
</style>
