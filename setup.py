from arabic_animations import __version__
from setuptools import setup, find_packages

setup(
    name="arabic-text-animator",
    version=__version__,
    packages=find_packages(),
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