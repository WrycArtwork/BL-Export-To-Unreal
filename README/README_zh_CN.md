## 简体中文
此插件专为 Blender 导出至 Unreal Engine 的 **骨架模型 (Skeletal Mesh)** 与 **动画序列 (Animation Sequence)** 设计。<br>
支持繁体中文、简体中文与英文，可在Preferences > Interface > Language内修改。<br>
建议版本:Blender 4.2+，Unreal 5.1+<br>
## 使用说明:
### 目标选择
在物体模式(Object Mode)中选中要导出的骨骼(Armature)与网格体(Mesh)。
![选中物体](https://github.com/user-attachments/assets/f8c6e06d-bb8d-4d5f-8c67-3335c3d46aa0)
### 插件开启位置
File > Export > BL Export to Unreal<br>
![开启位置](https://github.com/user-attachments/assets/5456db2e-8b74-477d-a387-aa118e95a2ac)
### 插件界面
![界面](https://github.com/user-attachments/assets/16954315-d322-4023-bdb0-291521f51691)
>[Feature 核心功能](#核心功能)
>>Auto Fix Scale 自动修正比例<br>
>>Use Virtual Deform 使用虚拟变形骨骼
>
>[Mesh/Armature 模型/骨架导出设定](#模型骨骼导出)
>>Mesh Path 物件导出路径<br>
>>Apply Modifiers 应用修改器<br>
>>Skeletal Prefix 骨骼网格体前缀
>
>[Action 动作导出设定](#动作导出)
>>Action Path 动作导出路径<br>
>>Export Type 导出模式<br>
>>Add Start/End keyframes 补齐首尾帧<br>
>>Bake NLA Strips 烘焙NLA片段<br>
>>Action prefix 动作前缀
>
>[进阶设定](#进阶设定)

## 核心功能:
![核心功能](https://github.com/user-attachments/assets/cd524f2b-c52d-40e0-b6ab-f29e263ce76f)
### Auto Fix Scale 自动修正比例:
依据blender场景单位为基准自动解算缩放比例，确保骨骼网格体及动作在Blender中的尺寸与导入Unreal的尺寸一致
### Use Virtual Deform 使用虚拟变形骨骼:
**适用场景**: Blender骨骼坐标系主轴为Y，Unreal骨骼坐标系主轴为X，且两者左右镜像映射逻辑不同。导致导出后骨架与Unreal其他系统无法适配时，常透过blender坐标系骨骼(控制骨)驱动另一组Unreal坐标系的骨骼(变形骨)作为导出使用。<br>
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
>>![骨骼变形设定](https://github.com/user-attachments/assets/65e52ed4-85fb-4f7b-a634-2b517ca6d234)<br>
>>网格体的顶点组 (Vertex Groups)名称对应控制骨名称<br>
>>![顶点组名称](https://github.com/user-attachments/assets/d9f181de-e55d-478b-9ce5-2273eac86fa4)
>
**运作方式**
自动将控制骨动画烘焙至变形骨。<br>
导出后自动移除变形骨前缀并启用Deform。
## 模型/骨骼导出:
![模型/骨骼导出](https://github.com/user-attachments/assets/5152a836-1822-4b24-9ff3-eb207ed8ea4d)<br>
**Export Mesh 是否输出模型:** 是否输出选中的骨架或网格体。<br>
<br>
**Mesh Path 导出路径:** 骨架及网格体导出路径。<br>
<br>
**Apply Modifiers 套用修改器:** 建议保持启用。<br>
<br>
**Skeletal Prefix 骨骼体前缀:** <br>
导出后的档案名称为Skeletal prefix + Armature名称。<br>
Armature名称:<br>
![骨骼体名称](https://github.com/user-attachments/assets/a064f303-9e1e-4058-ace8-4acb61a530fa)<br>
example: Skeletal Prefix :SK_，Armature 名称:Mannequin，导出后的名称为:SK_Mannequin<br>
<br>
**Static Prefix 网格体前缀:** <br>
导出后的档案名称为Static Prefix + 作用中Mesh/Empty名称。<br>
选中模型但没有选中骨骼时，会套用这个前缀。<br>
<br>
## 动作导出:
![动作导出](https://github.com/user-attachments/assets/6c908376-6a5f-4316-b8ae-888e521dd03a)<br>
**Export Action 是否输出动作:** 是否输出选中的动作。<br>
<br>
**Action Path 动作导出路径:** <br>
要导出的动作需启用小盾牌(fake_user)。
![小盾牌](https://github.com/user-attachments/assets/fcdff198-93a8-480a-b77c-9193a52bc49f)<br>

**Export Type 导出模式:** <br>
>Selected所选项
>>会导出当前blender视图中选择中的动作。<br>
>
>Batch批次
>>会出现Export Actions的按键，开启选单选择要导出的动作。<br>
>>![批次选单](https://github.com/user-attachments/assets/ca42d8a2-5b94-401f-959b-4afeb18f020a)<br>
>
>ALL全部
>>导出所有Armature使用的动作。可以设定File Name作为导出档案名称，保持空白则会以blend档名进行导出。<br>
>>![所有选单](https://github.com/user-attachments/assets/f8314b73-5288-4d93-bfcc-4567ee6879bc)<br>
>
**Add Start/End Keyframes 补齐首尾帧:** 建议保持启用。<br>
<br>
**Bake NLA Strips 烘焙NLA片段:** 此插件以Action为主，建议不使用NLA作为导出，按需求启用。<br>
> [!CAUTION]
> **注意：** 使用Use Virtual Deform时，避免NLA轨道干扰，会自动禁用Export Type的ALL模式以及Bake NLA Strips。<br>

**Action Prefix 动作前缀:** 为导出后的动画序列加上前缀。<br>
## 进阶设定:
![进阶设定](https://github.com/user-attachments/assets/24a95db5-0def-4b29-9949-787be6c47757)
