from BLExportToUnreal.common.i18n.dictionary import preprocess_dictionary

dictionary = {
    #("*", ""): "",
    "zh_TW": {
        ("*", "Feature"): "核心功能",
        ("*", "Mesh/Armature"): "模型/骨架",
        ("*", "Action"): "動畫動作",
        ("*", "Advanced Settings"): "進階設定",

        ("*", "Auto Fix Scale"): "自動修正比例",
        ("*", "Use Virtual Deform"): "使用虛擬變形骨骼",

        ("*", "Mesh Path"): "匯出路徑",
        ("*", "Apply Modifiers"): "應用修改器",
        ("*", "Skeletal Prefix:"): "骨骼體前綴:",

        ("*", "Action Path"): "匯出路徑",
        ("*", "Export Type"): "匯出模式",
        ("*", "Export Actions"): "匯出動作",
        ("*", "Add Start/End Keyframes"): "補齊首尾幀",
        ("*", "Bake NLA Strips"): "烘焙 NLA 片段",
        ("*", "File Name:"): "檔案名稱:",
        ("*", "Action Prefix:"): "動畫前綴:",

        ("*", "Selected"): "當前選中",
        ("*", "Batch"): "批次匯出",
        ("*", "All"): "匯出全部",

        ("*", "Only Deform Bones"): "僅匯出變形骨骼",
        ("*", "Add Leaf Bones"): "添加末梢骨",
        ("*", "Primary Bone Axis"): "骨骼主軸",
        ("*", "Secondary Bone Axis"): "骨骼次軸",
        ("*", "FBX Axis Forward"): "FBX 前向軸",
        ("*", "FBX Axis Up"): "FBX 向上軸",

        ("*", "Select Export Actions"): "選取匯出的動作清單",
        ("*", "Enable All"): "全部啟用",
        ("*", "Disable All"): "全部禁用",
    },
    "zh_CN": {
        ("*", "Feature"): "核心功能",
        ("*", "Mesh/Armature"): "模型/骨架",
        ("*", "Action"): "动画动作",
        ("*", "Advanced Settings"): "高级设置",

        ("*", "Auto Fix Scale"): "自动修正比例",
        ("*", "Use Virtual Deform"): "使用虚拟变形骨骼",

        ("*", "Mesh Path"): "导出路径",
        ("*", "Apply Modifiers"): "应用修改器",
        ("*", "Skeletal Prefix:"): "骨架前缀:",

        ("*", "Action Path"): "导出路径",
        ("*", "Export Type"): "导出模式",
        ("*", "Export Actions"): "导出动作",
        ("*", "Add Start/End Keyframes"): "补齐首尾帧",
        ("*", "Bake NLA Strips"): "烘焙 NLA 片段",
        ("*", "File Name:"): "文件名:",
        ("*", "Action Prefix:"): "动画前缀:",

        ("*", "Selected"): "当前选中",
        ("*", "Batch"): "批量导出",
        ("*", "All"): "导出全部",

        ("*", "Only Deform Bones"): "仅导出变形骨骼",
        ("*", "Add Leaf Bones"): "添加末梢骨",
        ("*", "Primary Bone Axis"): "骨骼主轴",
        ("*", "Secondary Bone Axis"): "骨骼次轴",
        ("*", "FBX Axis Forward"): "FBX 前向轴",
        ("*", "FBX Axis Up"): "FBX 向上轴",

        ("*", "Select Export Actions"): "选择导出的动作列表",
        ("*", "Enable All"): "全部启用",
        ("*", "Disable All"): "全部禁用",
    }
}

dictionary = preprocess_dictionary(dictionary)

dictionary["zh_HANT"] = dictionary["zh_TW"]
dictionary["zh_HANS"] = dictionary["zh_CN"]
