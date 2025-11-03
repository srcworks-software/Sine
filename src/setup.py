from setuptools import setup, find_packages

setup(
    name="sine-calc",
    version="1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "sine=sine.main:main",
        ],
    },
    data_files=[("share/applications", ["desktop.desktop"])],
)

