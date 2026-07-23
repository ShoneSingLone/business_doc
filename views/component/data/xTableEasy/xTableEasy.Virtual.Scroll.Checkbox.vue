<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<xTableEasy
				:columns="columns"
				:table-data="tableData"
				:max-height="400"
				:virtual-scroll-option="virtualScrollOption"
				:checkbox-option="checkboxOption"
				:row-key-field-name="'id'"
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
				mdDoc: "虚拟滚动结合行多选：大数据量表格中启用多选功能",
				virtualScrollOption: {
					enable: true
				},
				checkboxOption: {
					selectedRowChange: ({ row, isSelected, selectedRowKeys }) => {
						console.log("选中行:", row.name, "已选:", selectedRowKeys.length);
					}
				},
				columns: [
					{ type: "checkbox", width: 50 },
					{ field: "id", key: "id", title: "ID", width: 80, align: "center" },
					{ field: "name", key: "name", title: "Name", width: 150 },
					{ field: "date", key: "date", title: "Date", width: 200 },
					{ field: "hobby", key: "hobby", title: "Hobby", width: 300 },
					{ field: "address", key: "address", title: "Address", width: 400 }
				],
				tableData: this.generateData(5000)
			};
		},
		methods: {
			generateData(count) {
				const hobbies = ["coding", "reading", "gaming", "sports", "music"];
				const addresses = ["Shanghai", "Beijing", "Shenzhen", "Guangzhou", "Hangzhou"];
				return Array.from({ length: count }, (_, i) => ({
					id: i + 1,
					name: `User ${i + 1}`,
					date: `2024-${String(Math.floor(Math.random() * 12) + 1).padStart(2, "0")}-${String(Math.floor(Math.random() * 28) + 1).padStart(2, "0")}`,
					hobby: hobbies[Math.floor(Math.random() * hobbies.length)],
					address: addresses[Math.floor(Math.random() * addresses.length)]
				}));
			}
		}
	});
}
</script>
