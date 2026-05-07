# 12. 表头筛选（header-filter）

## 12.1 功能说明

1. 通过 `column` 对象的 `filter` 属性设置筛选功能
2. `filterList` 设置筛选条件。包含 `label`、`value`、`selected` 3 个属性
3. `isMultiple` 开启筛选项多选，默认为 false
4. `filterConfirm` 筛选确认函数
5. `filterReset` 筛选重置函数

---

## 12.2 单选筛选

通过 `filter` 属性配置单选筛选。

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
        {
          field: "name",
          key: "a",
          title: "Name",
          filter: {
            filterList: [
              { label: "全部", value: "", selected: true },
              { label: "John", value: "John" },
              { label: "Dickerson", value: "Dickerson" },
              { label: "Larsen", value: "Larsen" }
            ],
            filterConfirm: ({ value }) => {
              console.log('筛选值:', value);
            },
            filterReset: () => {
              console.log('筛选重置');
            }
          }
        },
        { field: "date", key: "b", title: "Date" },
        { field: "hobby", key: "c", title: "Hobby" },
        { field: "address", key: "d", title: "Address" }
      ],
      tableData: [...]
    };
  }
};
</script>
```

---

## 12.3 多选筛选

通过 `isMultiple` 属性开启多选筛选。

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
        {
          field: "hobby",
          key: "a",
          title: "Hobby",
          filter: {
            isMultiple: true,
            filterList: [
              { label: "coding", value: "coding", selected: true },
              { label: "reading", value: "reading" },
              { label: "swimming", value: "swimming" },
              { label: "running", value: "running" }
            ],
            filterConfirm: ({ value }) => {
              console.log('选中的值:', value);
            }
          }
        },
        { field: "name", key: "b", title: "Name" },
        { field: "date", key: "c", title: "Date" }
      ],
      tableData: [...]
    };
  }
};
</script>
```

---

## 12.4 混合筛选

同时使用单选和多选筛选。

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
        {
          field: "name",
          key: "a",
          title: "Name",
          filter: {
            filterList: [
              { label: "全部", value: "", selected: true },
              { label: "John", value: "John" },
              { label: "Dickerson", value: "Dickerson" }
            ],
            filterConfirm: ({ value }) => {
              console.log('姓名筛选:', value);
            }
          }
        },
        {
          field: "hobby",
          key: "b",
          title: "Hobby",
          filter: {
            isMultiple: true,
            filterList: [
              { label: "coding", value: "coding" },
              { label: "reading", value: "reading" }
            ],
            filterConfirm: ({ value }) => {
              console.log('爱好筛选:', value);
            }
          }
        },
        { field: "date", key: "c", title: "Date" }
      ],
      tableData: [...]
    };
  }
};
</script>
```

---

## 12.5 自定义图标

自定义筛选图标。

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
        {
          field: "name",
          key: "a",
          title: "Name",
          filter: {
            filterList: [
              { label: "全部", value: "", selected: true },
              { label: "John", value: "John" }
            ],
            icon: '🔍'
          }
        },
        { field: "date", key: "b", title: "Date" }
      ],
      tableData: [...]
    };
  }
};
</script>
```

---

## 12.6 API

### filter 配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| filterList | 筛选选项列表 | Array | [] |
| isMultiple | 是否多选 | Boolean | `false` |
| filterConfirm | 筛选确认回调 | Function | - |
| filterReset | 筛选重置回调 | Function | - |
| icon | 自定义图标 | String | - |

### filterList 配置项

| 属性 | 说明 | 类型 |
|------|------|------|
| label | 显示文本 | String |
| value | 值 | String/Number |
| selected | 是否选中 | Boolean |

---

[返回模块索引](../10-module-design.md)