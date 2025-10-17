"""
Setup configuration for calculator package
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="github-actions-calculator",
    version="1.0.0",
    author="GitHub Actions Lab",
    author_email="lab@example.com",
    description="一个用于演示 GitHub Actions CI/CD 的简单计算器库",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/github-actions-calculator",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "flake8>=6.0.0",
            "pylint>=2.17.0",
            "black>=23.7.0",
        ],
    },
)
