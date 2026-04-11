# zhi-xue-assistant

## 项目简介
基于本地大模型（DeepSeek R1 / Qwen）的个性化学习助手，支持错题诊断、举一反三、学习报告生成。

## 功能
- 错题知识点识别与错误原因分析
- 自动生成举一反三练习题
- 学习历史记录与周报生成
- 引导式反问与提问深度分析

## 技术栈
- Python + Ollama + DeepSeek R1 7B
- SQLite（数据存储）
- Streamlit（前端界面）

## 运行方法
1. 安装 Ollama：https://ollama.com
2. 下载模型：`ollama run deepseek-r1:7b`
3. 安装依赖：`pip install requests`
4. 运行脚本：`python src/call_model.py`

## 团队成员
- 钱源（软件工程） - 项目负责人、核心开发
- 徐一笑（英语） - 数据与教学设计师
- 郭诗雨（通信工程） - 部署与测试工程师
- 周越（信息安全） - 安全与校验工程师
