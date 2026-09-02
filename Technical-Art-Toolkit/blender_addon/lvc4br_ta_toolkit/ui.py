import bpy


class TA_PT_toolkit(bpy.types.Panel):
    bl_label = "TA Toolkit"
    bl_idname = "TA_PT_toolkit"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "TA Toolkit"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        box = layout.box()
        box.label(text="Scene Validation", icon='CHECKMARK')
        box.operator("ta_toolkit.validate_scene", icon='CHECKMARK')

        box = layout.box()
        box.label(text="Scene Organization", icon='OUTLINER')
        box.operator("ta_toolkit.organize_scene", icon='SORTALPHA')

        box = layout.box()
        box.label(text="Naming", icon='SORTALPHA')
        box.operator("ta_toolkit.rename_selected", icon='SORTALPHA')

        box = layout.box()
        box.label(text="Export Preparation", icon='EXPORT')
        box.operator("ta_toolkit.prepare_export", icon='EXPORT')

        box = layout.box()
        box.label(text="Procedural Tools", icon='MOD_ARRAY')
        box.prop(scene, "ta_variation_count")
        box.prop(scene, "ta_variation_seed")
        box.prop(scene, "ta_variation_spacing")
        box.operator("ta_toolkit.generate_variations", icon='MOD_ARRAY')


CLASSES = (TA_PT_toolkit,)


def register_ui():
    for cls in CLASSES:
        bpy.utils.register_class(cls)


def unregister_ui():
    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)
