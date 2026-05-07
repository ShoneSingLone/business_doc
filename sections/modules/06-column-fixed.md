# 6. 列固定（column-fixed）

## 6.1 功能说明

1. 属性 `scroll-width` 为滚动区域的宽度
2. 当外层容器宽度小于 `scroll-width` 值时，将会出现横向滚动条；当外层容器宽度大于 `scroll-width` 值时，将会跟随容器自适应；当 `scroll-width=0` 时，滚动条将根据列宽度决定
3. 列宽可以不设置、或者设置为百分比、或者为像素值（px）
4. 设置了 `scroll-width` 属性，列宽单位**强烈建议保持一致！**

---

## 6.2 左列固定

通过 `fixed: "left"` 设置需要固定的左列。

**配置示例**：
```vue
<template>
  <xTableEasy style="width:900px" :scroll-width="1200" border-y :columns="columns" :table-data="tableData" />
</template>
<script>
export default {
  data() {
    return {
      columns: [
        { field: "col1", key: "a", title: "Title1", fixed: "left" },
        { field: "col2", key: "b", title: "Title2", fixed: "left" },
        { field: "col3", key: "c", title: "Title3" },
        { field: "col4", key: "d", title: "Title4" },
        { field: "col5", key: "e", title: "Title5" },
        { field: "col6", key: "f", title: "Title6" },
        { field: "col7", key: "g", title: "Title7" },
        { field: "col8", key: "h", title: "Title8" },
        { field: "col9", key: "i", title: "Title9" },
        { field: "col10", key: "j", title: "Title10" }
      ],
      tableData: [...]
    };
  }
};
</script>
```

---

## 6.3 右列固定

通过 `fixed: "right"` 设置需要固定的右列。

**配置示例**：
```vue
<template>
  <xTableEasy style="width:900px" :scroll-width="1200" border-y :columns="columns" :table-data="tableData" />
</template>
<script>
export default {
  data() {
    return {
      columns: [
        { field: "col1", key: "a", title: "Title1" },
        { field: "col2", key: "b", title: "Title2" },
        { field: "col3", key: "c", title: "Title3" },
        { field: "col4", key: "d", title: "Title4" },
        { field: "col5", key: "e", title: "Title5" },
        { field: "col6", key: "f", title: "Title6" },
        { field: "col7", key: "g", title: "Title7" },
        { field: "col8", key: "h", title: "Title8" },
        { field: "col9", key: "i", title: "Title9", fixed: "right" },
        { field: "col10", key: "j", title: "Title10", fixed: "right" }
      ],
      tableData: [...]
    };
  }
};
</script>
```

---

## 6.4 左右列同时固定

同时设置左列和右列固定。

**配置示例**：
```vue
<template>
  <xTableEasy style="width:900px" :scroll-width="1200" border-y :columns="columns" :table-data="tableData" />
</template>
<script>
export default {
  data() {
    return {
      columns: [
        { field: "col1", key: "a", title: "Title1", fixed: "left" },
        { field: "col2", key: "b", title: "Title2", fixed: "left" },
        { field: "col3", key: "c", title: "Title3" },
        { field: "col4", key: "d", title: "Title4" },
        { field: "col5", key: "e", title: "Title5" },
        { field: "col6", key: "f", title: "Title6" },
        { field: "col7", key: "g", title: "Title7" },
        { field: "col8", key: "h", title: "Title8" },
        { field: "col9", key: "i", title: "Title9", fixed: "right" },
        { field: "col10", key: "j", title: "Title10", fixed: "right" }
      ],
      tableData: [...]
    };
  }
};
</script>
```

---

## 6.5 API

### 表格属性

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| scroll-width | 滚动区域宽度 | Number | `0` |

### 列配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| fixed | 是否固定列 | String | `-` |

**fixed 可选值**：
| 值 | 说明 |
|----|------|
| `left` | 左列固定 |
| `right` | 右列固定 |

---

[返回模块索引](../10-module-design.md)