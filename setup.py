import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="readercake",
    version="0.0.1",
    author="Jaasim",
    author_email="jaasim2008@gmail.com",
    description="A Easy Reader + Writer Module For Python 3.7+",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jaasim2008/ReaderCake-Module",
    project_urls={
        "Bug Tracker": "https://github.com/Jaasim2008/ReaderCake-Module/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)