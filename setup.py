from setuptools import setup, find_packages
with open("README.md", "r") as readme_file:
    readme = readme_file.read()
requirements = [
    "scikit-learn==1.0.2",
    "scipy==1.8.0",
    "numpy==1.21.5"
]
setup(
    name="ChE4230",
    version="1.0.0",
    author="Blake Nassar",
    author_email="bnassa1@lsu.edu",
    description="I be coding and shit",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/BlakeNassar/ChE4230",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.8",
    ],
)