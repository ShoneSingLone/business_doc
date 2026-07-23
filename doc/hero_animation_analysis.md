# Hero Animation 动画处理方式分析

## 动画效果概述

在 `hero_animation.html`
中实现了一种流畅的图片预览动画效果。当用户点击网格中的缩略图时，图片会从缩略图位置平滑地放大到全屏预览位置，同时背景会逐渐变暗。这种效果通常被称为 "Hero
Animation" 或 "共享元素过渡"。

## 核心动画处理流程

### 1. 状态管理

```javascript
let currentCard = null; // 当前正在显示的卡片
let isAnimating = false; // 动画状态标志
let animationFrameId = null; // 动画帧 ID
```

使用简单的变量来管理动画状态，确保在动画过程中不会触发新的动画。

### 2. 点击事件处理

```javascript
cards.forEach(card => {
	card.addEventListener("click", e => {
		// 如果正在动画，先取消当前动画
		if (isAnimating) {
			cancelAnimation();
		}
		// 直接切换到新图片，不需要先关闭
		switchToCard(card);
	});
});
```

点击事件处理函数会检查当前是否正在动画，如果是则先取消动画，然后直接切换到新图片，不需要先关闭旧图片。

### 3. 动画实现过程

#### 3.1 初始状态设置

```javascript
// 立即获取新卡片的位置信息
const rect = card.getBoundingClientRect();

// 重置所有样式到初始状态（无动画）
preview.style.transition = "none";
preview.style.width = rect.width + "px";
preview.style.height = rect.height + "px";
preview.style.left = rect.left + "px";
preview.style.top = rect.top + "px";
preview.style.transform = "translate(0, 0)";
preview.style.borderRadius = "18px";
preview.style.opacity = "0";

// 强制刷新 DOM，确保样式更新生效
preview.getBoundingClientRect();
```

1. 立即获取点击卡片的位置信息
2. 将预览图片的样式重置到初始状态，包括尺寸、位置、圆角和透明度
3. 使用 `preview.getBoundingClientRect()` 强制刷新 DOM，确保样式更新生效

#### 3.2 显示元素

```javascript
// 显示覆盖层和预览
overlay.classList.add("active");
preview.classList.add("active");

// 立即设置可见性
preview.style.opacity = "1";
```

添加 CSS 类来显示覆盖层和预览图片，并立即设置预览图片的可见性。

#### 3.3 开启动画

```javascript
// 开启动画
preview.style.transition = "all 0.42s cubic-bezier(0.2, 0, 0, 1)";

// 放大到中央
preview.style.width = "360px";
preview.style.height = "360px";
preview.style.left = "50%";
preview.style.top = "50%";
preview.style.transform = "translate(-50%, -50%)";
preview.style.borderRadius = "24px";
```

1. 设置过渡动画属性，使用 `cubic-bezier(0.2, 0, 0, 1)` 缓动函数
2. 开始动画，将预览图片放大到固定大小 360px × 360px（**问题：尺寸写死，不考虑图片原始比例**）
3. 将预览图片移动到屏幕中央位置
4. 增加预览图片的圆角

**问题分析：**

- 预览图尺寸写死为 360px × 360px 的正方形，不考虑源图片的原始比例
- 对于非正方形图片，会导致预览图拉伸或压缩
- 更好的方法是根据源图片比例计算预览图尺寸，确保图片不变形

#### 3.4 动画完成后状态更新

```javascript
// 动画完成后更新状态
animationFrameId = setTimeout(() => {
	isAnimating = false;
}, 420);
```

使用定时器在动画完成后更新动画状态标志。

### 4. 动画取消与关闭

```javascript
// 取消当前动画
function cancelAnimation() {
	if (animationFrameId) {
		clearTimeout(animationFrameId);
		animationFrameId = null;
	}
	// 强制停止所有动画
	preview.style.transition = "none";
	preview.getBoundingClientRect();
}

// 关闭动画
function closeHero() {
	if (!currentCard || isAnimating) return;
	isAnimating = true;
	const rect = currentCard.getBoundingClientRect();

	// 回到原图位置
	preview.style.width = rect.width + "px";
	preview.style.height = rect.height + "px";
	preview.style.left = rect.left + "px";
	preview.style.top = rect.top + "px";
	preview.style.transform = "translate(0, 0)";
	preview.style.borderRadius = "18px";

	setTimeout(() => {
		overlay.classList.remove("active");
		preview.classList.remove("active");
		isAnimating = false;
	}, 420);
}
```

- `cancelAnimation()` 函数用于取消正在进行的动画
- `closeHero()` 函数用于将预览图片缩小回原图位置并隐藏

## 动画特点

1. **缓动函数**：使用 `cubic-bezier(0.2, 0, 0, 1)` 缓动函数，实现快速启动和缓慢结束的效果
2. **动画时长**：0.42 秒，提供良好的用户体验
3. **缩放动画**：从缩略图大小到 360px × 360px 的缩放
4. **位置变化**：从点击位置到屏幕中央的平移
5. **圆角过渡**：从缩略图的 18px 圆角到预览图的 24px 圆角
6. **背景动画**：半透明黑色背景的淡入淡出效果

## 样式设置

```css
.overlay {
	position: fixed;
	inset: 0;
	background: rgba(0, 0, 0, 0.7);
	opacity: 0;
	pointer-events: none;
	z-index: 999;
	transition: opacity 0.4s ease;
}

.overlay.active {
	opacity: 1;
	pointer-events: auto;
}

.preview {
	position: fixed;
	z-index: 1000;
	will-change: transform;
	transition: all 0.42s cubic-bezier(0.2, 0, 0, 1);
	opacity: 0;
	pointer-events: none;
	border-radius: 18px;
	overflow: hidden;
}

.preview.active {
	opacity: 1;
	pointer-events: auto;
}
```

- 使用 CSS 过渡动画实现平滑效果
- 使用 `will-change: transform` 优化动画性能
- 使用 `pointer-events: none` 确保动画过程中元素不响应事件

## 学到的关键经验

1. **强制 DOM 刷新**：使用 `element.getBoundingClientRect()` 强制浏览器重新计算布局，确保样式更新生效
2. **状态管理**：使用简单的变量管理动画状态，防止动画叠加
3. **CSS 过渡**：使用 CSS 过渡而不是 JavaScript 动画，提高性能和代码可读性
4. **动画取消机制**：提供动画取消功能，提升用户体验
5. **共享元素过渡**：通过共享同一个 DOM 元素实现从缩略图到全屏预览的过渡效果

## 总结

`hero_animation.html` 中的动画处理方式简单而有效，使用 CSS 过渡和 JavaScript 状态管理相结合的方式，实现了流畅的 Hero
Animation 效果。这种方法具有良好的性能和可维护性，是实现图片预览动画的优秀参考。
