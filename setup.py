from setuptools import setup, find_packages

setup(
    name="TikTokenCost",
    version="0.3",
    packages=find_packages(),
    install_requires=[
        "tiktoken",
        "requests"
    ],
    author="Tu Nombre",
    author_email="tu_email@example.com",
    description="Module to estimate inference and training costs with each OpenAI model, over certain texts.",
    keywords="openai tiktoken cost calculator",
)