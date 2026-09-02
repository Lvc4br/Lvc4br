bl_info = {
    "name": "Lvc4br Technical Art Toolkit",
    "author": "Luca Toniolo",
    "version": (0, 1, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > TA Toolkit",
    "description": "Small utilities for Technical Art and 3D production workflows.",
    "category": "3D View",
}

from .operators import register_operators, unregister_operators
from .ui import register_ui, unregister_ui


def register():
    register_operators()
    register_ui()


def unregister():
    unregister_ui()
    unregister_operators()


if __name__ == "__main__":
    register()
