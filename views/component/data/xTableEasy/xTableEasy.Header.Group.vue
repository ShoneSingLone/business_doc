<template>
	<div>
		<div class="flex vertical">
			<xMd :md="mdDoc" />
			<xTableEasy :columns="columns" :table-data="tableData" borderX borderY />
		</div>
	</div>
</template>
<script lang="ts">
export default async function () {
	return defineComponent({
		data() {
			return {
				mdDoc: "通过在 columns 配置中设置 children 属性来实现表头分组",
				columns: [
					{
						field: "name",
						title: "基本信息",
						children: [
							{ field: "name", key: "a", title: "Name", width: 100 },
							{ field: "age", key: "b", title: "Age", width: 80, align: "center" }
						]
					},
					{
						field: "contact",
						title: "联系方式",
						children: [
							{ field: "date", key: "c", title: "Tel", width: 200 },
							{ field: "email", key: "d", title: "Email", width: 250 }
						]
					},
					{
						field: "other",
						title: "其他信息",
						children: [
							{ field: "hobby", key: "e", title: "Hobby", width: 200 },
							{ field: "address", key: "f", title: "Address", width: 300 }
						]
					}
				],
				tableData: [
					{
						name: "John",
						age: 28,
						date: "1900-05-20",
						email: "john@example.com",
						hobby: "coding and coding repeat",
						address: "No.1 Century Avenue, Shanghai"
					},
					{
						name: "Dickerson",
						age: 32,
						date: "1910-06-20",
						email: "dickerson@example.com",
						hobby: "coding and coding repeat",
						address: "No.1 Century Avenue, Beijing"
					},
					{
						name: "Larsen",
						age: 25,
						date: "2000-07-20",
						email: "larsen@example.com",
						hobby: "coding and coding repeat",
						address: "No.1 Century Avenue, Chongqing"
					},
					{
						name: "Geneva",
						age: 30,
						date: "2010-08-20",
						email: "geneva@example.com",
						hobby: "coding and coding repeat",
						address: "No.1 Century Avenue, Xiamen"
					},
					{
						name: "Jami",
						age: 26,
						date: "2020-09-20",
						email: "jami@example.com",
						hobby: "coding and coding repeat",
						address: "No.1 Century Avenue, Shenzhen"
					}
				]
			};
		}
	});
}
</script>
