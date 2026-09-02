import bpy


class TA_PT_toolkit(bpy.types.Panel):
    bl_label = "TA Toolkit"
    bl_idname = "TA_PT_toolkit"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "TA Toolkit"

    def draw(self, context):
        layout = self.layout

        box = layout.box()
        box.label(text="Scene Validation")
        box.operator("ta_toolkit.validate_scene", icon='CHECKMARK')

        box = layout.box()
        box.label(text="Naming")
        box.operator("ta_toolkit.rename_selected", icon='SORTALPHA')

        box = layout.box()
        box.label(text="Procedural Tools")
        operator = box.operator("ta_toolkit.generate_variations", icon='MOD_ARRAY')
        operator.count = 8
        operator.seed = 42
        operator.spacing = 2.5


CLASSES = (TA_PT_toolkit,)


def register_ui():
    for cls in CLASSES:
        bpy.utils.register_class(cls)


def unregister_ui():
    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)
