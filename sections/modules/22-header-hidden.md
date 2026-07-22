# 22. 表头隐藏（header-hidden）

## 22.1 功能说明

通过 `show-header` 属性控制表头的显示和隐藏。

---

## 22.2 基础用法

隐藏表头。

**配置示例**：

```vue
<template>
	<xTableEasy :columns="columns" :table-data="tableData" :show-header="false" />
</template>
<script>
export default {
  data() {
    return {
      columns: [...],
      tableData: [...]
    };
  }
};
</script>
```

---

## 22.3 API

### show-header

表头显示配置

| 属性        | 说明         | 类型    | 默认值 |
| ----------- | ------------ | ------- | ------ |
| show-header | 是否显示表头 | Boolean | `true` |

---

[返回模块索引](../10-module-design.md)
