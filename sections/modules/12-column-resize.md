# 12. 列宽调整（column-resize）

## 12.1 功能说明

通过 `resizable` 属性开启列宽拖拽调整功能。

---

## 12.2 基础用法

启用列宽调整功能。

**配置示例**：
```vue
<template>
  <xTableEasy :columns="columns" :table-data="tableData" />
</template>
<script>
export default {
  data() {
    return {
      columns: [
        { field: "name", title: "姓名", width: 120, resizable: true },
        { field: "age", title: "年龄", width: 80, resizable: true }
      ],
      tableData: [...]
    };
  }
};
</script>
```

---

## 12.3 禁用调整

通过 `resizable: false` 禁用某列的宽度调整。

---

## 12.4 API

### resizable

列宽调整配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| resizable | 是否可调整 | Boolean | `false` |
| minWidth | 最小宽度 | Number | - |
| maxWidth | 最大宽度 | Number | - |

---

[返回模块索引](../10-module-design.md)