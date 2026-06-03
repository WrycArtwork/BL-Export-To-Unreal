## English
This add-on is specifically designed for exporting **Skeletal Meshes** and **Animation Sequences** from Blender to Unreal Engine.<br>
Supports Traditional Chinese, Simplified Chinese, and English. Language can be changed in Preferences > Interface > Language.<br>
**Recommended Versions:** Blender 4.2+, Unreal 5.1+<br>
## Instructions:
### Object Selection
In **Object Mode**, select the Armature and Mesh objects you want to export.
![Selected Objects](https://github.com/user-attachments/assets/f8c6e06d-bb8d-4d5f-8c67-3335c3d46aa0)
### Accessing the Add-on
File > Export > BL Export to Unreal<br>
![Access Location](https://github.com/user-attachments/assets/5456db2e-8b74-477d-a387-aa118e95a2ac)
### Interface
![Interface](https://github.com/user-attachments/assets/16954315-d322-4023-bdb0-291521f51691)
>[Feature](#feature)
>>Auto Fix Scale<br>
>>Use Virtual Deform
>
>[Mesh/Armature Export Settings](#mesharmature)
>>Mesh Path<br>
>>Apply Modifiers<br>
>>Skeletal Prefix
>
>[Action Export Settings](#action)
>>Action Path<br>
>>Export Type<br>
>>Add Start/End keyframes<br>
>>Bake NLA Strips<br>
>>Action prefix
>
>[Advanced Settings](#advanced-settings)

## Feature:
![Feature](https://github.com/user-attachments/assets/cd524f2b-c52d-40e0-b6ab-f29e263ce76f)
### Auto Fix Scale:
Automatically calculates the scale based on Blender scene units. This ensures that the dimensions of the Skeletal Mesh and animations in Blender are consistent with their size when imported into Unreal.
### Use Virtual Deform:
**Use Case**: Blender's primary bone axis is Y, while Unreal's is X, and their left-right mirror mapping logic differs. When exported skeletons are incompatible with Unreal systems, a common workflow is to use Blender-oriented bones (Control Bones) to drive a set of Unreal-oriented bones (Deform Bones) for export.<br>
![Control/Deform Bones](https://github.com/user-attachments/assets/748a5f81-892c-4cd1-b94a-082e11f84c86)<br>
(Green = Control Bones, Red = Deform Bones)<br>
<br>
*To use this feature, follow these naming and setup rules:*
>**Rules**:
>> **Control Bone**:
>>>Name: `xxx`, Deform option set to **True**<br>
>>
>> **Deform Bone**:
>>>Name: `Prefix + xxx`, Deform option set to **False**<br>
>>>The prefix must match the "Deform Prefix" in Add-on Preferences.<br>
>>>![Preferences](https://github.com/user-attachments/assets/4a294b19-b091-4afc-bd70-dcc28bc4fefe)<br>
>>
>>Bone Deform setting location:<br>
>>![Bone Deform Settings](https://github.com/user-attachments/assets/65e52ed4-85fb-4f7b-a634-2b517ca6d234)<br>
>>Vertex Group names on the Mesh must correspond to the **Control Bone** names.<br>
>>![Vertex Group Names](https://github.com/user-attachments/assets/d9f181de-e55d-478b-9ce5-2273eac86fa4)
>
**How it works:**
Automatically bakes animations from Control Bones to Deform Bones.<br>
Upon export, the Deform Bones' prefixes are removed and the Deform options are enabled.
## Mesh/Armature:
![Mesh/Armature Export](https://github.com/user-attachments/assets/5152a836-1822-4b24-9ff3-eb207ed8ea4d)<br>
**Export Mesh:** Whether to export the selected armature or mesh.<br>
<br>
**Mesh Path:** Specifies the export path for the Armature and Mesh.<br>
<br>
**Apply Modifiers:** Recommended to stay enabled.<br>
<br>
**Skeletal Prefix:** The exported file name will be `Skeletal prefix + Armature name`.<br>
Armature name:<br>
![Armature Name](https://github.com/user-attachments/assets/a064f303-9e1e-4058-ace8-4acb61a530fa)<br>
example: Skeletal Prefix: `SK_`, Armature: `Mannequin`, Result: `SK_Mannequin`<br>
<br>
**Static Prefix:** <br>
The exported file name will be `Static Prefix + Active Mesh/Empty name`.<br>
This prefix is applied when a mesh is selected but no armature is selected.<br>
<br>
## Action:
![Action Export](https://github.com/user-attachments/assets/6c908376-6a5f-4316-b8ae-888e521dd03a)<br>
**Export Action:** Whether to export the selected actions.<br>
<br>
**Action Path:** <br>
Actions to be exported must have the **Fake User** (shield icon) enabled.
![Fake User Shield](https://github.com/user-attachments/assets/fcdff198-93a8-480a-b77c-9193a52bc49f)<br>

**Export Type:** <br>
>Selected
>>Exports the action currently selected in the Blender viewport.<br>
>
>Batch
>>Opens an "Export Actions" menu to select specific actions to export.<br>
>>![Batch Menu](https://github.com/user-attachments/assets/ca42d8a2-5b94-401f-959b-4afeb18f020a)<br>
>
>ALL
>>Exports all actions used by the Armature. You can set a "File Name"; if left blank, the .blend filename will be used.<br>
>>![All Menu](https://github.com/user-attachments/assets/f8314b73-5288-4d93-bfcc-4567ee6879bc)<br>
>
**Add Start/End Keyframes:** Recommended to keep enabled.<br>
<br>
**Bake NLA Strips:** This add-on focuses on Actions; NLA export is not recommended unless specifically required.<br>
> [!CAUTION]
> **Note:** When using **Use Virtual Deform**, to avoid NLA track interference, the "ALL" export mode and "Bake NLA Strips" will be automatically disabled.<br>

**Action Prefix:** Adds a prefix to the exported animation sequences.<br>

## Advanced Settings:
![Advanced Settings](https://github.com/user-attachments/assets/24a95db5-0def-4b29-9949-787be6c47757)
