import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pychip",
    version="0.0.1",
    author="xchgao",
    author_email="xxx@xxx.com",
    description="A python-based Hardware Description Language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords= ["HDL","hardware design","ASIC","FPGA","Verilog"],
    url="https://github.com/xchgao",
    project_urls={
        "Bug Tracker": "https://github.com/xchgao/PyChip/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(exclude=["test"]),
    python_requires=">=3.9",
)