import os

import bpy
from bpy.props import StringProperty, IntProperty, BoolProperty
from bpy.types import AddonPreferences

from ..config import __addon_name__


class WRYCAddonpreferences(bpy.types.AddonPreferences):
    bl_idname = __addon_name__
    addon_file = os.path.dirname(__file__)

    deform_prefix: StringProperty(
        name="Deform Prefix",
        default="DEF_",
    )

    original_prefix: StringProperty(
        name="original Prefix",
        default="ORIG_",
    )

    def draw(self, context):
        layout = self.layout
        layout.label(text="Preferences")
        layout.prop(self, "deform_prefix", text="Deform Prefix")