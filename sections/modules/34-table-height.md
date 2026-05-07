# 34. 表格高度（table-height）

## 34.1 功能说明

**配置要点**：
1. 表格高度可以设置固定值。如：`style="height:300px;"`
2. 表格高度可以设置动态值。如：`style="height:calc(100vh - 210px)"`

---

## 34.2 自动高度

表格高度随内容自动调整。

---

## 34.3 固定高度

设置固定像素高度。

**配置示例**：`style="height:300px;"`

---

## 34.4 动态高度（calc css 函数）

使用 calc 函数动态计算高度。

**配置示例**：`style="height:calc(100vh - 210px);"`

---

## 34.5 API

### 表格高度设置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| style | 表格样式，可设置 height 属性 | Object/String | - |
| max-height | 最大高度 | String/Number | - |

---

[返回模块索引](../10-module-design.md)