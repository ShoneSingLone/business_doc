# 32. 行样式（row-style）

## 32.1 功能说明

通过 `rowStyle` 属性自定义行样式。

---

## 32.2 斑马纹效果

通过 `rowStyle` 函数实现斑马纹效果。

**配置示例**：

```vue
<template>
	<xTableEasy :columns="columns" :table-data="tableData" :row-style="rowStyle" />
</template>
<script>
export default {
  data() {
    return {
      columns: [...],
      tableData: [...]
    };
  },
  methods: {
    rowStyle({ rowIndex }) {
      return rowIndex % 2 === 0
        ? { backgroundColor: '#f8f9fa' }
        : { backgroundColor: '#ffffff' };
    }
  }
};
</script>
```

---

## 32.3 鼠标悬停高亮

鼠标悬停时高亮行。

---

## 32.4 点击高亮

点击行时高亮。

---

## 32.5 API

### rowStyle

行样式函数

| 参数     | 说明       | 类型   |
| -------- | ---------- | ------ |
| row      | 当前行数据 | Object |
| rowIndex | 行索引     | Number |

---

[返回模块索引](../10-module-design.md)
