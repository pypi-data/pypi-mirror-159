import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="beadsnum",
    version="2.0.1",
    author="muzudho",
    author_email="muzudho1@gmail.com",
    description="Beads nested number notation package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/muzudho/beads-nested-number-notation",
    project_urls={
        "Bug Tracker": "https://github.com/muzudho/beads-nested-number-notation/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
