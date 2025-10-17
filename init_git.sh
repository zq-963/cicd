#!/bin/bash

# GitHub Actions 计算器项目 - Git 初始化脚本
# 此脚本帮助您快速初始化 Git 仓库并推送到 GitHub

echo "🚀 GitHub Actions 计算器项目 - Git 初始化"
echo "=========================================="
echo ""

# 检查是否已经是 Git 仓库
if [ -d ".git" ]; then
    echo "⚠️  此目录已经是 Git 仓库"
    read -p "是否要重新初始化? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "❌ 已取消"
        exit 1
    fi
    rm -rf .git
fi

# 初始化 Git 仓库
echo "📦 初始化 Git 仓库..."
git init

# 添加所有文件
echo "➕ 添加所有文件..."
git add .

# 创建初始提交
echo "💾 创建初始提交..."
git commit -m "Initial commit: GitHub Actions Calculator Lab

- Add calculator implementation with full test coverage
- Add 4 GitHub Actions workflows (CI, Release, Matrix, Scheduled)
- Add comprehensive documentation (README, LAB_MANUAL, QUICKSTART)
- Add project configuration files

This is a complete CI/CD learning project for GitHub Actions."

echo ""
echo "✅ Git 仓库初始化完成！"
echo ""
echo "📝 下一步："
echo "1. 在 GitHub 上创建一个新仓库"
echo "2. 运行以下命令连接到远程仓库："
echo ""
echo "   git remote add origin https://github.com/YOUR_USERNAME/github-actions-calculator.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "3. 推送后，访问 GitHub 仓库查看 Actions 运行情况"
echo ""
echo "🎉 开始您的 GitHub Actions 学习之旅吧！"
