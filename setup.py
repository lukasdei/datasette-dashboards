from pathlib import Path
from setuptools import setup


VERSION = "0.1"


def get_long_description():
    readme_path = Path(__file__).parent / "README.md"
    with open(readme_path.absolute(), mode="r", encoding="utf8") as fp:
        return fp.read()


setup(
    name="datasette-dashboards",
    description="Datasette plugin providing data dashboards from metadata",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Romain Clement",
    url="https://github.com/rclement/datasette-dashboards",
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_dashboards"],
    entry_points={"datasette": ["dashboards = datasette_dashboards"]},
    install_requires=["datasette"],
    extras_require={"test": ["pytest", "pytest-asyncio"]},
    tests_require=["datasette-my-plugin[test]"],
    package_data={"datasette_dashboards": ["templates/*.html", "static/*"]},
)