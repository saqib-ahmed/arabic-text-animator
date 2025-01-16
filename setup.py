from setuptools import setup, find_packages

setup(
    name="arabic_animations",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'pycairo>=1.23.0',
        'PyGObject>=3.44.1',
        'numpy>=1.24.0',
        'opencv-python>=4.8.0',
        'click>=8.1.7',
    ],
    entry_points={
        'console_scripts': [
            'arabic-animate=arabic_animations.main:cli',
        ],
    },
)