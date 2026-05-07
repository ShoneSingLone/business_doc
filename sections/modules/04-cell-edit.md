# 4. 单元格编辑（cell-edit）

## 4.1 功能说明

**配置要点**：
1. 通过 `editOption` 属性配置编辑功能
2. 通过在 `columns` 设置 `edit` 属性开启该列编辑
3. 双击单元格进入编辑状态

---

## 4.2 基础用法

开启单元格编辑功能。

---

## 4.3 快捷键支持

支持常用编辑快捷键：
- Enter：确认编辑
- Esc：取消编辑
- Tab：切换到下一个单元格

---

## 4.4 实例方法

通过实例方法控制编辑状态：
- `startEdit(rowKey, columnKey)`：开始编辑指定单元格
- `stopEdit()`：停止当前编辑

---

## 4.5 结合列固定

在固定列中使用编辑功能。

---

## 4.6 结合 Element UI

使用 Element UI 组件作为编辑器。

---

## 4.7 API

### editOption

编辑配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| trigger | 触发方式 | String | `dblclick` |
| mode | 编辑模式 | String | `cell` |

### 列配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| edit | 是否可编辑 | Boolean | `false` |
| editType | 编辑器类型 | String | `input` |
| editOptions | 下拉选项（当 editType 为 select 时） | Array | - |

### 事件

| 事件名 | 说明 | 参数 |
|--------|------|------|
| editStart | 开始编辑 | `row`, `column` |
| editEnd | 结束编辑 | `row`, `column`, `value` |

---

[返回模块索引](../10-module-design.md)