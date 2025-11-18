#!/usr/bin/env python3
"""
Setup script for Transformer Scalability Crisis analysis package.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_path = Path(__file__).parent / "README.md"
long_description = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""

# Read requirements
requirements_path = Path(__file__).parent / "requirements.txt"
if requirements_path.exists():
    with open(requirements_path) as f:
        requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]
else:
    requirements = [
        "pandas>=1.5.0",
        "numpy>=1.21.0", 
        "matplotlib>=3.5.0",
        "seaborn>=0.11.0",
        "scipy>=1.9.0",
        "scikit-learn>=1.1.0"
    ]

setup(
    name="transformer-scalability-crisis",
    version="1.0.0",
    author="Mahdi Naser Moghadasi",
    author_email="mahdi@brightmind-ai.com",
    description="Comprehensive empirical analysis of transformer scalability limitations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brightmind-ai/transformer-scalability-crisis",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.0.0", 
            "flake8>=4.0.0",
        ],
        "docs": [
            "sphinx>=4.0.0",
            "sphinx-rtd-theme>=1.0.0",
        ],
        "jupyter": [
            "jupyter>=1.0.0",
            "ipykernel>=6.0.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "analyze-scalability=scripts.analyze_scalability:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["data/raw/*.csv", "*.md", "*.txt"],
    },
    keywords="transformer, scalability, performance, nlp, machine-learning, benchmarking",
    project_urls={
        "Bug Reports": "https://github.com/brightmind-ai/transformer-scalability-crisis/issues",
        "Source": "https://github.com/brightmind-ai/transformer-scalability-crisis",
        "Documentation": "https://github.com/brightmind-ai/transformer-scalability-crisis/blob/main/README.md",
        "Paper": "https://arxiv.org/abs/XXXX.XXXXX",  # Update with actual arXiv link
    },
)
