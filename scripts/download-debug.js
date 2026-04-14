const { chromium } = require('playwright');
const fs = require('fs');

async function download() {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();

  // 尝试不同的关键词
  const keywords = ['debug', 'bug', 'debugger', 'debugging'];

  for (const keyword of keywords) {
    console.log(`尝试关键词: ${keyword}`);

    const url = `https://www.iconfont.cn/search/index?q=${encodeURIComponent(keyword)}&page=1&searchType=icon&fromCollection=-1`;
    await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 });
    await page.waitForTimeout(2000);

    const frame = page.frames()[0];
    const svgLocator = frame.locator('.block-icon-list li:first-child svg').first();
    const svgCount = await svgLocator.count();

    if (svgCount > 0) {
      const svgHtml = await svgLocator.evaluate(el => el.outerHTML);
      const outputPath = 'e:/ghca_code/m2o/statics/business_doc/assets/svg/icon_debug.svg';
      fs.writeFileSync(outputPath, svgHtml);
      console.log(`✓ 成功使用关键词 "${keyword}" 下载 icon_debug.svg`);
      break;
    } else {
      console.log(`✗ 关键词 "${keyword}" 未找到图标`);
    }
  }

  await browser.close();
}

download().catch(console.error);
