<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<xTableEasy
				:columns="columns"
				:table-data="tableData"
				:expand-option="expandOption"
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
				mdDoc: "默认展开：通过 `defaultExpandedRowKeys` 配置默认展开的行",
				expandOption: {
					enable: true,
					defaultExpandedRowKeys: [1, 3],
					render: (row) => {
						return `<div style="padding: 10px;">
							<strong>展开内容：</strong> ${row.name} 的详细信息 - ${row.address}
						</div>`;
					}
				},
				columns: [
					{ field: "name", key: "name", title: "Name", width: 100 },
					{ field: "date", key: "date", title: "Tel", width: 150 },
					{ field: "hobby", key: "hobby", title: "Hobby", width: 200 },
					{ field: "address", key: "address", title: "Address", width: 300 }
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
