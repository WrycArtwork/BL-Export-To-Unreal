import bpy
from bpy.props import EnumProperty, BoolProperty, StringProperty, CollectionProperty
from bpy.types import PropertyGroup

class ActionEntry(PropertyGroup):
    name: StringProperty()
    enabled: BoolProperty(default=False)

#__EXPORT TOOL__
def get_export_items(self, context):
    items = [
        ('SELECTED', "Selected", "Selected"),
        ('BATCH', "Batch", "Batch"),
    ]
    if not self.use_virtual_deform or self.get('export_type') == 2: #Cannot use export type 'ALL' at virtual deform.
        items.append(('ALL', "All", "All"))
    return items
def update_export_type(self, context):
    if self.use_virtual_deform and self.export_type == 'ALL':
        self.export_type = 'SELECTED'
class ExportToUnreal(PropertyGroup):
    #Mesh/Armature
    mesh_path: StringProperty(
        name="Mesh Path",
        subtype='DIR_PATH',
        default="//"
    )

    use_virtual_deform: BoolProperty(
        name="Use Virtual Deform Bones",
        default=False,
        update=update_export_type
    )

    apply_modifiers: BoolProperty(
        name="Apply Modifiers",
        default=True
    )

    skeletal_prefix: StringProperty(
        name="Skeletal Prefix",
        default="SK_"
    )

    static_prefix: StringProperty(
        name="Static Prefix",
        default="SM_"
    )

    #Action
    export_actions: CollectionProperty(type=ActionEntry)

    action_path: StringProperty(
        name="Action Path",
        subtype='DIR_PATH',
        default="//"
    )

    export_type: EnumProperty(
        name="Export Type",
        items=get_export_items,
    )

    is_add_start_end: BoolProperty(
        name="Add Start/End Keyframes",
        default=True
    )

    bake_nla_strips: BoolProperty(
        name="Bake NLA Strips",
        default=False
    )

    action_prefix: StringProperty(
        name="Action Prefix",
        default="AS_"
    )

    file_name: StringProperty(
        name="File Name",
        default="",
    )

    #Advanced
    show_advanced: BoolProperty(default=False)

    only_deform: BoolProperty(
        name="Only Deform Bones",
        default=True
    )

    add_leaf: BoolProperty(
        name="Add Leaf Bones",
        default=False
    )

    primary_bone_axis: EnumProperty(
        name="Primary Bone Axis",
        items=[
            ('X', "X", "X"),
            ('-X', "-X", "-X"),
            ('Y', "Y", "Y"),
            ('-Y', "-Y", "-Y"),
            ('Z', "Z", "Z"),
            ('-Z', "-Z", "-Z"),
        ],
        default='Y'
    )

    secondary_bone_axis: EnumProperty(
        name="Secondary Bone Axis",
        items=[
            ('X', "X", "X"),
            ('-X', "-X", "-X"),
            ('Y', "Y", "Y"),
            ('-Y', "-Y", "-Y"),
            ('Z', "Z", "Z"),
            ('-Z', "-Z", "-Z"),
        ],
        default='X'
    )

    axis_forward: EnumProperty(
        name="FBX Axis Forward",
        items=[
            ('X', "X", "X"),
            ('-X', "-X", "-X"),
            ('Y', "Y", "Y"),
            ('-Y', "-Y", "-Y"),
            ('Z', "Z", "Z"),
            ('-Z', "-Z", "-Z"),
        ],
        default='-Z'
    )

    axis_up: EnumProperty(
        name="FBX Axis Up",
        items=[
            ('X', "X", "X"),
            ('-X', "-X", "-X"),
            ('Y', "Y", "Y"),
            ('-Y', "-Y", "-Y"),
            ('Z', "Z", "Z"),
            ('-Z', "-Z", "-Z"),
        ],
        default='Y'
    )

    auto_fix_scale: BoolProperty(
        name="Auto Fix Scale",
        default=True
    )