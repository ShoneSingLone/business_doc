# 16. 自定义事件（event-custom）

## 16.1 功能说明

支持自定义事件处理，包括表头行、表头单元格、表体行、表体单元格的点击事件。

---

## 16.2 表头行点击事件

通过 `on-header-row-click` 监听表头行点击事件。

---

## 16.3 表头单元格点击事件

通过 `on-header-cell-click` 监听表头单元格点击事件。

---

## 16.4 表体行点击事件

通过 `on-body-row-click` 监听表体行点击事件。

---

## 16.5 表体单元格点击事件

通过 `on-body-cell-click` 监听表体单元格点击事件。

---

## 16.6 API

### 事件

| 事件名 | 说明 | 参数 |
|--------|------|------|
| on-header-row-click | 表头行点击 | `event`, `row`, `column` |
| on-header-cell-click | 表头单元格点击 | `event`, `row`, `column` |
| on-body-row-click | 表体行点击 | `event`, `row`, `column` |
| on-body-cell-click | 表体单元格点击 | `event`, `row`, `column` |

---

[返回模块索引](../10-module-design.md)