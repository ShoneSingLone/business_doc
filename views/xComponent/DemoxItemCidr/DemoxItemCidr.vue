<style lang="less"></style>
<template>
	<div>
		cidr:{{ cidr }}
		<xItem :configs="cidr" style="--xItem-wrapper-width: 450px" />
	</div>
</template>
<script lang="ts">
	export default async function () {
		return defineComponent({
			data() {
				return {
					cidr: defItem({
						label: "子网网段",
						value: "0/0",
						itemType: "xItemCidr",
						msg: ``,
						rules: [
							_rules.required(),
							{
								async validator({ val }) {
									console.log("🚀 ~ validator ~ val:", val);
									try {
										const [ipString, ipPort] = String(val).split("/");
										const [a, b, c, d] = String(ipString).split(".");
										if (
											_.some([a, b, c, d, ipPort], i => {
												const _i = Number(i);
												console.log(i, _i);
												if (_.isNaN(_i)) {
													return true;
												}

												if (_i < 0) {
													return true;
												}
												return false;
											})
										) {
											return i18n("IP地址不合法。");
										} else {
											return "";
										}
									} catch (error) {
										return i18n("IP地址不合法。");
									}
								},
								trigger: ["change", "blur"]
							}
						],
						tips: i18n("子网创建完成后，子网网段无法修改。")
					})
				};
			}
		});
	}
</script>
