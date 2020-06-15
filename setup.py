from setuptools import setup, find_packages
requires = ["flask","python-dotenv"]

setup(
    name="musicBoxServer",
    version="0.0.0",
    description="Flask server",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)
