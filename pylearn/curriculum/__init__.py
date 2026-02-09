"""Auto-discover curriculum modules from numbered subdirectories."""

import importlib
import pkgutil
import os
import re
from pylearn.curriculum.base import Module


def discover_modules():
    """Scan curriculum subdirectories and load Module objects.

    Each subdirectory (e.g., 01_basics/) must have an __init__.py
    that exposes a `module` variable of type Module.

    Returns:
        List of Module objects sorted by order.
    """
    modules = []
    package_dir = os.path.dirname(__file__)

    for item in sorted(os.listdir(package_dir)):
        item_path = os.path.join(package_dir, item)
        if not os.path.isdir(item_path):
            continue
        # Match numbered directories like 01_basics, 02_data_types
        match = re.match(r"^(\d+)_", item)
        if not match:
            continue
        order = int(match.group(1))

        init_file = os.path.join(item_path, "__init__.py")
        if not os.path.exists(init_file):
            continue

        try:
            mod = importlib.import_module(f"pylearn.curriculum.{item}")
            if hasattr(mod, "module"):
                curriculum_module = mod.module
                curriculum_module.order = order
                modules.append(curriculum_module)
        except Exception as e:
            print(f"Warning: Could not load module {item}: {e}")

    modules.sort(key=lambda m: m.order)
    return modules
