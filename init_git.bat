@echo off
REM GitHub Actions 计算器项目 - Git 初始化脚本 (Windows)
REM 此脚本帮助您快速初始化 Git 仓库并推送到 GitHub

echo.
echo ================================================
echo    GitHub Actions 计算器项目 - Git 初始化
echo ================================================
echo.

REM 检查是否已经是 Git 仓库
if exist ".git" (
    echo [警告] 此目录已经是 Git 仓库
    set /p confirm="是否要重新初始化? (y/N): "
    if /i not "%confirm%"=="y" (
        echo [已取消] 操作已取消
        exit /b 1
    )
    rmdir /s /q .git
)

REM 初始化 Git 仓库
echo [1/3] 初始化 Git 仓库...
git init

REM 添加所有文件
echo [2/3] 添加所有文件...
git add .

REM 创建初始提交
echo [3/3] 创建初始提交...
git commit -m "Initial commit: GitHub Actions Calculator Lab" -m "- Add calculator implementation with full test coverage" -m "- Add 4 GitHub Actions workflows (CI, Release, Matrix, Scheduled)" -m "- Add comprehensive documentation (README, LAB_MANUAL, QUICKSTART)" -m "- Add project configuration files" -m "" -m "This is a complete CI/CD learning project for GitHub Actions."

echo.
echo ================================================
echo    Git 仓库初始化完成！
echo ================================================
echo.
echo [下一步]
echo 1. 在 GitHub 上创建一个新仓库
echo 2. 运行以下命令连接到远程仓库：
echo.
echo    git remote add origin https://github.com/YOUR_USERNAME/github-actions-calculator.git
echo    git branch -M main
echo    git push -u origin main
echo.
echo 3. 推送后，访问 GitHub 仓库查看 Actions 运行情况
echo.
echo 开始您的 GitHub Actions 学习之旅吧！
echo.
pause
