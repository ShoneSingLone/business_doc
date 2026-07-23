<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<xTableEasy
				:scroll-width="1200"
				:columns="columns"
				:table-data="tableData"
				border-y />
		</div>
	</div>
</template>
<script lang="ts">
export default async function () {
	return defineComponent({
		data() {
			return {
				mdDoc: "容器自适应列固定：不设置外层容器宽度，表格跟随容器自适应，同时设置固定列",
				columns: [
					{ field: "col1", key: "a", title: "Title1", fixed: "left", width: 120 },
					{ field: "col2", key: "b", title: "Title2", fixed: "left", width: 120 },
					{ field: "col3", key: "c", title: "Title3", width: 120 },
					{ field: "col4", key: "d", title: "Title4", width: 120 },
					{ field: "col5", key: "e", title: "Title5", width: 120 },
					{ field: "col6", key: "f", title: "Title6", width: 120 },
					{ field: "col7", key: "g", title: "Title7", width: 120 },
					{ field: "col8", key: "h", title: "Title8", width: 120 },
					{ field: "col9", key: "i", title: "Title9", width: 120 },
					{ field: "col10", key: "j", title: "Title10", width: 120 }
				],
				tableData: Array.from({ length: 5 }, (_, i) => ({
					col1: `${i + 1}`,
					col2: `${i + 1}`,
					col3: `${i + 1}`,
					col4: `${i + 1}`,
					col5: `${i + 1}`,
					col6: `${i + 1}`,
					col7: `${i + 1}`,
					col8: `${i + 1}`,
					col9: `${i + 1}`,
					col10: `${i + 1}`
				}))
			};
		}
	});
}
</script>
