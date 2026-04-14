#!/usr/bin/env node
/**
 * Iconfont 图标下载脚本
 * 用法: node download-iconfont.js <keyword> <output-filename>
 * 示例: node download-iconfont.js table icon_table
 */

const CDP = require('chrome-remote-interface');
const fs = require('fs');
const path = require('path');

const ICONS_DIR = path.join(__dirname, '..', 'assets', 'svg');
const CDP_URL = process.env.CDP_URL || 'http://localhost:9222';

async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function downloadIcon(keyword, filename) {
  if (!keyword || !filename) {
    console.error('用法: node download-iconfont.js <keyword> <output-filename>');
    console.error('示例: node download-iconfont.js table icon_table');
    process.exit(1);
  }

  // 确保文件名有 .svg 后缀
  if (!filename.endsWith('.svg')) {
    filename += '.svg';
  }

  const outputPath = path.join(ICONS_DIR, filename);

  // 确保输出目录存在
  if (!fs.existsSync(ICONS_DIR)) {
    fs.mkdirSync(ICONS_DIR, { recursive: true });
  }

  console.log(`正在搜索图标: ${keyword}`);
  console.log(`输出路径: ${outputPath}`);

  let client;
  try {
    // 连接到 Chrome DevTools Protocol
    client = await CDP({ host: 'localhost', port: 9222 });
    const { Page, Runtime, DOM } = client;

    // 启用必要的 domain
    await Page.enable();
    await Runtime.enable();
    await DOM.enable();

    // 导航到搜索页面
    const searchUrl = `https://www.iconfont.cn/search/index?q=${encodeURIComponent(keyword)}`;
    console.log(`打开页面: ${searchUrl}`);
    
    await Page.navigate({ url: searchUrl });
    await Page.loadEventFired();
    
    // 等待页面加载和搜索结果
    console.log('等待页面加载...');
    await sleep(5000);

    // 获取第一个图标的 SVG
    const expression = `
      (function() {
        const iconItem = document.querySelector('.block-icon-list li:first-child');
        if (!iconItem) return null;
        const svg = iconItem.querySelector('svg');
        return svg ? svg.outerHTML : null;
      })()
    `;

    const result = await Runtime.evaluate({
      expression,
      returnByValue: true,
      awaitPromise: true
    });

    if (!result.result.value) {
      console.error('未找到图标，请检查搜索关键词');
      process.exit(1);
    }

    let svgContent = result.result.value;
    
    // 清理 SVG 内容，移除不必要的属性
    svgContent = svgContent.replace(/p-id="\d+"/g, '');
    svgContent = svgContent.replace(/fill="#[^"]*"/g, 'fill="currentColor"');
    
    // 保存文件
    fs.writeFileSync(outputPath, svgContent, 'utf-8');
    console.log(`✓ 图标已保存: ${outputPath}`);

  } catch (error) {
    console.error('错误:', error.message);
    console.error('\n请确保:');
    console.error('1. Chrome 已启动并开启了远程调试端口 (9222)');
    console.error('2. 命令示例: chrome.exe --remote-debugging-port=9222');
    process.exit(1);
  } finally {
    if (client) {
      await client.close();
    }
  }
}

// 批量下载图标
async function downloadIconsBatch(icons) {
  console.log(`开始批量下载 ${icons.length} 个图标...\n`);
  
  for (const [keyword, filename] of icons) {
    try {
      await downloadIcon(keyword, filename);
      console.log(''); // 空行分隔
      await sleep(2000); // 避免请求过快
    } catch (error) {
      console.error(`下载 ${filename} 失败:`, error.message);
    }
  }
  
  console.log('批量下载完成！');
}

// 主函数
async function main() {
  const args = process.argv.slice(2);
  
  // 检查是否是批量模式（JSON 文件）
  if (args.length === 1 && args[0].endsWith('.json')) {
    const jsonPath = path.resolve(args[0]);
    if (!fs.existsSync(jsonPath)) {
      console.error(`文件不存在: ${jsonPath}`);
      process.exit(1);
    }
    
    const icons = JSON.parse(fs.readFileSync(jsonPath, 'utf-8'));
    await downloadIconsBatch(icons);
    return;
  }
  
  // 单图标模式
  if (args.length < 2) {
    console.log('Iconfont 图标下载工具');
    console.log('');
    console.log('用法:');
    console.log('  单图标:  node download-iconfont.js <keyword> <filename>');
    console.log('  批量:    node download-iconfont.js <icons.json>');
    console.log('');
    console.log('示例:');
    console.log('  node download-iconfont.js table icon_table');
    console.log('  node download-iconfont.js ./icons.json');
    console.log('');
    console.log('icons.json 格式:');
    console.log('  [["table", "icon_table"], ["search", "icon_search"]]');
    process.exit(1);
  }
  
  const [keyword, filename] = args;
  await downloadIcon(keyword, filename);
}

main().catch(console.error);
