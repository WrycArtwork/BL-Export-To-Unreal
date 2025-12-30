import bpy

from .config import __addon_name__
from .i18n.dictionary import dictionary
from .properties.AddonProperties import ExportToUnreal
from ...common.class_loader import auto_load
from ...common.class_loader.auto_load import add_properties, remove_properties
from ...common.i18n.dictionary import common_dictionary
from ...common.i18n.i18n import load_dictionary

# Add-on info
bl_info = {
    "name": "BL Export To Unreal",
    "author": "WRYC",
    "blender": (4, 0, 2),
    "version": (0, 0, 1),
    "description": "Easily export meshes, armatures, and animations to Unreal Engine with automatically fixed naming, scale, and compatibility..",
    "doc_url": "https://github.com/WrycArtwork/BL-Export-To-Unreal",
    "category": "Import-Export"
}

_addon_properties = {
    bpy.types.Scene:{
        "export_to_unreal": bpy.props.PointerProperty(type=ExportToUnreal),
    }
}

def menu_func_export_ue(self, context):
    self.layout.operator("wryc.ot_export_to_unreal", text="BL Export to Unreal")

def register():
    # Register classes
    auto_load.init()
    auto_load.register()
    add_properties(_addon_properties)

    # ExportToUnreal
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export_ue)
    # Internationalization
    load_dictionary(dictionary)
    bpy.app.translations.register(__addon_name__, common_dictionary)

    print("{} addon is installed.".format(__addon_name__))


def unregister():
    # ExportToUnreal
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export_ue)
    # Internationalization
    bpy.app.translations.unregister(__addon_name__)
    # unRegister classes
    auto_load.unregister()
    remove_properties(_addon_properties)
    print("{} addon is uninstalled.".format(__addon_name__))
