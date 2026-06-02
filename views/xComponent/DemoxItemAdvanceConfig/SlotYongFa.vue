<template>
	<div>
		<xMd :md="md" />
		<xForm col="1" style="--xItem-label-position: flex-start; --xItem-wrapper-width: 500px">
			<xItem label="基础配置">
				<xItem :configs="form.baseName" />
			</xItem>
			<xItem label="高级配置">
				<xItemAdvanceConfig v-model="isAdvanceOpen">
					<xItem :configs="form.advParam1" />
					<xItem :configs="form.advParam2" />
					<xItem :configs="form.advParam3" />
				</xItemAdvanceConfig>
			</xItem>
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
				isAdvanceOpen: false,
				form: defItems({
					baseName: {
						value: "",
						label: i18n("名称"),
						itemType: "xItemInput",
						placeholder: i18n("请输入名称"),
						rules: [_rules.required()]
					},
					advParam1: {
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
					advParam2: {
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
					advParam3: {
						value: "TCP",
						label: i18n("协议类型"),
						itemType: "xItemSelect",
						options: [
							{ label: "TCP", value: "TCP" },
							{ label: "UDP", value: "UDP" },
							{ label: "HTTP", value: "HTTP" },
							{ label: "HTTPS", value: "HTTPS" }
						]
					}
				}),
				md: `### Slot 用法 — 独立 Wrapper 模式

直接使用 \`<xItemAdvanceConfig>\` 组件，通过 **slot** 传入任意子控件。

- 适合子控件结构复杂、不能简单用 children 数组描述的场景
- 外层用 \`<xItem label="高级配置">\` 包裹，利用 xItem 的 label 和校验能力
- 通过 \`v-model\` 控制开关状态
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
						_.$msgSuccess(JSON.stringify({ ...values, isAdvanceOpen: vm.isAdvanceOpen }, null, 2));
					}
				};
			}
		}
	});
}
</script>

<style lang="less"></style>
