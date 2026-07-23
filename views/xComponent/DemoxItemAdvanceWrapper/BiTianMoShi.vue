<template>
	<div>
		<xMd :md="md" />
		<xForm col="1" style="--xItem-label-position: flex-start; --xItem-wrapper-width: 500px">
			<xItem :configs="form.baseName" />
			<xItemAdvanceWrapper :required="true">
				<xItem :configs="form.timeout" />
				<xItem :configs="form.retries" />
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
						placeholder: i18n("请输入超时时间"),
						rules: [_rules.required()]
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
						placeholder: i18n("请输入重试次数"),
						rules: [_rules.required()]
					}
				}),
				md: `### 必填模式 — 强制展开

设置 \`required\` 为 \`true\` 时：
- Switch 开关**隐藏**，不允许折叠
- 子配置项始终可见
- 适用于子项中有必填字段的场景
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
