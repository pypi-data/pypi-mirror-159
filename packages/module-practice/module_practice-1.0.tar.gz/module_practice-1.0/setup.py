import setuptools
import pathlib
data = pathlib.Path(
    r"C:\Users\gs-3583\Documents\python_boto_project\description.txt").read_text()
setuptools.setup(name="module_practice",
                 version="1.0", long_description=data,
                 license="", packages=setuptools.find_packages(exclude='general_practice'))
