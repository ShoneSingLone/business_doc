<template>
	<DocContentOfDemo class="demo-input">
		<xMd :md="mdTips" />
		<DemoAndCode title="基础用法" path="@/views/component/form/select/JiChuYongFa.vue" unfold />
		<DemoAndCode
			title="有禁用选项"
			path="@/views/component/form/select/YouJinYongXuanXiang.vue"
			unfold />
		<DemoAndCode
			title="选择器不可用状态"
			path="@/views/component/form/select/XuanZeQiBuKeYongZhuangTai.vue"
			unfold />
		<DemoAndCode
			title="可清空单选"
			path="@/views/component/form/select/KeQingKongDanXuan.vue"
			unfold />
		<DemoAndCode
			title="基础多选"
			path="@/views/component/form/select/JiChuDuoXuan.vue"
			unfold />
		<DemoAndCode
			title="自定义模板"
			path="@/views/component/form/select/ZiDingYiMoBan.vue"
			unfold />
		<DemoAndCode title="分组" path="@/views/component/form/select/FenZu.vue" unfold />
		<DemoAndCode title="可搜索" path="@/views/component/form/select/KeSouSuo.vue" unfold />
		<DemoAndCode
			title="远程搜索"
			path="@/views/component/form/select/YuanChengSouSuo.vue"
			unfold />
		<DemoAndCode
			title="创建条目"
			path="@/views/component/form/select/ChuangJianTiaoMu.vue"
			unfold />
		<DemoAndCode
			title="测试：changePopperPositionTo"
			path="@/views/component/form/select/ChangePopperPositionTo.vue"
			unfold />
		<DemoAndCode
			title="获取 xSelect 实例"
			path="@/views/component/form/select/GetXSelectInstance.vue"
			unfold />
		<DemoAndCode
			title="获取 xSelect 实例 - 完整文档"
			path="@/views/component/form/select/GetXSelectInstanceDoc.vue"
			unfold />
		<xMd :md="apiString" data-role="api" />
	</DocContentOfDemo>
</template>

<script lang="ts">
export default async function () {
	return {
		data() {
			return {
				mdTips: "当选项过多时，使用下拉菜单展示并选择内容。\n\n>如果 Select 的绑定值为对象类型，请务必指定 `value-key` 作为它的唯一性标识。",
				apiString: `
> 如果 Select 的绑定值为对象类型，请务必指定 \`value-key\` 作为它的唯一性标识。

### Select Attributes
| 参数      | 说明          | 类型      | 可选值                           | 默认值  |
|---------- |-------------- |---------- |--------------------------------  |-------- |
| value / v-model | 绑定值 | boolean / string / number | — | — |
| multiple | 是否多选 | boolean | — | false |
| disabled | 是否禁用 | boolean | — | false |
| value-key | 作为 value 唯一标识的键名，绑定值为对象类型时必填 | string | — | value |
| size | 输入框尺寸 | string | medium/small/mini | — |
| clearable | 是否可以清空选项 | boolean | — | false |
| collapse-tags | 多选时是否将选中值按文字的形式展示 | boolean | — | false |
| multiple-limit | 多选时用户最多可以选择的项目数，为 0 则不限制 | number | — | 0 |
| name | select input 的 name 属性 | string | — | — |
| autocomplete | select input 的 autocomplete 属性 | string | — | off |
| auto-complete | 下个主版本弃用 | string | — | off |
| placeholder | 占位符 | string | — | 请选择 |
| filterable | 是否可搜索 | boolean | — | false |
| allow-create | 是否允许用户创建新条目，需配合 \`filterable\` 使用 | boolean | — | false |
| filter-method | 自定义搜索方法 | function | — | — |
| remote | 是否为远程搜索 | boolean | — | false |
| remote-method | 远程搜索方法 | function | — | — |
| loading | 是否正在从远程获取数据 | boolean | — | false |
| loading-text | 远程加载时显示的文字 | string | — | 加载中 |
| no-match-text | 搜索条件无匹配时显示的文字，也可以使用\`slot="empty"\`设置 | string | — | 无匹配数据 |
| no-data-text | 选项为空时显示的文字，也可以使用\`slot="empty"\`设置 | string | — | 无数据 |
| popper-class | Select 下拉框的类名 | string | — | — |
| reserve-keyword | 多选且可搜索时，是否在选中一个选项后保留当前的搜索关键词 | boolean | — | false |
| default-first-option | 在输入框按下回车，选择第一个匹配项。需配合 \`filterable\` 或 \`remote\` 使用 | boolean | - | false |
| popper-append-to-body | 是否将弹出框插入至 body 元素。在弹出框的定位出现问题时，可将该属性设置为 false | boolean | - | true |
| automatic-dropdown | 对于不可搜索的 Select，是否在输入框获得焦点后自动弹出选项菜单 | boolean | - | false |

### Select Events
| 事件名称 | 说明 | 回调参数 |
|---------|---------|---------|
| change | 选中值发生变化时触发 | 目前的选中值 |
| visible-change | 下拉框出现/隐藏时触发 | 出现则为 true，隐藏则为 false |
| remove-tag | 多选模式下移除tag时触发 | 移除的tag值 |
| clear | 可清空的单选模式下用户点击清空按钮时触发 | — |
| blur | 当 input 失去焦点时触发 | (event: Event) |
| focus | 当 input 获得焦点时触发 | (event: Event) |

### Select Slots
|   name  | 说明     |
|---------|---------|
|    —    | Option 组件列表 |
| prefix  | Select 组件头部内容 |
| empty | 无选项时的列表 |

### Option Group Attributes
| 参数      | 说明          | 类型      | 可选值                           | 默认值  |
|---------- |-------------- |---------- |--------------------------------  |-------- |
| label | 分组的组名 | string | — | — |
| disabled | 是否将该分组下所有选项置为禁用 | boolean | — | false |

### Option Attributes
| 参数      | 说明          | 类型      | 可选值                           | 默认值  |
|---------- |-------------- |---------- |--------------------------------  |-------- |
| value | 选项的值 | string/number/object | — | — |
| label | 选项的标签，若不设置则默认与 \`value\` 相同 | string/number | — | — |
| disabled | 是否禁用该选项 | boolean | — | false |

### Methods
| 方法名 | 说明 | 参数 |
| ---- | ---- | ---- |
| focus | 使 input 获取焦点 | - |
| blur | 使 input 失去焦点，并隐藏下拉框 | - |
| changePopperPositionTo | 强制切换下拉框 DOM 位置。调用时立即将下拉框移动到 body 下或组件内部，并添加对应的状态样式类 | mode: 'body' \| string - 传入 'body' 时移动到 body 下 (appendToBody 模式)，传入其他值时移回组件内部 (非 appendToBody 模式) |

### 状态样式
| 类名 | 说明 | 触发条件 |
| ---- | ---- | ---- |
| is-append-to-body | 下拉框在 body 下 (appendToBody 模式) | 调用 changePopperPositionTo('body') 后添加 |
| is-append-to-self | 下拉框在组件内部 (非 appendToBody 模式) | 调用 changePopperPositionTo(非 'body' 值) 后添加 |

### 使用示例
\`\`\`javascript
// 获取 xSelect 组件实例
const selectVm = this.$refs.mySelect;

// 强制将下拉框移动到 body 下
selectVm.changePopperPositionTo('body');

// 强制将下拉框移回组件内部
selectVm.changePopperPositionTo('other');

// 组件根元素会自动添加对应的状态类:
// - appendToBody 模式：<div class="el-select is-append-to-body">
// - 非 appendToBody 模式：<div class="el-select is-append-to-self">
\`\`\`
	
`
			};
		}
	};
}
</script>

<style lang="less"></style>
