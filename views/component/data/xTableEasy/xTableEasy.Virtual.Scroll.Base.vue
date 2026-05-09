<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<xTableEasy
				:columns="columns"
				:table-data="tableData"
				:max-height="400"
				:virtual-scroll-option="virtualScrollOption"
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
				mdDoc: "通过 virtual-scroll-option 属性启用虚拟滚动，用于大数据量表格",
				virtualScrollOption: {
					enable: true
				},
				columns: [
					{ field: "id", key: "id", title: "ID", width: 80, align: "center" },
					{ field: "name", key: "name", title: "Name", width: 150 },
					{ field: "date", key: "date", title: "Date", width: 200 },
					{ field: "hobby", key: "hobby", title: "Hobby", width: 300 },
					{ field: "address", key: "address", title: "Address", width: 400 }
				],
				tableData: this.generateData(1000)
			};
		},
		methods: {
			generateData(count) {
				const hobbies = ["coding", "reading", "gaming", "sports", "music"];
				const addresses = [
					"Shanghai",
					"Beijing",
					"Shenzhen",
					"Guangzhou",
					"Hangzhou"
				];
				const data = [];
				for (let i = 0; i < count; i++) {
					data.push({
						id: i + 1,
						name: `User ${i + 1}`,
						date: `2024-${String(Math.floor(Math.random() * 12) + 1).padStart(2, "0")}-${String(Math.floor(Math.random() * 28) + 1).padStart(2, "0")}`,
						hobby: hobbies[Math.floor(Math.random() * hobbies.length)],
						address: addresses[Math.floor(Math.random() * addresses.length)]
					});
				}
				return data;
			}
		}
	});
}
</script>