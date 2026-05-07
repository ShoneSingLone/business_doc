# 31. 行单选（row-radio）

## 31.1 功能说明

**配置要点**：
1. 通过 `radioOption` 属性开启单选功能
2. 通过在 `columns` 设置 `type=radio` 作为单选的列
3. 设置 `rowKeyFieldName` 属性对应行数据的列名

---

## 31.2 基础用法

通过设置 `radioOption` 和 `type=radio` 列开启单选功能。

---

## 31.3 默认选中

通过 `selectedRowKey` 设置默认选中的行。

---

## 31.4 禁用行选中

通过 `disabled` 函数控制某些行不可选中。

---

## 31.5 点击行选中

设置 `checkStrictly=false`，点击行即可选中。

---

## 31.6 自定义列位置

将单选列放在任意位置。

---

## 31.7 API

### radioOption

单选配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| selectedRowKey | 默认选中的行 key | Any | - |
| disabled | 禁用选中的函数 | Function | - |
| checkStrictly | 是否严格模式（仅点击 radio 选中） | Boolean | `true` |

### 事件

| 事件名 | 说明 | 参数 |
|--------|------|------|
| selectedRowChange | 行选中状态改变 | `row`, `isSelected`, `selectedRowKey` |

---

[返回模块索引](../10-module-design.md)