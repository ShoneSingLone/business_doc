# 21. 表头分组（header-grouping）

## 21.1 功能说明

通过 `columns` 配置实现表头分组功能。

---

## 21.2 基础用法

配置多级表头分组。

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
        { field: "name", title: "姓名", width: 120 },
        {
          title: "成绩",
          children: [
            { field: "math", title: "数学", width: 100 },
            { field: "chinese", title: "语文", width: 100 }
          ]
        }
      ],
      tableData: [...]
    };
  }
};
</script>
```

---

## 21.3 分组表头与固定列

结合列固定功能使用表头分组。

---

## 21.4 API

### columns

表头分组配置

| 属性     | 说明     | 类型   |
| -------- | -------- | ------ |
| title    | 分组标题 | String |
| children | 子列配置 | Array  |

---

[返回模块索引](../10-module-design.md)
