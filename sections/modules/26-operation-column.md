# 26. 操作列（operation-column）

## 26.1 功能说明

通过 `render` 属性配置操作列，添加操作按钮。

---

## 26.2 基础用法

添加操作列。

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
          title: "操作", 
          width: 200,
          render: (row) => {
            return `
              <button onclick="edit(${row.id})">编辑</button>
              <button onclick="del(${row.id})">删除</button>
            `;
          }
        }
      ],
      tableData: [...]
    };
  },
  methods: {
    edit(id) {
      console.log('编辑:', id);
    },
    del(id) {
      console.log('删除:', id);
    }
  }
};
</script>
```

---

## 26.3 API

### render

操作列渲染函数

| 参数 | 说明 | 类型 |
|------|------|------|
| row | 当前行数据 | Object |
| column | 当前列配置 | Object |
| rowIndex | 行索引 | Number |

---

[返回模块索引](../10-module-design.md)