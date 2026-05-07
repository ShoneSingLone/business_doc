# 13. 表头分组（header-grouping）

## 13.1 功能说明

1. 通过设置 `columns` 的 `children` 属性，即可实现表头分组功能
2. `children` 属性指定需要合并的列
3. 表头分组功能必须指定列的 `key` 属性！！
4. 当需要固定分组的列时，只需要将 fixed 属性设置在顶层配置中即可

---

## 13.2 基础用法

通过 `children` 属性实现表头分组。

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
          title: "基本信息",
          children: [
            { field: "name", key: "a", title: "Name" },
            { field: "date", key: "b", title: "Date" }
          ]
        },
        {
          title: "详细信息",
          children: [
            { field: "hobby", key: "c", title: "Hobby" },
            { field: "address", key: "d", title: "Address" }
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

## 13.3 多层分组

支持多层表头分组嵌套。

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
          title: "个人信息",
          children: [
            {
              title: "基本资料",
              children: [
                { field: "name", key: "a", title: "Name" },
                { field: "age", key: "b", title: "Age" }
              ]
            },
            {
              title: "联系方式",
              children: [
                { field: "phone", key: "c", title: "Phone" },
                { field: "email", key: "d", title: "Email" }
              ]
            }
          ]
        },
        {
          title: "工作信息",
          children: [
            { field: "company", key: "e", title: "Company" },
            { field: "position", key: "f", title: "Position" }
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

## 13.4 分组列固定

在分组表头中使用列固定功能。

**配置示例**：
```vue
<template>
  <xTableEasy
    style="width:900px"
    :scroll-width="1200"
    border-y
    :columns="columns"
    :table-data="tableData" />
</template>
<script>
export default {
  data() {
    return {
      columns: [
        {
          title: "固定列",
          fixed: "left",
          children: [
            { field: "name", key: "a", title: "Name", width: 150 },
            { field: "date", key: "b", title: "Date", width: 150 }
          ]
        },
        {
          title: "中间列",
          children: [
            { field: "col1", key: "c", title: "Col1", width: 150 },
            { field: "col2", key: "d", title: "Col2", width: 150 },
            { field: "col3", key: "e", title: "Col3", width: 150 }
          ]
        },
        {
          title: "右侧固定",
          fixed: "right",
          children: [
            { field: "action", key: "f", title: "Action", width: 150 }
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

## 13.5 结合其他功能

表头分组可以与其他功能结合使用。

**配置示例**：
```vue
<template>
  <xTableEasy
    :columns="columns"
    :table-data="tableData"
    :edit-option="editOption" />
</template>
<script>
export default {
  data() {
    return {
      editOption: { trigger: 'click' },
      columns: [
        {
          title: "可编辑列",
          children: [
            { field: "name", key: "a", title: "Name", edit: true },
            { field: "age", key: "b", title: "Age", edit: true }
          ]
        },
        {
          title: "不可编辑",
          children: [
            { field: "hobby", key: "c", title: "Hobby" },
            { field: "address", key: "d", title: "Address" }
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

## 13.6 API

### 列配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| title | 分组标题 | String | - |
| key | 列唯一标识 | String | - |
| children | 子列配置 | Array | [] |
| fixed | 是否固定 | String | - |
| width | 宽度 | Number/String | - |

---

[返回模块索引](../10-module-design.md)