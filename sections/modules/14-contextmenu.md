# 14. 右键菜单（contextmenu）

## 14.1 功能说明

有些操作可以通过右键菜单更方便的完成。比如单元格编辑功能，可以通过右键操作很方便的插入行或者移除行。当然你也可以自定义右键菜单功能。

---

## 14.2 右键菜单清单

### 14.2.1 header 右键菜单清单

| 功能               | 类型                           |
| :----------------- | :----------------------------- |
| 分割线             | `SEPARATOR`                    |
| 剪切               | `CUT`                          |
| 拷贝               | `COPY`                         |
| 清空列             | `EMPTY_COLUMN`                 |
| 左列冻结至该列     | `LEFT_FIXED_COLUMN_TO`         |
| 右列冻结至该列     | `RIGHT_FIXED_COLUMN_TO`        |
| 取消左列冻结至该列 | `CANCEL_LEFT_FIXED_COLUMN_TO`  |
| 取消右列冻结至该列 | `CANCEL_RIGHT_FIXED_COLUMN_TO` |

### 14.2.2 body 右键菜单清单

| 功能         | 类型               |
| :----------- | :----------------- |
| 分割线       | `SEPARATOR`        |
| 剪切         | `CUT`              |
| 拷贝         | `COPY`             |
| 在上方插入行 | `INSERT_ROW_ABOVE` |
| 在下方插入行 | `INSERT_ROW_BELOW` |
| 删除行       | `REMOVE_ROW`       |
| 清空行       | `EMPTY_ROW`        |
| 清空单元格   | `EMPTY_CELL`       |

---

## 14.3 基础用法

右键表格区域查看效果。你可以根据需要进行组合使用。

**基本配置**：

- 通过 `contextmenu-header-option` 配置表头右键菜单
- 通过 `contextmenu-body-option` 配置表体右键菜单
- 每个配置包含 `beforeShow`、`afterMenuClick` 和 `contextmenus` 三个主要属性

---

## 14.4 自定义右键菜单

支持自定义右键菜单功能，包括：

- 自定义菜单项标签
- 嵌套子菜单
- 禁用菜单项
- 自定义菜单类型

---

## 14.5 API

### 14.5.1 contextmenuHeaderOption

header 右键菜单配置

| 属性           | 说明                           | 类型     |
| -------------- | ------------------------------ | -------- |
| beforeShow     | 菜单显示前回调，可修改菜单配置 | Function |
| afterMenuClick | 菜单点击后回调                 | Function |
| contextmenus   | 菜单项配置数组                 | Array    |

**contextmenus 菜单项配置**：| 属性 | 说明 | 类型 | |------|------|------| | type | 菜单类型 | String | | label
| 自定义标签 | String | | disabled | 是否禁用 | Boolean | | children | 子菜单 | Array |

### 14.5.2 contextmenuBodyOption

body 右键菜单配置

| 属性           | 说明                           | 类型     |
| -------------- | ------------------------------ | -------- |
| beforeShow     | 菜单显示前回调，可修改菜单配置 | Function |
| afterMenuClick | 菜单点击后回调                 | Function |
| contextmenus   | 菜单项配置数组                 | Array    |

**contextmenus 菜单项配置**：| 属性 | 说明 | 类型 | |------|------|------| | type | 菜单类型 | String | | label
| 自定义标签 | String | | disabled | 是否禁用 | Boolean | | children | 子菜单 | Array |

---

[返回模块索引](../10-module-design.md)
