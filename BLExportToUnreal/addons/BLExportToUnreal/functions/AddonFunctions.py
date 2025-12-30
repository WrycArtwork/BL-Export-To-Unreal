import bpy

from ..config import __addon_name__
def get_preferences():
    return bpy.context.preferences.addons[__addon_name__].preferences

def sort_actions(collection):
    #class is AddonProperties.ActionEntry
    data = [{"name": item.name, "enabled": getattr(item, "enabled", False)} for item in collection]
    sorted_data = sorted(data, key=lambda x: x["name"].lower())

    collection.clear()
    for entry in sorted_data:
        item = collection.add()
        item.name = entry["name"]
        item.enabled = entry["enabled"]

#__EXPORT TOOL__
def auto_fix_scale(context):
    settings = context.scene.export_to_unreal
    scene = context.scene

    if settings.auto_fix_scale == True:
        scale_factor =  0.01/scene.unit_settings.scale_length
    else:
        scale_factor = 1.0

    return scale_factor

def bake_action(context, arm, act_list, export_prefix=""):
    action_map = {}
    baked_list = []
    coll_visibility = {}
    con_states = {}
    nla_states = {}

    #Record original bone collection visibility states
    if hasattr(arm.data, "collections"):
        for coll in arm.data.collections:
            coll_visibility[coll.name] = coll.is_visible
            coll.is_visible = True #Set all collection to visibility for bake

    # Mute all NLA tracks
    if arm.animation_data.nla_tracks:
        for track in arm.animation_data.nla_tracks:
            nla_states[track.name] = {
                'mute': track.mute,
                'is_solo': track.is_solo,
            }
            track.mute = True
            track.is_solo = False

    #Select deform bones
    bpy.ops.object.mode_set(mode='POSE')
    bpy.ops.pose.select_all(action='DESELECT')
    for pb in arm.pose.bones:
        if pb.bone.use_deform:
            pb.bone.select = True
        #Record original constraint states
        for con in pb.constraints:
            con_states[(pb.name, con.name)] = con.mute

    #Bake actions in action list
    for act in act_list:
        if not act or act.name.startswith("__orig__"):
            continue

        #backup original action name xxx -> __orig__xxx
        orig_name = act.name
        backup_name = f"__orig__{orig_name}"
        act.name = backup_name
        action_map[orig_name] = backup_name

        #Set up frame range
        frame_start, frame_end = act.frame_range
        #Force set action
        context.scene.frame_set(int(act.frame_range[0]))
        context.scene.view_layers.update()
        arm.animation_data.action = act

        #bake actions
        bpy.ops.nla.bake(
            frame_start=int(frame_start),
            frame_end=int(frame_end),
            step=1,
            only_selected=True,
            visual_keying=True,
            clear_constraints=False,
            use_current_action=False,
            bake_types={'POSE'},
        )

        #Set baked action name as export action name
        baked_action = arm.animation_data.action
        baked_action.name = f"{export_prefix}{orig_name}"
        baked_list.append(baked_action)

    #Mute bones constraints
    for pb in arm.pose.bones:
        for con in pb.constraints:
            con.mute = True

    states_pack = {'coll_visibility': coll_visibility, 'con_states': con_states, 'nla_states': nla_states}

    return action_map, baked_list, states_pack

def restore_baked_action(arm, action_map, export_prefix="", states_pack={}):
    #Restore bone collections visibility
    coll_visibility = states_pack.get('coll_visibility', {})
    if hasattr(arm.data, "collections"):
        for coll_name, was_visible in coll_visibility.items():
            if coll_name in arm.data.collections:
                arm.data.collections[coll_name].is_visible = was_visible

    #Restore NLA states
    nla_states = states_pack.get('nla_states', {})
    if arm.animation_data.nla_tracks:
        for track in arm.animation_data.nla_tracks:
            if track.name in nla_states:
                track.mute = nla_states[track.name]['mute']
                track.is_solo = nla_states[track.name]['is_solo']

    #Restore constraint original mute state
    con_states = states_pack.get('con_states', {})
    for pb in arm.pose.bones:
        for con in pb.constraints:
            state = (pb.name, con.name)
            if state in con_states:
                con.mute = con_states[state]

    #Restore original actions and delete baked actions
    for orig_name, backup_name in action_map.items():
        baked_action = bpy.data.actions.get(f"{export_prefix}{orig_name}")
        orig_action = bpy.data.actions.get(backup_name)

        if baked_action:
            bpy.data.actions.remove(baked_action)
        if orig_action:
            orig_action.name = orig_name

def apply_virtual_deform_conversion(context, arm, meshes):
    arm_data = arm.data
    pref = get_preferences()
    bone_name_map = {"ctrl": {}, "def": {}}

    bpy.ops.object.mode_set(mode='OBJECT')

    #Mesh Vertex Groups rename to __temp__xxx
    for mesh in meshes:
        for vg in mesh.vertex_groups:
            if vg.name in arm_data.bones:
                temp_name = f"__temp__{vg.name}"
                vg.name = temp_name

    #Rename control bones xxx → ORIG_xxx
    for bone in arm_data.bones:
        if not bone.name.startswith(pref.deform_prefix) and bone.use_deform:
            orig = bone.name
            new_name = pref.original_prefix + orig
            bone.name = new_name
            bone.use_deform = False
            bone_name_map["ctrl"][new_name] = orig

    #Rename deform bones DEF_xxx → xxx
    for bone in arm_data.bones:
        if bone.name.startswith(pref.deform_prefix):
            orig = bone.name
            new_name = orig[len(pref.deform_prefix):]
            bone.name = new_name
            bone.use_deform = True
            bone_name_map["def"][new_name] = orig

    #Restore vertex groups to final names
    for mesh in meshes:
        for vg in mesh.vertex_groups:
            if vg.name.startswith("__temp__"):
                vg.name = vg.name[8:]
    context.view_layer.update()
    return bone_name_map

def revert_virtual_deform_conversion(context, arm, meshes, bone_name_map):
    arm_data = arm.data
    pref = get_preferences()

    #Mesh Vertex Groups rename to __temp__xxx
    for mesh in meshes:
        for vg in mesh.vertex_groups:
            vg.name =  f"__temp__{vg.name}"

    #Rename deform bones xxx -> DEF_xxx
    for current_name, orig_name in bone_name_map["def"].items():
        bone = arm_data.bones.get(current_name)
        if bone:
            bone.name = orig_name
            bone.use_deform = False

    # Rename control bones ORIG_xxx -> xxx
    for current_name, orig_name in bone_name_map["ctrl"].items():
            bone = arm_data.bones.get(current_name)
            if bone:
                bone.name = orig_name
                bone.use_deform = True

    #Restore vertex groups to final names
    for mesh in meshes:
        for vg in mesh.vertex_groups:
            if vg.name.startswith("__temp__"):
                vg.name = vg.name[8:]
    context.view_layer.update()

def do_export(context, filepath, object_type={'ARMATURE'}, bake_anim=False, bake_all=False, action=None):
    settings = context.scene.export_to_unreal
    scale = auto_fix_scale(context)

    if bake_all == False:
        scene = context.scene
        if action:
            start, end = map(int, action.frame_range)
            scene.frame_start = start
            scene.frame_end = end

    if settings.use_virtual_deform:
        use_nla = False
    else:
        use_nla = settings.bake_nla_strips

    bpy.ops.export_scene.fbx(
        object_types=object_type,
        filepath=filepath,
        use_selection=True,
        apply_unit_scale=True,
        global_scale=scale,
        bake_anim_use_all_bones=True,
        use_armature_deform_only=settings.only_deform,
        add_leaf_bones=settings.add_leaf,
        apply_scale_options='FBX_SCALE_ALL',
        armature_nodetype='ROOT',
        primary_bone_axis=settings.primary_bone_axis,
        secondary_bone_axis=settings.secondary_bone_axis,
        axis_forward=settings.axis_forward,
        axis_up=settings.axis_up,
        bake_anim=bake_anim,
        bake_anim_use_all_actions=bake_all,
        bake_anim_force_startend_keying=settings.is_add_start_end,
        bake_anim_use_nla_strips=use_nla,
        mesh_smooth_type='EDGE',
        use_triangles=True,
        use_tspace=True,
    )