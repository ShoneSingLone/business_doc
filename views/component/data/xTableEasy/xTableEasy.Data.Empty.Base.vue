<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<div class="data-empty-demo">
				<xTableEasy :columns="columns" :table-data="[]" border-x border-y />
			</div>
		</div>
	</div>
</template>
<script lang="ts">
export default async function () {
	return defineComponent({
		data() {
			return {
				mdDoc: "当 table-data 为空数组时，表格只显示表头，表体为空",
				columns: [
					{ field: "name", key: "a", title: "Name", width: 100 },
					{ field: "date", key: "b", title: "Tel", width: 200 },
					{ field: "hobby", key: "c", title: "Hobby", width: 300 },
					{ field: "address", key: "d", title: "Address", width: 400 }
				]
			};
		}
	});
}
</script>
<style lang="less">
.data-empty-demo {
	.ve-table-container {
		min-height: 100px;
	}
}
</style>
