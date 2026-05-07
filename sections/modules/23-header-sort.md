# 23. 表头排序（header-sort）

## 23.1 功能说明

**配置要点**：
1. 通过 `sortBy` 属性设置需要排序的列
2. 通过 `sort-option` 对象设置更多排序功能
3. 排序功能需要配合 `sortChange` 回调函数实现

**sortBy 属性说明**：
- `sortBy="asc"`：默认当前列升序
- `sortBy="desc"`：默认当前列降序
- `sortBy=""`：允许排序但无排序规则

---

## 23.2 单条件排序

默认只支持单选排序。

**配置示例**：
```vue
<template>
  <xTableEasy
    :columns="columns"
    :table-data="tableData"
    :sort-option="sortOption"
    border-y />
</template>
<script>
export default {
  data() {
    return {
      sortOption: {
        sortChange: params => {
          console.log("sortChange::", params);
          this.sortChange(params);
        }
      },
      columns: [
        { field: "name", key: "a", title: "Name", align: "left" },
        {
          field: "age",
          key: "b",
          title: "Age",
          align: "center",
          sortBy: ""
        },
        {
          field: "weight",
          key: "c",
          title: "Weight(kg)",
          align: "center",
          sortBy: "asc"
        },
        { field: "hobby", key: "d", title: "Hobby", align: "center" },
        { field: "address", key: "e", title: "Address", align: "left" }
      ],
      tableData: [
        { name: "John", age: 25, weight: 66, hobby: "coding", address: "Shanghai" },
        { name: "Dickerson", age: 20, weight: 70, hobby: "coding", address: "Beijing" },
        { name: "Larsen", age: 18, weight: 65, hobby: "coding", address: "Chongqing" },
        { name: "Geneva", age: 17, weight: 80, hobby: "coding", address: "Xiamen" },
        { name: "Jami", age: 26, weight: 72, hobby: "coding", address: "Shenzhen" }
      ]
    };
  },
  methods: {
    sortChange(params) {
      this.tableData.sort((a, b) => {
        if (params.age) {
          if (params.age === "asc") {
            return a.age - b.age;
          } else if (params.age === "desc") {
            return b.age - a.age;
          } else {
            return 0;
          }
        } else if (params.weight) {
          if (params.weight === "asc") {
            return a.weight - b.weight;
          } else if (params.weight === "desc") {
            return b.weight - a.weight;
          } else {
            return 0;
          }
        }
      });
    }
  }
};
</script>
```

---

## 23.3 多条件排序

通过 `multipleSort=true` 开启多字段排序。

**配置示例**：
```vue
<template>
  <xTableEasy
    :columns="columns"
    :table-data="tableData"
    :sort-option="sortOption"
    border-y />
</template>
<script>
export default {
  data() {
    return {
      sortOption: {
        multipleSort: true,
        sortChange: params => {
          console.log("sortChange::", params);
          this.sortChange(params);
        }
      },
      columns: [
        { field: "name", key: "a", title: "Name", align: "left" },
        { field: "age", key: "b", title: "Age", align: "center", sortBy: "" },
        { field: "weight", key: "c", title: "Weight(kg)", align: "center", sortBy: "asc" },
        { field: "hobby", key: "d", title: "Hobby", align: "center" },
        { field: "address", key: "e", title: "Address", align: "left" }
      ],
      tableData: [...]
    };
  },
  methods: {
    sortChange(params) {
      let data = this.tableData.slice(0);
      data.sort((a, b) => {
        if (params.age) {
          return params.age === "asc" ? a.age - b.age : b.age - a.age;
        }
        return 0;
      });
      data.sort((a, b) => {
        if (params.weight) {
          return params.weight === "asc" ? a.weight - b.weight : b.weight - a.weight;
        }
        return 0;
      });
      this.tableData = data;
    }
  }
};
</script>
```

**注意**：排序字段的优先级需要自己指定，具体逻辑自行实现（一般由后端服务返回）。

---

## 23.4 始终排序

设置 `sortAlways` 使排序始终生效。

**配置示例**：
```vue
<template>
  <xTableEasy
    :columns="columns"
    :table-data="tableData"
    :sort-option="{ sortAlways: true }" />
</template>
<script>
export default {
  data() {
    return {
      columns: [
        { field: "name", title: "姓名" },
        { field: "age", title: "年龄", sortBy: "asc" }
      ],
      tableData: [...]
    };
  }
};
</script>
```

---

## 23.5 API

### sort-option

排序配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| multipleSort | 是否支持多条件排序 | Boolean | `false` |
| sortAlways | 是否始终排序 | Boolean | `false` |
| sortChange | 排序状态改变回调 | Function | - |

### 列配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| sortBy | 排序类型 | String | - |

**sortBy 值说明**：
| 值 | 说明 |
|----|------|
| `asc` | 默认升序 |
| `desc` | 默认降序 |
| `""` | 允许排序但无默认排序规则 |

### sortChange 参数

| 参数 | 说明 | 类型 |
|------|------|------|
| fieldName | 排序字段名 | String |
| sortType | 排序类型（asc/desc） | String |

---

[返回模块索引](../10-module-design.md)