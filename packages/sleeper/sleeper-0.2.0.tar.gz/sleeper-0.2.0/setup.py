import setuptools

with open("README.md") as f:
    readMe = f.read()

with open("LICENSE") as f:
    license = f.read()

setuptools.setup(
    name="sleeper",
    version="0.2.0",
    author="Joey Greco",
    author_email="joeyagreco@gmail.com",
    description="A Python wrapper for the Sleeper API.",
    long_description_content_type="text/markdown",
    long_description=readMe,
    license=license,
    packages=setuptools.find_packages(exclude=("test", "docs")),
    install_requires=["requests",
                      "configparser",
                      "setuptools"]
)
