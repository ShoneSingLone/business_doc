<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<xTableEasy
				:columns="columns"
				:table-data="tableData"
				:expand-option="expandOption"
				:row-key-field-name="'name'"
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
				mdDoc: "通过 expand-option 属性配置行展开功能",
				expandOption: {
					enable: true,
					render: (params, h) => {
						const { row } = params;
						return h("div", { style: { padding: "12px" } }, [
							h("strong", `展开行详情：`),
							h("span", ` ${row.name} - ${row.address}`)
						]);
					}
				},
				columns: [
					{ type: "expand", key: "expand", width: 50 },
					{ field: "name", key: "a", title: "Name", width: 100 },
					{ field: "date", key: "b", title: "Tel", width: 200 },
					{ field: "hobby", key: "c", title: "Hobby", width: 300 },
					{ field: "address", key: "d", title: "Address", width: 400 }
				],
				tableData: [
					{ name: "John", date: "1900-05-20", hobby: "coding", address: "Shanghai" },
					{ name: "Dickerson", date: "1910-06-20", hobby: "reading", address: "Beijing" },
					{ name: "Larsen", date: "2000-07-20", hobby: "gaming", address: "Chongqing" },
					{ name: "Geneva", date: "2010-08-20", hobby: "sports", address: "Xiamen" },
					{ name: "Jami", date: "2020-09-20", hobby: "music", address: "Shenzhen" }
				]
			};
		}
	});
}
</script>
