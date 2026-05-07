# 8. 事件自定义（event-custom）

## 8.1 功能说明

1. `eventCustomOption` 配置自定义事件
2. 支持 body、header、footer 行和列事件自定义
3. 支持以下事件自定义：
   - click
   - dblclick
   - contextmenu
   - mouseenter
   - mouseleave
   - mousemove
   - mouseover
   - mousedown
   - mouseup

---

## 8.2 body 行事件自定义

通过 `bodyRowEvents` 配置表体行的自定义事件。

**配置示例**：
```vue
<template>
  <xTableEasy
    :columns="columns"
    :table-data="tableData"
    :event-custom-option="eventCustomOption" />
</template>
<script>
export default {
  data() {
    return {
      eventCustomOption: {
        bodyRowEvents: ({ row, rowIndex }) => {
          return {
            click: (event) => {
              console.log('Row clicked:', rowIndex);
            },
            dblclick: (event) => {
              console.log('Row double clicked:', rowIndex);
            },
            contextmenu: (event) => {
              console.log('Right click on row:', rowIndex);
              event.preventDefault();
            },
            mouseenter: (event) => {
              console.log('Mouse enter row:', rowIndex);
            },
            mouseleave: (event) => {
              console.log('Mouse leave row:', rowIndex);
            }
          };
        }
      },
      columns: [...],
      tableData: [...]
    };
  }
};
</script>
```

**bodyRowEvents 参数**：
| 参数 | 说明 | 类型 |
|------|------|------|
| row | 当前行数据 | Object |
| rowIndex | 行索引 | Number |

---

## 8.3 body 单元格事件自定义

通过 `bodyCellEvents` 配置表体单元格的自定义事件。

**配置示例**：
```vue
<template>
  <xTableEasy
    :columns="columns"
    :table-data="tableData"
    :event-custom-option="eventCustomOption" />
</template>
<script>
export default {
  data() {
    return {
      eventCustomOption: {
        bodyCellEvents: ({ row, column, rowIndex, columnIndex }) => {
          return {
            click: (event) => {
              console.log(`Cell clicked: row=${rowIndex}, col=${columnIndex}`);
            },
            dblclick: (event) => {
              console.log(`Cell double clicked: ${column.field}`);
            }
          };
        }
      },
      columns: [...],
      tableData: [...]
    };
  }
};
</script>
```

**bodyCellEvents 参数**：
| 参数 | 说明 | 类型 |
|------|------|------|
| row | 当前行数据 | Object |
| column | 当前列配置 | Object |
| rowIndex | 行索引 | Number |
| columnIndex | 列索引 | Number |

---

## 8.4 header 行事件自定义

通过 `headerRowEvents` 配置表头行的自定义事件。

**配置示例**：
```vue
<template>
  <xTableEasy
    :columns="columns"
    :table-data="tableData"
    :event-custom-option="eventCustomOption" />
</template>
<script>
export default {
  data() {
    return {
      eventCustomOption: {
        headerRowEvents: ({ rowIndex }) => {
          return {
            click: (event) => {
              console.log('Header row clicked:', rowIndex);
            },
            contextmenu: (event) => {
              console.log('Right click on header row:', rowIndex);
            }
          };
        }
      },
      columns: [...],
      tableData: [...]
    };
  }
};
</script>
```

**headerRowEvents 参数**：
| 参数 | 说明 | 类型 |
|------|------|------|
| rowIndex | 行索引 | Number |

---

## 8.5 header 单元格事件自定义

通过 `headerCellEvents` 配置表头单元格的自定义事件。

**配置示例**：
```vue
<template>
  <xTableEasy
    :columns="columns"
    :table-data="tableData"
    :event-custom-option="eventCustomOption" />
</template>
<script>
export default {
  data() {
    return {
      eventCustomOption: {
        headerCellEvents: ({ column, rowIndex, columnIndex }) => {
          return {
            click: (event) => {
              console.log(`Header cell clicked: ${column.title}`);
            },
            mouseenter: (event) => {
              console.log(`Mouse enter header: ${column.title}`);
            }
          };
        }
      },
      columns: [...],
      tableData: [...]
    };
  }
};
</script>
```

**headerCellEvents 参数**：
| 参数 | 说明 | 类型 |
|------|------|------|
| column | 当前列配置 | Object |
| rowIndex | 行索引 | Number |
| columnIndex | 列索引 | Number |

---

## 8.6 footer 行事件自定义

通过 `footerRowEvents` 配置表尾行的自定义事件。

**配置示例**：
```vue
<template>
  <xTableEasy
    :columns="columns"
    :table-data="tableData"
    :footer-data="footerData"
    :event-custom-option="eventCustomOption" />
</template>
<script>
export default {
  data() {
    return {
      eventCustomOption: {
        footerRowEvents: ({ row, rowIndex }) => {
          return {
            click: (event) => {
              console.log('Footer row clicked:', rowIndex);
            }
          };
        }
      },
      columns: [...],
      tableData: [...],
      footerData: [...]
    };
  }
};
</script>
```

**footerRowEvents 参数**：
| 参数 | 说明 | 类型 |
|------|------|------|
| row | 当前行数据 | Object |
| rowIndex | 行索引 | Number |

---

## 8.7 footer 单元格事件自定义

通过 `footerCellEvents` 配置表尾单元格的自定义事件。

**配置示例**：
```vue
<template>
  <xTableEasy
    :columns="columns"
    :table-data="tableData"
    :footer-data="footerData"
    :event-custom-option="eventCustomOption" />
</template>
<script>
export default {
  data() {
    return {
      eventCustomOption: {
        footerCellEvents: ({ row, column, rowIndex, columnIndex }) => {
          return {
            click: (event) => {
              console.log(`Footer cell clicked: ${column.title}`);
            }
          };
        }
      },
      columns: [...],
      tableData: [...],
      footerData: [...]
    };
  }
};
</script>
```

**footerCellEvents 参数**：
| 参数 | 说明 | 类型 |
|------|------|------|
| row | 当前行数据 | Object |
| column | 当前列配置 | Object |
| rowIndex | 行索引 | Number |
| columnIndex | 列索引 | Number |

---

## 8.8 API

### eventCustomOption

事件自定义配置

| 属性 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| bodyRowEvents | body 行事件自定义 | Function | - |
| bodyCellEvents | body 单元格事件自定义 | Function | - |
| headerRowEvents | header 行事件自定义 | Function | - |
| headerCellEvents | header 单元格事件自定义 | Function | - |
| footerRowEvents | footer 行事件自定义 | Function | - |
| footerCellEvents | footer 单元格事件自定义 | Function | - |

### 支持的事件类型

| 事件类型 | 说明 |
|----------|------|
| click | 单击事件 |
| dblclick | 双击事件 |
| contextmenu | 右键菜单事件 |
| mouseenter | 鼠标进入事件 |
| mouseleave | 鼠标离开事件 |
| mousemove | 鼠标移动事件 |
| mouseover | 鼠标悬停事件 |
| mousedown | 鼠标按下事件 |
| mouseup | 鼠标释放事件 |

---

[返回模块索引](../10-module-design.md)