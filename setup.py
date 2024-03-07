from setuptools import setup, find_packages

setup(
    name="TikTokenCost",
    version="0.3",
    packages=find_packages(),
    install_requires=[
        "tiktoken",
        "requests"
    ],
    author="@MrCaabs69",
    author_email="",
    description="Module to estimate inference and training costs with each OpenAI model, over certain texts.",
    keywords="openai tiktoken cost calculator",
)