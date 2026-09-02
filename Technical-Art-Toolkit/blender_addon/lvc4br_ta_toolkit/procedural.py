import bpy
import random


def create_variation(count=8, seed=42, spacing=2.5, collection_name="TA_Variations"):
    """Create deterministic geometry variations for workflow testing."""
    rng = random.Random(seed)

    collection = bpy.data.collections.get(collection_name)
    if collection is None:
        collection = bpy.data.collections.new(collection_name)
        bpy.context.scene.collection.children.link(collection)

    for index in range(count):
        bpy.ops.mesh.primitive_cube_add(location=(index * spacing, 0, 0))
        obj = bpy.context.object
        obj.name = f"VAR_{index + 1:03d}"

        obj.scale = (
            rng.uniform(0.7, 1.4),
            rng.uniform(0.7, 1.4),
            rng.uniform(0.7, 1.8),
        )
        obj.rotation_euler[2] = rng.uniform(-0.5, 0.5)
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

        for old_collection in list(obj.users_collection):
            old_collection.objects.unlink(obj)
        collection.objects.link(obj)

    return collection
