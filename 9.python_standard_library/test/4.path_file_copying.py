from pathlib import Path

import shutil

source_path = Path("9.python_standard_library/4.path_file_copying.py")

target_path = Path("9.python_standard_library/test")

shutil.copy(source_path,target_path)