# 5. 单元格省略（cell-ellipsis）

## 5.1 功能说明

1. 通过 `column` 的 `ellipsis` 属性设置超出显示省略
2. 通过 `lineClamp` 设置内容超出多少行开始出现省略

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

**特点**：

- 默认单行省略
- 鼠标悬停显示完整内容（通过 title 属性）
- 简单实用

---

## 5.3 多行省略

通过 `lineClamp` 设置超过多少行省略。

> 此功能目前只支持 [-webkit-line-clamp 属性](https://developer.mozilla.org/zh-CN/docs/Web/CSS/-webkit-line-clamp)
> 的浏览器

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
        { field: "name", title: "姓名", width: "15%" },
        { field: "address", title: "地址", width: "40%", ellipsis: {
          showTitle: true,
          lineClamp: 2
        }}
      ],
      tableData: [...]
    };
  }
};
</script>
```

**多行省略配置**：| 属性 | 说明 | 类型 | 默认值 | |------|------|------|--------| | showTitle | 是否显示 title 提示 |
Boolean | `true` | | lineClamp | 省略行数 | Number | `1` |

---

## 5.4 基础省略配置

简单模式下，可以直接设置 `ellipsis: true`。

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
        { field: "name", title: "姓名" },
        { field: "desc", title: "描述", ellipsis: true }
      ],
      tableData: [...]
    };
  }
};
</script>
```

---

## 5.5 API

### ellipsis 相关配置

| 属性     | 说明                   | 类型           | 默认值  |
| -------- | ---------------------- | -------------- | ------- |
| ellipsis | 是否启用省略或省略配置 | Boolean/Object | `false` |

**ellipsis 为对象时的配置**：| 属性 | 说明 | 类型 | 默认值 | |------|------|------|--------| | showTitle
| 是否显示 title 提示 | Boolean | `true` | | lineClamp | 省略行数 | Number | `1` |

---

[返回模块索引](../10-module-design.md)
