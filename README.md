# THE AL Medical Agent

医学PET-CT AI诊断系统 - 基于Hermes智能体 + 医学大模型

## 🏥 项目概述

这是一个集成了医学影像AI模型的智能诊断系统，通过Hermes智能体框架进行任务编排和多模型协同。

### 核心功能

- **智能任务规划**：Hermes智能体自动拆解诊断任务
- **多模型协同**：CT→PET生成、多器官分割、肿瘤检测
- **会话记忆管理**：完整的病历历史和诊断上下文
- **实时报告生成**：基于医学大模型的诊断报告
- **医学方案生成**：个性化治疗方案推荐

## 📁 项目架构

```
project/
├── static/                          # 前端HTML页面
├── api/
│   ├── fastapi_app.py              # FastAPI主入口
│   └── routes.py                   # 智能体API路由
├── business/
│   ├── unet_model.py               # U-Net分割模型
│   ├── spark_report.py             # 报告生成
│   ├── treatment_plan.py           # 治疗方案
│   └── medical_models.py           # 医学模型适配器
├── db/
│   ├── models.py                   # SQLAlchemy数据模型
│   └── database.py                 # 数据库连接
├── hermes_agent/
│   ├── __init__.py
│   ├── agent_core.py               # 智能体核心
│   ├── memory_manager.py           # 会话记忆
│   ├── task_planner.py             # 任务规划
│   ├── tool_registry.py            # 工具注册
│   ├── plugins/                    # 医学模型插件
│   │   ├── base.py
│   │   ├── cpdm_plugin.py          # CT→PET生成
│   │   ├── moose_plugin.py         # 多器官分割
│   │   └── autopet_plugin.py       # 肿瘤分割
│   └── prompts/
│       └── medical_prompts.yaml    # 提示词模板
├── utils/
│   ├── logger.py                   # 日志工具
│   └── config.py                   # 配置管理
├── requirements.txt                # Python依赖
├── main.py                         # 统一启动入口
└── .env.example                    # 环境变量示例
```

## 🚀 快速开始

### 1. 环境准备

\`\`\`bash
git clone https://github.com/liuQB52/THE-AL-medical-agent.git
cd THE-AL-medical-agent

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\\Scripts\\activate  # Windows

# 安装依赖
pip install -r requirements.txt
\`\`\`

### 2. 配置环境变量

\`\`\`bash
cp .env.example .env
# 编辑 .env 文件，配置API密钥和模型路径
\`\`\`

### 3. 启动应用

\`\`\`bash
python main.py
\`\`\`

应用将在 \`http://localhost:8000\` 启动。

## 📚 核心模块说明

### Hermes智能体框架

#### agent_core.py - 智能体中枢
\`\`\`python
from hermes_agent.agent_core import HermesAgent

agent = HermesAgent(patient_id=\"P12345\")
result = agent.execute(task=\"分析PET-CT影像并生成诊断报告\")
\`\`\`

#### memory_manager.py - 会话记忆
\`\`\`python
from hermes_agent.memory_manager import MemoryManager

memory = MemoryManager(patient_id=\"P12345\")
memory.add_context({\"type\": \"diagnosis\", \"findings\": [...]})
\`\`\`

#### task_planner.py - 任务规划
\`\`\`python
from hermes_agent.task_planner import TaskPlanner

planner = TaskPlanner()
tasks = planner.decompose(\"进行全身PET-CT分析\")
\`\`\`

### 医学模型插件

#### CPDM - CT→PET生成
\`\`\`python
from hermes_agent.plugins.cpdm_plugin import CPDMPlugin

cpdm = CPDMPlugin(model_path=\"./models/cpdm.pt\")
pet_image = cpdm.translate(ct_image, quality=\"high\")
\`\`\`

#### MOOSE - 多器官分割
\`\`\`python
from hermes_agent.plugins.moose_plugin import MOOSEPlugin

moose = MOOSEPlugin()
segmentation = moose.segment(pet_ct_image)
\`\`\`

#### autoPET - 肿瘤分割
\`\`\`python
from hermes_agent.plugins.autopet_plugin import AutoPETPlugin

autopet = AutoPETPlugin()
tumor_mask = autopet.segment_tumor(pet_ct_image)
\`\`\`

## 🔌 API端点

### POST /api/agent/diagnose
诊断PET-CT影像

### POST /api/agent/plan
生成治疗方案

### GET /api/agent/memory/<patient_id>
获取患者会话记忆

## 📜 许可证

MIT License
"