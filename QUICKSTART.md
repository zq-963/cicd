# 快速开始指南

欢迎使用 GitHub Actions 实验项目！本指南将帮助您在 5 分钟内启动并运行。

## 📋 前提条件

- Git
- Python 3.8 或更高版本
- GitHub 账号

## 🚀 5 分钟快速开始

### 步骤 1: Fork 并克隆项目（1 分钟）

```bash
# 1. 在 GitHub 上 Fork 本项目
# 2. 克隆到本地（替换 YOUR_USERNAME）
git clone https://github.com/YOUR_USERNAME/github-actions-calculator.git
cd github-actions-calculator
```

### 步骤 2: 设置 Python 环境（2 分钟）

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 安装依赖
pip install -r requirements-dev.txt
pip install -e .
```

### 步骤 3: 运行测试（1 分钟）

```bash
# 运行所有测试
pytest tests/ -v

# 查看覆盖率
pytest tests/ --cov=calculator --cov-report=term
```

预期输出：
```
===== test session starts =====
collected 11 items

tests/test_calculator.py::TestCalculator::test_add PASSED
tests/test_calculator.py::TestCalculator::test_subtract PASSED
...
===== 11 passed in 0.15s =====
```

### 步骤 4: 触发 GitHub Actions（1 分钟）

```bash
# 创建一个小改动
echo "# Test commit" >> README.md

# 提交并推送
git add .
git commit -m "Test: Trigger GitHub Actions"
git push origin main
```

### 步骤 5: 查看工作流运行

1. 访问您的 GitHub 仓库
2. 点击 "Actions" 标签
3. 查看正在运行的 "CI - 持续集成" 工作流
4. 点击进入查看详细日志

🎉 **恭喜！您已成功触发第一个 GitHub Actions 工作流！**

## 📚 下一步

### 了解项目结构
```
.github/workflows/  ← GitHub Actions 配置文件
calculator/         ← Python 源代码
tests/             ← 测试代码
```

### 查看工作流

项目包含 4 个工作流：

1. **[ci.yml](.github/workflows/ci.yml)** - 代码质量检查和测试
2. **[release.yml](.github/workflows/release.yml)** - 自动发布
3. **[matrix.yml](.github/workflows/matrix.yml)** - 多环境测试
4. **[scheduled.yml](.github/workflows/scheduled.yml)** - 定时任务

### 深入学习

阅读完整的实验手册：[LAB_MANUAL.md](LAB_MANUAL.md)

实验手册包含：
- GitHub Actions 核心概念
- 详细的工作流讲解
- 7 个实践任务
- 最佳实践和常见问题

## 🎯 快速实践任务

### 任务 1: 添加一个新功能（5 分钟）

```bash
# 1. 在 calculator/calculator.py 添加方法
def modulo(self, a: float, b: float) -> float:
    """取模运算"""
    if b == 0:
        raise ValueError("除数不能为0")
    return a % b

# 2. 在 tests/test_calculator.py 添加测试
def test_modulo(self):
    assert self.calc.modulo(10, 3) == 1

# 3. 运行测试
pytest tests/ -v

# 4. 提交并查看 CI
git add .
git commit -m "feat: Add modulo operation"
git push
```

### 任务 2: 创建 Pull Request（3 分钟）

```bash
# 1. 创建新分支
git checkout -b feature/my-feature

# 2. 做一些修改，例如改进文档
echo "## My Improvement" >> README.md

# 3. 提交并推送
git add .
git commit -m "docs: Improve documentation"
git push origin feature/my-feature

# 4. 在 GitHub 上创建 Pull Request
# 5. 观察 CI 在 PR 中的运行
```

### 任务 3: 手动触发工作流（2 分钟）

1. 进入 GitHub Actions 页面
2. 选择 "Scheduled - 定时任务"
3. 点击 "Run workflow"
4. 选择 main 分支并运行
5. 观察执行过程

## 🔧 常用命令

```bash
# 运行测试
pytest tests/ -v

# 查看覆盖率
pytest tests/ --cov=calculator --cov-report=html
open htmlcov/index.html  # 查看 HTML 报告

# 代码检查
flake8 calculator tests
pylint calculator

# 格式化代码
black calculator tests

# 查看 Git 状态
git status

# 查看远程仓库
git remote -v
```

## ❓ 遇到问题？

### 测试失败？
```bash
# 查看详细输出
pytest tests/ -vv
```

### 导入错误？
```bash
# 确保已安装包
pip install -e .
```

### GitHub Actions 没触发？
- 检查 `.github/workflows/` 文件是否存在
- 确认已推送到正确的分支（main 或 develop）
- 查看仓库 Settings -> Actions 是否启用

### 需要帮助？
- 查看 [LAB_MANUAL.md](LAB_MANUAL.md) 的常见问题部分
- 查看 [README.md](README.md) 的详细文档
- 提交 Issue

## 📖 学习路径

**初学者**（1 小时）：
1. ✅ 完成快速开始
2. 📖 阅读 README.md
3. 🎯 完成快速实践任务 1-3

**进阶**（2-3 小时）：
1. 📚 学习 LAB_MANUAL.md
2. 🎯 完成实验手册中的 7 个任务
3. 🔧 探索不同的工作流配置

**专家**（5+ 小时）：
1. 🚀 完成所有扩展练习
2. 🔨 自定义工作流
3. 🌟 应用到自己的项目

## 🎓 成功检查清单

完成以下检查，确保您已掌握基础知识：

- [ ] 成功运行本地测试
- [ ] 触发并查看 CI 工作流
- [ ] 创建并合并 Pull Request
- [ ] 手动触发一个工作流
- [ ] 理解工作流的基本结构
- [ ] 能够添加新功能并编写测试
- [ ] 查看测试覆盖率报告

完成这些，您就可以开始深入学习了！

---

**准备好了吗？开始您的 GitHub Actions 学习之旅吧！** 🚀

有问题随时查看 [LAB_MANUAL.md](LAB_MANUAL.md) 或提交 Issue。
