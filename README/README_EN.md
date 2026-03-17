## English
This add-on is specifically designed for exporting **Skeletal Meshes** and **Animation Sequences** from Blender to Unreal Engine.<br>
Supports Traditional Chinese, Simplified Chinese, and English. Language can be changed in Preferences > Interface > Language. The following documentation is based on English UI.<br>
**Recommended Versions:** Blender 4.2+, Unreal 5.1+<br>
## Instructions:
### Object Selection
In **Object Mode**, select the Armature and Mesh objects you want to export.
![選中物體](https://github.com/user-attachments/assets/f8c6e06d-bb8d-4d5f-8c67-3335c3d46aa0)
### Accessing the Add-on
File > Export > BL Export to Unreal<br>
![開啟位置](https://github.com/user-attachments/assets/5456db2e-8b74-477d-a387-aa118e95a2ac)
### Interface
![介面](https://github.com/user-attachments/assets/3cb221e4-c883-4cfb-bcad-974caadad798)
>[Feature](#feature)
>
>[Mesh/Armature](#mesharmature)
>
>[Action](#action)
>
>[Advanced Settings](#advanced-settings)

## Feature:
![核心功能](https://github.com/user-attachments/assets/cd524f2b-c52d-40e0-b6ab-f29e263ce76f)
### Auto Fix Scale
Automatically calculates the scale based on Blender scene units. This ensures that the dimensions of the Skeletal Mesh and animations in Blender are consistent with their size when imported into Unreal.
### Use Virtual Deform
**Use Case**: Blender's primary bone axis is Y, while Unreal's is X, and their left-right mirror mapping logic differs. When exported skeletons are incompatible with Unreal systems, a common workflow is to use Blender-oriented bones (Control Bones) to drive a set of Unreal-oriented bones (Deform Bones) for export.<br>
![控制變形骨](https://github.com/user-attachments/assets/748a5f81-892c-4cd1-b94a-082e11f84c86)<br>
(Green = Control Bones, Red = Deform Bones)<br>
<br>
*To use this feature, follow these naming and setup rules:*
>**Rules**:
>> **Control Bone**:
>>>Name: `xxx`, Deform option set to **True**<br>
>>
>> ***Deform Bone**:
>>>Name: `Prefix + xxx`, Deform option set to **False**<br>
>>>The prefix must match the "Deform Prefix" in Add-on Preferences.<br>
>>>![偏好設定](https://github.com/user-attachments/assets/4a294b19-b091-4afc-bd70-dcc28bc4fefe)<br>
>>
>>Bone Deform setting location:<br>
>>![骨骼變形設定](https://github.com/user-attachments/assets/65e52ed4-85fb-4f7b-a634-2b517ca6d234)<br>
>>Vertex Group names on the Mesh must correspond to the **Control Bone** names.<br>
>>![頂點組名稱](https://github.com/user-attachments/assets/d9f181de-e55d-478b-9ce5-2273eac86fa4)
>
**How it works:**
Automatically bakes animations from Control Bones to Deform Bones.<br>
Upon export, the Deform Bones' prefixs are removed and the Deform options are enabled.
## Mesh/Armature:
![模型/骨骼輸出](https://github.com/user-attachments/assets/51f6fdc1-0226-4888-86fe-b689e6507614)<br>
**Mesh Path:** Specifies the export path for the Armature and Mesh.<br>
<br>
**Apply Modifiers:** Recommended to stay enabled.<br>
<br>
**Skeletal Prefix:** The exported file name will be `Skeletal prefix + Armature name`.<br>
Armature name:<br>
![骨骼體名稱](https://github.com/user-attachments/assets/a064f303-9e1e-4058-ace8-4acb61a530fa)<br>
EX: Prefix: `SK_`, Armature: `Mannequin`, Result: `SK_Mannequin`<br>
## Action:
![動作輸出](https://github.com/user-attachments/assets/d7a8f9e2-7cfc-450c-b0e7-d98e26a18e97)<br>
**Action Path:** Specifies the path to export selected actions.<br>
Actions to be exported must have the **Fake User** (shield icon) enabled.
![小盾牌](https://github.com/user-attachments/assets/fcdff198-93a8-480a-b77c-9193a52bc49f)<br>

**Export Type:** <br>
>Selected
>>Exports the action currently selected in the Blender viewport.<br>
>
>Batch
>>Opens an "Export Actions" menu to select specific actions to export.<br>
>>![批次選單](https://github.com/user-attachments/assets/95867858-0c7d-47b4-b53d-f1966755a145)<br>
>
>ALL
>>Exports all actions used by the Armature. You can set a "File Name"; if left blank, the .blend filename will be used.<br>
>>![所有選單](https://github.com/user-attachments/assets/dea4f047-eded-4e6f-a03b-b108af76c762)<br>
>
**Add Start/End Keyframes:** Recommended to keep enabled.<br>
<br>
**Bake NLA Strips:** This add-on focuses on Actions; NLA export is not recommended unless specifically required.<br>
> [!CAUTION]
> **Note:** When using **Use Virtual Deform**, to avoid NLA track interference, the "ALL" export mode and "Bake NLA Strips" will be automatically disabled.<br>

**Action Prefix:** Adds a prefix to the exported animation sequences.<br>

## Advanced Settings:
![進階設定](https://github.com/user-attachments/assets/24a95db5-0def-4b29-9949-787be6c47757)
