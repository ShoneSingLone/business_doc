<template>
	<DocContentOfDemo class="x-item-select-get-instance">
		<xMd :md="mdTips" />
		<DemoAndCode
			title="获取 xSelect 实例"
			path="@/views/component/form/select/GetXSelectInstance.vue"
			unfold />
		<xMd :md="apiString" data-role="api" />
	</DocContentOfDemo>
</template>

<script lang="ts">
export default async function () {
	return {
		data() {
			return {
				mdTips: `
# xItemSelect 获取内部 xSelect 实例

当你使用 xItem 包裹 xSelect 时，有时需要访问内部的 xSelect 组件实例来调用其方法或访问属性。

## 组件层级结构

\`\`\`
xItem (wrapper) 
  └─ xItemSelect (中间层，childVm 指向这里)
       └─ xSelect (真正的 xSelect 组件)
\`\`\`

## 获取方式

### 方式一：使用工具函数（最推荐）

我们提供了专门的工具函数来安全地获取 xSelect 实例。

#### 1. 通过 selector 获取

\`\`\`javascript
// 引入工具函数
const { getXSelectInstanceBySelector } = await _.$importVue('/common/utils/xSelectHelper.vue');

// 获取 xSelect 实例
const xSelectVm = await getXSelectInstanceBySelector('select1');

// 调用方法
xSelectVm.toggleMenu();
xSelectVm.focus();
\`\`\`

#### 2. 通过 xItem 实例获取

\`\`\`javascript
const { getXSelectInstance } = await _.$importVue('/common/utils/xSelectHelper.vue');

// 获取 xItem 实例
const xItemVm = Vue._X_ITEM_VM_S['your-item-id'];

// 获取 xSelect 实例
const xSelectVm = await getXSelectInstance(xItemVm, {
  maxRetries: 10,  // 最大重试次数
  interval: 100    // 重试间隔（毫秒）
});

// 调用方法
xSelectVm.changePopperPositionTo('body');
\`\`\`

#### 3. 在 onMounted 回调中使用

\`\`\`javascript
// 在 xItem 配置中
{
  label: '选择器',
  itemType: 'xItemSelect',
  async onMounted({ xItem }) {
    const { getXSelectInstance } = await _.$importVue('/common/utils/xSelectHelper.vue');
    
    try {
      const xSelectVm = await getXSelectInstance(xItem);
      
      // 确保下拉框初始化完成
      await vm.$nextTick();
      
      // 调用方法
      xSelectVm.changePopperPositionTo('body');
      
      console.log('✅ 成功获取 xSelect 实例');
    } catch (error) {
      console.error('❌ 获取 xSelect 实例失败:', error);
      _.$msgError('初始化选择器失败');
    }
  }
}
\`\`\`

#### 4. 批量获取多个 xSelect 实例

\`\`\`javascript
const { batchGetXSelectInstances } = await _.$importVue('/common/utils/xSelectHelper.vue');

// 批量获取
const xSelectMap = await batchGetXSelectInstances(['select1', 'select2', 'select3']);

// 使用
xSelectMap.get('select1').toggleMenu();
xSelectMap.get('select2').focus();
\`\`\`

### 方式二：通过 getXSelect() 方法

\`\`\`javascript
// 1. 获取 xItem 实例
const xItemVm = Vue._X_ITEM_VM_S['your-item-id'];

// 2. 获取 xItemSelect 实例（中间层）
const xItemSelectVm = xItemVm.childVm;

// 3. 调用 getXSelect() 获取真正的 xSelect 实例
const xSelectVm = xItemSelectVm.getXSelect();

// 4. 现在可以调用 xSelect 的方法
xSelectVm.toggleMenu();  // 打开/关闭下拉菜单
xSelectVm.focus();       // 聚焦
xSelectVm.blur();        // 失去焦点

// 访问 xSelect 的属性
console.log('xSelect value:', xSelectVm.value);
console.log('xSelect options:', xSelectVm.options);
console.log('xSelect visible:', xSelectVm.visible);
\`\`\`

### 方式二：通过 $children 访问

\`\`\`javascript
const xItemVm = Vue._X_ITEM_VM_S['your-item-id'];
const xItemSelectVm = xItemVm.childVm;

// xSelect 是 xItemSelect 的第一个子组件
const xSelectVm = xItemSelectVm.$children[0];

// 调用方法
xSelectVm.toggleMenu();
\`\`\`

## 实际使用示例

### 示例 1：打开下拉菜单

\`\`\`javascript
function openSelect(itemId) {
  const xItemVm = Vue._X_ITEM_VM_S[itemId];
  if (!xItemVm) return;
  
  const xItemSelectVm = xItemVm.childVm;
  const xSelectVm = xItemSelectVm.getXSelect();
  
  // 打开下拉菜单
  xSelectVm.visible = true;
  
  // 或者使用 toggleMenu 方法
  xSelectVm.toggleMenu();
}
\`\`\`

### 示例 2：设置值并聚焦

\`\`\`javascript
function setValueAndFocus(itemId, value) {
  const xItemVm = Vue._X_ITEM_VM_S[itemId];
  const xItemSelectVm = xItemVm.childVm;
  const xSelectVm = xItemSelectVm.getXSelect();
  
  // 设置值
  xSelectVm.$emit('change', value);
  
  // 聚焦
  xSelectVm.focus();
}
\`\`\`

### 示例 3：远程搜索

\`\`\`javascript
function remoteSearch(itemId, keyword) {
  const xItemVm = Vue._X_ITEM_VM_S[itemId];
  const xItemSelectVm = xItemVm.childVm;
  const xSelectVm = xItemSelectVm.getXSelect();
  
  // 设置搜索关键词
  xSelectVm.query = keyword;
  
  // 触发远程搜索
  if (xSelectVm.remoteMethod) {
    xSelectVm.remoteMethod(keyword);
  }
}
\`\`\`

### 示例 4：在业务代码中的完整应用

\`\`\`javascript
// 在某个按钮点击事件中
async function handleEdit() {
  // 打开编辑弹窗
  this.showDialog = true;
  
  // 等待弹窗渲染完成后操作 xSelect
  await this.$nextTick();
  
  // 获取 xSelect 实例并设置焦点
  const xItemVm = Vue._X_ITEM_VM_S['edit-form-select'];
  if (xItemVm) {
    const xItemSelectVm = xItemVm.childVm;
    const xSelectVm = xItemSelectVm.getXSelect();
    
    if (xSelectVm) {
      // 清空搜索词
      xSelectVm.query = '';
      
      // 打开下拉框
      xSelectVm.visible = true;
      
      // 聚焦输入框
      xSelectVm.focus();
    }
  }
}
\`\`\`

## 常用 xSelect 方法

| 方法名 | 说明 | 参数 |
|--------|------|------|
| toggleMenu | 切换下拉菜单的显示/隐藏 | - |
| focus | 使输入框获取焦点 | - |
| blur | 使输入框失去焦点，并隐藏下拉框 | - |
| handleClearClick | 清空选中值 | - |
| selectOption | 选中当前高亮的选项 | - |
| handleNavigate | 导航到上一个/下一个选项 | 'prev' 或 'next' |

## 常用 xSelect 属性

| 属性名 | 说明 | 类型 |
|--------|------|------|
| value | 绑定值 | any |
| visible | 下拉框是否显示 | boolean |
| options | 选项列表 | Array |
| query | 搜索关键词 | string |
| loading | 是否正在加载 | boolean |
| selectDisabled | 是否禁用 | boolean |
| selected | 已选中的选项 | Array |

## 注意事项

1. **获取时机**：确保在组件挂载完成后再获取实例，最好在 \`$nextTick\` 之后
2. **空值检查**：获取实例后先检查是否存在，避免调用不存在的方法
3. **响应式更新**：修改 xSelect 的属性时，注意使用响应式的方式（如 \`$emit('change', value)\`）
4. **性能考虑**：频繁操作 xSelect 实例可能影响性能，建议合理控制操作频率
`,
				apiString: `
## API 文档

### xItemSelect 实例方法

#### getXSelect()

获取内部的 xSelect 组件实例。

**返回值**: Vue 实例（xSelect 组件）

**示例**:
\`\`\`javascript
const xItemVm = Vue._X_ITEM_VM_S['your-item-id'];
const xItemSelectVm = xItemVm.childVm;
const xSelectVm = xItemSelectVm.getXSelect();

// 调用 xSelect 的方法
xSelectVm.toggleMenu();
\`\`\`

### xSelect 组件实例方法

#### toggleMenu()

切换下拉菜单的显示/隐藏状态。

**示例**:
\`\`\`javascript
const xSelectVm = xItemSelectVm.getXSelect();
xSelectVm.toggleMenu();
\`\`\`

#### focus()

使输入框获取焦点。

**示例**:
\`\`\`javascript
const xSelectVm = xItemSelectVm.getXSelect();
xSelectVm.focus();
\`\`\`

#### blur()

使输入框失去焦点，并隐藏下拉框。

**示例**:
\`\`\`javascript
const xSelectVm = xItemSelectVm.getXSelect();
xSelectVm.blur();
\`\`\`

#### handleClearClick()

清空选中的值（仅在 clearable 为 true 时有效）。

**示例**:
\`\`\`javascript
const xSelectVm = xItemSelectVm.getXSelect();
xSelectVm.handleClearClick();
\`\`\`

#### selectOption()

选中当前高亮的选项（通常在按下 Enter 键时调用）。

**示例**:
\`\`\`javascript
const xSelectVm = xItemSelectVm.getXSelect();
xSelectVm.selectOption();
\`\`\`

#### handleNavigate(direction)

导航到上一个或下一个选项。

**参数**:
- direction {string} - 导航方向：'prev'（上一个）或 'next'（下一个）

**示例**:
\`\`\`javascript
const xSelectVm = xItemSelectVm.getXSelect();
// 导航到上一个选项
xSelectVm.handleNavigate('prev');
// 导航到下一个选项
xSelectVm.handleNavigate('next');
\`\`\`

### xSelect 组件实例属性

#### value

绑定值，可以是字符串、数字、对象或数组（多选时）。

**类型**: any

**示例**:
\`\`\`javascript
const xSelectVm = xItemSelectVm.getXSelect();
console.log('当前选中的值:', xSelectVm.value);
\`\`\`

#### visible

下拉框的显示/隐藏状态。

**类型**: boolean

**示例**:
\`\`\`javascript
const xSelectVm = xItemSelectVm.getXSelect();
if (xSelectVm.visible) {
  console.log('下拉框已打开');
}
\`\`\`

#### options

选项列表。

**类型**: Array

**示例**:
\`\`\`javascript
const xSelectVm = xItemSelectVm.getXSelect();
console.log('所有选项:', xSelectVm.options);
\`\`\`

#### query

搜索关键词（仅在可搜索的 Select 中有效）。

**类型**: string

**示例**:
\`\`\`javascript
const xSelectVm = xItemSelectVm.getXSelect();
xSelectVm.query = '搜索关键词';
\`\`\`

#### loading

远程加载状态。

**类型**: boolean

**示例**:
\`\`\`javascript
const xSelectVm = xItemSelectVm.getXSelect();
if (xSelectVm.loading) {
  console.log('正在加载数据...');
}
\`\`\`

#### selectDisabled

是否禁用状态。

**类型**: boolean

**示例**:
\`\`\`javascript
const xSelectVm = xItemSelectVm.getXSelect();
if (xSelectVm.selectDisabled) {
  console.log('选择器已禁用');
}
\`\`\`

#### selected

已选中的选项列表（多选时）。

**类型**: Array

**示例**:
\`\`\`javascript
const xSelectVm = xItemSelectVm.getXSelect();
console.log('已选中的选项:', xSelectVm.selected);
\`\`\`
`
			};
		}
	};
}
</script>

<style lang="less">
.x-item-select-get-instance {
	// 自定义样式
}
</style>
