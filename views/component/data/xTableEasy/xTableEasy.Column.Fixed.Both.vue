<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<xTableEasy
				style="width: 600px"
				:scroll-width="900"
				border-y
				:columns="columns"
				:table-data="tableData" />
		</div>
	</div>
</template>

<script lang="ts">
export default async function () {
	return defineComponent({
		data() {
			return {
				mdDoc: "同时设置左侧和右侧固定列",
				columns: [
					{ field: "col1", key: "a", title: "左固定1", fixed: "left", width: 120 },
					{ field: "col2", key: "b", title: "左固定2", fixed: "left", width: 120 },
					{ field: "col3", key: "c", title: "普通列3", width: 150 },
					{ field: "col4", key: "d", title: "普通列4", width: 150 },
					{ field: "col5", key: "e", title: "右固定5", fixed: "right", width: 120 },
					{ field: "col6", key: "f", title: "右固定6", fixed: "right", width: 120 }
				],
				tableData: Array.from({ length: 5 }, (_, i) => ({
					col1: `数据${i + 1}-1`,
					col2: `数据${i + 1}-2`,
					col3: `数据${i + 1}-3`,
					col4: `数据${i + 1}-4`,
					col5: `数据${i + 1}-5`,
					col6: `数据${i + 1}-6`
				}))
			};
		}
	});
}
</script>
