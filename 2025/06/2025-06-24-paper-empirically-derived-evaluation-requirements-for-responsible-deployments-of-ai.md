# Paper: Empirically derived evaluation requirements for responsible deployments of AI
- URL: https://ferd.ca/notes/paper-empirically-derived-evaluation-requirements-for-responsible-deployments-of-ai.html
- Added At: 2025-06-24 02:03:18
- [Link To Text](2025-06-24-paper-empirically-derived-evaluation-requirements-for-responsible-deployments-of-ai_raw.md)

## Summary
**摘要**：这篇论文研究了在安全关键环境中AI辅助系统对护士和护理学生远程监测患者生命体征性能的影响。通过实验设计，研究人员测试了三种AI辅助模式（带解释的预测、仅预测、仅解释）对450名护理学生和12名持证护士决策的影响。结果显示，当AI预测正确时，人机联合系统表现更好；但当AI出错时，其负面影响是积极影响的两倍。研究特别指出，AI解释并不能有效帮助人类识别和纠正AI错误，反而可能增强错误建议的可信度。作者强调不应仅优化AI算法性能，而应关注人机联合系统的整体表现，并提出评估AI部署的两个关键标准：实证测量人机联合性能，以及考察涵盖AI表现强弱的各种案例。

**要点总结**：
1. **AI辅助的双刃剑效应**：研究发现，当AI预测准确时能提升护理人员判断，但当AI出错时（特别是带有解释的预测），会导致护理人员对紧急和非紧急情况的判断准确度显著下降，负面影响是正面影响的两倍。这揭示了AI辅助系统在增强性能的同时也可能放大错误。

2. **AI解释的局限性**：传统观点认为AI解释能帮助人类审核AI决策，但实验显示解释反而可能增强错误建议的可信度。这与当前软件工程中"可解释AI"的普遍假设形成对比，表明需要重新评估解释机制的实际效果。

3. **经验因素的非决定性**：研究发现护理经验水平对人机联合性能无明显影响，这与另一项针对放射科医生的研究结果一致。这一发现挑战了"资深专业人士能更好处理AI错误"的常见假设。

4. **实验设计的合理性辩护**：虽然实验刻意包含了AI表现极好和极差的案例（而非按实际错误频率），但作者论证这是必要的：一方面真实场景中罕见错误更难纠正，另一方面医疗从业者需要对每个个案而非整体准确率负责，最坏后果决定系统安全性。

5. **评估标准的重构**：论文提出评估AI部署的两大核心要求：必须实证测量人机联合系统性能（而非单独评估AI），并考察AI表现的全范围案例。强调AI开发目标应是"辅助人类完成认知工作"，而非单纯提高算法指标。
