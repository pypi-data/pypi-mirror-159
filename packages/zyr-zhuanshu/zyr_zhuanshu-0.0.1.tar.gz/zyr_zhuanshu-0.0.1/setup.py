import setuptools

with open("README.txt", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zyr_zhuanshu",
    version="0.0.1",
    author="zyr_studio",
    author_email="hexin991@qq.com",
    description="zyr_zhuanshu",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jamwusjki/zyr_zhuanshu",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)