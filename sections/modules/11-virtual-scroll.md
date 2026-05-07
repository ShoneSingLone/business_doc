# 11. 虚拟滚动（virtual-scroll）

## 11.1 功能说明

1. 属性 `virtualScrollOption` 开启虚拟滚动。建议当一次性需要展示 **1000 以上** 数据时使用，可以支撑 **20 万以上**数据
2. 属性 `maxHeight` 设置虚拟滚动区域的最大高度。`maxHeight` 为必传属性
3. `rowKeyFieldName` 为必传属性。`rowKeyFieldName` 属性对应行数据的列名
4. **开启虚拟滚动功能后，其他功能依然可用**

---

## 11.2 基础功能

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
        { field: "index", key: "a", title: "#", width: 100 },
        { field: "name", key: "b", title: "Name", width: 200 },
        { field: "hobby", key: "c", title: "Hobby", width: 300 },
        { field: "address", key: "d", title: "Address" }
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

## 11.3 动态启用

支持动态开启/关闭虚拟滚动。

**配置示例**：
```vue
<template>
  <div>
    <button @click="toggleVirtualScroll">
      {{ virtualScrollOption.enable ? '关闭' : '开启' }}虚拟滚动
    </button>
    <xTableEasy
      :max-height="500"
      :virtual-scroll-option="virtualScrollOption"
      :columns="columns"
      :table-data="tableData"
      row-key-field-name="rowKey" />
  </div>
</template>
<script>
export default {
  data() {
    return {
      virtualScrollOption: {
        enable: false
      },
      columns: [...],
      tableData: [...]
    };
  },
  methods: {
    toggleVirtualScroll() {
      this.virtualScrollOption.enable = !this.virtualScrollOption.enable;
    }
  }
};
</script>
```

---

## 11.4 滚动回调

通过 `scrolling` 回调获取滚动信息。

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
      startRowIndex: 0,
      virtualScrollOption: {
        enable: true,
        scrolling: this.onScrolling
      },
      columns: [
        { 
          field: "index", 
          key: "a", 
          title: "#", 
          width: 100,
          renderBodyCell: ({ row, rowIndex }, h) => {
            return rowIndex + this.startRowIndex + 1;
          }
        },
        { field: "name", key: "b", title: "Name", width: 200 }
      ],
      tableData: []
    };
  },
  methods: {
    onScrolling({ startRowIndex }) {
      this.startRowIndex = startRowIndex;
    },
    initData() {
      let data = [];
      for (let i = 0; i < 10000; i++) {
        data.push({ rowKey: i, name: `name${i}` });
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

## 11.5 结合列固定

在虚拟滚动中使用列固定功能。

**配置示例**：
```vue
<template>
  <xTableEasy
    style="width:900px"
    :scroll-width="1200"
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
        { field: "col1", key: "a", title: "Col1", fixed: "left", width: 100 },
        { field: "col2", key: "b", title: "Col2", width: 200 },
        { field: "col3", key: "c", title: "Col3", width: 200 },
        { field: "col4", key: "d", title: "Col4", width: 200 },
        { field: "col5", key: "e", title: "Col5", fixed: "right", width: 100 }
      ],
      tableData: [...]
    };
  }
};
</script>
```

---

## 11.6 结合懒加载

虚拟滚动结合懒加载使用。

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
        scrolling: this.onScrolling
      },
      columns: [...],
      tableData: []
    };
  },
  methods: {
    onScrolling({ startRowIndex, endRowIndex }) {
      // 当滚动到接近底部时加载更多数据
      if (endRowIndex >= this.tableData.length - 100) {
        this.loadMoreData();
      }
    },
    loadMoreData() {
      // 模拟异步加载
      setTimeout(() => {
        const start = this.tableData.length;
        for (let i = start; i < start + 100; i++) {
          this.tableData.push({
            rowKey: i,
            name: `name${i}`,
            hobby: `hobby${i}`,
            address: `address${i}`
          });
        }
      }, 500);
    },
    initData() {
      for (let i = 0; i < 100; i++) {
        this.tableData.push({
          rowKey: i,
          name: `name${i}`,
          hobby: `hobby${i}`,
          address: `address${i}`
        });
      }
    }
  },
  created() {
    this.initData();
  }
};
</script>
```

---

## 11.7 API

### virtualScrollOption

虚拟滚动配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| enable | 是否开启虚拟滚动 | Boolean | `false` |
| scrolling | 滚动时的回调函数 | Function | - |

**scrolling 回调参数**：
| 参数 | 说明 | 类型 |
|------|------|------|
| startRowIndex | 当前可视区域起始行索引 | Number |
| endRowIndex | 当前可视区域结束行索引 | Number |

### 表格属性

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| max-height | 虚拟滚动区域最大高度 | Number/String | - |
| row-key-field-name | 行唯一标识字段名 | String | - |

---

[返回模块索引](../10-module-design.md)