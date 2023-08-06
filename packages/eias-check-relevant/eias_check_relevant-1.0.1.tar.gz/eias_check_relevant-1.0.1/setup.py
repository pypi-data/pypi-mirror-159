import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="eias_check_relevant",
    version="1.0.1",
    author="J4CK_VVH173",
    author_email="i78901234567890@gmail.com",
    description="A small package that checks date relevant for EIAS system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/J4CKVVH173/eias_check_relevant",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
