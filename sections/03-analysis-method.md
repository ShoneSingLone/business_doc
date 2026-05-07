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
| `table-width` | `xTableEasy.TableWidth.vue` | `/component/data/x-table-easy/table_width` |

## 3.4 模块结构对应规律

通过分析 `table-width` 模块的源文档与目标文档的对应关系，总结出以下规律：

### 3.4.1 目录结构对应

| 源文档结构 | 目标文档结构 | 说明 |
|-----------|------------|------|
| `table-width/main.vue` | `xTableEasy.TableWidth.vue` | 主入口组件 |
| `table-width/explain.md` | `mdTips` 数据属性 | 功能说明文档 |
| `table-width/auto-width.md` | `xTableEasy.TableWidth.AutoWidth.vue` | 自动宽度示例 |
| `table-width/fixed-width.md` | `xTableEasy.TableWidth.FixedWidth.vue` | 固定宽度示例 |
| `table-width/calc-width.md` | `xTableEasy.TableWidth.DynamicWidth.vue` | calc函数动态宽度示例 |
| `table-width/percent-width.md` | `xTableEasy.TableWidth.PercentWidth.vue` | 百分比宽度示例 |

### 3.4.2 组件加载模式

**源文档模式**（Vue 单文件组件）：
```vue
<template>
  <div>
    <h2>模块标题</h2>
    <Explain />
    <AutoWidth />
    <FixedWidth />
    <CalcWidth />
    <PercentWidth />
  </div>
</template>
<script>
import Explain from "./explain.md";
import AutoWidth from "./auto-width.md";
// ...
</script>
```

**目标文档模式**（业务文档平台模式）：
```vue
<template>
  <DocContentOfDemo class="x-table-easy-xxx">
    <xMd :md="mdTips" />
    <DemoAndCode title="示例1" path="@/views/..." unfold />
    <DemoAndCode title="示例2" path="@/views/..." unfold />
    <xMd :md="apiString" data-role="api" />
  </DocContentOfDemo>
</template>
```

### 3.4.3 命名转换规则

| 转换类型 | 源格式 | 目标格式 | 示例 |
|---------|--------|---------|------|
| 模块主文件 | `{module}/main.vue` | `xTableEasy.{Module}.vue` | `table-width/main.vue` → `xTableEasy.TableWidth.vue` |
| 子示例文件 | `{module}/{sub}.md` | `xTableEasy.{Module}.{Sub}.vue` | `table-width/auto-width.md` → `xTableEasy.TableWidth.AutoWidth.vue` |
| 路由路径 | 直接使用模块名 | 下划线连接 | `table-width` → `/component/data/x-table-easy/table_width` |

### 3.4.4 内容映射规则

| 源文档内容 | 目标文档位置 | 格式转换 |
|-----------|------------|---------|
| `explain.md` | `mdTips` 数据 | Markdown → 内联字符串 |
| `xxx.md` 中的代码块 | 独立 `.vue` 文件 | Markdown代码块 → Vue单文件组件 |
| API说明 | `apiString` 数据 | Markdown表格 → 内联字符串 |

---

[返回首页](../PRD_xTableEasy_Doc_Complete.md)