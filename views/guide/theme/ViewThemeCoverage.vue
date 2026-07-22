<template>
	<div class="card-theme-coverage">
		<xMd md="# 主题与业务覆盖演示页" />
		<xMd
			md="用于展示 common/tiny 主题差异、CSS 变量覆盖能力，并作为 small 等尺寸对齐的验收基准。" />
		<div class="card-theme-coverage__controls">
			<div class="flex middle">
				<span class="card-theme-coverage__label">主题</span>
				<xRadioGroup v-model="theme" size="small" @change="onThemeChange">
					<xRadioButton label="common">common</xRadioButton>
					<xRadioButton label="tiny">tiny</xRadioButton>
				</xRadioGroup>
				<xGap l="16" />
				<span class="card-theme-coverage__label">尺寸</span>
				<xRadioGroup v-model="size" size="small">
					<xRadioButton label="mini">mini</xRadioButton>
					<xRadioButton label="small">small</xRadioButton>
					<xRadioButton label="medium">medium</xRadioButton>
				</xRadioGroup>
				<xGap l="16" />
				<span class="card-theme-coverage__label">作用域</span>
				<xRadioGroup v-model="scope" size="small">
					<xRadioButton label="page">页面</xRadioButton>
					<xRadioButton label="root">全局</xRadioButton>
				</xRadioGroup>
			</div>
		</div>

		<div class="card-theme-coverage__layout">
			<div class="card-theme-coverage__panel">
				<xMd md="## Preview（对齐验收区）" />
				<div class="card-theme-coverage__preview-row flex middle">
					<xBtn :size="size">按钮</xBtn>
					<xBtn :size="size" icon="refresh">图标按钮</xBtn>
					<xBtn :size="size" disabled>禁用</xBtn>
					<xGap f />
					<xRadioGroup v-model="radioValue" :size="size">
						<xRadioButton label="left">左</xRadioButton>
						<xRadioButton label="right">右</xRadioButton>
					</xRadioGroup>
				</div>
				<div class="card-theme-coverage__preview-row flex middle">
					<xInput :size="size" placeholder="xInput 对齐观察" style="width: 260px" />
				</div>
			</div>

			<div class="card-theme-coverage__panel">
				<xMd md="## Tokens（可覆盖项）" />
				<div class="card-theme-coverage__tokens">
					<div
						v-for="item in cptTokenRows"
						:key="item.key"
						class="card-theme-coverage__token-row">
						<div class="card-theme-coverage__token-key">{{ item.key }}</div>
						<div class="card-theme-coverage__token-value">{{ item.currentValue }}</div>
						<div class="card-theme-coverage__token-editor">
							<xInput
								size="small"
								:value="item.overrideValue"
								:placeholder="item.placeholder"
								@input="val => onTokenInput(item.key, val)" />
						</div>
						<div class="card-theme-coverage__token-actions">
							<xBtn size="small" @click="applyToken(item.key)">应用</xBtn>
							<xBtn size="small" @click="resetToken(item.key)">重置</xBtn>
						</div>
					</div>
				</div>
			</div>

			<div class="card-theme-coverage__panel">
				<xMd md="## Export（导出覆盖片段）" />
				<div class="flex middle">
					<xBtn size="small" preset="primary" @click="exportCss">生成片段</xBtn>
					<xGap l="8" />
					<xBtn size="small" @click="exportJson">导出JSON</xBtn>
					<xGap l="8" />
					<xBtn size="small" @click="clearAllOverrides">清空覆盖</xBtn>
				</div>
				<pre class="card-theme-coverage__export">{{ exportText || "（暂无覆盖）" }}</pre>
				<xMd md="## Presets（localStorage 预设）" />
				<div class="card-theme-coverage__preset-ops">
					<div class="flex middle">
						<xInput
							v-model="presetName"
							size="small"
							placeholder="预设名称（例如：tiny-small-紧凑）"
							style="width: 320px" />
						<xGap l="8" />
						<xBtn size="small" preset="primary" @click="savePreset">保存预设</xBtn>
						<xGap l="8" />
						<xBtn size="small" @click="refreshPresets">刷新列表</xBtn>
					</div>
					<div class="card-theme-coverage__preset-tip">
						localStorage Key：{{ STORAGE_KEY }}
					</div>
				</div>

				<div class="card-theme-coverage__preset-list">
					<div
						v-for="preset in cptPresets"
						:key="preset.id"
						class="card-theme-coverage__preset-row">
						<div class="card-theme-coverage__preset-name">
							{{ preset.name }}
						</div>
						<div class="card-theme-coverage__preset-meta">
							{{ preset.theme }} / {{ preset.scope }} /
							{{ formatTime(preset.updatedAt || preset.createdAt) }}
						</div>
						<div class="card-theme-coverage__preset-actions">
							<xBtn size="small" preset="primary" @click="applyPreset(preset)">
								应用
							</xBtn>
							<xBtn size="small" @click="copyPresetJson(preset)">复制JSON</xBtn>
							<xBtn size="small" @click="removePreset(preset)">删除</xBtn>
						</div>
					</div>
					<div v-if="cptPresets.length === 0" class="card-theme-coverage__preset-empty">
						（暂无预设）
					</div>
				</div>

				<xMd md="## Import（导入 JSON 并回放）" />
				<xInput
					v-model="importText"
					type="textarea"
					:autosize="{ minRows: 4, maxRows: 10 }"
					placeholder="粘贴 JSON（支持 tokens 或 preset 结构）" />
				<div class="flex middle mt8">
					<xBtn size="small" preset="primary" @click="importJson('replace')">
						导入并替换
					</xBtn>
					<xGap l="8" />
					<xBtn size="small" @click="importJson('merge')">导入并合并</xBtn>
					<xGap l="8" />
					<xBtn size="small" @click="clearImportText">清空</xBtn>
				</div>
			</div>
		</div>
	</div>
</template>

<script lang="ts">
export default async function () {
	const STORAGE_KEY = "xspace:doc:theme_coverage:presets:v1";

	return {
		data() {
			return {
				STORAGE_KEY,
				theme: "tiny",
				size: "small",
				scope: "page",
				radioValue: "left",
				tokenList: [
					{ key: "--ui-height", placeholder: "例如：32px" },
					{ key: "--border-radius", placeholder: "例如：4px / 0" },
					{ key: "--border-radius--small", placeholder: "例如：3px / 0" },
					{ key: "--border-radius--mini", placeholder: "例如：2px / 0" },
					{ key: "--xRadioButton-height--small", placeholder: "例如：32px" },
					{ key: "--xRadioButton-padding-x--small", placeholder: "例如：15px" },
					{ key: "--xRadioButton-border-radius--small", placeholder: "例如：3px / 0" }
				],
				overrideMap: {},
				exportText: "",
				presetName: "",
				presetsState: {
					v: 1,
					updatedAt: 0,
					activePresetId: "",
					presets: []
				},
				importText: ""
			};
		},
		computed: {
			cptTargetEl() {
				if (this.scope === "root") {
					return document.documentElement;
				}
				return this.$el;
			},
			cptTokenRows() {
				const el = this.cptTargetEl || document.documentElement;
				const style = window.getComputedStyle(el);
				return _.map(this.tokenList, item => {
					const key = item.key;
					return {
						key,
						placeholder: item.placeholder,
						currentValue: (style.getPropertyValue(key) || "").trim() || "--",
						overrideValue: this.overrideMap[key] || ""
					};
				});
			},
			cptPresets() {
				const presets = _.$val(this, "presetsState.presets") || [];
				return _.orderBy(presets, ["updatedAt", "createdAt"], ["desc", "desc"]);
			}
		},
		mounted() {
			this.theme = $("html").attr("data-theme") || this.theme;
			this.refreshPresets();
		},
		methods: {
			onThemeChange() {
				/* 【需求】演示页支持切换 html[data-theme] 并触发 ui-x 的主题切换流程，便于对比 common/tiny */
				$("html").attr("data-theme", this.theme);
				$(window).trigger("x_ui_theme_change");
			},
			formatTime(ts) {
				if (!ts) return "--";
				try {
					return new Date(ts).toLocaleString();
				} catch (e) {
					return String(ts);
				}
			},
			readStorageSafe() {
				/* 【需求】Phase2：从 localStorage 读取预设 JSON，支持保存/加载/列表管理 */
				try {
					const raw = localStorage.getItem(this.STORAGE_KEY);
					if (!raw) return null;
					const data = JSON.parse(raw);
					if (!data || data.v !== 1) return null;
					return data;
				} catch (e) {
					return null;
				}
			},
			writeStorageSafe(nextState) {
				/* 【需求】Phase2：写入 localStorage，确保异常不阻断页面使用 */
				try {
					localStorage.setItem(this.STORAGE_KEY, JSON.stringify(nextState));
					return true;
				} catch (e) {
					return false;
				}
			},
			refreshPresets() {
				/* 【需求】Phase2：刷新 localStorage 预设列表 */
				const data = this.readStorageSafe() || this.presetsState || { v: 1, presets: [] };
				if (!data.presets) data.presets = [];
				this.presetsState = data;
			},
			onTokenInput(key, val) {
				this.$set(this.overrideMap, key, val);
			},
			getCleanOverrideMap() {
				const map = {};
				_.each(_.keys(this.overrideMap || {}), key => {
					const val = String(this.overrideMap[key] || "").trim();
					if (!val) return;
					if (!/^--/.test(key)) return;
					map[key] = val;
				});
				return map;
			},
			applyToken(key) {
				/* 【需求】将覆盖值写入选定作用域（页面/全局），用于即时预览变量生效效果 */
				const val = (this.overrideMap[key] || "").trim();
				if (!val) {
					this.resetToken(key);
					return;
				}
				const el = this.cptTargetEl || document.documentElement;
				el.style.setProperty(key, val);
			},
			resetToken(key) {
				/* 【需求】移除覆盖值，让变量回退链恢复生效，便于对比默认值 */
				this.$delete(this.overrideMap, key);
				const el = this.cptTargetEl || document.documentElement;
				el.style.removeProperty(key);
			},
			clearAllOverrides() {
				/* 【需求】一键清理当前作用域内所有覆盖项，方便重做调参 */
				const el = this.cptTargetEl || document.documentElement;
				_.each(_.keys(this.overrideMap), key => {
					el.style.removeProperty(key);
				});
				this.overrideMap = {};
				this.exportText = "";
			},
			exportCss() {
				/* 【需求】导出可复制的 CSS 变量片段，供业务落地到独立的 style.vue 覆盖文件 */
				const cleanMap = this.getCleanOverrideMap();
				const keys = _.keys(cleanMap);
				if (keys.length === 0) {
					this.exportText = "";
					return;
				}
				const selector = this.scope === "root" ? ":root" : ".card-theme-coverage";
				const lines = _.map(keys, key => {
					return `\t${key}: ${cleanMap[key]};`;
				});
				this.exportText = selector + " {\n" + lines.join("\n") + "\n}";
			},
			exportJson() {
				/* 【需求】Phase2：导出当前覆盖项为 JSON，便于保存到 localStorage 或后续接入后端持久化 */
				const tokens = this.getCleanOverrideMap();
				const payload = {
					v: 1,
					theme: this.theme,
					scope: this.scope,
					size: this.size,
					updatedAt: Date.now(),
					tokens
				};
				this.importText = JSON.stringify(payload, null, 2);
			},
			getPresetNameDefault() {
				const theme = this.theme || "common";
				const size = this.size || "small";
				return `${theme}-${size}-${new Date().toLocaleString()}`;
			},
			savePreset() {
				/* 【需求】Phase2：将当前 tokens 保存为 localStorage 预设（支持同名覆盖） */
				const tokens = this.getCleanOverrideMap();
				if (_.keys(tokens).length === 0) {
					_.$msg?.warning?.("当前没有可保存的覆盖项");
					return;
				}
				const name = String(this.presetName || "").trim() || this.getPresetNameDefault();
				const state = this.readStorageSafe() || this.presetsState || { v: 1, presets: [] };
				if (!state.presets) state.presets = [];
				const now = Date.now();
				const existIndex = _.findIndex(state.presets, p => p && p.name === name);
				if (existIndex >= 0) {
					const ok = window.confirm(`已存在同名预设「${name}」，是否覆盖？`);
					if (!ok) return;
					const old = state.presets[existIndex] || {};
					state.presets.splice(existIndex, 1, {
						...old,
						name,
						theme: this.theme,
						scope: this.scope,
						size: this.size,
						updatedAt: now,
						tokens
					});
				} else {
					state.presets.unshift({
						id: `preset_${now}_${_.random(1000, 9999)}`,
						name,
						theme: this.theme,
						scope: this.scope,
						size: this.size,
						createdAt: now,
						updatedAt: now,
						tokens
					});
				}
				state.updatedAt = now;
				this.writeStorageSafe(state);
				this.presetsState = state;
				this.presetName = name;
				_.$msg?.success?.("已保存到 localStorage");
			},
			async applyPreset(preset) {
				/* 【需求】Phase2：应用预设（自动切 theme/scope，并回放 tokens） */
				if (!preset) return;
				this.theme = preset.theme || this.theme;
				this.scope = preset.scope || this.scope;
				this.size = preset.size || this.size;
				this.onThemeChange();
				await this.$nextTick();
				this.clearAllOverrides();
				const tokens = preset.tokens || {};
				_.each(_.keys(tokens), key => {
					this.$set(this.overrideMap, key, tokens[key]);
				});
				const el = this.cptTargetEl || document.documentElement;
				_.each(_.keys(tokens), key => {
					el.style.setProperty(key, String(tokens[key] || "").trim());
				});
				const state = this.readStorageSafe() || this.presetsState;
				if (state) {
					state.activePresetId = preset.id || "";
					state.updatedAt = Date.now();
					this.writeStorageSafe(state);
					this.presetsState = state;
				}
			},
			removePreset(preset) {
				/* 【需求】Phase2：删除预设 */
				if (!preset) return;
				const ok = window.confirm(`确认删除预设「${preset.name}」？`);
				if (!ok) return;
				const state = this.readStorageSafe() || this.presetsState || { v: 1, presets: [] };
				state.presets = _.filter(state.presets || [], p => p && p.id !== preset.id);
				if (state.activePresetId === preset.id) {
					state.activePresetId = "";
				}
				state.updatedAt = Date.now();
				this.writeStorageSafe(state);
				this.presetsState = state;
			},
			copyText(text) {
				try {
					if (navigator.clipboard?.writeText) {
						return navigator.clipboard.writeText(text);
					}
				} catch (e) {}
				return Promise.reject(new Error("clipboard not available"));
			},
			async copyPresetJson(preset) {
				/* 【需求】Phase2：复制预设 JSON，便于粘贴到业务 style.vue 或分享给他人 */
				if (!preset) return;
				const payload = {
					v: 1,
					id: preset.id,
					name: preset.name,
					theme: preset.theme,
					scope: preset.scope,
					size: preset.size,
					updatedAt: preset.updatedAt,
					tokens: preset.tokens || {}
				};
				const text = JSON.stringify(payload, null, 2);
				try {
					await this.copyText(text);
					_.$msg?.success?.("已复制 JSON");
				} catch (e) {
					this.importText = text;
					_.$msg?.warning?.("复制失败，已写入导入框，可手动复制");
				}
			},
			parseImportText() {
				const raw = String(this.importText || "").trim();
				if (!raw) return null;
				try {
					return JSON.parse(raw);
				} catch (e) {
					return { __error: "JSON 解析失败" };
				}
			},
			normalizeTokensFromPayload(payload) {
				if (!payload) return { __error: "空数据" };
				const tokens = payload.tokens || payload;
				if (!_.isPlainObject(tokens)) return { __error: "tokens 必须是对象" };
				const res = {};
				_.each(_.keys(tokens), key => {
					const val = String(tokens[key] || "").trim();
					if (!/^--/.test(key)) return;
					if (!val) return;
					res[key] = val;
				});
				return res;
			},
			importJson(mode) {
				/* 【需求】Phase2：导入 JSON（替换/合并）并立即回放到当前作用域 */
				const payload = this.parseImportText();
				if (!payload) return;
				if (payload.__error) {
					_.$msg?.error?.(payload.__error);
					return;
				}
				const tokens = this.normalizeTokensFromPayload(payload);
				if (tokens.__error) {
					_.$msg?.error?.(tokens.__error);
					return;
				}
				const el = this.cptTargetEl || document.documentElement;
				if (mode === "replace") {
					this.clearAllOverrides();
				}
				_.each(_.keys(tokens), key => {
					this.$set(this.overrideMap, key, tokens[key]);
					el.style.setProperty(key, tokens[key]);
				});
				if (payload.theme && payload.theme !== this.theme) {
					this.theme = payload.theme;
					this.onThemeChange();
				}
				if (payload.scope && payload.scope !== this.scope) {
					this.scope = payload.scope;
				}
				if (payload.size && payload.size !== this.size) {
					this.size = payload.size;
				}
				_.$msg?.success?.("导入成功");
			},
			clearImportText() {
				this.importText = "";
			}
		}
	};
}
</script>

<style lang="less">
.card-theme-coverage {
	padding: 16px;

	&__controls {
		margin: 12px 0;
	}

	&__label {
		margin-right: 8px;
		color: var(--el-text-color-regular);
	}

	&__layout {
		display: grid;
		grid-template-columns: 1fr;
		gap: 16px;
	}

	&__panel {
		padding: 12px;
		border: 1px solid var(--el-border-color-lighter);
		background: var(--ui-base-bg, #fff);
	}

	&__preview-row {
		gap: 12px;
		margin-top: 8px;
	}

	&__tokens {
		display: grid;
		gap: 8px;
		margin-top: 8px;
	}

	&__token-row {
		display: grid;
		grid-template-columns: 260px 160px 1fr 160px;
		align-items: center;
		gap: 8px;
	}

	&__token-key {
		font-family: monospace;
	}

	&__token-value {
		color: var(--el-text-color-secondary);
	}

	&__token-actions {
		display: flex;
		gap: 8px;
		justify-content: flex-end;
	}

	&__export {
		margin-top: 8px;
		padding: 8px;
		background: var(--el-color-info-light-9);
		border: 1px solid var(--el-border-color-lighter);
		overflow: auto;
	}

	&__preset-ops {
		margin-top: 8px;
	}

	&__preset-tip {
		margin-top: 8px;
		color: var(--el-text-color-secondary);
	}

	&__preset-list {
		margin-top: 8px;
		display: grid;
		gap: 8px;
	}

	&__preset-row {
		display: grid;
		grid-template-columns: 220px 1fr 260px;
		align-items: center;
		gap: 8px;
		padding: 8px;
		border: 1px solid var(--el-border-color-lighter);
	}

	&__preset-name {
		font-weight: 600;
	}

	&__preset-meta {
		color: var(--el-text-color-secondary);
	}

	&__preset-actions {
		display: flex;
		gap: 8px;
		justify-content: flex-end;
	}

	&__preset-empty {
		color: var(--el-text-color-secondary);
		padding: 8px;
		border: 1px dashed var(--el-border-color-lighter);
	}
}
</style>
