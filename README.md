# 醫學教育評估表單系統

台大醫院新竹分院 教學部

Medical Education Assessment System - NTUH Hsinchu Branch

## 📋 系統簡介

本系統提供完整的醫學教育評估工具，包含：
- **4份EPA評估表**：見習醫師、PGY醫師、住院醫師、NP專科護理師
- **1份OSCE評估表**：客觀結構式臨床測驗（含5種站別模板）

## 🚀 GitHub Pages 部署步驟

### 方法一：直接上傳（最簡單）

1. **在GitHub建立新Repository**
   - 登入GitHub
   - 點選右上角 `+` → `New repository`
   - Repository name: `medical-assessment` (或自訂名稱)
   - 設為 Public
   - 點選 `Create repository`

2. **上傳檔案**
   - 在Repository頁面點選 `Add file` → `Upload files`
   - 將以下檔案拖曳上傳：
     ```
     index.html
     EPA_見習醫師.html
     EPA_PGY醫師.html
     EPA_住院醫師.html
     EPA_NP專科護理師.html
     OSCE評估表.html
     ```
   - 點選 `Commit changes`

3. **啟用GitHub Pages**
   - 進入Repository的 `Settings`
   - 左側選單找到 `Pages`
   - Source 選擇 `Deploy from a branch`
   - Branch 選擇 `main` (或 `master`)，資料夾選擇 `/ (root)`
   - 點選 `Save`

4. **訪問您的網站**
   - 等待1-2分鐘
   - 網址會是：`https://您的GitHub用戶名.github.io/repository名稱/`
   - 例如：`https://username.github.io/medical-assessment/`

### 方法二：使用Git指令（適合熟悉Git的使用者）

```bash
# 1. 初始化Git repository
git init

# 2. 添加所有檔案
git add index.html EPA_*.html OSCE*.html

# 3. 提交
git commit -m "Initial commit: Medical Assessment System"

# 4. 連結到GitHub repository
git remote add origin https://github.com/您的用戶名/repository名稱.git

# 5. 推送到GitHub
git branch -M main
git push -u origin main
```

然後按照方法一的步驟3啟用GitHub Pages。

## 📱 系統架構

```
index.html (首頁導航)
├── EPA_見習醫師.html
├── EPA_PGY醫師.html
├── EPA_住院醫師.html
├── EPA_NP專科護理師.html
└── OSCE評估表.html
```

## 🎨 特色功能

### EPA評估表
- ✅ 5級信任量表評估
- ✅ 依學員層級差異化設計
- ✅ 具體評語欄位
- ✅ 列印友善格式
- ✅ 整體評估與建議

### OSCE評估表
- ✅ 5種預設站別模板
- ✅ 雙重評分系統（檢核表 + 全球評量）
- ✅ 自動計算分數
- ✅ 通過/不通過判定
- ✅ 自訂項目功能

## 💡 使用建議

1. **EPA評估**：建議每次臨床教學後評估1-2項EPA
2. **OSCE測驗**：適合期中期末考核或能力認證
3. **即時回饋**：評估後應與學員討論並給予建議
4. **累積數據**：定期追蹤學習進展

## 🔧 客製化修改

所有HTML檔案可直接用文字編輯器修改：
- 修改配色：搜尋 `background: linear-gradient`
- 增減項目：複製貼上評估項目區塊
- 調整文字：直接修改中文內容
- 新增科別：在下拉選單中添加選項

## 📞 技術支援

如需協助或有任何問題，請聯繫教學部。

## 📄 授權

© 2025 台大醫院新竹分院 教學部
本系統僅供醫療教育使用

---

## 🌐 訪問連結

部署完成後，您的系統將可透過以下網址訪問：

**首頁**: `https://您的GitHub用戶名.github.io/repository名稱/`

**各評估表直接連結**:
- 見習醫師EPA: `https://您的GitHub用戶名.github.io/repository名稱/EPA_見習醫師.html`
- PGY醫師EPA: `https://您的GitHub用戶名.github.io/repository名稱/EPA_PGY醫師.html`
- 住院醫師EPA: `https://您的GitHub用戶名.github.io/repository名稱/EPA_住院醫師.html`
- NP專科護理師EPA: `https://您的GitHub用戶名.github.io/repository名稱/EPA_NP專科護理師.html`
- OSCE評估表: `https://您的GitHub用戶名.github.io/repository名稱/OSCE評估表.html`

## 📱 行動裝置支援

所有表單都採用響應式設計，完美支援：
- 💻 桌上型電腦
- 📱 平板電腦
- 📱 智慧型手機

---

**版本**: v1.0  
**更新日期**: 2025-11-08
