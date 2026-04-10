# xTableEasy 文档页补齐计划

## 目标

补齐 `business_doc`
中 xTableEasy 缺失的新命名文档页，并修正文档路由指向不存在文件的问题，保证菜单、路由、文档页三者一致。

## 当前已确认问题

1. `routes.vue` 中存在多处 xTableEasy 重复路由声明。
2. 多个路由仍指向不存在的旧/新页面文件。
3. 已确认缺失或引用异常的页面包括：
    - `xTableEasy.Header.Group.vue`
    - `xTableEasy.Row.Style.vue`
    - `xTableEasy.Row.Expand.vue`
    - `xTableEasy.Virtual.Scroll.vue`
    - `examples/HangZhanKai.vue`
    - 以及部分旧中文文件引用（需逐项校对是否真实存在）

## 本批次处理策略

1. 先以现有可运行页面为基础补齐缺失的新命名页面。
2. 对已有旧页面内容进行复用或适度整理，减少重复实现。
3. 再统一修正 `statics/business_doc/router/routes.vue` 的路由映射，避免继续指向不存在文件。
4. 保留当前菜单地址不变，优先保证 `http://localhost:3002/#/component/data/x-table-easy/...` 可访问。

## 优先顺序

1. 补齐 `Header.Group / Row.Style / Virtual.Scroll / Row.Expand` 页面。
2. 修复 `routes.vue` 中对应目标路径。
3. 再继续推进排序、筛选、行展开等能力的示例与移植质量。
