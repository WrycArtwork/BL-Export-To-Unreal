# BL Export To Unreal
![介面](https://github.com/user-attachments/assets/3cb221e4-c883-4cfb-bcad-974caadad798)<br><br>
[English](#english) | [繁體中文](#繁體中文) | [簡體中文](#簡體中文)

---

## English


---

## 繁體中文
此插件專為 Blender 導出至 Unreal Engine 的 **骨架模型 (Skeletal Mesh)** 與 **動畫動作 (Animation Sequence)** 設計。<br>
此插件支持繁體中文，可在Preferences > Interface > Language內修改，以下功能說明以英文為主。<br>
Blender版本建議在4.2以上<br>
## 使用說明:
### 目標選擇
使用前需在Object Mode物體模式中選中要輸出的骨骼與網格體。
### 插件開啟位置
![開啟位置](https://github.com/user-attachments/assets/5456db2e-8b74-477d-a387-aa118e95a2ac)
## 核心功能:
![核心功能](https://github.com/user-attachments/assets/cd524f2b-c52d-40e0-b6ab-f29e263ce76f)
### Auto Fix Scale 自動修正比例
依據blender場景單位為基準自動解算縮放比例，確保骨骼網格體及動作在Blender中的尺寸與匯入Unreal的尺寸一致
### Use Virtual Deform 使用虛擬變形骨骼
> **適用場景**:骨架由blender轉換軸向後的骨骼與控制器(控制骨)驅動另一組用於輸出的骨骼(變形骨)時使用。<br>
<img width="511" height="552" alt="image" src="https://github.com/user-attachments/assets/6ab4a0d6-8ab7-4aa9-bd29-f88b763da8d0" /><br>
>**命名規則**:
>> **控制骨**:xxx<br>
>> **變形骨**:前綴 + xxx (變形骨名稱需有與插件偏好設定相同的前綴)<br>
>>![偏好設定](https://github.com/user-attachments/assets/4a294b19-b091-4afc-bd70-dcc28bc4fefe)<br>
>>網格體的頂點組 (Vertex Groups)名稱對應 啟用Deform的控制骨名稱<br>
>>>---
> **設定要求**：<br>
>>變形骨的「變形 (Deform)」選項需設為 `False`<br>
>>對應名稱控制骨的「變形 (Deform)」選項需設為 `True`。<br>
<img width="330" height="479" alt="image" src="https://github.com/user-attachments/assets/65e52ed4-85fb-4f7b-a634-2b517ca6d234" /><br>

>**運作方式**:
>>自動將控制骨動畫烘培至變形骨。<br>
>>**輸出後自動移除前綴**，確保 Unreal 識別正確的骨骼名稱。
### 模型/骨骼輸出:
<img width="407" height="119" alt="image" src="https://github.com/user-attachments/assets/51f6fdc1-0226-4888-86fe-b689e6507614" /><br>
Mesh Path有指定匯出路徑就會在輸出時輸出骨架及網格體。輸出後的檔案名稱為Skeletal prefix + Armature名稱<br>
<img width="323" height="189" alt="image" src="https://github.com/user-attachments/assets/a064f303-9e1e-4058-ace8-4acb61a530fa" /><br>
EX:Skeletal Prefix :SK_，Armature 名稱:Mannequin，輸出後的名稱為:SK_Mannequin<br>
Apply Modifiers套用修改器建議保持啟用<br>
### 動作輸出:
<img width="407" height="149" alt="image" src="https://github.com/user-attachments/assets/d7a8f9e2-7cfc-450c-b0e7-d98e26a18e97" /><br>
Action Path有指定匯出路徑就會輸出指定的動作。<br>
<img width="1528" height="184" alt="image" src="https://github.com/user-attachments/assets/fcdff198-93a8-480a-b77c-9193a52bc49f" /><br>
需啟用fake_user。
Export Type匯出模式為Selected所選項時，會匯出當前blender視圖中選擇中的動作。<br>
Export Type匯出模式為Batch批次時，會出現Export Actions的按鍵可以選擇要匯出的動作。<br>
<img width="701" height="639" alt="image" src="https://github.com/user-attachments/assets/95867858-0c7d-47b4-b53d-f1966755a145" /><br>
Export Type匯出模式為ALL全部時，將會輸出所有選中Armature使用的動作。可以設定File Name作為輸出檔案名稱，保持空白則會以blend檔名進行輸出。<br>
<img width="406" height="172" alt="image" src="https://github.com/user-attachments/assets/dea4f047-eded-4e6f-a03b-b108af76c762" /><br>
Add Start/End Keyframes補齊首尾幀建議保持啟用<br>
Bake NLA Strips烘焙NLA片段，此插件以Action為主，建議不使用NLA作為輸出，按需求啟用。<br>
> [!CAUTION]
> **注意：** 使用Use Virtual Deform時，避免NLA軌道干擾，會自動禁用Export Type的ALL模式以及Bake NLA Strips。<br>
* Action Prefix用以設定動畫序列前綴。<br>
### 進階設定:
<img width="405" height="113" alt="image" src="https://github.com/user-attachments/assets/24a95db5-0def-4b29-9949-787be6c47757" />

















