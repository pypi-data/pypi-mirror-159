from zipfile import ZipFile
from pathlib import Path
source = Path("__init__.py").read_text()
target = Path(
    r"C:\Users\gs-3583\Documents\python_boto_project\module_practice\__init__.py")
target.write_text(source)
dir = Path(r"module_practice")
file_list = dir.rglob("*.py")


with ZipFile("myfile.zip", "w") as zipdir:
    for files in file_list:
        zipdir.write(files)

with ZipFile("myfile.zip", "r") as zipdir:
    zipdir.extractall("extracteddir")
