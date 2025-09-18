```markdown
# RAG (检索增强生成) 学习项目

这是一个简单易懂的RAG（Retrieval-Augmented Generation）技术学习项目，包含了从基础向量化到完整RAG系统实现的示例代码。

## 📋 项目简介

RAG是一种将大型语言模型与外部知识库结合的AI技术，能够：
- 提高回答的准确性和相关性
- 减少模型"幻觉"现象
- 无需重训练即可获取最新信息
- 降低模型维护成本

## 🗂️ 项目结构

```
rag/
├── README.md           # 项目说明文档
├── chunk.py           # 文本分块示例
├── vertstion.py       # 文本向量化示例  
└── test_01.py         # 完整RAG系统实现
```

## 🚀 快速开始

### 环境要求

- Python 3.9+
- pip包管理器

### 安装依赖

```bash
# 安装基础依赖
pip install sentence-transformers torch numpy

# 安装FAISS向量检索库
pip install faiss-cpu

# 如果有GPU可选择安装GPU版本
# pip install faiss-gpu
```

### 运行示例

1. **文本向量化示例**
```bash
python3 vertstion.py
```

2. **完整RAG系统**
```bash
python3 test_01.py
```

## 📚 代码说明

### vertstion.py - 文本向量化
演示如何将中文文本转换为数值向量：
- 使用 `sentence-transformers` 模型
- 支持中文语义理解
- 生成384维向量表示

### test_01.py - 完整RAG实现
包含RAG系统的完整工作流程：

#### 阶段1：离线准备
1. **知识库构建** - 定义文本数据源
2. **文本分块** - 将长文本切分为检索单元
3. **向量化** - 转换为数值向量
4. **索引构建** - 使用FAISS建立检索索引

#### 阶段2：实时问答
1. **问题向量化** - 将用户问题转换为向量
2. **相似性检索** - 从知识库中找到最相关内容
3. **提示词增强** - 结合检索内容和用户问题
4. **生成回答** - 模拟LLM生成最终答案

## 🔧 技术栈

- **sentence-transformers**: 文本向量化模型
- **FAISS**: 高效向量相似性搜索
- **NumPy**: 数值计算支持
- **PyTorch**: 深度学习框架

## ⚠️ 常见问题

### SSL警告
如果看到urllib3的SSL警告，这是正常现象，不影响程序运行。

### FAISS安装问题
如果`pip install faiss-cpu`失败，可尝试：
```bash
# 使用conda安装
conda install -c conda-forge faiss-cpu

# 或升级pip后重试
python3 -m pip install --upgrade pip
pip install faiss-cpu
```

### 模型下载
首次运行会自动下载模型文件（约90MB），请确保网络连接正常。

## 🎯 学习目标

通过这个项目，您将学会：
1. RAG技术的基本原理和工作流程
2. 如何进行文本向量化和语义检索
3. 向量数据库的基本使用方法
4. 如何构建知识问答系统的原型

## 🔜 扩展方向

- 集成真实的LLM API（如OpenAI、Gemini等）
- 支持更多文档格式（PDF、Word等）
- 实现Web界面
- 添加更复杂的文本分块策略
- 支持多模态检索（图文结合）

## 📝 许可证

MIT License

## 🤝 贡献

欢迎提交Issue和Pull Request来改进这个学习项目！

---

**注意**: 这是一个学习用途的简化实现，生产环境使用需要考虑更多因素如安全性、扩展性等。
```

这个README文档包含了：
- 项目介绍和目标
- 完整的安装指南
- 代码结构说明
- 常见问题解决方案
- 学习目标和扩展方向

您可以直接将这个内容保存为 `README.md` 文件上传到GitHub。我来为您创建一个完整的GitHub说明文档：

```markdown
# RAG (检索增强生成) 学习项目

这是一个简单易懂的RAG（Retrieval-Augmented Generation）技术学习项目，包含了从基础向量化到完整RAG系统实现的示例代码。

## 📋 项目简介

RAG是一种将大型语言模型与外部知识库结合的AI技术，能够：
- 提高回答的准确性和相关性
- 减少模型"幻觉"现象
- 无需重训练即可获取最新信息
- 降低模型维护成本

## 🗂️ 项目结构

```
rag/
├── README.md           # 项目说明文档
├── chunk.py           # 文本分块示例
├── vertstion.py       # 文本向量化示例  
└── test_01.py         # 完整RAG系统实现
```

## 🚀 快速开始

### 环境要求

- Python 3.9+
- pip包管理器

### 安装依赖

```bash
# 安装基础依赖
pip install sentence-transformers torch numpy

# 安装FAISS向量检索库
pip install faiss-cpu

# 如果有GPU可选择安装GPU版本
# pip install faiss-gpu
```

### 运行示例

1. **文本向量化示例**
```bash
python3 vertstion.py
```

2. **完整RAG系统**
```bash
python3 test_01.py
```

## 📚 代码说明

### vertstion.py - 文本向量化
演示如何将中文文本转换为数值向量：
- 使用 `sentence-transformers` 模型
- 支持中文语义理解
- 生成384维向量表示

### test_01.py - 完整RAG实现
包含RAG系统的完整工作流程：

#### 阶段1：离线准备
1. **知识库构建** - 定义文本数据源
2. **文本分块** - 将长文本切分为检索单元
3. **向量化** - 转换为数值向量
4. **索引构建** - 使用FAISS建立检索索引

#### 阶段2：实时问答
1. **问题向量化** - 将用户问题转换为向量
2. **相似性检索** - 从知识库中找到最相关内容
3. **提示词增强** - 结合检索内容和用户问题
4. **生成回答** - 模拟LLM生成最终答案

## 🔧 技术栈

- **sentence-transformers**: 文本向量化模型
- **FAISS**: 高效向量相似性搜索
- **NumPy**: 数值计算支持
- **PyTorch**: 深度学习框架

## ⚠️ 常见问题

### SSL警告
如果看到urllib3的SSL警告，这是正常现象，不影响程序运行。

### FAISS安装问题
如果`pip install faiss-cpu`失败，可尝试：
```bash
# 使用conda安装
conda install -c conda-forge faiss-cpu

# 或升级pip后重试
python3 -m pip install --upgrade pip
pip install faiss-cpu
```

### 模型下载
首次运行会自动下载模型文件（约90MB），请确保网络连接正常。

## 🎯 学习目标

通过这个项目，您将学会：
1. RAG技术的基本原理和工作流程
2. 如何进行文本向量化和语义检索
3. 向量数据库的基本使用方法
4. 如何构建知识问答系统的原型

## 🔜 扩展方向

- 集成真实的LLM API（如OpenAI、Gemini等）
- 支持更多文档格式（PDF、Word等）
- 实现Web界面
- 添加更复杂的文本分块策略
- 支持多模态检索（图文结合）

## 📝 许可证

MIT License

## 🤝 贡献

欢迎提交Issue和Pull Request来改进这个学习项目！

---

**注意**: 这是一个学习用途的简化实现，生产环境使用需要考虑更多因素如安全性、扩展性等。
```

这个README文档包含了：
- 项目介绍和目标
- 完整的安装指南
- 代码结构说明
- 常见问题解决方案
- 学习目标和扩展方向

