<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<xTableEasy :columns="columns" :table-data="tableData" border-x border-y />
		</div>
	</div>
</template>
<script lang="ts">
export default async function () {
	return defineComponent({
		data() {
			return {
				mdDoc: '默认单元格内的文本超出宽度时，换行显示',
				columns: [
					{ field: "name", key: "name", title: "姓名", width: 150 },
					{ field: "hobby", key: "hobby", title: "爱好", width: 200 },
					{ field: "address", key: "address", title: "地址", width: 300 }
				],
				tableData: [
					{
						name: "John",
						hobby: "coding and coding repeat",
						address: "No.1 Century Avenue, Shanghai,this is a long text,this is a long text"
					},
					{
						name: "Dickerson",
						hobby: "coding and coding repeat",
						address: "No.1 Century Avenue, Beijing"
					}
				]
			};
		}
	});
}
</script>
<style lang="less"></style>
