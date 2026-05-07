# 3. 对应关系分析方法

## 3.1 数据源定义

| 数据源 | 路径 | 描述 |
|--------|------|------|
| 路由配置 | `router/routes.vue` | 定义文档页面的访问路径和组件映射 |
| 现有文档 | `views/component/data/xTableEasy/` | 已实现的文档页面集合 |
| 源文档 | `E:\ghca_code\vue-easytable-master/examples/src/docs/zh/ve-table/` | 第三方库的完整文档 |

## 3.2 分析流程

```
源文档目录扫描 → 现有文档目录扫描 → 路由配置解析
         ↓                ↓                ↓
    功能模块识别    已实现模块清单    路由映射提取
         ↓                ↓                ↓
         └────────→  对应关系比对  ←────────┘
                        ↓
              缺失模块识别与优先级排序
```

## 3.3 命名规范映射

| 源文档命名 | 现有文档命名 | 路由路径 |
|-----------|------------|----------|
| `cell-align` | `xTableEasy.Cell.Align.vue` | `/component/data/x-table-easy/cell_align` |
| `column-fixed` | `xTableEasy.Column.Fixed.vue` | `/component/data/x-table-easy/column_fixed` |
| `header-filter` | `xTableEasy.Filter.vue` | `/component/data/x-table-easy/filter` |

---

[返回首页](../PRD_xTableEasy_Doc_Complete.md)