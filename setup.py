from setuptools import setup, find_packages

setup(
    name="terrk",
    version="0.1.0",
    description="A simple CLI tool for managing Terraform cloud resources",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="ayomodu",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "click>=8.1.7",
        "requests>=2.32.3",
        "PyYaml>=6.0.2",
        "prettytable>=3.12.0",
        "python-dateutil>=2.9.0",
        "pandas>=2.2.3",
        "openpyxl>=3.1.5",
        "pydantic>=2.10.4",
        "jsonschema>=4.23.0"
    ],
    entry_points={
        "console_scripts": [
            "terrk=terrk.__main__:cli",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11,<3.14",
)
