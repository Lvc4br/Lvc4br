bl_info = {
    "name": "Lvc4br Technical Art Toolkit",
    "author": "Luca Toniolo",
    "version": (0, 2, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > TA Toolkit",
    "description": "Utilities for Technical Art and 3D production workflows.",
    "category": "3D View",
}

import bpy

from .operators import register_operators, unregister_operators
from .ui import register_ui, unregister_ui


def register():
    bpy.types.Scene.ta_variation_count = bpy.props.IntProperty(
        name="Count", default=8, min=1, max=100
    )
    bpy.types.Scene.ta_variation_seed = bpy.props.IntProperty(
        name="Seed", default=42
    )
    bpy.types.Scene.ta_variation_spacing = bpy.props.FloatProperty(
        name="Spacing", default=2.5, min=0.1
    )

    register_operators()
    register_ui()


def unregister():
    unregister_ui()
    unregister_operators()

    del bpy.types.Scene.ta_variation_count
    del bpy.types.Scene.ta_variation_seed
    del bpy.types.Scene.ta_variation_spacing


if __name__ == "__main__":
    register()
