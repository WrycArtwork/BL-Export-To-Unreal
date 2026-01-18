# BL Export To Unreal
![介面](https://github.com/user-attachments/assets/3cb221e4-c883-4cfb-bcad-974caadad798)<br><br>
[English](#english) | [繁體中文](#繁體中文) | [简体中文](#简体中文)

---

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

**Export Type**<br>
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


---

## 繁體中文
此插件專為 Blender 導出至 Unreal Engine 的 **骨架模型 (Skeletal Mesh)** 與 **動畫動作 (Animation Sequence)** 設計。<br>
支持繁體中文、簡體中文與英文，可在Preferences > Interface > Language內修改。<br>
建議版本:Blender 4.2+，Unreal 5.1+<br>
## 使用說明:
### 目標選擇
在物體模式(Object Mode)中選中要輸出的骨骼(Armature)與網格體(Mesh)。
![選中物體](https://github.com/user-attachments/assets/f8c6e06d-bb8d-4d5f-8c67-3335c3d46aa0)
### 插件開啟位置
File > Export > BL Export to Unreal<br>
![開啟位置](https://github.com/user-attachments/assets/5456db2e-8b74-477d-a387-aa118e95a2ac)
### 插件介面
![介面](https://github.com/user-attachments/assets/3cb221e4-c883-4cfb-bcad-974caadad798)
>[Feature 核心功能](#核心功能)
>>Auto Fix Scale 自動修正比例<br>
>>Use Virtual Deform 使用虛擬變形骨骼
>
>[Mesh/Armature 模型/骨架輸出設定](#模型骨骼輸出)
>>Mesh Path 物件輸出路徑<br>
>>Apply Modifiers 應用修改器<br>
>>Skeletal Prefix 骨骼網格體前綴
>
>[Action 動作輸出設定](#動作輸出)
>>Action Path 動作輸出路徑<br>
>>Export Type 輸出模式<br>
>>Add Start/End keyframes 補齊首尾幀<br>
>>Bake NLA Strips 烘培NLA片段
>>Action prifix 動作前綴
>
>[進階設定](#進階設定)

## 核心功能:
![核心功能](https://github.com/user-attachments/assets/cd524f2b-c52d-40e0-b6ab-f29e263ce76f)
### Auto Fix Scale 自動修正比例
依據blender場景單位為基準自動解算縮放比例，確保骨骼網格體及動作在Blender中的尺寸與匯入Unreal的尺寸一致
### Use Virtual Deform 使用虛擬變形骨骼
**適用場景**: Blender骨骼坐標系主軸為Y，Unreal骨骼坐標系主軸為X，且兩者左右鏡像映射邏輯不同。導致輸出後骨架與Unreal其他系統無法適配時，常透過blender坐標系骨骼(控制骨)驅動另一組Unreal坐標系的骨骼(變形骨)作為輸出使用。<br>
![控制變形骨](https://github.com/user-attachments/assets/748a5f81-892c-4cd1-b94a-082e11f84c86)<br>
(綠色為控制骨，紅色為變形骨)<br>
<br>
*使用此功能需按照以下規則進行骨骼命名與設定*
>**規則**:
>> **控制骨**:
>>>名稱: xxx ，變形 (Deform)選項設為 True<br>
>>
>> **變形骨**:
>>>名稱:前綴 + xxx , 變形 (Deform)選項設為 False<br>
>>>前綴需與偏好設定中變形骨前綴相同<br>
>>>![偏好設定](https://github.com/user-attachments/assets/4a294b19-b091-4afc-bd70-dcc28bc4fefe)<br>
>>
>>骨骼變形選項位置:<br>
>>![骨骼變形設定](https://github.com/user-attachments/assets/65e52ed4-85fb-4f7b-a634-2b517ca6d234)<br>
>>網格體的頂點組 (Vertex Groups)名稱對應控制骨名稱<br>
>>![頂點組名稱](https://github.com/user-attachments/assets/d9f181de-e55d-478b-9ce5-2273eac86fa4)
>
**運作方式:**
自動將控制骨動畫烘培至變形骨。<br>
輸出後自動移除變形骨前綴並啟用Deform。
## 模型/骨骼輸出:
![模型/骨骼輸出](https://github.com/user-attachments/assets/51f6fdc1-0226-4888-86fe-b689e6507614)<br>
**Mesh Path輸出路徑:** 骨架及網格體輸出路徑。<br>
<br>
**Apply Modifiers套用修改器:** 建議保持啟用。<br>
<br>
**Skeletal Prefix骨骼體前綴:** <br>
輸出後的檔案名稱為Skeletal prefix + Armature名稱<br>
Armature名稱:<br>
![骨骼體名稱](https://github.com/user-attachments/assets/a064f303-9e1e-4058-ace8-4acb61a530fa)<br>
EX:Skeletal Prefix :SK_，Armature 名稱:Mannequin，輸出後的名稱為:SK_Mannequin<br>
## 動作輸出:
![動作輸出](https://github.com/user-attachments/assets/d7a8f9e2-7cfc-450c-b0e7-d98e26a18e97)<br>
**Action Path:** 動作輸出路徑。<br>
要輸出的動作需啟用小盾牌(fake_user)。
![小盾牌](https://github.com/user-attachments/assets/fcdff198-93a8-480a-b77c-9193a52bc49f)<br>

**Export Type輸出模式**<br>
>Selected所選項
>>會輸出當前blender視圖中選擇中的動作。<br>
>
>Batch批次
>>會出現Export Actions的按鍵，開啟選單選擇要輸出的動作。<br>
>>![批次選單](https://github.com/user-attachments/assets/95867858-0c7d-47b4-b53d-f1966755a145)<br>
>
>ALL全部
>>輸出所有Armature使用的動作。可以設定File Name作為輸出檔案名稱，保持空白則會以blend檔名進行輸出。<br>
>>![所有選單](https://github.com/user-attachments/assets/dea4f047-eded-4e6f-a03b-b108af76c762)<br>
>
**Add Start/End Keyframes 補齊首尾幀:** 建議保持啟用。<br>
<br>
**Bake NLA Strips 烘焙NLA片段:** 此插件以Action為主，建議不使用NLA作為輸出，按需求啟用。<br>
> [!CAUTION]
> **注意：** 使用Use Virtual Deform時，避免NLA軌道干擾，會自動禁用Export Type的ALL模式以及Bake NLA Strips。<br>

**Action Prefix動作前綴:** 為輸出後的動畫序列加上前綴。<br>
## 進階設定:
![進階設定](https://github.com/user-attachments/assets/24a95db5-0def-4b29-9949-787be6c47757)

---

## 简体中文
此插件专为 Blender 导出至 Unreal Engine 的 骨架模型 (Skeletal Mesh) 与 动画序列 (Animation Sequence) 设计。<br>
支持繁体中文、简体中文与英文。可在 Preferences > Interface > Language 内修改。<br>
建议版本: Blender 4.2+，Unreal 5.1+<br>
## 使用说明:
### 目标选择
在 物体模式 (Object Mode) 中选中要导出的骨骼 (Armature) 与网格体 (Mesh)。
![选中物体](https://github.com/user-attachments/assets/f8c6e06d-bb8d-4d5f-8c67-3335c3d46aa0)
### 插件开启位置
文件 (File) > 导出 (Export) > BL Export to Unreal<br>
![开启位置](https://github.com/user-attachments/assets/5456db2e-8b74-477d-a387-aa118e95a2ac)
### 插件界面说明
![介面](https://github.com/user-attachments/assets/3cb221e4-c883-4cfb-bcad-974caadad798)
>[Feature 核心功能](#核心功能)
>>Auto Fix Scale 自动修正比例<br>
>>Use Virtual Deform 使用虚拟变形骨骼
>
>[Mesh/Armature 模型/骨架汇出设定](#模型骨骼汇出)
>>Mesh Path 物件汇出路径<br>
>>Apply Modifiers 应用修改器<br>
>>Skeletal Prefix 骨骼网格体前缀
>
>[Action 动作汇出设定](#动作汇出)
>>Action Path 动作汇出路径<br>
>>Export Type 汇出模式<br>
>>Add Start/End keyframes 补齐首尾帧<br>
>>Bake NLA Strips 烘培NLA片段
>>Action prifix 动作前缀
>
>[进阶设定](#进阶设定)

## 核心功能:
![核心功能](https://github.com/user-attachments/assets/cd524f2b-c52d-40e0-b6ab-f29e263ce76f)
### Auto Fix Scale 自动修正比例
依据blender场景单位为基准自动解算缩放比例，确保骨骼网格体及动作在Blender中的尺寸与汇入Unreal的尺寸一致
### Use Virtual Deform 使用虚拟变形骨骼
**适用场景**: Blender骨骼坐标系主轴为Y，Unreal骨骼坐标系主轴为X，且两者左右镜像映射逻辑不同。导致汇出后骨架与Unreal其他系统无法适配时，常透过blender坐标系骨骼(控制骨)驱动另一组Unreal坐标系的骨骼(变形骨)作为汇出使用。<br>
![控制变形骨](https://github.com/user-attachments/assets/748a5f81-892c-4cd1-b94a-082e11f84c86)<br>
(绿色为控制骨，红色为变形骨)<br>
<br>
*使用此功能需按照以下规则进行骨骼命名与设定*
>**规则**:
>> **控制骨**:
>>>名称: xxx ，变形 (Deform)选项设为 True<br>
>>
>> **变形骨**:
>>>名称:前缀 + xxx , 变形 (Deform)选项设为 False<br>
>>>前缀需与偏好设定中变形骨前缀相同<br>
>>>![偏好设定](https://github.com/user-attachments/assets/4a294b19-b091-4afc-bd70-dcc28bc4fefe)<br>
>>
>>骨骼变形选项位置:<br>
>>![骨骼變形設定](https://github.com/user-attachments/assets/65e52ed4-85fb-4f7b-a634-2b517ca6d234)<br>
>>网格体的顶点组 (Vertex Groups)名称对应控制骨名称<br>
>>![顶点组名称](https://github.com/user-attachments/assets/d9f181de-e55d-478b-9ce5-2273eac86fa4)
>
**运作方式:**
自动将控制骨动画烘培至变形骨。<br>
汇出后自动移除变形骨前缀并启用Deform。
## 模型/骨骼汇出:
![模型/骨骼汇出](https://github.com/user-attachments/assets/51f6fdc1-0226-4888-86fe-b689e6507614)<br>
**Mesh Path汇出路径:** 动作汇出路径。<br>
<br>
**Apply Modifiers套用修改器:** 建议保持启用。<br>
<br>
**Skeletal Prefix骨骼体前缀:** <br>
汇出后的档案名称为Skeletal prefix + Armature名称。<br>
Armature名称:<br>
![骨骼体名称](https://github.com/user-attachments/assets/a064f303-9e1e-4058-ace8-4acb61a530fa)<br>
EX:Skeletal Prefix :SK_，Armature 名称:Mannequin，汇出后的名称为:SK_Mannequin<br>
## 动作汇出:
![动作汇出](https://github.com/user-attachments/assets/d7a8f9e2-7cfc-450c-b0e7-d98e26a18e97)<br>
**Action Path:** 有指定汇出路径就会汇出指定的动作。<br>
要汇出的动作需启用小盾牌(fake_user)。
![小盾牌](https://github.com/user-attachments/assets/fcdff198-93a8-480a-b77c-9193a52bc49f)<br>

**Export Type汇出模式**<br>
>Selected所选项
>>会汇出当前blender视图中选择中的动作。<br>
>
>Batch批次
>>会出现Export Actions的按键，开启选单选择要汇出的动作。<br>
>>![批次选单](https://github.com/user-attachments/assets/95867858-0c7d-47b4-b53d-f1966755a145)<br>
>
>ALL全部
>>汇出所有Armature使用的动作。可以设定File Name作为汇出档案名称，保持空白则会以blend档名进行汇出。<br>
>>![所有选单](https://github.com/user-attachments/assets/dea4f047-eded-4e6f-a03b-b108af76c762)<br>
>
**Add Start/End Keyframes 补齐首尾帧:** 建议保持启用。<br>
<br>
**Bake NLA Strips 烘焙NLA片段:** 此插件以Action为主，建议不使用NLA作为汇出，按需求启用。<br>
> [!CAUTION]
> **注意：** 使用Use Virtual Deform时，避免NLA轨道干扰，会自动禁用Export Type的ALL模式以及Bake NLA Strips。<br>

**Action Prefix动作前缀:** 为汇出后的动画序列加上前缀。<br>
## 进阶设定:
![进阶设定](https://github.com/user-attachments/assets/24a95db5-0def-4b29-9949-787be6c47757)
