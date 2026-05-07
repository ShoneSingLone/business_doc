# 5. 单元格省略（cell-ellipsis）

## 5.1 功能说明

**配置要点**：
1. 通过 `ellipsis` 属性开启省略功能
2. 单行省略：内容超出宽度时显示省略号
3. 多行省略：内容超出指定行数时显示省略号

---

## 5.2 单行省略

默认单行省略，鼠标悬停显示完整内容。

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
        { field: "name", title: "姓名", width: 100 },
        { field: "address", title: "地址", width: 200, ellipsis: true }
      ],
      tableData: [...]
    };
  }
};
</script>
```

---

## 5.3 多行省略

设置 `ellipsisLine` 属性指定显示行数。

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
        { field: "desc", title: "描述", width: 300, ellipsis: true, ellipsisLine: 3 }
      ],
      tableData: [...]
    };
  }
};
</script>
```

---

## 5.4 API

### ellipsis 相关配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| ellipsis | 是否启用省略 | Boolean | `false` |
| ellipsisLine | 多行省略行数 | Number | `1` |

---

[返回模块索引](../10-module-design.md)