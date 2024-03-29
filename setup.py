import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    required = f.read().splitlines()

setuptools.setup(
    name="dutils",
    version="0.1",
    author="Pepijn Boers",
    author_email="pepijnbb@gmail.com",
    description="(D)ashboard utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PepijnBoers/template-dashboard",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=required,
    include_package_data=True,
    python_requires=">=3.6",
)
