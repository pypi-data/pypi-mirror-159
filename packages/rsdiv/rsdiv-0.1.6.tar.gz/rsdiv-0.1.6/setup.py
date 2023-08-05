from pathlib import Path

from setuptools import find_packages, setup

SETUP_DIRECTORY = Path(__file__).resolve().parent

with (SETUP_DIRECTORY / "README.md").open() as ifs:
    LONG_DESCRIPTION = ifs.read()


setup(
    name="rsdiv",
    version="0.1.6",
    author="Yin Cheng",
    author_email="yin.sjtu@gmail.com",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/smartnews/rsdiv",
    python_requires=">=3.6",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
)
