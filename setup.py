import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tigosdk",
    version="0.0.1",
    author="Pius Alfred",
    author_email="me.pius1102@gmail.com",
    description="Tigo Push Pay API wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/piusalfred/tigopesasdk",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
)

