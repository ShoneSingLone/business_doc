# 29. 行展开（row-expand）

## 29.1 功能说明

**配置要点**：

1. 通过 `expandOption` 属性配置展开行功能
2. 通过在 `columns` 设置 `type=expand` 展开的列
3. 设置 `rowKeyFieldName` 属性对应行数据的列名
4. `render` 函数允许自定义展开内容，支持 jsx 语法

---

## 29.2 基础用法

通过 `expandOption` 和 `type=expand` 列开启行展开功能。

---

## 29.3 默认展开

通过 `expandedRowKeys` 设置默认展开的行。

---

## 29.4 自定义触发方式

设置 `trigger` 属性自定义展开触发方式（click/dblclick）。

---

## 29.5 控制展开

通过 API 控制行的展开和收起。

---

## 29.6 展开事件

监听展开和收起事件。

---

## 29.7 展开表格

在展开区域内嵌表格。

---

## 29.8 展开图表

在展开区域内嵌图表。

---

## 29.9 自定义展开列位置

将展开列放在任意位置。

---

## 29.10 条件展开

通过 `expandable` 函数控制哪些行可以展开。

---

## 29.11 API

### expandOption

展开配置

| 属性            | 说明                  | 类型     | 默认值  |
| --------------- | --------------------- | -------- | ------- |
| expandedRowKeys | 默认展开的行 key 数组 | Array    | -       |
| trigger         | 触发方式              | String   | `click` |
| expandable      | 是否可展开的函数      | Function | -       |
| render          | 自定义展开内容        | Function | -       |

### 事件

| 事件名       | 说明         | 参数              |
| ------------ | ------------ | ----------------- |
| expandChange | 展开状态改变 | `row`, `expanded` |

---

[返回模块索引](../10-module-design.md)
