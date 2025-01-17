from arabic_animations import __version__
from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="arabic-text-animator",
    version=__version__,
    description="A Python library for creating Arabic text writing animations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Saqib Ahmed",
    author_email="saqibahmed515@gmail.com",
    url="https://github.com/saqib-ahmed/arabic-text-animator",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        'pycairo>=1.23.0',
        'PyGObject>=3.44.1',
        'numpy>=1.24.0',
        'opencv-python>=4.8.0',
        'click>=8.1.7',
        'PyQt5>=5.15.0',
        'mkdocs>=1.5.0',
        'mkdocs-material>=9.0.0',
        'mkdocstrings>=0.24.0',
        'mkdocstrings-python>=1.7.0',
    ],
    extras_require={
        'docs': [
            'mkdocs>=1.5.0',
            'mkdocs-material>=9.0.0',
            'mkdocstrings>=0.24.0',
            'mkdocstrings-python>=1.7.0',
            'mike>=1.1.2',
        ],
    },
    entry_points={
        'console_scripts': [
            'ata=arabic_animations.main:cli',
            'arabic-animate=arabic_animations.main:cli',
        ],
    },
)