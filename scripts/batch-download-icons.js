const { execSync } = require('child_process');
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

// 执行 agent-browser 命令
function runCommand(cmd) {
  try {
    return execSync(cmd, { encoding: 'utf-8', timeout: 30000 });
  } catch (e) {
    console.error(`命令失败: ${cmd}`);
    console.error(e.message);
    return null;
  }
}

// 下载单个图标
async function downloadIcon(keyword, filename) {
  if (fileExists(filename)) {
    console.log(`✓ ${filename}.svg 已存在，跳过`);
    return true;
  }

  console.log(`\n下载: ${keyword} -> ${filename}.svg`);
  
  const url = `https://www.iconfont.cn/search/index?q=${encodeURIComponent(keyword)}&page=1&searchType=icon&fromCollection=-1`;
  
  // 打开页面
  runCommand(`agent-browser open "${url}"`);
  
  // 等待页面加载
  execSync('timeout /t 2 > nul', { shell: 'cmd.exe' });
  
  // 获取 SVG
  const result = runCommand('agent-browser eval "document.querySelector(\'.block-icon-list li:first-child svg\')?.outerHTML || \'NOT_FOUND\'"');
  
  if (!result || result.includes('NOT_FOUND') || result.includes('null')) {
    console.error(`✗ ${keyword}: 未找到图标`);
    return false;
  }
  
  // 保存 SVG
  const svgPath = path.join(outputDir, `${filename}.svg`);
  fs.writeFileSync(svgPath, result.trim());
  console.log(`✓ 已保存: ${svgPath}`);
  return true;
}

// 主函数
async function main() {
  console.log('开始批量下载图标...\n');
  
  let success = 0;
  let failed = 0;
  
  for (const icon of icons) {
    const ok = await downloadIcon(icon.keyword, icon.filename);
    if (ok) success++;
    else failed++;
    
    // 间隔一下避免请求过快
    execSync('timeout /t 1 > nul', { shell: 'cmd.exe' });
  }
  
  console.log(`\n\n完成! 成功: ${success}, 失败: ${failed}`);
  
  // 关闭浏览器
  runCommand('agent-browser close');
}

main().catch(console.error);
