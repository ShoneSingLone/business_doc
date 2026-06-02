<template>
	<div>
		<xMd :md="md" />
		<xForm col="1" style="--xItem-label-position: flex-start; --xItem-wrapper-width: 500px">
			<xItem :configs="form.advanceConfig" />
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
			const vm = this;
			return {
				form: defItems({
					advanceConfig: {
						value: false,
						itemType: "xItemAdvanceConfig",
						label: i18n("高级配置"),
						activeText: i18n("展开"),
						inactiveText: i18n("收起"),
						children: [
							{
								_key: "param1",
								value: "",
								label: i18n("参数1"),
								itemType: "xItemInput",
								placeholder: i18n("请输入参数1"),
								rules: [_rules.required()]
							},
							{
								_key: "param2",
								value: "",
								label: i18n("参数2"),
								itemType: "xItemSelect",
								options: [
									{ label: "选项A", value: "a" },
									{ label: "选项B", value: "b" },
									{ label: "选项C", value: "c" }
								],
								placeholder: i18n("请选择参数2")
							},
							{
								_key: "param3",
								value: "",
								label: i18n("参数3"),
								itemType: "xItemInput",
								isNumber: true,
								precision: 0,
								step: 1,
								min: 1,
								max: 100,
								placeholder: i18n("请输入数字")
							}
						]
					}
				}),
				md: `### 基础用法 — itemType 模式

通过 \`itemType: "xItemAdvanceConfig"\` 在 configs 中配置，配合 \`children\` 定义子 xItem。

- Switch 关闭时仅显示开关
- Switch 打开后展开子配置项
- 配置 \`required: true\` 可隐藏开关、强制展开
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
