# Lu-Xing Yang IEEE Transactions Research Skill

一个面向 IEEE Transactions 研究全流程的 Codex SKILL，固化了 **Lu-Xing Yang 的个人研究方向、论证结构、写作偏好与证据门槛**。

> [!IMPORTANT]
> **这不是适用于所有人的通用 IEEE 写作模板。**
>
> 它带有鲜明的个人研究风格：偏好从可操作的网络安全决策问题出发，经过机制建模、控制或博弈形式化、理论条件、可复现算法与分层证据，最后形成边界清楚的结论。它会主动缩小过宽题目、保留负面证据、设置 `GO / NO-GO` 门槛，并拒绝证据不支持的“首次、最优、显著、鲁棒、实用”等强表述。
>
> 如果你的研究范式、目标期刊、证据标准或写作习惯与此不同，请把它当作可选择的个人化研究框架，而不是必须照搬的规范。

## 这是什么

这套 SKILL 不是单纯的论文润色提示词，而是一套可执行的个人研究工作流：

```text
operational problem
→ full-text novelty boundary
→ minimal model and solution notion
→ theorem / algorithm / estimator
→ adequate evidence track
→ reproducible results
→ calibrated IEEE prose
→ claim-by-claim preflight
```

它面向 TIFS、TDSC、TSMC、TNSE、TCSS 等期刊，覆盖研究方向规划、全文新颖性审计、数学推导、实验与仿真、论文写作、投稿前检查和审稿回复。

## 强个人风格体现在哪里

- **问题驱动，而不是模块堆叠。** 先锁定决策者、动作、成本、信息、预算和结果，再决定是否需要数据、神经网络、额外玩家或定理。
- **机制与干预双缺口。** 区分“现有模型不能表达什么”和“现有方法不能决定什么”。
- **形式对象明确。** 倾向于命名并定义模型、问题、最优性系统、均衡概念、算法或估计器。
- **理论—代码—证据闭环。** 要求假设、方程、约束、重置、定理条件与实现、测试或局限逐项对应。
- **证据先于宣传。** 强调匹配预算的基线、独立核验、重复实验、不确定性、敏感性、失败记录和可复现配置。
- **结论克制。** 接受负结果、缩窄主张和 `NO-GO`；不会为了让论文“看起来更强”而隐藏不利证据。
- **个人风格是软约束。** 事实、数学正确性、版权伦理和期刊当前要求始终优先于个人措辞习惯。

## 适合与不一定适合

| 更适合 | 不一定适合直接照搬 |
|---|---|
| 网络安全传播、恶意软件与 APT 防御 | 与网络、动态决策或形式验证关系很弱的主题 |
| 最优控制、脉冲/混合控制、微分博弈 | 主要依赖纯定性叙事的研究范式 |
| Stackelberg、联盟、重复或多智能体博弈 | 只追求快速生成流畅文字、不希望设置证据门槛的写作 |
| 网络拓扑、异质性、节点级仿真 | 希望直接继承“首次、最优、真实世界”等强结论的工作流 |
| RL/MARL/MPC 与 PINN/PIDL 的机制化扩展 | 不接受负结果、范围收缩或 `NO-GO` 判断的项目 |
| 强调理论—算法—实验一致性的 IEEE Transactions 工作 | 与 Lu-Xing Yang 个人研究结构明显不同的作者风格 |

## 个人研究方向组合

### 已建立的研究核心

- 传播动力学、阈值与稳定性分析；
- 恶意软件、IoT 威胁与 APT 防御；
- 最优控制、微分博弈与战略互动；
- 补丁、隔离、备份、恢复和成本效益决策。

### 当前扩展

- 脉冲与混合控制；
- 网络宣传、谣言、意识与意见耦合；
- 社会工程恶意软件；
- 员工安全合规、激励—审计和 Stackelberg 分层决策；
- 真实拓扑上的节点级反事实仿真。

### 谨慎加入的能力

- RL、MARL、自博弈和 MPC；
- attack-graph 与传播动力学混合建模；
- PINN、PIDL、逆问题与缺失机制学习；
- 真实数据校准、网络靶场、仿真器和硬件在环证据。

这些能力只有在研究问题和数据条件确实需要时才加入，不作为装饰性“创新模块”。

## 可以完成什么

| 任务 | 典型输出 |
|---|---|
| 新方向与研究包分析 | scope lock、研究问题、主张、证据轨道、终止条件 |
| 全文新颖性审计 | closest-work matrix、负面证据、must-cite list、主张收缩 |
| 数学模型与推导 | 状态/单位/信息契约、定理依赖、最优性或均衡条件 |
| 实验与仿真设计 | 拓扑卡、基线、种子/参数矩阵、独立求解器检查 |
| IEEE 论文写作 | 摘要、Introduction、贡献链、方法、结果与局限 |
| 投稿前检查 | claim–evidence 对齐、过度主张、理论—代码偏差、隐私版权 |
| 审稿回复 | comment–action–evidence ledger、逐条回复与剩余风险 |

## 快速安装

该仓库目前为私有仓库，需要先完成 GitHub CLI 登录：

```bash
gh auth login
gh repo clone LYang910920/luxing-ieee-transactions-skill \
  "${CODEX_HOME:-$HOME/.codex}/skills/luxing-ieee-transactions"
```

安装后可以用自然语言触发，例如：

```text
使用 $luxing-ieee-transactions 开始一个新的 TIFS 研究方向。
使用我的论文风格，分析这个新方向并给出 GO / NO-GO 条件。
按照我的 TIFS 风格，先做全文新颖性审计，再开始推导和仿真。
检查这篇论文的理论—代码—证据是否闭环。
为这篇 Stackelberg 微分博弈论文生成 IEEE Transactions 结构与实验计划。
```

## 证据基础与边界

当前版本为 `v0.3.1`，状态为 `attachment-key-corpus-calibrated`：

- 42 篇作者提供的关键论文全文用于本地派生分析；
- 20 篇 first/corresponding-author 核心语料用于较强的个人文风信号；
- 17 篇 IEEE Transactions 全文用于期刊结构与研究架构校准；
- 当前 17 篇优先 Transactions 论文均有私有全文；
- 1 篇不同技术子领域论文由作者明确标为非优先。

> [!NOTE]
> 这些数字描述的是关键论文语料，不代表已核验完整发表全集。共同作者论文也不自动等于个人逐句写作风格；无明确写作角色的论文主要用于研究架构、方法组合和实验设计。

仓库只保留书目信息、哈希、派生指标和改写后的 paper cards，**不包含论文 PDF、抽取正文、图表、公式原文、Deakin 下载文件或其他受限材料**。

## 证据轨道

| Track | 主要证据 | 默认允许的主张边界 |
|---|---|---|
| A | 机制模型、形式结果、核验数值 | 声明假设下的行为与条件 |
| B | 随机、智能体、事件驱动或闭环仿真 | 仿真器假设下的策略分布行为 |
| C | 观测拓扑/轨迹与合成或反事实动态 | 对观测结构或记录条件的敏感性 |
| D | 真实数据校准与留出预测 | 观测模型下的拟合、有效参数和预测 |
| E | 靶场、仿真、硬件在环或现场证据 | 有边界的可行性与实测行为 |

真实拓扑加合成传播只能称为 `real-topology simulation`，不能升级为真实世界验证。

## 仓库入口

- [`SKILL.md`](SKILL.md)：Codex 运行时主入口与路由。
- [`references/PERSONAL_RESEARCH_DIRECTIONS.md`](references/PERSONAL_RESEARCH_DIRECTIONS.md)：个人研究方向与成熟度。
- [`references/PERSONAL_STYLE_PROFILE.md`](references/PERSONAL_STYLE_PROFILE.md)：个人写作和论证结构。
- [`references/RESEARCH_PIPELINE.md`](references/RESEARCH_PIPELINE.md)：端到端研究流程。
- [`references/QUALITY_GATES.md`](references/QUALITY_GATES.md)：理论、算法、证据与主张门槛。
- [`references/THIRD_PARTY_NOTICES.md`](references/THIRD_PARTY_NOTICES.md)：版权、论文和第三方材料边界。
- [`assets/templates/`](assets/templates/)：项目、证据、数据、拓扑和论文模板。
- [`scripts/luxing_ieee.py`](scripts/luxing_ieee.py)：校验、预检、脚手架和证据推荐工具。

## 本地校验

```bash
SKILL_DIR="${CODEX_HOME:-$HOME/.codex}/skills/luxing-ieee-transactions"
python "$SKILL_DIR/scripts/luxing_ieee.py" validate
python "$SKILL_DIR/scripts/validate_skill.py" --json
```

## 使用原则

1. 不把个人历史习惯置于事实、数学正确性和当前期刊要求之上。
2. 不模仿历史语法缺陷或机械重复个人常用连接词。
3. 不把共同作者身份直接解释为个人句法所有权。
4. 不把真实拓扑、合成参数或一次收敛运行包装成现场验证或全局最优。
5. 不隐藏不利文献、失败实验、不可识别性或使方向失效的结果。

## License

SKILL 工作流与原创模板按 [`LICENSE`](LICENSE) 授权。论文、数据集、教学仓库及其他第三方材料仍受各自权利和许可约束；本仓库不会重新授权这些内容。

---

**English summary:** A strongly personalized Codex skill for Lu-Xing Yang's IEEE Transactions research workflow in cybersecurity, network dynamics, optimal/impulse control, differential and Stackelberg games, topology-aware simulation, and evidence-bounded academic writing. It is intentionally opinionated and is not a universal template for every researcher or paper.
