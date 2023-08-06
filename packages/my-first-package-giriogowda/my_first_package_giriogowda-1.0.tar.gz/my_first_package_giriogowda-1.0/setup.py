import setuptools
from pathlib import Path
license_file=Path(r'LICENSE').read_text()
readme_file=Path(r'README.md').read_text()

setuptools.setup(name="my_first_package_giriogowda",
version="1.0",description=readme_file,maintainer_email="gowdagirish333@gmai.com",requires=['pathlib']
,license=license_file,packages=setuptools.find_packages())