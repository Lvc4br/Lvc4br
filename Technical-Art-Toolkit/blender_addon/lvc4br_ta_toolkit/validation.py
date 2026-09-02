import bpy


def collect_scene_issues():
    issues = []

    for obj in bpy.context.scene.objects:
        if not obj.name or obj.name[0].isdigit():
            issues.append((obj.name or "<unnamed>", "Invalid object name"))

        if obj.type == 'MESH':
            if len(obj.data.vertices) == 0:
                issues.append((obj.name, "Mesh has no vertices"))
            if not obj.data.materials:
                issues.append((obj.name, "Mesh has no material"))

            scale = obj.scale
            if any(abs(value - 1.0) > 0.0001 for value in scale):
                issues.append((obj.name, "Scale is not applied"))

    return issues
