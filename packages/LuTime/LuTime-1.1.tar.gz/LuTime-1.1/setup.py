import setuptools
from pathlib import Path

file = Path("README.md")

setuptools.setup(
    name="LuTime",
    version="1.1",
    long_description_content_type="text/markdown",
    long_description=file.read_text(encoding="utf-8"),
    packages=setuptools.find_packages(exclude=["tests", "data"]),
    install_requires=["time", "datetime"]
)
