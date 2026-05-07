# 2. 单元格自动填充（cell-autofill）

## 2.1 功能说明

当存在需要重复拷贝的数据，你可以像 excel 那样进行单元格内容的自动填充。

**配置要点**：
1. 通过 `cell-autofill-option` 属性开启自动填充功能
2. 支持配置填充方向（水平、垂直、双向）
3. 支持填充前后的回调函数

---

## 2.2 基础用法

启用自动填充功能。

**配置示例**：
```vue
<template>
  <xTableEasy
    :columns="columns"
    :table-data="tableData"
    rowKeyFieldName="rowKey"
    :cell-autofill-option="cellAutofillOption" />
</template>
<script>
export default {
  data() {
    return {
      cellAutofillOption: {
        directionX: true,
        directionY: true,
        beforeAutofill: ({ direction, sourceSelectionRangeIndexes, targetSelectionRangeIndexes, sourceSelectionData, targetSelectionData }) => {
          console.log("填充前", direction);
        },
        afterAutofill: ({ direction, sourceSelectionRangeIndexes, targetSelectionRangeIndexes, sourceSelectionData, targetSelectionData }) => {
          console.log("填充后", direction);
        }
      },
      columns: [...],
      tableData: [...]
    };
  }
};
</script>
```

---

## 2.3 功能特点

- 支持数字序列填充（1, 2, 3...）
- 支持日期序列填充
- 支持复制填充（相同内容）
- 自动识别序列模式

---

## 2.4 快捷键

暂无

---

## 2.5 自动填充方向

可以设置在某一个方向开启自动填充。

**配置示例**：
```vue
<template>
  <xTableEasy
    :columns="columns"
    :table-data="tableData"
    :cell-autofill-option="cellAutofillOption"
    rowKeyFieldName="rowKey" />
</template>
<script>
export default {
  data() {
    return {
      cellAutofillOption: {
        directionX: true,   // 水平方向填充
        directionY: true    // 垂直方向填充
      },
      columns: [...],
      tableData: [...]
    };
  }
};
</script>
```

**方向配置说明**：
| 配置项 | 说明 |
|--------|------|
| directionX | 启用水平方向自动填充 |
| directionY | 启用垂直方向自动填充 |

---

## 2.6 API

### cell-autofill-option

自动填充配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| directionX | 是否启用水平方向填充 | Boolean | `true` |
| directionY | 是否启用垂直方向填充 | Boolean | `true` |
| beforeAutofill | 填充前回调函数 | Function | - |
| afterAutofill | 填充后回调函数 | Function | - |

**beforeAutofill / afterAutofill 参数**：
| 参数 | 说明 | 类型 |
|------|------|------|
| direction | 填充方向 | String |
| sourceSelectionRangeIndexes | 源选区索引 | Object |
| targetSelectionRangeIndexes | 目标选区索引 | Object |
| sourceSelectionData | 源选区数据 | Array |
| targetSelectionData | 目标选区数据 | Array |

---

[返回模块索引](../10-module-design.md)