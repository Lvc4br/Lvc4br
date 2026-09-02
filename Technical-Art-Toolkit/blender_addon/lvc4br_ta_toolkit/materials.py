import bpy


def get_or_create_material(name="TA_Default_Material"):
    material = bpy.data.materials.get(name)
    if material is None:
        material = bpy.data.materials.new(name=name)
        material.use_nodes = True
    return material


def assign_material(obj, material_name="TA_Default_Material"):
    if obj.type != 'MESH':
        return False
    material = get_or_create_material(material_name)
    if obj.data.materials:
        obj.data.materials[0] = material
    else:
        obj.data.materials.append(material)
    return True
