<template>
	<div class="get-x-select-instance-demo">
		<xForm :configs="formConfigs" ref="xForm">
			<xItem
				:configs="formConfigs.select1"
				selector="select1"
				item-type="xItemSelect" />
			
			<div class="mt16">
				<xBtn @click="handleOpenMenu">打开下拉菜单</xBtn>
				<xBtn @click="handleCloseMenu" class="ml8">关闭下拉菜单</xBtn>
				<xBtn @click="handleFocus" class="ml8">聚焦</xBtn>
				<xBtn @click="handleGetValue" class="ml8">获取值</xBtn>
				<xBtn @click="handleSetValue" class="ml8">设置值</xBtn>
			</div>
			
			<div class="mt16">
				<p>操作日志：</p>
				<div class="log-box">{{ log }}</div>
			</div>
		</xForm>
	</div>
</template>

<script lang="ts">
export default async function () {
	const i18n = await _.$importI18n();
	
	return {
		data() {
			return {
				log: '',
				formConfigs: {
					select1: {
						label: '选择器',
						value: '',
						placeholder: '请选择',
						options: [
							{ label: '选项 1', value: '1' },
							{ label: '选项 2', value: '2' },
							{ label: '选项 3', value: '3' },
							{ label: '选项 4', value: '4' },
							{ label: '选项 5', value: '5' }
						],
						clearable: true,
						filterable: true
					}
				}
			};
		},
		methods: {
			/**
			 * 获取 xSelect 实例的封装方法
			 * @param {string} selector - xItem 的 selector
			 * @returns {Vue} xSelect 实例
			 */
			getXSelectBySelector(selector) {
				// 通过 selector 查找 xItem 的 DOM 元素
				const xItemElement = document.querySelector(`[data-form-item-selector="${selector}"]`);
				if (!xItemElement) {
					this.log = `未找到 selector 为 ${selector} 的 xItem`;
					return null;
				}
				
				// 获取 data-form-item-id
				const itemId = xItemElement.getAttribute('data-form-item-id');
				if (!itemId) {
					this.log = `未找到 data-form-item-id`;
					return null;
				}
				
				// 通过 Vue._X_ITEM_VM_S 获取 xItem 实例
				const xItemVm = Vue._X_ITEM_VM_S[itemId];
				if (!xItemVm) {
					this.log = `未找到 xItem 实例，ID: ${itemId}`;
					return null;
				}
				
				// 获取 xItemSelect 实例
				const xItemSelectVm = xItemVm.childVm;
				if (!xItemSelectVm) {
					this.log = `xItemSelect 实例不存在`;
					return null;
				}
				
				// 获取 xSelect 实例
				const xSelectVm = xItemSelectVm.getXSelect();
				if (!xSelectVm) {
					this.log = `xSelect 实例不存在`;
					return null;
				}
				
				return xSelectVm;
			},
			
			/**
			 * 打开下拉菜单
			 */
			handleOpenMenu() {
				const xSelectVm = this.getXSelectBySelector('select1');
				if (xSelectVm) {
					xSelectVm.toggleMenu();
					this.log = '✅ 已打开下拉菜单';
					console.log('打开下拉菜单，xSelect 实例:', xSelectVm);
				}
			},
			
			/**
			 * 关闭下拉菜单
			 */
			handleCloseMenu() {
				const xSelectVm = this.getXSelectBySelector('select1');
				if (xSelectVm && xSelectVm.visible) {
					xSelectVm.visible = false;
					this.log = '✅ 已关闭下拉菜单';
				}
			},
			
			/**
			 * 聚焦
			 */
			handleFocus() {
				const xSelectVm = this.getXSelectBySelector('select1');
				if (xSelectVm) {
					xSelectVm.focus();
					this.log = '✅ 已聚焦到选择器';
				}
			},
			
			/**
			 * 获取值
			 */
			handleGetValue() {
				const xSelectVm = this.getXSelectBySelector('select1');
				if (xSelectVm) {
					const value = xSelectVm.value;
					this.log = `当前值：${value || '空'}`;
					console.log('xSelect value:', value);
				}
			},
			
			/**
			 * 设置值
			 */
			handleSetValue() {
				const xSelectVm = this.getXSelectBySelector('select1');
				if (xSelectVm) {
					// 使用 $emit 触发 change 事件来设置值
					xSelectVm.$emit('change', '3');
					this.log = '✅ 已设置值为 "3"';
				}
			}
		}
	};
}
</script>

<style lang="less" scoped>
.get-x-select-instance-demo {
	padding: 20px;
	
	.log-box {
		margin-top: 8px;
		padding: 12px;
		background-color: #f5f7fa;
		border: 1px solid #e4e7ed;
		border-radius: 4px;
		font-family: 'Courier New', monospace;
		font-size: 13px;
		line-height: 1.6;
		color: #606266;
		min-height: 40px;
	}
}
</style>
