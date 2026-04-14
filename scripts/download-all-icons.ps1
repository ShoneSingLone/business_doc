# 图标下载脚本
$icons = @(
    @{keyword="card"; filename="icon_card"},
    @{keyword="tag"; filename="icon_tag"},
    @{keyword="pagination"; filename="icon_pagination"},
    @{keyword="badge"; filename="icon_badge"},
    @{keyword="menu"; filename="icon_menu"},
    @{keyword="tabs"; filename="icon_tabs"},
    @{keyword="step"; filename="icon_step"},
    @{keyword="dropdown"; filename="icon_dropdown"},
    @{keyword="network"; filename="icon_network"},
    @{keyword="cron"; filename="icon_cron"},
    @{keyword="demo"; filename="icon_demo"},
    @{keyword="dev"; filename="icon_dev"},
    @{keyword="test"; filename="icon_test"},
    @{keyword="template"; filename="icon_template"},
    @{keyword="render"; filename="icon_render"},
    @{keyword="socket"; filename="icon_socket"},
    @{keyword="debug"; filename="icon_debug"},
    @{keyword="descriptions"; filename="icon_descriptions"}
)

$outputDir = "e:/ghca_code/m2o/statics/business_doc/assets/svg"

# 检查并安装 playwright
if (!(Get-Command npx -ErrorAction SilentlyContinue)) {
    Write-Host "需要安装 Node.js 和 npm" -ForegroundColor Red
    exit 1
}

Write-Host "检查 playwright..." -ForegroundColor Yellow
npx playwright install chromium 2>$null

# 创建临时下载脚本
$scriptContent = @'
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const icons = 'ICON_LIST_PLACEHOLDER';
const outputDir = "OUTPUT_DIR_PLACEHOLDER";

async function downloadIcons() {
    console.log('启动浏览器...');
    const browser = await chromium.launch({ headless: true });
    const page = await browser.newPage();
    
    let success = 0;
    let failed = 0;
    
    for (const icon of icons) {
        const svgPath = path.join(outputDir, `${icon.filename}.svg`);
        if (fs.existsSync(svgPath)) {
            console.log(`[SKIP] ${icon.filename}.svg 已存在`);
            continue;
        }
        
        console.log(`[${success + failed + 1}/${icons.length}] 下载: ${icon.keyword}`);
        
        try {
            const url = `https://www.iconfont.cn/search/index?q=${encodeURIComponent(icon.keyword)}&page=1&searchType=icon&fromCollection=-1`;
            await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 });
            await page.waitForSelector('.block-icon-list', { timeout: 10000 });
            
            const svgHtml = await page.evaluate(() => {
                const svg = document.querySelector('.block-icon-list li:first-child svg');
                return svg ? svg.outerHTML : null;
            });
            
            if (svgHtml) {
                fs.writeFileSync(svgPath, svgHtml);
                console.log(`[OK] ${icon.filename}.svg`);
                success++;
            } else {
                console.log(`[FAIL] ${icon.keyword}: 未找到图标`);
                failed++;
            }
            
            await page.waitForTimeout(800);
        } catch (e) {
            console.log(`[ERROR] ${icon.keyword}: ${e.message}`);
            failed++;
        }
    }
    
    await browser.close();
    console.log(`\n完成! 成功: ${success}, 失败: ${failed}`);
}

downloadIcons();
'@

# 替换占位符
$iconJson = ($icons | ForEach-Object { "{keyword:'$($_.keyword)',filename:'$($_.filename)'}" }) -join ","
$iconJson = "[$iconJson]"
$scriptContent = $scriptContent -replace "'ICON_LIST_PLACEHOLDER'", $iconJson
$scriptContent = $scriptContent -replace "OUTPUT_DIR_PLACEHOLDER", $outputDir

$tempScript = "$env:TEMP\download-icons-temp.js"
$scriptContent | Out-File -FilePath $tempScript -Encoding UTF8

Write-Host "开始下载图标..." -ForegroundColor Green
node $tempScript

Remove-Item $tempScript -Force
Write-Host "`n下载完成!" -ForegroundColor Green
