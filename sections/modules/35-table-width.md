# 35. 表格宽度（table-width）

## 35.1 功能说明

**配置要点**：
1. 表格宽度可以设置固定值。如：`style="width:900px;"`
2. 表格宽度可以设置动态值。如：`style="width:calc(100vh - 210px)"` 或者 `style="width:80%"`

---

## 35.2 表格自动宽度

如果不设置表格宽度，等同于 `style="width:100%;"`，表格会自适应父容器宽度。

**特点**：
- 无需设置 style 属性
- 自动填满父容器宽度
- 响应式适应父容器变化

**配置示例**：
```vue
<template>
  <xTableEasy :columns="columns" :table-data="tableData" />
</template>
```

---

## 35.3 表格宽度固定

表格的固定宽度，需要设置外层容器宽度。可以通过 `style="width:900px"` 方式设置。

**特点**：
- 宽度固定，不随父容器变化
- 适用于固定布局场景
- 超出部分可横向滚动

**配置示例**：
```vue
<template>
  <xTableEasy style="width:900px;" :columns="columns" :table-data="tableData" />
</template>
```

---

## 35.4 表格动态宽度（calc css 函数）

你可以使用 [calc css 函数](https://developer.mozilla.org/en-US/docs/Web/CSS/calc()) 实现表格动态宽度。

**特点**：
- 支持数学表达式计算
- 可结合视窗单位(vw, vh)使用
- 实现响应式动态布局

**配置示例**：
```vue
<template>
  <xTableEasy style="width:calc(55vw - 10px);" :columns="columns" :table-data="tableData" />
</template>
```

**calc()函数支持的运算**：
| 运算符 | 说明 | 示例 |
|--------|------|------|
| `+` | 加法 | `calc(100px + 50px)` |
| `-` | 减法 | `calc(100% - 20px)` |
| `*` | 乘法 | `calc(100% * 0.8)` |
| `/` | 除法 | `calc(100px / 2)` |

---

## 35.5 表格动态宽度（百分比）

你可以使用百分比实现表格动态宽度。

**特点**：
- 相对于父容器宽度的百分比
- 响应式适应父容器变化
- 常用值：50%, 75%, 80%, 90%, 100%

**配置示例**：
```vue
<template>
  <xTableEasy style="width:80%" :columns="columns" :table-data="tableData" />
</template>
```

---

## 35.6 API

### 表格宽度设置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| style | 表格样式，可设置 width 属性 | Object/String | `{width: '100%'}` |

---

[返回模块索引](../10-module-design.md)