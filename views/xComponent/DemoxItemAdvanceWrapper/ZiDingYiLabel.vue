<template>
	<div>
		<xMd :md="md" />
		<xForm col="1" style="--xItem-label-position: flex-start; --xItem-wrapper-width: 500px">
			<xItem :configs="form.baseName" />
			<xItemAdvanceWrapper label="自定义标签名">
				<xItem :configs="form.customParam1" />
				<xItem :configs="form.customParam2" />
			</xItemAdvanceWrapper>
			<xItemAdvanceWrapper label="更多选项">
				<xItem :configs="form.customParam3" />
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
					customParam1: {
						value: "",
						label: i18n("自定义参数A"),
						itemType: "xItemInput",
						placeholder: i18n("请输入自定义参数")
					},
					customParam2: {
						value: "",
						label: i18n("自定义参数B"),
						itemType: "xItemInput",
						placeholder: i18n("请输入自定义参数")
					},
					customParam3: {
						value: "",
						label: i18n("额外参数"),
						itemType: "xItemSelect",
						options: [
							{ label: "选项1", value: "1" },
							{ label: "选项2", value: "2" }
						]
					}
				}),
				md: `### 自定义 Label

通过 \`label\` prop 自定义 Switch 旁的标签文本，默认为"高级设置"。

- 支持任意文本，适配不同业务场景
- 同一页面可以放置多个不同 label 的 \`xItemAdvanceWrapper\`
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
