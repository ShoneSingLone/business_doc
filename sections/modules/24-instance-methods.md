# 24. 实例方法（instance-methods）

## 24.1 功能说明

表格提供了一些实例方法供外部调用。

---

## 24.2 滚动到指定位置

### 24.2.1 滚动到指定坐标

使用 `scrollTo(x, y)` 方法滚动到指定坐标。

### 24.2.2 滚动到指定行

使用 `scrollToRowKey(rowKey)` 方法滚动到指定行。

### 24.2.3 滚动到指定列

使用 `scrollToColKey(colKey)` 方法滚动到指定列。

---

## 24.3 API

### 实例方法

| 方法名 | 说明 | 参数 |
|--------|------|------|
| scrollTo(x, y) | 滚动到指定坐标 | `x`: 水平位置, `y`: 垂直位置 |
| scrollToRowKey(rowKey) | 滚动到指定行 | `rowKey`: 行标识 |
| scrollToColKey(colKey) | 滚动到指定列 | `colKey`: 列标识 |

---

[返回模块索引](../10-module-design.md)