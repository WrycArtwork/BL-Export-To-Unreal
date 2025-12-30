from .addons.BLExportToUnreal import register as addon_register, unregister as addon_unregister

bl_info = {
    "name": 'BL Export To Unreal',
    "author": 'WRYC',
    "blender": (4, 0, 2),
    "version": (0, 0, 1),
    "description": 'Easily export meshes, armatures, and animations to Unreal Engine with automatically fixed naming, scale, and compatibility..',
    "doc_url": 'https://github.com/WrycArtwork/BL-Export-To-Unreal',
    "category": 'Import-Export'
}

def register():
    addon_register()

def unregister():
    addon_unregister()

    