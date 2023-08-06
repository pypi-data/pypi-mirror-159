import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hlfiles",
    version="0.0.1",
    description="Handle lots of files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="UePG",
    author_email="hanlin.warng@gmail.com",
    url="https://github.com/UePG-21/hlfiles",
    license="MIT",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
