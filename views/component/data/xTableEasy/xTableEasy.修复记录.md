# xTableEasy 组件修复记录

## 问题描述

xTableEasy 组件渲染表格时，数据行显示为空（`<!---->`），用户无法看到列表数据。

## 问题原因

经过分析，发现以下两个问题：

### 1. 组件注册缺失

多个组件缺少 `components` 对象注册子组件，导致子组件无法被正确渲染：

- **`body-tr.vue`**: 缺少 `BodyTd` 和 `VueDomResizeObserver` 组件注册
- **`body/index.vue`**: 缺少 `BodyTr`、`BodyTrScrolling`、`ExpandTr` 和 `VueDomResizeObserver` 组件注册
- **`body-td.vue`**: 缺少 `BodyCheckboxContent`、`BodyRadioContent` 和 `ExpandTrIcon` 组件注册

### 2. 导入语法错误

`_.$importVue()` 返回组件对象本身，而不是带有 `default` 属性的对象。但代码中错误地使用了解构 `default` 属性的语法：

```javascript
// 错误写法
const [{ default: BodyTd }, ...] = await Promise.all([_.$importVue("...")]);

// 正确写法
const [BodyTd, ...] = await Promise.all([_.$importVue("...")]);
```

## 修复内容

### 文件修改列表

| 文件路径 | 修改内容 |
|---------|---------|
| `statics/common/ui-x/components/data/xTableEasy/body/body-tr.vue` | 添加 `components` 对象注册子组件，并修复导入语法 |
| `statics/common/ui-x/components/data/xTableEasy/body/index.vue` | 添加 `components` 对象注册子组件 |
| `statics/common/ui-x/components/data/xTableEasy/body/body-td.vue` | 添加 `components` 对象注册子组件 |

### 关键代码变更

**body-tr.vue**:
```javascript
// 添加 components 对象
components: {
    BodyTd,
    VueDomResizeObserver
},

// 修复导入语法（去掉 default 解构）
const [BodyTd, ...] = await Promise.all([_.$importVue("...")]);
```

**body/index.vue**:
```javascript
// 添加 components 对象
components: {
    BodyTr,
    BodyTrScrolling,
    ExpandTr,
    VueDomResizeObserver
},
```

**body-td.vue**:
```javascript
// 添加 components 对象
components: {
    BodyCheckboxContent,
    BodyRadioContent,
    ExpandTrIcon
},
```

## 验证结果

修复后，表格数据正确显示：

| ID | 姓名 | 年龄 | 性别 | 电话号码 | 地址 |
|---|---|---|---|---|---|
| 1 | 张三 | 18 | 男 | 13800000001 | 上海市普陀区金沙江路 1518 弄 |
| 2 | 李四 | 20 | 女 | 13800000002 | 上海市浦东新区张江高科技园区 |
| ... | ... | ... | ... | ... | ... |

## 修复时间

2026年5月

## 注意事项

1. 使用 `_.$importVue()` 加载组件时，直接获取返回值即可，不需要解构 `default` 属性。
2. 在 Vue 组件中使用子组件时，必须在 `components` 对象中注册。
3. 异步组件加载完成后，确保组件对象被正确传递和使用。