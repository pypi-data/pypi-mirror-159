import setuptools
import pathlib
readmefile = pathlib.Path(r"README.md")
readmefile_license = pathlib.Path(r"LICENSE")


setuptools.setup(name='passwdmakergiri27', 
author_email='gowdagirish333@gmail.com', version='1.0',
long_description=readmefile.read_text(), packages=setuptools.find_packages(exclude=["LICENSE",'README.md',"setup.py"]),
license=readmefile_license.read_text(),requires='sys')
