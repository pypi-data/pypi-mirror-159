import setuptools


with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="EasyIPCLarge",
    version="0.8.0",
    author="YunWen",
    author_email="yunwen@xiaobing.ai",
    description="A library for high-speed transfer of large data between processes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    license="MIT",
    python_requires=" >= 3.8",
    install_requires=[
        'thrift >= 0.16.0',
    ]
)
