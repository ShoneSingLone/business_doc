# 4. 源文档与目标文档对比分析

## 4.1 源文档功能模块清单

通过扫描 `vue-easytable-master/examples/src/docs/zh/ve-table/` 目录，共识别出 **35 个功能模块**：

| 序号 | 模块名称             | 功能描述           | 源文档路径              |
| :--: | -------------------- | ------------------ | ----------------------- |
|  1   | cell-align           | 单元格对齐方式设置 | `cell-align/`           |
|  2   | cell-autofill        | 单元格自动填充功能 | `cell-autofill/`        |
|  3   | cell-custom          | 自定义单元格渲染   | `cell-custom/`          |
|  4   | cell-edit            | 单元格编辑功能     | `cell-edit/`            |
|  5   | cell-ellipsis        | 单元格内容省略     | `cell-ellipsis/`        |
|  6   | cell-selection       | 单元格选择功能     | `cell-selection/`       |
|  7   | cell-span            | 单元格合并         | `cell-span/`            |
|  8   | cell-style           | 单元格样式自定义   | `cell-style/`           |
|  9   | clipboard            | 剪贴板操作支持     | `clipboard/`            |
|  10  | column-fixed         | 列固定功能         | `column-fixed/`         |
|  11  | column-hidden        | 列隐藏功能         | `column-hidden/`        |
|  12  | column-resize        | 列宽拖拽调整       | `column-resize/`        |
|  13  | column-width         | 列宽配置           | `column-width/`         |
|  14  | contextmenu          | 右键菜单           | `contextmenu/`          |
|  15  | data-empty           | 空数据状态展示     | `data-empty/`           |
|  16  | event-custom         | 自定义事件处理     | `event-custom/`         |
|  17  | footer-summary       | 页脚汇总行         | `footer-summary/`       |
|  18  | header-filter        | 表头筛选           | `header-filter/`        |
|  19  | header-filter-custom | 自定义表头筛选     | `header-filter-custom/` |
|  20  | header-fixed         | 表头固定           | `header-fixed/`         |
|  21  | header-grouping      | 表头分组           | `header-grouping/`      |
|  22  | header-hidden        | 表头隐藏           | `header-hidden/`        |
|  23  | header-sort          | 表头排序           | `header-sort/`          |
|  24  | instance-methods     | 实例方法           | `instance-methods/`     |
|  25  | loading              | 加载状态展示       | `loading/`              |
|  26  | operation-column     | 操作列             | `operation-column/`     |
|  27  | pagination           | 分页功能           | `pagination/`           |
|  28  | row-checkbox         | 行多选             | `row-checkbox/`         |
|  29  | row-expand           | 行展开             | `row-expand/`           |
|  30  | row-index            | 行序号             | `row-index/`            |
|  31  | row-radio            | 行单选             | `row-radio/`            |
|  32  | row-style            | 行样式             | `row-style/`            |
|  33  | table-border         | 表格边框           | `table-border/`         |
|  34  | table-height         | 表格高度           | `table-height/`         |
|  35  | table-width          | 表格宽度           | `table-width/`          |
|  36  | virtual-scroll       | 虚拟滚动           | `virtual-scroll/`       |

## 4.2 现有文档页面清单

通过扫描 `business_doc/views/component/data/xTableEasy/` 目录，共识别出 **45 个文档页面文件**：

| 序号 | 文件名称                              | 功能描述       |
| :--: | ------------------------------------- | -------------- |
|  1   | `xTableEasy.Cell.Align.vue`           | 单元格对齐     |
|  2   | `xTableEasy.Cell.Autofill.vue`        | 单元格自动填充 |
|  3   | `xTableEasy.Cell.Custom.vue`          | 自定义单元格   |
|  4   | `xTableEasy.Cell.Edit.vue`            | 单元格编辑     |
|  5   | `xTableEasy.Cell.Merge.vue`           | 单元格合并     |
|  6   | `xTableEasy.Cell.Selection.vue`       | 单元格选择     |
|  7   | `xTableEasy.Cell.Style.vue`           | 单元格样式     |
|  8   | `xTableEasy.Clipboard.vue`            | 剪贴板         |
|  9   | `xTableEasy.Column.Fixed.vue`         | 列固定         |
|  10  | `xTableEasy.Column.Hidden.vue`        | 列隐藏         |
|  11  | `xTableEasy.ColumnWidth.Dragging.vue` | 列宽拖拽       |
|  12  | `xTableEasy.ColumnWidth.vue`          | 列宽配置       |
|  13  | `xTableEasy.Contextmenu.vue`          | 右键菜单       |
|  14  | `xTableEasy.Filter.vue`               | 表头筛选       |
|  15  | `xTableEasy.Filter.Custom.vue`        | 自定义表头筛选 |
|  16  | `xTableEasy.Header.Fixed.vue`         | 表头固定       |
|  17  | `xTableEasy.Header.Group.vue`         | 表头分组       |
|  18  | `xTableEasy.Header.Hidden.vue`        | 表头隐藏       |
|  19  | `xTableEasy.Row.Expand.vue`           | 行展开         |
|  20  | `xTableEasy.Row.Style.vue`            | 行样式         |
|  21  | `xTableEasy.Sort.vue`                 | 表头排序       |
|  22  | `xTableEasy.TableBorder.vue`          | 表格边框       |
|  23  | `xTableEasy.TableHeight.vue`          | 表格高度       |
|  24  | `xTableEasy.TableWidth.vue`           | 表格宽度       |
|  25  | `xTableEasy.Virtual.Scroll.vue`       | 虚拟滚动       |

## 4.3 路由配置分析

通过解析 `routes.vue` 文件，共识别出 **28 条** xTableEasy 相关路由：

| 序号 | 路由路径                                             | 组件路径                                                                | 文件存在性 |
| :--: | ---------------------------------------------------- | ----------------------------------------------------------------------- | :--------: |
|  1   | `/component/data/x-table-easy`                       | `@/views/component/data/xTableEasy/DocDemoXTableEasy.vue`               |     ✅     |
|  2   | `/component/data/x-table-easy/table_width`           | `@/views/component/data/xTableEasy/xTableEasy.TableWidth.vue`           |     ✅     |
|  3   | `/component/data/x-table-easy/table_height`          | `@/views/component/data/xTableEasy/xTableEasy.TableHeight.vue`          |     ✅     |
|  4   | `/component/data/x-table-easy/table_border`          | `@/views/component/data/xTableEasy/xTableEasy.TableBorder.vue`          |     ✅     |
|  5   | `/component/data/x-table-easy/column_width`          | `@/views/component/data/xTableEasy/xTableEasy.ColumnWidth.vue`          |     ✅     |
|  6   | `/component/data/x-table-easy/column_width_dragging` | `@/views/component/data/xTableEasy/xTableEasy.ColumnWidth.Dragging.vue` |     ✅     |
|  7   | `/component/data/x-table-easy/column_fixed`          | `@/views/component/data/xTableEasy/xTableEasy.Column.Fixed.vue`         |     ✅     |
|  8   | `/component/data/x-table-easy/column_hidden`         | `@/views/component/data/xTableEasy/xTableEasy.Column.Hidden.vue`        |     ✅     |
|  9   | `/component/data/x-table-easy/header_fixed`          | `@/views/component/data/xTableEasy/xTableEasy.Header.Fixed.vue`         |     ✅     |
|  10  | `/component/data/x-table-easy/header_group`          | `@/views/component/data/xTableEasy/xTableEasy.Header.Group.vue`         |     ✅     |
|  11  | `/component/data/x-table-easy/header_hidden`         | `@/views/component/data/xTableEasy/xTableEasy.Header.Hidden.vue`        |     ✅     |
|  12  | `/component/data/x-table-easy/filter`                | `@/views/component/data/xTableEasy/xTableEasy.Filter.vue`               |     ✅     |
|  13  | `/component/data/x-table-easy/filter_custom`         | `@/views/component/data/xTableEasy/xTableEasy.Filter.Custom.vue`        |     ✅     |
|  14  | `/component/data/x-table-easy/sort`                  | `@/views/component/data/xTableEasy/xTableEasy.Sort.vue`                 |     ✅     |
|  15  | `/component/data/x-table-easy/cell_align`            | `@/views/component/data/xTableEasy/xTableEasy.Cell.Align.vue`           |     ✅     |
|  16  | `/component/data/x-table-easy/cell_style`            | `@/views/component/data/xTableEasy/xTableEasy.Cell.Style.vue`           |     ✅     |
|  17  | `/component/data/x-table-easy/cell_custom`           | `@/views/component/data/xTableEasy/xTableEasy.Cell.Custom.vue`          |     ✅     |
|  18  | `/component/data/x-table-easy/cell_merge`            | `@/views/component/data/xTableEasy/xTableEasy.Cell.Merge.vue`           |     ✅     |
|  19  | `/component/data/x-table-easy/action_column`         | `@/views/component/data/xTableEasy/xTableEasy.Action.Column.vue`        |     ✅     |
|  20  | `/component/data/x-table-easy/cell_selection`        | `@/views/component/data/xTableEasy/xTableEasy.Cell.Selection.vue`       |     ✅     |
|  21  | `/component/data/x-table-easy/cell_edit`             | `@/views/component/data/xTableEasy/xTableEasy.Cell.Edit.vue`            |     ✅     |
|  22  | `/component/data/x-table-easy/virtual_scroll`        | `@/views/component/data/xTableEasy/xTableEasy.Virtual.Scroll.vue`       |     ✅     |
|  23  | `/component/data/x-table-easy/row_style`             | `@/views/component/data/xTableEasy/xTableEasy.Row.Style.vue`            |     ✅     |
|  24  | `/component/data/x-table-easy/row_expand`            | `@/views/component/data/xTableEasy/xTableEasy.Row.Expand.vue`           |     ✅     |
|  25  | `/component/data/x-table-easy/clipboard`             | `@/views/component/data/xTableEasy/xTableEasy.Clipboard.vue`            |     ✅     |
|  26  | `/component/data/x-table-easy/contextmenu`           | `@/views/component/data/xTableEasy/xTableEasy.Contextmenu.vue`          |     ✅     |
|  27  | `/component/data/x-table-easy/cell_autofill`         | `@/views/component/data/xTableEasy/xTableEasy.Cell.Autofill.vue`        |     ✅     |
|  28  | `/component/data/x-table-easy/base_usage`            | `@/views/component/data/xTableEasy/JiChuYongFa.vue`                     |     ✅     |

---

[返回首页](../PRD_xTableEasy_Doc_Complete.md)
