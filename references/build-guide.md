# 学术海报重建指南

制作前读完项目的 `POSTER-DESIGN.md`，尤其是“参考内容架构”“目标内容图与映射”“偏离记录”。实现以设计规格为准；下面的代码只是结构示例，数值需要换成实际提取结果。

## 1. 先排内容，再写样式

1. 从目标内容图建立每个模块的内容：标题、主张、证据、图注、限定条件与来源。不要直接复制参考海报的原句和数据。
2. 按关系边确定位置：步骤的顺序、比较项的共同标签、图表与主张的距离、限定与结论的距离。画一张简短线框图，检查从入口到出口的阅读路径。
3. 用视觉 token 实现相同的层级、比例和组件规则。不同目标尺寸允许调整绝对数值，并记录偏离原因。
4. 渲染、检查、导出。发生溢出时优先压缩冗余文案、调整模块组织和留白；不得牺牲证据、限定条件或可读性。

若内容结构与参考图冲突，科学逻辑优先：保留可识别的视觉语法，调整栏数、跨栏或模块数量。

## 2. HTML/CSS 起点

```html
<main class="poster">
  <header class="poster-title" data-module="T0">...</header>
  <section class="problem" data-module="T1">...</section>
  <section class="method" data-module="T2">...</section>
  <figure class="evidence" data-module="T3">
    <img src="figure.svg" alt="图表内容摘要">
    <figcaption>图号、指标、单位及必要条件</figcaption>
  </figure>
  <section class="conclusion" data-module="T4" aria-describedby="limit-T5">...</section>
  <p class="limitation" id="limit-T5" data-module="T5">...</p>
</main>
```

`data-module` 不是装饰：它让源材料 ID、映射表与最终 HTML 可以逐项核对。图片本身的替代文本应描述图的实际内容；图注要说明图与主张的关系。

```css
@page {
  size: 841mm 1189mm; /* 替换为目标纸张 */
  margin: 0;
}

:root {
  --canvas: #fff;
  --ink: #1a1a1a;
  --accent: #0b4f8a;
  --panel: #f5f7fa;
  --font-body: Arial, sans-serif;
  --title-size: 90pt;
  --section-size: 38pt;
  --body-size: 24pt;
  --caption-size: 17pt;
  --margin: 35mm;
  --gutter: 16mm;
  --section-gap: 24mm;
}

* { box-sizing: border-box; }
html, body { margin: 0; }
body {
  background: var(--canvas);
  color: var(--ink);
  font-family: var(--font-body);
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}
.poster {
  width: 841mm;
  min-height: 1189mm;
  padding: var(--margin);
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: var(--section-gap) var(--gutter);
}
.poster-title { grid-column: 1 / -1; font-size: var(--title-size); }
.poster section h2 { font-size: var(--section-size); }
.poster section p { font-size: var(--body-size); }
.poster figcaption { font-size: var(--caption-size); }
.evidence img { display: block; max-width: 100%; height: auto; }
```

最终文件中的颜色、字号、栏数及跨栏位置应来自 `POSTER-DESIGN.md`。使用 CSS 变量集中管理重复值；组件特有且有依据的数值可以直接写在组件里，不必为每一个数字都造 token。CSS 内部像素值并非禁用；纸张尺寸、外边距和打印字号需要以物理单位验证。

如果参考图有通栏色块或出血，按实际印刷要求设置延伸区域；不要用负 margin 假装满足印厂的出血规范。带出血的交付应确认目标 PDF 的裁切尺寸和出血尺寸。

## 3. 图表、照片与字体

- **统计图与结构图**：优先复用用户提供的矢量文件，或用真实数据重绘。统一刻度、单位、颜色含义和图例；只有相同量纲和统计口径才叠放或共轴。
- **实验照片、显微图、扫描图**：原本就是像素资料，可以使用足够分辨率的位图。裁剪不得抹掉比例尺、标签或关键实验条件。
- **图文关联**：每张图应有能定位到的结论或解释；条件与误差写在图注或相邻文字。避免“图在左栏，解释在另一端”。
- **字体**：优先保持字族、字重与宽度气质。实际字体缺失时选择可用替代，并检查标题换行、符号与中英文混排。不要把可编辑的文字烘焙成生成图片。
- **真实性**：缺数据时不画假曲线，也不从参考海报挪数值或图像来填空。

## 4. 导出与页面检查

在浏览器打印预览中选择目标页面尺寸、零额外页边距与背景图形；确认预览只有预期页数。自动化导出时，使用能尊重 CSS `@page` 的浏览器 PDF 接口，并核对实际 PDF 页面尺寸。不同浏览器/版本对页面缩放和色彩处理可能不同，必要时用实物打印样张确认。

检查以下项目后再交付：

- [ ] 从标题进入的阅读路径与规格一致；跨栏元素没有切断论证。
- [ ] 每个目标模块都有来源；每个核心主张都有证据或被明确标为待补。
- [ ] 方法与结果、图与图注、限定与被限定主张保持对应。
- [ ] 对比项指标、单位、样本与坐标轴可比；并列项没有无依据的权重差。
- [ ] 没有沿用参考海报的研究事实、姓名、logo 或图表。
- [ ] 没有占位文字、断图、文字溢出、异常换行或额外空白页。
- [ ] PDF 的物理尺寸、页数、背景与字体渲染正确；图表放大后仍清楚。
- [ ] 作者、单位、致谢与匿名要求符合用户材料和会议规范。

缩小预览可以检查整体层级，但屏幕缩放百分比不能等同于固定的观看距离；可读性仍需按最终纸张和展示环境判断。

