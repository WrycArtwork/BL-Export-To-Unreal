#WRYC Export To Unreal<br>
[English](#english) | [繁體中文](#繁體中文)

---

##English
###

---

##繁體中文<br>
此插件主要用於Blender至Unreal的骨骼體及動作輸出。<br>
此插件支持繁體中文，可在Preferences/Interface/Language內修改，以下功能說明以英文為主。<br>
###使用說明<br>
插件輸出位置:<br>
<img width="484" height="529" alt="image" src="https://github.com/user-attachments/assets/5456db2e-8b74-477d-a387-aa118e95a2ac" /><br>
基礎面板:<br>
<img width="414" height="449" alt="image" src="https://github.com/user-attachments/assets/3cb221e4-c883-4cfb-bcad-974caadad798" /><br>
使用前需在Object Mode物體模式中選中欲輸出的骨骼與網格體。
####核心功能:<br>
<img width="408" height="72" alt="image" src="https://github.com/user-attachments/assets/cd524f2b-c52d-40e0-b6ab-f29e263ce76f" /><br>
Auto Fix Scale 自動修正比例<br>
會以blender內場景單位為基準，自動進行匯出至Unreal骨架及動作的縮放修正，blender中的尺寸會與匯出至Unreal的尺寸相同。<br>
Use Virtual Deform 使用虛擬變形骨骼<br>
<img width="511" height="552" alt="image" src="https://github.com/user-attachments/assets/6ab4a0d6-8ab7-4aa9-bd29-f88b763da8d0" /><br>
如果骨架由blender轉換軸向後的骨骼與控制器(下稱控制骨)驅動Unreal/Maya或其他座標系的骨骼(下稱變形骨)，勾選此選項可以烘培控制骨動畫至變形骨進行輸出。<br>
變形骨名稱需有與插件中偏好設定的前綴相同的前綴，輸出後會自動去除這個前綴。<br>
<img width="648" height="404" alt="image" src="https://github.com/user-attachments/assets/4a294b19-b091-4afc-bd70-dcc28bc4fefe" /><br>
且變形骨的骨骼變形選項需為False<br>
<img width="330" height="479" alt="image" src="https://github.com/user-attachments/assets/65e52ed4-85fb-4f7b-a634-2b517ca6d234" /><br>
由對應名稱的控制骨進行驅動，控制骨名稱:xxx，變形骨名稱:前綴+xxx。<br>
需設定對應名稱在匯出後模型網格體的頂點組才會對應至去除前綴的虛擬變形骨。<br>
####模型/骨骼輸出:<br>
<img width="407" height="119" alt="image" src="https://github.com/user-attachments/assets/51f6fdc1-0226-4888-86fe-b689e6507614" /><br>
Mesh Path有指定位置就會在輸出時輸出骨架及網格體。輸出後的檔案名稱為Skeletal prefix











