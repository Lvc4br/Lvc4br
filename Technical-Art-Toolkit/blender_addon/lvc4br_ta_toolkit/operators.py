import bpy
import re

from .procedural import create_variation
from .validation import collect_scene_issues


class TA_OT_validate_scene(bpy.types.Operator):
    bl_idname = "ta_toolkit.validate_scene"
    bl_label = "Validate Scene"
    bl_description = "Check object names, meshes, materials and transforms"

    def execute(self, context):
        issues = collect_scene_issues()
        if issues:
            self.report({'WARNING'}, f"Scene validation found {len(issues)} issue(s).")
            print("[TA Toolkit] Scene validation report")
            for object_name, message in issues:
                print(f"  - {object_name}: {message}")
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
        create_variation(count=scene.ta_variation_count, seed=scene.ta_variation_seed, spacing=scene.ta_variation_spacing)
        self.report({'INFO'}, f"Generated {scene.ta_variation_count} variation(s) with seed {scene.ta_variation_seed}.")
        return {'FINISHED'}


class TA_OT_organize_scene(bpy.types.Operator):
    bl_idname = "ta_toolkit.organize_scene"
    bl_label = "Organize Scene"
    bl_description = "Move objects into standard Technical Art collections"

    def execute(self, context):
        scene = context.scene
        collections = {}
        for name in ("TA_Assets", "TA_Lights", "TA_Cameras", "TA_Other"):
            collection = bpy.data.collections.get(name)
            if collection is None:
                collection = bpy.data.collections.new(name)
                scene.collection.children.link(collection)
            collections[name] = collection

        for obj in list(scene.objects):
            if obj.type == 'MESH':
                target = collections["TA_Assets"]
            elif obj.type == 'LIGHT':
                target = collections["TA_Lights"]
            elif obj.type == 'CAMERA':
                target = collections["TA_Cameras"]
            else:
                target = collections["TA_Other"]
            for old_collection in list(obj.users_collection):
                old_collection.objects.unlink(obj)
            target.objects.link(obj)

        self.report({'INFO'}, "Scene organized into Technical Art collections.")
        return {'FINISHED'}


class TA_OT_prepare_export(bpy.types.Operator):
    bl_idname = "ta_toolkit.prepare_export"
    bl_label = "Prepare Selected for Export"
    bl_description = "Apply rotation and scale to selected mesh objects"

    def execute(self, context):
        meshes = [obj for obj in context.selected_objects if obj.type == 'MESH']
        if not meshes:
            self.report({'WARNING'}, "Select at least one mesh object.")
            return {'CANCELLED'}

        bpy.ops.object.select_all(action='DESELECT')
        for obj in meshes:
            obj.select_set(True)
        context.view_layer.objects.active = meshes[0]
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
        self.report({'INFO'}, f"Prepared {len(meshes)} mesh object(s) for export.")
        return {'FINISHED'}


CLASSES = (TA_OT_validate_scene, TA_OT_rename_selected, TA_OT_generate_variations, TA_OT_organize_scene, TA_OT_prepare_export)


def register_operators():
    for cls in CLASSES:
        bpy.utils.register_class(cls)


def unregister_operators():
    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)
