# Performance Engineering

## Measure First

以真实用户数据判断体验，以实验室工具诊断原因。分别观察移动/桌面、网络/设备分层和第 75 百分位，不用一次本机 Lighthouse 分数宣称完成。

Core Web Vitals 的当前良好基线：

- **LCP** ≤ 2.5 s；
- **INP** ≤ 200 ms；
- **CLS** ≤ 0.1。

在项目中另设可执行预算：首屏 JS、路由 chunk、图片、字体、第三方脚本、API latency 和长任务。

## Rendering and JavaScript

- 为每条路由选择静态、服务端或客户端渲染，不默认 SPA；
- 缩小 hydration 与 client boundary；
- 路由、编辑器、图表等重型功能按需加载；
- 删除重复依赖与无用 polyfill，验证 tree shaking；
- 拆分超过约 50 ms 的长任务，必要时让出主线程或使用 Worker；
- 不因动画或测量造成 layout thrashing。

## LCP and Assets

- 让 LCP 资源从初始 HTML/CSS 可发现；LCP 图片不要懒加载；
- 为图片提供正确尺寸、响应式候选、压缩和 width/height；
- 字体子集化、减少字重、选择合适加载策略；
- 预加载只给真正关键且可验证的资源，避免争抢带宽；
- 服务端响应、缓存与 CDN 同样进入 LCP 分析。

## INP

- 找出高延迟交互与主线程阻塞，而非只看平均值；
- 减少每次交互的同步工作和不必要渲染；
- 大量过滤、解析或计算分块/下放；
- 先提供即时视觉反馈，再完成非关键工作；
- 控制 DOM 规模和第三方脚本。

## CLS

- 图片、广告、嵌入、骨架和动态区域预留尺寸；
- 不在现有内容上方无预期插入内容；
- 字体切换与 fallback 指标经过检查；
- 动画优先 transform/opacity，避免改变布局属性。

## Verification

使用 production build、bundle report、DevTools Performance、Lighthouse/PSI 与 RUM。把基线、变更前后、测试环境和剩余风险写入交付。

## Sources

- [web.dev: Web Vitals](https://web.dev/articles/vitals)
- [web.dev: Optimize LCP](https://web.dev/articles/optimize-lcp)
- [web.dev: Optimize INP](https://web.dev/articles/optimize-inp)
- [web.dev: Optimize CLS](https://web.dev/articles/optimize-cls)
- [web.dev: Optimize Long Tasks](https://web.dev/articles/optimize-long-tasks)
- [web.dev: Addy Osmani](https://web.dev/authors/addyosmani/)
