import bpy
import re


class TA_OT_validate_names(bpy.types.Operator):
    bl_idname = "ta_toolkit.validate_names"
    bl_label = "Validate Object Names"
    bl_description = "Report objects whose names do not follow the toolkit convention"

    def execute(self, context):
        pattern = re.compile(r"^[A-Za-z][A-Za-z0-9_]*$")
        invalid = [obj.name for obj in bpy.data.objects if not pattern.match(obj.name)]

        if invalid:
            message = f"{len(invalid)} object(s) need naming review."
            self.report({'WARNING'}, message)
            for name in invalid[:10]:
                print(f"[TA Toolkit] Naming review: {name}")
        else:
            self.report({'INFO'}, "All object names pass the basic validation.")

        return {'FINISHED'}


class TA_OT_rename_selected(bpy.types.Operator):
    bl_idname = "ta_toolkit.rename_selected"
    bl_label = "Rename Selected"
    bl_description = "Rename selected objects using a shared prefix"

    prefix: bpy.props.StringProperty(name="Prefix", default="ASSET")

    def execute(self, context):
        selected = list(context.selected_objects)
        for index, obj in enumerate(selected, start=1):
            obj.name = f"{self.prefix}_{index:03d}"

        self.report({'INFO'}, f"Renamed {len(selected)} object(s).")
        return {'FINISHED'}


CLASSES = (
    TA_OT_validate_names,
    TA_OT_rename_selected,
)


def register_operators():
    for cls in CLASSES:
        bpy.utils.register_class(cls)


def unregister_operators():
    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)
