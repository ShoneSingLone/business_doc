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
				mdDoc: '通过在 columns 配置中设置 width 属性来定义列宽',
				columns: [
			