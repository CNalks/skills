# Mobile Product Design

## Reprioritize, Do Not Shrink

移动端先重新排序任务：什么必须立即完成，什么可以渐进披露，什么应移到后续页面。不要把桌面三栏压成一条无限长页面，或把核心动作全部藏进溢出菜单。

## Platform and Context

- 遵循目标平台的导航、返回、输入、权限和系统反馈约定；
- 考虑安全区域、软键盘、横竖屏、动态字体和系统栏；
- 为单手、走动、强光、弱网、中断与重复进入设计；
- 明确 Web、iOS、Android 的共同产品模型与必要平台差异。

## Navigation

稳定的高频顶层目的地应持续可见；层级深处提供清楚的当前位置和返回。标签比仅图标更易理解。不要混用多个竞争的顶层导航模型。

## Touch and Input

- 核心目标采用宽松触控尺寸与间距，检查拇指可达和误触成本；
- 手势必须有可发现、可操作的替代；
- 选择正确键盘与输入格式，减少手动输入；
- 扫描、定位、相机、通知等权限在价值出现时请求，并提供拒绝后的路径。

## Continuity

长表单和创作任务保存进度；登录、跳转系统应用、来电或网络切换后能恢复。明确离线、同步中、冲突、上传失败和后台完成状态。

## Mobile Review

用最窄目标视口、最大文本、长语言、软键盘打开、横屏、弱网和单手操作检查核心任务。关注 sticky 元素是否遮挡焦点或内容。

## Sources

- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [Material Design: Layout](https://m3.material.io/foundations/layout/understanding-layout/overview)
- [WCAG 2.2: Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)
- [WCAG 2.2: Target Size Minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)
