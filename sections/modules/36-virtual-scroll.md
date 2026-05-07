# 36. 虚拟滚动（virtual-scroll）

## 36.1 功能说明

**配置要点**：
1. 通过 `virtual-scroll-option` 属性开启虚拟滚动
2. 建议当一次性需要展示 **1000 以上** 数据时使用，可以支撑 **20 万以上**数据
3. `max-height` 为必传属性，设置虚拟滚动区域的最大高度
4. `row-key-field-name` 为必传属性，对应行数据的唯一标识字段名
5. 开启虚拟滚动功能后，其他功能依然可用

---

## 36.2 基础用法

开启虚拟滚动功能。

**配置示例**：
```vue
<template>
  <xTableEasy
    :max-height="500"
    :virtual-scroll-option="virtualScrollOption"
    :columns="columns"
    :table-data="tableData"
    row-key-field-name="rowKey" />
</template>
<script>
export default {
  data() {
    return {
      virtualScrollOption: {
        enable: true
      },
      columns: [
        { field: "index", key: "a", title: "#", width: 100, align: "left" },
        { field: "name", key: "b", title: "Name", width: 200, align: "left" },
        { field: "hobby", key: "c", title: "Hobby", width: 300, align: "left" },
        { field: "address", key: "d", title: "Address", align: "left" }
      ],
      tableData: []
    };
  },
  methods: {
    initData() {
      let data = [];
      for (let i = 0; i < 10000; i++) {
        data.push({
          rowKey: i,
          index: i,
          name: `name${i}`,
          hobby: `hobby${i}`,
          address: `address${i}`
        });
      }
      this.tableData = data;
    }
  },
  created() {
    this.initData();
  }
};
</script>
```

---

## 36.3 动态启用

根据数据量动态启用虚拟滚动。

**配置示例**：
```vue
<template>
  <xTableEasy
    :max-height="500"
    :virtual-scroll-option="virtualScrollOption"
    :columns="columns"
    :table-data="tableData"
    row-key-field-name="rowKey" />
</template>
<script>
export default {
  data() {
    return {
      tableData: [],
      columns: [...],
      virtualScrollOption: {
        enable: false
      }
    };
  },
  watch: {
    tableData(newVal) {
      this.virtualScrollOption.enable = newVal.length > 1000;
    }
  }
};
</script>
```

---

## 36.4 结合行展开

虚拟滚动模式下使用行展开功能。

**配置示例**：
```vue
<template>
  <xTableEasy
    :max-height="500"
    :virtual-scroll-option="virtualScrollOption"
    :columns="columns"
    :table-data="tableData"
    row-key-field-name="rowKey"
    :expand-option="expandOption" />
</template>
<script>
export default {
  data() {
    return {
      virtualScrollOption: {
        enable: true
      },
      expandOption: {
        enable: true,
        expandRows: [0, 1]
      },
      columns: [
        { field: "name", title: "Name" },
        { field: "age", title: "Age" }
      ],
      tableData: [...]
    };
  }
};
</script>
```

---

## 36.5 结合行多选

虚拟滚动模式下使用多选功能。

**配置示例**：
```vue
<template>
  <xTableEasy
    :max-height="500"
    :virtual-scroll-option="virtualScrollOption"
    :columns="columns"
    :table-data="tableData"
    row-key-field-name="rowKey"
    :checkbox-option="checkboxOption" />
</template>
<script>
export default {
  data() {
    return {
      virtualScrollOption: {
        enable: true
      },
      checkboxOption: {
        enable: true
      },
      columns: [...],
      tableData: [...]
    };
  }
};
</script>
```

---

## 36.6 结合行单选

虚拟滚动模式下使用单选功能。

**配置示例**：
```vue
<template>
  <xTableEasy
    :max-height="500"
    :virtual-scroll-option="virtualScrollOption"
    :columns="columns"
    :table-data="tableData"
    row-key-field-name="rowKey"
    :radio-option="radioOption" />
</template>
<script>
export default {
  data() {
    return {
      virtualScrollOption: {
        enable: true
      },
      radioOption: {
        enable: true
      },
      columns: [...],
      tableData: [...]
    };
  }
};
</script>
```

---

## 36.7 结合列固定

虚拟滚动模式下使用列固定功能。

**配置示例**：
```vue
<template>
  <xTableEasy
    :max-height="500"
    :scroll-width="1200"
    :virtual-scroll-option="virtualScrollOption"
    :columns="columns"
    :table-data="tableData"
    row-key-field-name="rowKey" />
</template>
<script>
export default {
  data() {
    return {
      virtualScrollOption: {
        enable: true
      },
      columns: [
        { field: "name", title: "Name", fixed: "left", width: 150 },
        { field: "col1", title: "Column 1" },
        { field: "col2", title: "Column 2" },
        { field: "col3", title: "Column 3", fixed: "right", width: 150 }
      ],
      tableData: [...]
    };
  }
};
</script>
```

---

## 36.8 结合懒加载

虚拟滚动模式下实现懒加载。

**配置示例**：
```vue
<template>
  <xTableEasy
    :max-height="500"
    :virtual-scroll-option="virtualScrollOption"
    :columns="columns"
    :table-data="tableData"
    row-key-field-name="rowKey" />
</template>
<script>
export default {
  data() {
    return {
      virtualScrollOption: {
        enable: true,
        scrolling: ({ startRowIndex }) => {
          this.loadMoreData(startRowIndex);
        }
      },
      columns: [...],
      tableData: [],
      page: 1
    };
  },
  methods: {
    loadMoreData(startRowIndex) {
      if (startRowIndex > this.tableData.length - 100 && !this.loading) {
        this.loading = true;
        this.page++;
        this.fetchData(this.page).then(data => {
          this.tableData = [...this.tableData, ...data];
          this.loading = false;
        });
      }
    },
    fetchData(page) {
      return new Promise(resolve => {
        setTimeout(() => {
          let data = [];
          for (let i = 0; i < 200; i++) {
            data.push({
              rowKey: (page - 1) * 200 + i,
              name: `name${(page - 1) * 200 + i}`
            });
          }
          resolve(data);
        }, 500);
      });
    }
  },
  created() {
    this.fetchData(1).then(data => {
      this.tableData = data;
    });
  }
};
</script>
```

---

## 36.9 API

### virtual-scroll-option

虚拟滚动配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| enable | 是否启用虚拟滚动 | Boolean | `false` |
| estimatedRowHeight | 预估行高（用于计算可视区域） | Number | `40` |
| bufferSize | 缓冲区域大小（行数） | Number | `5` |
| scrolling | 滚动回调函数 | Function | - |

### 必传属性

| 属性 | 说明 | 类型 |
|------|------|------|
| max-height | 虚拟滚动区域最大高度 | Number/String |
| row-key-field-name | 行数据唯一标识字段名 | String |

### scrolling 参数

| 参数 | 说明 | 类型 |
|------|------|------|
| startRowIndex | 当前可视区域起始行索引 | Number |
| endRowIndex | 当前可视区域结束行索引 | Number |

---

[返回模块索引](../10-module-design.md)