const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

// 需要下载的图标列表
const icons = [
  { keyword: "card", filename: "icon_card" },
  { keyword: "tag", filename: "icon_tag" },
  { keyword: "pagination", filename: "icon_pagination" },
  { keyword: "badge", filename: "icon_badge" },
  { keyword: "menu", filename: "icon_menu" },
  { keyword: "tabs", filename: "icon_tabs" },
  { keyword: "step", filename: "icon_step" },
  { keyword: "dropdown", filename: "icon_dropdown" },
  { keyword: "network", filename: "icon_network" },
  { keyword: "cron", filename: "icon_cron" },
  { keyword: "demo", filename: "icon_demo" },
  { keyword: "dev", filename: "icon_dev" },
  { keyword: "test", filename: "icon_test" },
  { keyword: "template", filename: "icon_template" },
  { keyword: "render", filename: "icon_render" },
  { keyword: "socket", filename: "icon_socket" },
  { keyword: "debug", filename: "icon_debug" },
  { keyword: "descriptions", filename: "icon_descriptions" }
];

const outputDir = "e:/ghca_code/m2o/statics/business_doc/assets/svg";

// 检查文件是否已存在
function fileExists(filename) {
  return fs.existsSync(path.join(outputDir, `${filename}.svg`));
}

async function downloadIcons() {
  console.log('启动浏览器...');
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page = await context.newPage();

  let success = 0;
  let failed = 0;
  let skipped = 0;

  for (const icon of icons) {
    if (fileExists(icon.filename)) {
      console.log(`✓ ${icon.filename}.svg 已存在，跳过`);
      skipped++;
      continue;
    }

    console.log(`\n[${success + failed + skipped + 1}/${icons.length}] 下载: ${icon.keyword} -> ${icon.filename}.svg`);

    try {
      const url = `https://www.iconfont.cn/search/index?q=${encodeURIComponent(icon.keyword)}&page=1&searchType=icon&fromCollection=-1`;
      await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 });

      // 等待页面加载，给 JS 渲染时间
      await page.waitForTimeout(2000);

      // 获取第一个 frame（主 frame）中的图标
      const frame = page.frames()[0];
      const svgLocator = frame.locator('.block-icon-list li:first-child svg').first();
      const svgCount = await svgLocator.count();
      let svgHtml = null;
      if (svgCount > 0) {
        svgHtml = await svgLocator.evaluate(el => el.outerHTML);
      }

      if (!svgHtml) {
        console.error(`✗ ${icon.keyword}: 未找到图标`);
        failed++;
        continue;
      }

      // 保存 SVG
      const svgPath = path.join(outputDir, `${icon.filename}.svg`);
      fs.writeFileSync(svgPath, svgHtml);
      console.log(`✓ 已保存: ${svgPath}`);
      success++;

      // 延迟避免请求过快
      await page.waitForTimeout(1000);

    } catch (error) {
      console.error(`✗ ${icon.keyword}: ${error.message}`);
      failed++;
    }
  }

  await browser.close();

  console.log(`\n\n========== 下载完成 ==========`);
  console.log(`成功: ${success}`);
  console.log(`跳过(已存在): ${skipped}`);
  console.log(`失败: ${failed}`);
  console.log(`==============================`);
}

downloadIcons().catch(err => {
  console.error('发生错误:', err);
  process.exit(1);
});
