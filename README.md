# poster-mimic

把参考学术海报拆成可复用的 `POSTER-DESIGN.md`，再将新的研究材料按同一视觉语言与内容逻辑编排成海报。

这个 skill 受到 [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) 的文本设计规格思路启发；本项目针对学术海报增加了**参考海报内容模块关系**、**阅读路径**、**目标论文的主张—证据映射**。它是独立编写的工作流，不是 VoltAgent 项目的官方扩展。

## 为什么需要内容架构

颜色、字号、网格只能告诉模型“看起来怎样”。学术海报还需要说明：

- 参考海报有哪些模块，各自回答什么问题；
- 模块之间是引出、回应、产生、支持、限定、对比、并列，还是汇总；
- 读者先看哪里、沿什么路径找到证据和结论；
- 哪些是可复用的编排语法，哪些是参考论文的具体事实。

有了这些记录，新海报才能复用风格，同时保持目标研究的科学逻辑。

## 安装与使用

将整个 `poster-mimic/` 目录放到支持 `SKILL.md` 的技能目录中。例如 WorkBuddy 可放在 `~/.workbuddy/skills/poster-mimic/`。启动新会话后，提供参考海报和待编排的研究材料，说明目标尺寸、输出格式及署名要求。

示例请求：

> 请用 poster-mimic 提取这张参考海报的设计和内容关系，输出 POSTER-DESIGN.md；再把我的论文摘要、图 1–3 和结论做成 A0 海报。不要沿用参考图中的研究数据。

只有参考海报时，可以先只要求提取 `POSTER-DESIGN.md`；已有规格时可直接用于另一篇论文。没有参考图时，`references/archetypes.md` 提供原创起点。

## 文件

| 文件 | 用途 |
|---|---|
| `SKILL.md` | 入口、工作流程与边界 |
| `references/poster-design-schema.md` | 提取模板、关系图及证据等级 |
| `references/content-architecture-example.md` | 虚构案例：参考关系图与目标内容映射 |
| `references/build-guide.md` | HTML/CSS 制作和导出核查 |
| `references/archetypes.md` | 无参考图时的编排原型 |

## 产物

- `POSTER-DESIGN.md`：可复用的视觉规格和内容架构。
- `poster.html`：在制作任务中交付的可编辑源文件。
- `poster.pdf`：用户需要印刷或提交版时交付。

实际文件名和格式可随用户要求调整。参考图的文字、数据、图表和标识不会作为新研究的事实来源。
