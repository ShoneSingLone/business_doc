<template>
	<div>
		<h2>长文本破坏布局</h2>
		<xMd :md="mdDoc" />
		<p>
			word-break：
			<xRadioGroup v-model="wordBreak">
				<xRadio label="normal">normal</xRadio>
				<xRadio label="keep-all">keep-all</xRadio>
				<xRadio label="break-all">break-all</xRadio>
				<xRadio label="break-word">break-word</xRadio>
			</xRadioGroup>
		</p>
		<br />
		<xTableEasy
			:style="{ 'word-break': wordBreak }"
			:table-data="tableData"
			:columns="columns"
			:border-around="true"
			:border-x="true"
			:border-y="true" />
	</div>
</template>

<script lang="ts">
export default async function () {
	return {
		data() {
			return {
				wordBreak: "normal",
				mdDoc: `1、当单元格文本内容过多时会破坏布局，此时可以通过样式word-break控制
				2、你也可以结合单元格省略功能一起使用`,
				columns: [
					{
						field: "name",
						key: "a",
						title: "Name 40%",
						width: "40%"
					},
					{ field: "date", key: "b", title: "Tel 20%", width: "20%" },
					{
						field: "hobby",
						key: "c",
						title: "Hobby 20%",
						width: "20%"
					},
					{
						field: "address",
						key: "d",
						title: "Address 20%",
						width: "20%"
					}
				],
				tableData: [
					{
						name: "John",
						date: "1900-05-20",
						hobby: "Honorificabilitudinitatibus califragilisticexpialidocious Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu 大江东去浪淘尽千古风流人物故垒西边人道是三国周郎赤壁乱石穿空惊涛拍岸卷起千堆雪江山如画一时多少豪杰",
						address: "No.1 Century Avenue, Xiamen"
					},
					{
						name: "Dickerson",
						date: "1910-06-20",
						hobby: "coding and coding repeat",
						address: "No.1 Century Avenue, Beijing"
					},
					{
						name: "Larsen",
						date: "2000-07-20",
						hobby: "coding and coding repeat",
						address: "No.1 Century Avenue, Chongqing"
					},
					{
						name: "Geneva",
						date: "2010-08-20",
						hobby: "coding and coding repeat",
						address: "No.1 Century Avenue, Xiamen"
					},
					{
						name: "Jami",
						date: "2020-09-20",
						hobby: "coding and coding repeat",
						address: "No.1 Century Avenue, Shenzhen"
					}
				]
			};
		}
	};
}
</script>

<style lang="less"></style>
