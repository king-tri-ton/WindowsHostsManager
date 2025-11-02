from setuptools import setup, find_packages

setup(
    name="windows-hosts-manager",
    version="2.0.0",
    author="King Triton",
    description="Кроссплатформенная CLI-утилита для управления файлом hosts (Windows/Linux).",
    packages=find_packages(),
    install_requires=[
        "typer>=0.20.0",
    ],
    entry_points={
        "console_scripts": [
            "whm=whm.cli:app",
        ],
    },
    python_requires=">=3.8",
)
