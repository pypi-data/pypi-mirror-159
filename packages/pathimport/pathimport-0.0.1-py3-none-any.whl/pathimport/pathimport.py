import sys
import inspect
from pathlib import Path


def set_module_root(relative_path: str) -> None:
    """
    Add a module to a path to enable relative imports.

    Parameters
    ----------
    relative_path : Path
        Relative path to the root of the module
    """
    # checking the function stack to obtain the
    # caller Path
    caller_path = Path((inspect.stack()[1])[1])

    # adding the module to PATH
    relative_path = caller_path.parent / Path(relative_path)
    sys.path.append(str(relative_path))
