# GitHub Actions 计算器 - CI/CD 实验项目

[![CI Status](https://github.com/yourusername/github-actions-calculator/workflows/CI%20-%20%E6%8C%81%E7%BB%AD%E9%9B%86%E6%88%90/badge.svg)](https://github.com/yourusername/github-actions-calculator/actions)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

一个用于学习和演示 GitHub Actions CI/CD 流程的 Python 计算器项目。

## 项目简介

这是一个完整的 GitHub Actions 实验项目，通过一个简单的 Python 计算器库，全面展示了如何使用 GitHub Actions 实现：

- ✅ 自动化测试和代码质量检查
- ✅ 多环境矩阵测试
- ✅ 自动化构建和发布
- ✅ 定时任务和健康检查
- ✅ CI/CD 最佳实践

## 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/yourusername/github-actions-calculator.git
cd github-actions-calculator
```

### 2. 安装依赖

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 安装开发依赖
pip install -r requirements-dev.txt
pip install -e .
```

### 3. 运行测试

```bash
# 运行所有测试
pytest tests/ -v

# 运行测试并查看覆盖率
pytest tests/ -v --cov=calculator --cov-report=term --cov-report=html
```

### 4. 代码质量检查

```bash
# 代码风格检查
flake8 calculator tests

# 代码质量分析
pylint calculator

# 代码格式化检查
black --check calculator tests
```

## 功能特性

### 计算器功能

- 基本运算：加、减、乘、除
- 高级运算：幂运算、平方根
- 完整的错误处理（除零、负数平方根等）
- 100% 测试覆盖率

### GitHub Actions 工作流

#### 🔄 CI 工作流（[ci.yml](.github/workflows/ci.yml)）

**触发条件**：推送到 main/develop 分支，或创建 Pull Request

**功能**：
- 代码质量检查（Flake8, Pylint, Black）
- 单元测试和覆盖率报告
- 构建检查和产物上传

**运行时间**：约 3-5 分钟

#### 🚀 发布工作流（[release.yml](.github/workflows/release.yml)）

**触发条件**：推送版本标签（v*.*.* ）

**功能**：
- 自动创建 GitHub Release
- 生成变更日志
- 构建并发布 Python 包

**使用示例**：
```bash
git tag v1.0.0
git push origin v1.0.0
```

#### 🧪 矩阵测试工作流（[matrix.yml](.github/workflows/matrix.yml)）

**触发条件**：推送到 main，PR，每周一定时运行

**测试环境**：
- 操作系统：Ubuntu, Windows, macOS
- Python 版本：3.8, 3.9, 3.10, 3.11, 3.12
- 总共 14 个测试场景

**运行时间**：约 10-15 分钟

#### ⏰ 定时任务工作流（[scheduled.yml](.github/workflows/scheduled.yml)）

**触发条件**：
- 每天 9:00 UTC - 快速健康检查
- 每周日 2:00 UTC - 完整检查

**功能**：
- 代码质量监控
- 依赖更新检查
- 安全漏洞扫描

## 项目结构

```
github-actions-calculator/
├── .github/
│   └── workflows/          # GitHub Actions 工作流配置
│       ├── ci.yml         # 持续集成
│       ├── release.yml    # 自动发布
│       ├── matrix.yml     # 多环境测试
│       └── scheduled.yml  # 定时任务
│
├── calculator/            # 源码
│   ├── __init__.py
│   └── calculator.py      # 计算器实现
│
├── tests/                 # 测试代码
│   ├── __init__.py
│   └── test_calculator.py # 单元测试
│
├── requirements.txt       # 生产依赖（无）
├── requirements-dev.txt   # 开发依赖
├── setup.py              # 包配置
├── pyproject.toml        # 项目配置
├── pytest.ini            # Pytest 配置（可选）
├── .gitignore            # Git 忽略规则
├── LICENSE               # MIT 许可证
├── README.md             # 本文件
└── LAB_MANUAL.md         # 详细实验手册
```

## 使用指南

### 基本使用

```python
from calculator import Calculator

calc = Calculator()

# 基本运算
print(calc.add(5, 3))        # 8
print(calc.subtract(10, 4))  # 6
print(calc.multiply(3, 7))   # 21
print(calc.divide(15, 3))    # 5.0

# 高级运算
print(calc.power(2, 3))      # 8
print(calc.square_root(16))  # 4.0
```

### 错误处理

```python
try:
    calc.divide(10, 0)
except ValueError as e:
    print(e)  # "除数不能为0"

try:
    calc.square_root(-1)
except ValueError as e:
    print(e)  # "不能对负数求平方根"
```

## 实验教程

详细的实验步骤和教程，请查看 [LAB_MANUAL.md](LAB_MANUAL.md)

实验内容包括：
1. GitHub Actions 基础知识
2. 环境准备和配置
3. 各个工作流的详细讲解
4. 7 个实践任务
5. 高级主题和最佳实践
6. 常见问题解答
7. 扩展练习

预计学习时间：2-3 小时

## 开发指南

### 添加新功能

1. 创建新分支：
   ```bash
   git checkout -b feature/new-operation
   ```

2. 在 `calculator/calculator.py` 中添加新方法

3. 在 `tests/test_calculator.py` 中添加测试

4. 本地运行测试：
   ```bash
   pytest tests/ -v --cov=calculator
   ```

5. 提交并创建 Pull Request：
   ```bash
   git add .
   git commit -m "Add new operation"
   git push origin feature/new-operation
   ```

### 代码规范

- 遵循 PEP 8 代码风格
- 所有函数必须有文档字符串
- 测试覆盖率应保持在 100%
- 使用类型提示（Type Hints）

### 提交规范

提交信息格式：
```
<type>: <subject>

<body>
```

类型（type）：
- `feat`: 新功能
- `fix`: 修复 bug
- `docs`: 文档更新
- `style`: 代码格式调整
- `refactor`: 代码重构
- `test`: 测试相关
- `chore`: 构建/工具相关

示例：
```
feat: Add modulo operation

- Add modulo method to Calculator class
- Add comprehensive tests
- Update documentation
```

## GitHub Actions 详解

### 查看工作流状态

1. 进入项目的 GitHub 页面
2. 点击 "Actions" 标签
3. 查看所有工作流的运行历史

### 手动触发工作流

部分工作流支持手动触发：

1. 进入 Actions 页面
2. 选择要运行的工作流
3. 点击 "Run workflow"
4. 选择分支并运行

### 查看测试报告

测试覆盖率报告以 artifact 形式保存：

1. 进入具体的工作流运行
2. 滚动到页面底部
3. 在 "Artifacts" 部分下载报告
4. 解压并打开 `index.html`

## 常见问题

### Q: 工作流没有自动触发？

**A**: 检查以下几点：
- 确认 `.github/workflows/` 目录下的 YAML 文件语法正确
- 检查触发条件（分支名称、事件类型）
- 查看仓库的 Actions 设置是否启用

### Q: 测试在本地通过，但在 CI 中失败？

**A**: 可能的原因：
- 环境差异（操作系统、Python 版本）
- 依赖版本不一致
- 时区或路径问题

解决方法：
- 使用矩阵测试验证多环境
- 在 `requirements-dev.txt` 中固定版本
- 使用 `pytest -v` 查看详细错误信息

### Q: 如何添加自己的 secrets？

**A**:
1. 进入仓库 Settings
2. 选择 "Secrets and variables" -> "Actions"
3. 点击 "New repository secret"
4. 在工作流中使用：`${{ secrets.YOUR_SECRET }}`

## 贡献指南

欢迎贡献！请遵循以下步骤：

1. Fork 本项目
2. 创建功能分支（`git checkout -b feature/AmazingFeature`）
3. 提交更改（`git commit -m 'Add some AmazingFeature'`）
4. 推送到分支（`git push origin feature/AmazingFeature`）
5. 创建 Pull Request

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 致谢

- [GitHub Actions](https://github.com/features/actions) - CI/CD 平台
- [pytest](https://pytest.org/) - 测试框架
- [pytest-cov](https://pytest-cov.readthedocs.io/) - 覆盖率插件

## 联系方式

如有问题或建议，请：
- 提交 [Issue](https://github.com/yourusername/github-actions-calculator/issues)
- 创建 [Pull Request](https://github.com/yourusername/github-actions-calculator/pulls)

## 相关资源

- [实验手册](LAB_MANUAL.md) - 详细的实验教程
- [GitHub Actions 文档](https://docs.github.com/actions)
- [Python 打包指南](https://packaging.python.org/)
- [pytest 文档](https://docs.pytest.org/)

---

**Happy Learning! 🚀**
