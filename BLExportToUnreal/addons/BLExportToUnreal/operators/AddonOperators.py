import math
import os
import bpy
from bpy_extras.io_utils import ExportHelper
from ..functions import AddonFunctions
from pathlib import Path

# __EXPORT TOOL__
class WRYC_OT_SelectExportActions(bpy.types.Operator):
    bl_idname = "wryc.ot_select_export_actions"
    bl_label = "Select Export Actions"
    bl_description = "Only actions that use or set fake_user can be selected."
    bl_options = {'REGISTER', 'UNDO'}

    def invoke(self, context, event):
        settings = context.scene.export_to_unreal
        exiting_names = {a.name for a in settings.export_actions}
        old_states = {item.name: item.enabled for item in settings.export_actions}

        if bpy.data.actions:
            for action in bpy.data.actions:
                if not action.users and not action.use_fake_user:
                    continue

                if action.name not in exiting_names:
                    item = settings.export_actions.add()
                    item.name = action.name
                    item.enabled = old_states.get(action.name, False)

        valid_names = {a.name for a in bpy.data.actions}
        to_remove = [i for i, a in enumerate(settings.export_actions) if a.name not in valid_names]
        for i in reversed(to_remove):
            settings.export_actions.remove(i)

        AddonFunctions.sort_actions(settings.export_actions)
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        actions = context.scene.export_to_unreal.export_actions

        if not bpy.data.actions:
            layout.label(text="No actions selected")
            return

        row = layout.row(align=True)
        row.operator("wryc.ot_enable_all_export_actions", text="Enable All")
        row.operator("wryc.ot_disable_all_export_actions", text="Disable All")

        box = layout.box()
        for entry in actions:
            box.prop(entry, "enabled", text=entry.name)

    def execute(self, context):
        settings = context.scene.export_to_unreal
        selected_actions = [a.name for a in settings.export_actions if a.enabled]
        if not selected_actions:
            self.report({'ERROR'}, "No action can export (Only using or fake_user actions can be selected).")
            return {'CANCELLED'}
        return {'FINISHED'}

class WRYC_OT_EnableAllExportActions(bpy.types.Operator):
    bl_idname = "wryc.ot_enable_all_export_actions"
    bl_label = "Enable All"
    bl_description = "Enable All (Only actions that use or set fake_user can be selected.)"
    bl_options = {'INTERNAL'}

    def execute(self, context):
        settings = context.scene.export_to_unreal
        for item in settings.export_actions:
            item.enabled = True
        return {'FINISHED'}

class WRYC_OT_DisableAllExportActions(bpy.types.Operator):
    bl_idname = "wryc.ot_disable_all_export_actions"
    bl_label = "Disable All"
    bl_description = "Disable All (Only actions that use or set fake_user can be selected.)"
    bl_options = {'INTERNAL'}

    def execute(self, context):
        settings = context.scene.export_to_unreal
        for item in settings.export_actions:
            item.enabled = False
        return {'FINISHED'}

class WRYC_OT_ExportToUnreal(bpy.types.Operator, ExportHelper):
    bl_idname = "wryc.ot_export_to_unreal"
    bl_label = "BL Export to Unreal"
    bl_options = {'REGISTER', 'UNDO'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=400)

    def draw(self, context):
        layout = self.layout

        settings = context.scene.export_to_unreal
        box_feature = layout.box()
        box_feature.label(text="Feature")
        row = box_feature.row(align=True)
        row = box_feature.row()
        row.prop(settings, "auto_fix_scale", text="Auto Fix Scale")
        row.prop(settings, "use_virtual_deform", text="Use Virtual Deform")

        box_mesh = layout.box()
        box_mesh.label(text="Mesh/Armature")
        box_mesh.prop(settings, "mesh_path", text="Mesh Path")
        row = box_mesh.row(align=True)
        row.prop(settings, "apply_modifiers", text="Apply Modifiers")
        box_mesh.prop(settings, "skeletal_prefix", text="Skeletal Prefix")

        box_action = layout.box()
        box_action.label(text="Action")
        box_action.prop(settings, "action_path", text="Action Path")
        box_action.prop(settings, "export_type", text="Export Type")
        if settings.export_type == 'BATCH':
            box_action.operator("wryc.ot_select_export_actions", text="Export Actions")

        row = box_action.row(align=True)
        row.prop(settings, "is_add_start_end", text="Add Start/End Keyframes")
        if settings.use_virtual_deform == False:
            row.prop(settings, "bake_nla_strips", text="Bake NLA Strips")
        if settings.export_type == "ALL":
            box_action.prop(settings, "file_name", text="File Name:")
        else:
            box_action.prop(settings, "action_prefix", text="Action Prefix")

        box_advanced = layout.box()
        row = box_advanced.row()
        col = row.column(align=True)
        split = col.split(factor=0.95, align=True)
        split.label(text="Advanced Settings")
        split.prop(settings, "show_advanced", text="", icon='TRIA_DOWN' if settings.show_advanced else "TRIA_RIGHT",
                   emboss=False)

        if settings.show_advanced:
            row = box_advanced.row()
            row.prop(settings, "only_deform", text="Only Deform Bones")
            row.prop(settings, "add_leaf", text="Add Leaf Bones")

            row = box_advanced.row()
            col = row.column(align=True)
            split = col.split(factor=0.7, align=True)
            split.label(text="Primary Bone Axis")
            split.prop(settings, "primary_bone_axis", text="")
            split = col.split(factor=0.7, align=True)
            split.label(text="Secondary Bone Axis")
            split.prop(settings, "secondary_bone_axis", text="")

            col = row.column(align=True)
            split = col.split(factor=0.7, align=True)
            split.label(text="FBX Axis Forward")
            split.prop(settings, "axis_forward", text="")
            split = col.split(factor=0.7, align=True)
            split.label(text="FBX Axis Up")
            split.prop(settings, "axis_up", text="")

    def execute(self, context):
        settings = context.scene.export_to_unreal
        pref = AddonFunctions.get_preferences()
        scale_factor = AddonFunctions.auto_fix_scale(context) #If auto fix scale is true, calculate scale factor.

        #Set up armature
        arm = [obj for obj in context.selected_objects if obj.type == 'ARMATURE'][0]
        if not arm:
            self.report({'ERROR'}, "No armature selected")
            return {'CANCELLED'}

        #Set up meshes
        meshs = [obj for obj in context.selected_objects if obj.type == 'MESH']
        if settings.mesh_path.strip() and not meshs:
            self.report({'ERROR'}, "No mesh selected")
            return {'CANCELLED'}

        # Temporarily original states
        selected_objects = context.selected_objects[:]
        active_obj = context.view_layer.objects.active
        orig_name = arm.name
        orig_action = arm.animation_data.action if arm.animation_data else None
        orig_pose_position = arm.data.pose_position
        orig_timeline_range = context.scene.frame_start, context.scene.frame_end

        #Select Actions by action export type
        if settings.action_path.strip():
            actions_to_process = []

            if settings.export_type == "SELECTED":
                if arm.animation_data.action:
                    actions_to_process = [arm.animation_data.action]
                else:
                    self.report({'ERROR'}, "No active action in selected armature")
            elif settings.export_type == "BATCH":
                actions_to_process = [bpy.data.actions.get(a.name) for a in settings.export_actions if a.enabled]
            elif settings.export_type == "ALL":
                actions_to_process = list(bpy.data.actions)

        action_map = {}
        export_list = []
        baked_states_pack = {}
        bone_name_map = None

        try:
            #___Pre Process___
            bpy.context.view_layer.objects.active = arm
            arm.name = "Armature" #Rename armature name -> "Armature"
            if arm.data.users > 1:
                arm.data = arm.data.copy()

            #If root bone isn't exist, add root bone.
            bpy.ops.object.mode_set(mode='EDIT')
            edit_bones = arm.data.edit_bones
            if settings.use_virtual_deform:#Add deform root bone.
                def_root_name = f"{pref.deform_prefix}root"
                if f"{pref.deform_prefix}root" not in edit_bones:
                    def_root = edit_bones.new(def_root_name)
                    def_root.head = (0, 0, 0)
                    def_root.roll = math.radians(-90)
                    def_root.tail = (0, 0.1, 0)
                    for b in [eb for eb in edit_bones if eb.name.startswith(pref.deform_prefix)]:
                        if b.name != def_root_name and b.parent is None:
                            b.parent = def_root
                else:
                    def_root = edit_bones[f"{pref.deform_prefix}root"]
                    def_root.head = (0, 0, 0)

            if "root" not in edit_bones:
                root = edit_bones.new("root")
                root.head = (0, 0, 0)
                root.tail = (0, 0, 0.1)
                root.use_deform = True
                for b in edit_bones:
                    if b.name != "root" and b.name != def_root_name and b.parent is None:
                        b.parent = root
            else:
                root = edit_bones["root"]
                root.head = (0, 0, 0)

            # Process virtual deform bones and original bones
            if settings.use_virtual_deform:
                if hasattr(pref, 'deform_prefix') and hasattr(pref, 'original_prefix'):
                    bone_name_map = AddonFunctions.apply_virtual_deform_conversion(
                        context, arm, meshs
                    )
                else:
                    self.report({'ERROR'}, "Preferences for necessary prefixes are not set.")
                    return {'CANCELLED'}

                # Bake actions
                if settings.action_path.strip() and actions_to_process:
                    action_map, baked_list, baked_states_pack = AddonFunctions.bake_action(
                        context, arm, actions_to_process, settings.action_prefix
                    )
                    export_list =baked_list
            else:
                export_list = actions_to_process

            #Auto fix scale
            if scale_factor != 1.0:
                bpy.ops.object.mode_set(mode='OBJECT')
                bpy.ops.object.select_all(action='DESELECT')
                arm.select_set(True)
                context.view_layer.objects.active = arm

                arm.scale *= 1 / scale_factor
                bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

                for action in export_list:
                    for fcurve in action.fcurves:
                        if fcurve.data_path.endswith('location'):
                            for kp in fcurve.keyframe_points:
                                kp.co.y *= 1 / scale_factor
                                kp.handle_left.y *= 1 / scale_factor
                                kp.handle_right.y *= 1 / scale_factor

            #Select armature and meshes for export
            bpy.ops.object.select_all(action='DESELECT')
            arm.select_set(True)
            for mesh in meshs:
                mesh.select_set(True)
            bpy.context.view_layer.objects.active = arm

            #___Export___
            # Mesh/Armature
            if settings.mesh_path.strip():
                arm.data.pose_position = 'REST'
                export_dir = bpy.path.abspath(settings.mesh_path)
                sk_file_name = settings.skeletal_prefix + orig_name
                export_file = os.path.join(export_dir, sk_file_name + ".fbx")
                AddonFunctions.do_export(
                    context, filepath=export_file, object_type={'ARMATURE', 'MESH'}, bake_anim=False
                )
                self.report({'INFO'}, f"Mesh/Armature Exported Successfully")

            # Action
            if settings.action_path.strip():
                bpy.ops.object.select_all(action='DESELECT')
                arm.select_set(True)
                bpy.context.view_layer.objects.active = arm
                arm.data.pose_position = 'POSE'

                if settings.export_type == "SELECTED":
                    export_action = export_list[0]
                    if export_action:
                        act_file = bpy.path.abspath(
                            settings.action_path + "/" + f"{export_action.name}.fbx"
                        )
                        arm.animation_data.action = export_action
                        AddonFunctions.do_export(
                            context, filepath=act_file, object_type={'ARMATURE'}, bake_anim=True, bake_all=False,
                            action=export_action,
                        )
                        self.report({'INFO'}, f"Exported selected action successfully: {act_file}")

                elif settings.export_type == "BATCH":
                    if export_list:
                        for export_action in export_list:
                            act_file = bpy.path.abspath(
                                settings.action_path + "/" + f"{export_action.name}.fbx"
                            )
                            arm.animation_data.action = export_action
                            AddonFunctions.do_export(
                                context, filepath=act_file, object_type={'ARMATURE'}, bake_anim=True, bake_all=False,
                                action=export_action,
                            )
                        self.report({'INFO'}, f"Exported action by batch successfully")

                elif settings.export_type == "ALL":
                    for track in list(arm.animation_data.nla_tracks):
                        arm.animation_data.nla_tracks.remove(track)

                    arm.animation_data.action = None

                    #Set original actions fake_user use as False, export actions fake_user use as True
                    excluded_actions = [act for act in bpy.data.actions if act.name.startswith("__orig__")]
                    action_fake_user_states = {}
                    for act in excluded_actions:
                        action_fake_user_states[act] = act.use_fake_user
                        act.use_fake_user = False
                    for act in export_list:
                        act.use_fake_user = True

                    context.view_layer.update()

                    try:
                        if export_list:
                            file_name = settings.file_name or Path(bpy.data.filepath).stem
                            export_file = os.path.join(bpy.path.abspath(settings.action_path), file_name + ".fbx")
                            AddonFunctions.do_export(
                                context, filepath=export_file, object_type={'ARMATURE'}, bake_anim=True, bake_all=True
                            )
                            self.report({'INFO'}, f"Exported all action successfully")
                    finally:
                        #Restore fake users state
                        for act, state in action_fake_user_states.items():
                            act.use_fake_user = state
                else:
                    self.report({'INFO'}, "Action path is empty, skip action export")

        finally:
            #___Restore___
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.select_all(action='DESELECT')
            arm.select_set(True)
            bpy.context.view_layer.objects.active = arm
            if arm.data.users > 1:
                arm.data = arm.data.copy()
            arm.name = orig_name
            arm.data.pose_position = orig_pose_position

            #Restore Scale to original
            if scale_factor != 1.0:
                arm.scale *= scale_factor
                bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
                if settings.use_virtual_deform is False:
                    for action in export_list:
                        for fcurve in action.fcurves:
                            if fcurve.data_path.endswith('location'):
                                for kp in fcurve.keyframe_points:
                                    kp.co.y *= scale_factor
                                    kp.handle_left.y *= scale_factor
                                    kp.handle_right.y *= scale_factor

            #Restore before baked state
            AddonFunctions.restore_baked_action(arm, action_map, settings.action_prefix, baked_states_pack)

            # Restore action as original selected action
            if orig_action:
                arm.animation_data.action = orig_action

            # If use virtual deform is true, restore deform and control bones state
            if settings.use_virtual_deform and bone_name_map is not None:
                AddonFunctions.revert_virtual_deform_conversion(
                    context, arm, meshs, bone_name_map
                )

            # Restore timeline to origin
            context.scene.frame_start, context.scene.frame_end = orig_timeline_range

            #Restore selected objects as before execute state
            bpy.ops.object.select_all(action='DESELECT')
            for obj in selected_objects:
                obj.select_set(True)
            if active_obj:
                context.view_layer.objects.active = active_obj

        return {'FINISHED'}