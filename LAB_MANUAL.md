# GitHub Actions 实验手册

## 实验概述

本实验将通过一个 Python 计算器项目，帮助您全面掌握 GitHub Actions 的使用方法和 CI/CD 最佳实践。

### 实验目标

1. 理解 GitHub Actions 的核心概念和工作流程
2. 学会编写和配置 GitHub Actions 工作流
3. 掌握自动化测试、代码质量检查、构建和发布流程
4. 了解多环境矩阵测试和定时任务
5. 实践 CI/CD 最佳实践

### 实验时长

预计 2-3 小时

### 前置要求

- 基本的 Git 操作知识
- Python 基础知识
- GitHub 账号
- 本地安装 Python 3.8+

---

## 第一部分：GitHub Actions 基础知识

### 1.1 什么是 GitHub Actions？

GitHub Actions 是 GitHub 提供的持续集成和持续部署（CI/CD）平台，允许您自动化构建、测试和部署流程。

### 1.2 核心概念

#### Workflow（工作流）
- 定义在 `.github/workflows/` 目录下的 YAML 文件
- 包含一个或多个 Job
- 由特定事件触发

#### Event（事件）
触发工作流的操作，例如：
- `push` - 代码推送
- `pull_request` - 拉取请求
- `schedule` - 定时触发
- `workflow_dispatch` - 手动触发

#### Job（任务）
- 一组在同一运行器上执行的步骤
- 默认情况下并行运行
- 可以配置依赖关系

#### Step（步骤）
- Job 中的单个任务
- 可以运行命令或使用 Action

#### Action（动作）
- 可重用的代码单元
- 可以是自己编写的，也可以使用社区提供的

#### Runner（运行器）
- 执行工作流的服务器
- GitHub 提供托管运行器（Ubuntu, Windows, macOS）
- 也可以使用自托管运行器

---

## 第二部分：环境准备

### 2.1 克隆实验项目

```bash
# 1. Fork 本项目到您的 GitHub 账号

# 2. 克隆到本地
git clone https://github.com/YOUR_USERNAME/github-actions-calculator.git
cd github-actions-calculator

# 3. 查看项目结构
ls -la
```

### 2.2 项目结构说明

```
github-actions-calculator/
├── .github/
│   └── workflows/          # GitHub Actions 工作流配置
│       ├── ci.yml         # 持续集成流程
│       ├── release.yml    # 发布流程
│       ├── matrix.yml     # 多环境测试
│       └── scheduled.yml  # 定时任务
├── calculator/            # 计算器源码
│   ├── __init__.py
│   └── calculator.py
├── tests/                 # 测试代码
│   ├── __init__.py
│   └── test_calculator.py
├── requirements.txt       # 生产依赖
├── requirements-dev.txt   # 开发依赖
├── setup.py              # 包配置
├── pyproject.toml        # 项目配置
├── README.md             # 项目说明
└── LAB_MANUAL.md         # 本实验手册
```

### 2.3 本地环境配置

```bash
# 1. 创建虚拟环境
python -m venv venv

# 2. 激活虚拟环境
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 3. 安装依赖
pip install -r requirements-dev.txt
pip install -e .

# 4. 运行测试验证环境
pytest tests/ -v
```

---

## 第三部分：工作流详解

### 3.1 CI 工作流（ci.yml）

这是最基础和重要的工作流，每次代码推送或创建 PR 时自动运行。

#### 触发条件
```yaml
on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]
  workflow_dispatch:
```

#### 主要功能
1. **代码质量检查**
   - Flake8：代码风格检查
   - Pylint：代码质量分析
   - Black：代码格式化检查

2. **单元测试**
   - 运行所有测试用例
   - 生成测试覆盖率报告
   - 上传覆盖率报告为 artifact

3. **构建检查**
   - 构建 Python 包
   - 验证包的完整性
   - 上传构建产物

#### 关键配置点

**使用缓存加速构建**
```yaml
- uses: actions/setup-python@v5
  with:
    python-version: '3.11'
    cache: 'pip'  # 缓存 pip 依赖
```

**任务依赖关系**
```yaml
jobs:
  test:
    needs: code-quality  # test 依赖于 code-quality
```

**上传 artifacts**
```yaml
- uses: actions/upload-artifact@v4
  with:
    name: coverage-report
    path: htmlcov/
    retention-days: 30
```

### 3.2 发布工作流（release.yml）

自动化版本发布流程。

#### 触发条件
```yaml
on:
  push:
    tags:
      - 'v*.*.*'  # 当推送 v1.0.0 格式的 tag 时触发
  workflow_dispatch:
    inputs:
      version:
        description: '发布版本号'
        required: true
```

#### 主要功能
1. **创建 GitHub Release**
   - 自动生成变更日志
   - 创建 Release 页面
   - 附加构建产物

2. **构建和发布**
   - 运行测试确保质量
   - 构建 Python 包
   - 上传到 PyPI（可选）

#### 使用 Secrets
```yaml
env:
  TWINE_USERNAME: __token__
  TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
```

### 3.3 矩阵测试工作流（matrix.yml）

在多个环境中测试代码兼容性。

#### 矩阵策略
```yaml
strategy:
  fail-fast: false
  matrix:
    os: [ubuntu-latest, windows-latest, macos-latest]
    python-version: ['3.8', '3.9', '3.10', '3.11', '3.12']
    exclude:
      - os: macos-latest
        python-version: '3.8'
```

#### 优势
- 同时在多个环境测试
- 发现平台特定问题
- 验证不同版本兼容性
- 总共运行 14 个测试场景

### 3.4 定时任务工作流（scheduled.yml）

定期执行健康检查和维护任务。

#### Cron 表达式
```yaml
schedule:
  - cron: '0 9 * * *'    # 每天 9:00 UTC
  - cron: '0 2 * * 0'    # 每周日 2:00 UTC
```

#### 不同任务类型
1. **每日健康检查** - 快速测试
2. **每周完整检查** - 全面测试 + 依赖更新检查
3. **安全扫描** - 检查已知漏洞

---

## 第四部分：实验任务

### 任务 1：触发 CI 工作流

**目标**：理解 CI 工作流的触发和执行过程

**步骤**：
1. 修改 `calculator/calculator.py`，添加一个新方法：
   ```python
   def modulo(self, a: float, b: float) -> float:
       """取模运算"""
       if b == 0:
           raise ValueError("除数不能为0")
       return a % b
   ```

2. 提交并推送代码：
   ```bash
   git add .
   git commit -m "Add modulo operation"
   git push origin main
   ```

3. 在 GitHub 上观察：
   - 进入项目页面
   - 点击 "Actions" 标签
   - 查看正在运行的工作流
   - 点击工作流查看详细日志

**观察要点**：
- CI 工作流会自动触发吗？
- 代码质量检查是否通过？
- 测试是否会失败？（因为没有添加测试）

### 任务 2：完善测试并查看覆盖率

**目标**：理解测试在 CI 中的重要性

**步骤**：
1. 在 `tests/test_calculator.py` 中添加测试：
   ```python
   def test_modulo(self):
       """测试取模运算"""
       assert self.calc.modulo(10, 3) == 1
       assert self.calc.modulo(7, 2) == 1
       assert self.calc.modulo(15, 4) == 3

   def test_modulo_by_zero(self):
       """测试模零异常"""
       with pytest.raises(ValueError, match="除数不能为0"):
           self.calc.modulo(10, 0)
   ```

2. 本地运行测试：
   ```bash
   pytest tests/ -v --cov=calculator
   ```

3. 提交并推送：
   ```bash
   git add .
   git commit -m "Add tests for modulo operation"
   git push origin main
   ```

4. 查看 Actions 页面的测试结果和覆盖率报告

### 任务 3：创建 Pull Request

**目标**：了解 PR 触发的 CI 流程

**步骤**：
1. 创建新分支：
   ```bash
   git checkout -b feature/add-factorial
   ```

2. 添加阶乘函数：
   ```python
   def factorial(self, n: int) -> int:
       """计算阶乘"""
       if n < 0:
           raise ValueError("不能对负数求阶乘")
       if n == 0 or n == 1:
           return 1
       result = 1
       for i in range(2, n + 1):
           result *= i
       return result
   ```

3. 添加测试并提交：
   ```bash
   git add .
   git commit -m "Add factorial function"
   git push origin feature/add-factorial
   ```

4. 在 GitHub 上创建 Pull Request

**观察要点**：
- PR 页面会显示 CI 状态吗？
- 可以合并失败的 PR 吗？

### 任务 4：手动触发工作流

**目标**：了解 workflow_dispatch 的使用

**步骤**：
1. 进入 GitHub Actions 页面
2. 选择 "Scheduled - 定时任务" 工作流
3. 点击 "Run workflow" 按钮
4. 选择分支并运行
5. 观察执行结果

### 任务 5：创建发布版本

**目标**：体验自动化发布流程

**步骤**：
1. 确保所有测试通过
2. 创建版本标签：
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```

3. 观察 Actions 页面的 Release 工作流
4. 检查 GitHub Releases 页面

**观察要点**：
- Release 自动创建了吗？
- 变更日志是如何生成的？
- 构建产物在哪里？

### 任务 6：查看矩阵测试结果

**目标**：理解多环境测试的价值

**步骤**：
1. 手动触发 "Matrix - 多环境测试" 工作流
2. 等待所有测试完成（可能需要 10-15 分钟）
3. 查看测试矩阵的可视化结果
4. 检查是否有特定环境的失败

### 任务 7：故意制造失败

**目标**：了解 CI 如何捕获问题

**步骤**：
1. 修改代码引入错误：
   ```python
   def divide(self, a: float, b: float) -> float:
       # 删除零检查
       return a / b
   ```

2. 提交并推送
3. 观察 CI 失败的详细信息
4. 修复问题并重新推送

---

## 第五部分：高级主题

### 5.1 使用 Secrets 管理敏感信息

**配置步骤**：
1. 进入 GitHub 仓库设置
2. 选择 "Secrets and variables" -> "Actions"
3. 点击 "New repository secret"
4. 添加敏感信息（如 API Token）

**在工作流中使用**：
```yaml
env:
  API_TOKEN: ${{ secrets.MY_API_TOKEN }}
```

### 5.2 条件执行

```yaml
steps:
  - name: 仅在主分支执行
    if: github.ref == 'refs/heads/main'
    run: echo "This is the main branch"

  - name: 仅在成功时执行
    if: success()
    run: echo "Previous steps succeeded"

  - name: 总是执行
    if: always()
    run: echo "This always runs"
```

### 5.3 环境变量

```yaml
env:
  # 全局环境变量
  GLOBAL_VAR: value

jobs:
  job1:
    env:
      # Job 级别环境变量
      JOB_VAR: value
    steps:
      - name: Step with env
        env:
          # Step 级别环境变量
          STEP_VAR: value
        run: echo $STEP_VAR
```

### 5.4 复用工作流

创建可复用的工作流：
```yaml
# .github/workflows/reusable.yml
on:
  workflow_call:
    inputs:
      python-version:
        required: true
        type: string

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ inputs.python-version }}
```

调用可复用工作流：
```yaml
jobs:
  call-workflow:
    uses: ./.github/workflows/reusable.yml
    with:
      python-version: '3.11'
```

### 5.5 自定义 Action

创建自己的 Action（action.yml）：
```yaml
name: 'My Custom Action'
description: 'A custom action example'
inputs:
  name:
    description: 'Name to greet'
    required: true
runs:
  using: 'composite'
  steps:
    - run: echo "Hello ${{ inputs.name }}"
      shell: bash
```

---

## 第六部分：最佳实践

### 6.1 工作流设计原则

1. **快速失败**：将快速检查放在前面
2. **并行执行**：独立的 Job 应并行运行
3. **使用缓存**：缓存依赖以加速构建
4. **最小权限**：只授予必要的权限
5. **清晰命名**：使用描述性的 Job 和 Step 名称

### 6.2 安全建议

1. **不要在日志中输出 Secrets**
2. **使用 CODEOWNERS 保护工作流文件**
3. **限制工作流权限**：
   ```yaml
   permissions:
     contents: read
     pull-requests: write
   ```
4. **审查第三方 Actions**
5. **使用固定版本的 Actions**：`uses: actions/checkout@v4`

### 6.3 性能优化

1. **使用缓存**：
   ```yaml
   - uses: actions/cache@v4
     with:
       path: ~/.cache/pip
       key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
   ```

2. **矩阵测试优化**：
   ```yaml
   strategy:
     fail-fast: true  # 一个失败就停止其他
   ```

3. **条件执行**：避免不必要的步骤
4. **工件保留期**：适当设置 retention-days

### 6.4 调试技巧

1. **启用调试日志**：
   - 在仓库设置 Secret：`ACTIONS_STEP_DEBUG = true`
   - 在仓库设置 Secret：`ACTIONS_RUNNER_DEBUG = true`

2. **使用 tmate 调试**：
   ```yaml
   - name: Setup tmate session
     uses: mxschmitt/action-tmate@v3
   ```

3. **本地测试工作流**：
   使用 [act](https://github.com/nektos/act) 工具

---

## 第七部分：常见问题

### Q1: 工作流没有触发？
**解决方案**：
- 检查 YAML 语法是否正确
- 确认文件位于 `.github/workflows/` 目录
- 检查分支保护规则
- 查看 Actions 是否被禁用

### Q2: 测试超时？
**解决方案**：
- 增加超时设置：`timeout-minutes: 30`
- 优化测试代码
- 使用并行测试

### Q3: 权限错误？
**解决方案**：
```yaml
permissions:
  contents: write
  pull-requests: write
```

### Q4: 依赖安装失败？
**解决方案**：
- 检查 requirements.txt 格式
- 指定明确的版本号
- 使用 `pip install --upgrade pip`

### Q5: Artifacts 找不到？
**解决方案**：
- 检查 path 是否正确
- 确认文件已生成
- 查看 retention-days 设置

---

## 第八部分：扩展练习

### 练习 1: 添加代码覆盖率徽章
在 README.md 中添加覆盖率徽章，使用 Codecov 或 Coveralls

### 练习 2: 集成代码质量工具
添加 SonarQube 或 CodeClimate 集成

### 练习 3: 实现自动依赖更新
使用 Dependabot 自动创建依赖更新 PR

### 练习 4: 添加容器化部署
创建 Dockerfile 并在工作流中构建 Docker 镜像

### 练习 5: 多阶段部署
实现 Dev -> Staging -> Production 的部署流程

---

## 第九部分：参考资源

### 官方文档
- [GitHub Actions 文档](https://docs.github.com/actions)
- [工作流语法](https://docs.github.com/actions/reference/workflow-syntax-for-github-actions)
- [GitHub Actions Marketplace](https://github.com/marketplace?type=actions)

### 常用 Actions
- `actions/checkout@v4` - 检出代码
- `actions/setup-python@v5` - 设置 Python
- `actions/cache@v4` - 缓存依赖
- `actions/upload-artifact@v4` - 上传产物
- `codecov/codecov-action@v3` - 上传覆盖率

### 学习资源
- [GitHub Skills](https://skills.github.com/)
- [Awesome Actions](https://github.com/sdras/awesome-actions)

---

## 实验总结

完成本实验后，您应该能够：

- ✅ 理解 GitHub Actions 的核心概念
- ✅ 编写和配置 CI/CD 工作流
- ✅ 实现自动化测试和代码质量检查
- ✅ 配置多环境测试矩阵
- ✅ 设置定时任务和自动发布
- ✅ 调试和优化工作流
- ✅ 应用 CI/CD 最佳实践

## 下一步

1. 将所学应用到自己的项目中
2. 探索更多高级特性（如自定义 Action）
3. 参与开源项目，学习他们的 CI/CD 实践
4. 关注 GitHub Actions 的最新更新

---

**祝您学习愉快！如有问题，请提交 Issue。**
