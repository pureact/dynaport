import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dynaport",
    version="0.0.6",
    author="naek",
    author_email="naek2k@outlook.com",
    description="dynamic module importer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/naek2k/dynaport",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=2",
)
