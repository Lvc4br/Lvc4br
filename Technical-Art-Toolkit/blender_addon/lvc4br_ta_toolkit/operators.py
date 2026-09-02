import bpy
import re

from .procedural import create_variation


class TA_OT_validate_scene(bpy.types.Operator):
    bl_idname = "ta_toolkit.validate_scene"
    bl_label = "Validate Scene"
    bl_description = "Check object names, meshes, materials and transforms"

    def execute(self, context):
        name_pattern = re.compile(r"^[A-Za-z][A-Za-z0-9_]*$")
        invalid_names = []
        empty_meshes = []
        missing_materials = []
        unapplied_scale = []

        for obj in bpy.data.objects:
            if not name_pattern.match(obj.name):
                invalid_names.append(obj.name)

            if obj.type == 'MESH':
                if len(obj.data.vertices) == 0:
                    empty_meshes.append(obj.name)
                if len(obj.data.materials) == 0:
                    missing_materials.append(obj.name)
                if any(abs(value - 1.0) > 0.001 for value in obj.scale):
                    unapplied_scale.append(obj.name)

        total = (
            len(invalid_names)
            + len(empty_meshes)
            + len(missing_materials)
            + len(unapplied_scale)
        )

        if total:
            self.report({'WARNING'}, f"Scene validation found {total} issue(s).")
            print("[TA Toolkit] Scene validation report")
            print(f"  Naming issues: {len(invalid_names)}")
            print(f"  Empty meshes: {len(empty_meshes)}")
            print(f"  Missing materials: {len(missing_materials)}")
            print(f"  Unapplied scale: {len(unapplied_scale)}")
        else:
            self.report({'INFO'}, "Scene validation passed with no detected issues.")

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


class TA_OT_generate_variations(bpy.types.Operator):
    bl_idname = "ta_toolkit.generate_variations"
    bl_label = "Generate Variations"
    bl_description = "Generate deterministic procedural geometry variations"

    def execute(self, context):
        scene = context.scene
        create_variation(
            count=scene.ta_variation_count,
            seed=scene.ta_variation_seed,
            spacing=scene.ta_variation_spacing,
        )
        self.report(
            {'INFO'},
            f"Generated {scene.ta_variation_count} variation(s) with seed {scene.ta_variation_seed}.",
        )
        return {'FINISHED'}


CLASSES = (
    TA_OT_validate_scene,
    TA_OT_rename_selected,
    TA_OT_generate_variations,
)


def register_operators():
    for cls in CLASSES:
        bpy.utils.register_class(cls)


def unregister_operators():
    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)
