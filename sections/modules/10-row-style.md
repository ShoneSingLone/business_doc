# 10. 行样式（row-style）

## 10.1 功能说明

1. 通过属性 `rowStyleOption` 设置行的样式
2. 通过属性 `stripe=true` 开启斑马纹
3. 通过属性 `hoverHighlight=true` 开启行 hover 高亮效果。默认开启
4. 通过属性 `clickHighlight=true` 开启行 click 高亮效果。默认开启

---

## 10.2 斑马纹

通过 `stripe` 属性开启斑马纹效果。

**配置示例**：
```vue
<template>
  <xTableEasy :row-style-option="rowStyleOption" :columns="columns" :table-data="tableData" />
</template>
<script>
export default {
  data() {
    return {
      rowStyleOption: {
        stripe: true
      },
      columns: [
        {
          field: "",
          key: "a",
          title: "",
          width: 50,
          align: "center",
          renderBodyCell: ({ row, column, rowIndex }, h) => {
            return ++rowIndex;
          }
        },
        { field: "name", key: "b", title: "Name", width: 200 },
        { field: "hobby", key: "c", title: "Hobby", width: 300 },
        { field: "address", key: "d", title: "Address" }
      ],
      tableData: [...]
    };
  }
};
</script>
```

---

## 10.3 行 hover 高亮

默认行 hover 高亮效果开启，可通过 `hoverHighlight` 配置。

**配置示例**：
```vue
<template>
  <xTableEasy :row-style-option="rowStyleOption" :columns="columns" :table-data="tableData" />
</template>
<script>
export default {
  data() {
    return {
      rowStyleOption: {
        hoverHighlight: true
      },
      columns: [...],
      tableData: [...]
    };
  }
};
</script>
```

---

## 10.4 行 click 高亮

默认行 click 高亮效果开启，需要设置 `row-key-field-name` 属性。

**配置示例**：
```vue
<template>
  <div>
    <button @click="setHighlightRow(1002)">选中第2行</button>
    <xTableEasy
      ref="tableRef"
      :row-style-option="rowStyleOption"
      :columns="columns"
      :table-data="tableData"
      row-key-field-name="rowKey" />
  </div>
</template>
<script>
export default {
  data() {
    return {
      rowStyleOption: {
        clickHighlight: true
      },
      columns: [...],
      tableData: [...]
    };
  },
  methods: {
    setHighlightRow(rowKey) {
      this.$refs.tableRef.setHighlightRow({ rowKey: rowKey });
    }
  }
};
</script>
```

---

## 10.5 API

### rowStyleOption

行样式配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| stripe | 是否开启斑马纹 | Boolean | `false` |
| hoverHighlight | 是否开启 hover 高亮 | Boolean | `true` |
| clickHighlight | 是否开启 click 高亮 | Boolean | `true` |

### 实例方法

| 方法名 | 说明 | 参数 |
|--------|------|------|
| setHighlightRow | 设置高亮行 | `{ rowKey: number }` |
| clearHighlightRow | 清除高亮行 | 无 |

---

[返回模块索引](../10-module-design.md)