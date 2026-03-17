import bpy

# __BLENDER API COMPAT__
class Compat:

    @staticmethod
    def bone_selection(pb, select_state=True):
        version = bpy.app.version

        if version >= (5, 0, 0):
            pb.select = select_state
        else:
            pb.bone.select = select_state

    @staticmethod
    def get_fcurves_list(action):
        if not action:
            return []
        # Blender 4.0+
        if hasattr(action, 'fcurves') and len(action.fcurves) > 0:
            return action.fcurves
        # Blender 5.0+
        if hasattr(action, 'bindings'):
            fcurves = []
            for b in action.bindings:
                fcurves.extend(list(b.fcurves))
            return fcurves
        return []