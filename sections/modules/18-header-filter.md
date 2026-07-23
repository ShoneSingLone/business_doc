# 18. 表头筛选（header-filter）

## 18.1 功能说明

通过 `column` 对象的 `filter` 属性设置筛选功能，支持单条件筛选和多条件筛选。

**配置要点**：

1. 通过 `column` 对象的 `filter` 属性设置筛选功能
2. `filterList` 设置筛选条件，包含 `label`、`value`、`selected` 三个属性
3. `isMultiple` 开启筛选项多选，默认为 false
4. `filterConfirm` 筛选确认函数
5. `filterReset` 筛选重置函数

---

## 18.2 单条件筛选

默认只支持单选筛选，点击表头筛选图标即可打开筛选下拉框。

**特点**：

- 只能选择一个选项
- 适合互斥的筛选条件
- 简单直观

---

## 18.3 多条件筛选

设置 `isMultiple: true` 开启多选模式。

**特点**：

- 可选择多个选项
- 适合组合筛选条件
- 当筛选框内容很多时，可通过 `maxHeight` 属性设置筛选框的最大高度

---

## 18.4 混合使用

根据不同的业务场景，任意搭配使用单条件筛选和多条件筛选。

**特点**：

- 不同列可配置不同筛选模式
- 通过 `selected: true` 设置默认选中的项
- 支持组合筛选逻辑

---

## 18.5 自定义图标

`filterIcon` 回调函数，支持返回自定义的图标。

**特点**：

- 可自定义筛选图标
- 支持使用内置图标或第三方图标库

---

## 18.6 API

### filter

表头筛选配置

| 属性          | 说明           | 类型     | 默认值  |
| ------------- | -------------- | -------- | ------- |
| filterList    | 筛选条件列表   | Array    | -       |
| isMultiple    | 是否多选       | Boolean  | `false` |
| maxHeight     | 筛选框最大高度 | Number   | -       |
| filterConfirm | 筛选确认回调   | Function | -       |
| filterReset   | 筛选重置回调   | Function | -       |
| filterIcon    | 自定义筛选图标 | Function | -       |

**filterList 项配置**：| 属性 | 说明 | 类型 | |------|------|------| | value | 值 | Any | | label | 显示标签 | String |
| selected | 是否选中 | Boolean |

---

[返回模块索引](../10-module-design.md)
