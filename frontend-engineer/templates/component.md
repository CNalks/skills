# Component Contract

## Identity

- Name：
- Layer：primitive / composed / feature / page
- Framework / version：
- Existing source / dependency：
- Design spec / wireframe：

## Responsibility

- Purpose：
- User task：
- Owns：
- Non-goals：
- Product decisions that must not change：

## Composition

```text
Component
  -> child / slot
  -> child / slot
```

- Semantic root：
- Required wrappers / compound structure：
- Allowed children / slots：

## Public API

| Prop / event / slot | Type | Required | Default | Meaning / constraints |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

- Controlled / uncontrolled behavior：
- Ref / imperative API（若必须）：
- Backward compatibility：

## Variants and Tokens

| Variant / size | Semantic intent | Token mapping | Allowed combinations |
| --- | --- | --- | --- |
|  |  |  |  |

## State Matrix

| State | Visual | Behavior | Accessible state / announcement |
| --- | --- | --- | --- |
| Default |  |  |  |
| Hover / active |  |  |  |
| Focus-visible |  |  |  |
| Disabled / read-only |  |  |  |
| Loading |  |  |  |
| Empty |  |  |  |
| Error |  |  |  |
| Selected / expanded |  |  |  |

## Data and Side Effects

- Data owner：
- Reads / writes：
- Async states：
- Effects and cleanup：
- Cache / invalidation：

## Adaptation

- Narrow / wide：
- Keyboard / pointer / touch：
- RTL / localization / long text：
- Dark / high contrast / reduced motion：

## Accessibility

- Accessible name / description：
- Keyboard model：
- Focus entry / movement / return：
- Error / status relationship：
- Target size / contrast：

## Performance Constraints

- Bundle / lazy-load：
- Render frequency / large data：
- Asset / network：

## Tests

- Unit：
- Component：
- Integration / E2E：
- Visual：
- Accessibility：

## Acceptance Checklist

- [ ] API、语义、variant 和状态矩阵一致。
- [ ] 没有重复 state 或不必要 Effect/watch。
- [ ] 键盘、焦点、读屏、缩放与目标尺寸通过。
- [ ] 响应式、长内容、error/empty/loading 已验证。
- [ ] 需要 Product Designer 决策的问题已退回，而非静默补齐。
