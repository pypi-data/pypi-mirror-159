
from time import ctime
from pathlib import Path
path = Path("path_practice.py")
# print(path.read_text())
sec = path.stat().st_atime
print(ctime(sec))
# print(path.absolute())
# # print(path.exists())
# print(path.suffix)
# print(path.with_name("django.txt"))

# print(path.with_stem("file1"))
# print(path.home())
# print(path.is_dir())
# print(path.is_file())
# print(path.exists())
