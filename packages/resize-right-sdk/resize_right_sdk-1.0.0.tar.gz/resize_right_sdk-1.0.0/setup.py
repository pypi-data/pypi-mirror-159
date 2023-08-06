from setuptools import setup, find_packages

setup(
    name="resize_right_sdk",
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=["blobfile>=1.0.5", "torch", "tqdm"],
)
