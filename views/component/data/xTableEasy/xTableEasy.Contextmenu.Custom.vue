<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<xTableEasy
				:columns="columns"
				:table-data="tableData"
				:contextmenu-body-option="contextmenuBodyOption"
				border-x
				border-y />
		</div>
	</div>
</template>
<script lang="ts">
export default async function () {
	return defineComponent({
		data() {
			return {
				mdDoc: "自定义右键菜单：配置自定义的菜单项和子菜单",
				contextmenuBodyOption: {
					contextmenus: [
						{
							label: "复制行",
							action: (row, rowIndex) => {
								console.log("复制行:", row.name);
							}
						},
						{
							label: "删除行",
							action: (row, rowIndex) => {
								console.log("删除行:", row.name);
							}
						},
						{
							label: "更多操作",
							children: [
								{
									label: "导出",
									action: (row) => {
										console.log("导出:", row.name);
									}
								},
								{
									label: "打印",
									action: (row) => {
										console.log("打印:", row.name);
									}
								}
							]
						}
					]
				},
				columns: [
					{ field: "name", key: "name", title: "Name", width: 150 },
					{ field: "age", key: "age", title: "Age", width: 100, align: "center" },
					{ field: "hobby", key: "hobby", title: "Hobby", width: 200 }
				],
				tableData: [
					{ name: "John", age: 28, hobby: "coding" },
					{ name: "Dickerson", age: 32, hobby: "reading" },
					{ name: "Larsen", age: 25, hobby: "gaming" }
				]
			};
		}
	});
}
</script>
