const { chromium } = require('playwright');

async function test() {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();

  const url = 'https://www.iconfont.cn/search/index?q=card&page=1&searchType=icon&fromCollection=-1';
  await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 });
  await page.waitForTimeout(3000);

  // 截图看看
  await page.screenshot({ path: 'e:/ghca_code/m2o/statics/business_doc/scripts/debug-screenshot.png', fullPage: true });

  // 获取页面 HTML
  const html = await page.content();
  console.log('页面长度:', html.length);

  // 检查 block-icon-list
  const lists = await page.locator('.block-icon-list').count();
  console.log('block-icon-list 数量:', lists);

  // 等待图标加载 - 尝试多种选择器
  try {
    await page.waitForSelector('.block-icon-list li', { timeout: 10000 });
    console.log('等待 li 成功');
  } catch (e) {
    console.log('等待 li 失败:', e.message);
  }

  // 检查是否有 iframe
  const frames = page.frames();
  console.log('frame 数量:', frames.length);

  // 检查每个 frame
  for (let i = 0; i < frames.length; i++) {
    const frame = frames[i];
    const url = frame.url();
    console.log(`Frame ${i} URL:`, url);

    try {
      const listCount = await frame.locator('.block-icon-list').count();
      console.log(`Frame ${i} block-icon-list 数量:`, listCount);

      if (listCount > 0) {
        const items = await frame.locator('.block-icon-list li').count();
        console.log(`Frame ${i} li 数量:`, items);

        if (items > 0) {
          const svgHtml = await frame.locator('.block-icon-list li:first-child svg').first().evaluate(el => el.outerHTML);
          console.log(`Frame ${i} SVG (locator):`, svgHtml.substring(0, 100));
        }
      }

      // 测试 frame.evaluate
      const svgFromEval = await frame.evaluate(() => {
        const list = document.querySelector('.block-icon-list');
        if (!list) return 'NO_LIST';
        const svg = list.querySelector('li:first-child svg');
        return svg ? svg.outerHTML.substring(0, 100) : 'NO_SVG';
      });
      console.log(`Frame ${i} SVG (evaluate):`, svgFromEval);

    } catch (e) {
      console.log(`Frame ${i} 错误:`, e.message);
    }
  }

  await browser.close();
}

test().catch(console.error);
