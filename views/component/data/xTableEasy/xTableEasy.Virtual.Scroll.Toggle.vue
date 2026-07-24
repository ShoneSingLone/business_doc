<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<div class="demo-controls">
				<xBtn type="primary" @click="toggleVirtualScroll">
					{{ virtualScrollEnabled ? "关闭虚拟滚动" : "开启虚拟滚动" }}
				</xBtn>
				<span>当前状态：{{ virtualScrollEnabled ? "已开启" : "已关闭" }}</span>
			</div>
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
				mdDoc: "动态开启或关闭虚拟滚动：通过按钮切换虚拟滚动状态",
				virtualScrollEnabled: true,
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
		computed: {
			virtualScrollOption() {
				return {
					enable: this.virtualScrollEnabled
				};
			}
		},
		methods: {
			toggleVirtualScroll() {
				this.virtualScrollEnabled = !this.virtualScrollEnabled;
			},
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
<style scoped>
.demo-controls {
	margin-bottom: 16px;
	padding: 12px;
	background-color: #f5f7fa;
	border-radius: 4px;
	display: flex;
	align-items: center;
	gap: 12px;
}
</style>
