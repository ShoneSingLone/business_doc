<template>
	<div>
		<xMd :md="md" />
		<xForm col="1" style="--xItem-label-position: flex-start; --xItem-wrapper-width: 500px">
			<xItem :configs="form.baseName" />
			<xItemAdvanceWrapper>
				<xItem :configs="form.timeout" />
				<xItem :configs="form.retries" />
				<xItem :configs="form.protocol" />
			</xItemAdvanceWrapper>
		</xForm>
		<div class="mt16">
			<xBtn :configs="btnSubmit" />
		</div>
	</div>
</template>

<script lang="ts">
export default async function () {
	return defineComponent({
		data() {
			return {
				form: defItems({
					baseName: {
						value: "",
						label: i18n("名称"),
						itemType: "xItemInput",
						placeholder: i18n("请输入名称"),
						rules: [_rules.required()]
					},
					timeout: {
						value: "",
						label: i18n("超时时间(秒)"),
						itemType: "xItemInput",
						isNumber: true,
						precision: 0,
						step: 1,
						min: 1,
						max: 3600,
						placeholder: i18n("请输入超时时间")
					},
					retries: {
						value: "",
						label: i18n("重试次数"),
						itemType: "xItemInput",
						isNumber: true,
						precision: 0,
						step: 1,
						min: 0,
						max: 10,
						placeholder: i18n("请输入重试次数")
					},
					protocol: {
						value: "TCP",
						label: i18n("协议类型"),
						itemType: "xItemSelect",
						options: [
							{ label: "TCP", value: "TCP" },
							{ label: "UDP", value: "UDP" },
							{ label: "HTTP", value: "HTTP" }
						]
					}
				}),
				md: `### 基础用法 — Slot 模式

直接使用 \`<xItemAdvanceWrapper>\` 组件，通过 **slot** 传入子控件。

- 点击"高级设置" Switch 展开/收起子配置项
- 自带 xItem 风格的 label 对齐，与外层表单一致
- 未展开时子项不渲染，表单校验不受影响
`
			};
		},
		computed: {
			btnSubmit() {
				const vm = this;
				return {
					label: i18n("提交"),
					preset: "blue",
					async onClick() {
						const values = _.$pickFormValues(vm.form);
						_.$msgSuccess(JSON.stringify(values, null, 2));
					}
				};
			}
		}
	});
}
</script>

<style lang="less"></style>
