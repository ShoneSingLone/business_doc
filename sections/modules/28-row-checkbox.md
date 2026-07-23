# 28. 行多选（row-checkbox）

## 28.1 功能说明

**配置要点**：

1. 通过 `checkboxOption` 属性开启多选功能
2. 通过在 `columns` 设置 `type=checkbox` 作为多选的列
3. 设置 `rowKeyFieldName` 属性对应行数据的列名
4. `selectedRowChange` 行改变事件，接收 3 个参数：`row`、`isSelected`、`selectedRowKeys`
5. `selectedAllChange` 全选事件，接收 2 个参数：`isSelected`、`selectedRowKeys`

---

## 28.2 基础用法

通过设置 `checkboxOption` 和 `type=checkbox` 列开启多选功能。

---

## 28.3 默认选中

通过 `selectedRowKeys` 设置默认选中的行。

---

## 28.4 禁用行选中

通过 `disabled` 函数控制某些行不可选中。

---

## 28.5 点击行选中

设置 `checkStrictly=false`，点击行即可选中。

---

## 28.6 自定义列位置

将多选列放在任意位置。

---

## 28.7 隐藏全选框

设置 `hideDefaultCheckbox` 隐藏全选框。

---

## 28.8 API

### checkboxOption

多选配置

| 属性                | 说明                                 | 类型     | 默认值  |
| ------------------- | ------------------------------------ | -------- | ------- |
| selectedRowKeys     | 默认选中的行 key 数组                | Array    | -       |
| disabled            | 禁用选中的函数                       | Function | -       |
| checkStrictly       | 是否严格模式（仅点击 checkbox 选中） | Boolean  | `true`  |
| hideDefaultCheckbox | 是否隐藏全选框                       | Boolean  | `false` |

### 事件

| 事件名            | 说明           | 参数                                   |
| ----------------- | -------------- | -------------------------------------- |
| selectedRowChange | 行选中状态改变 | `row`, `isSelected`, `selectedRowKeys` |
| selectedAllChange | 全选状态改变   | `isSelected`, `selectedRowKeys`        |

---

[返回模块索引](../10-module-design.md)
