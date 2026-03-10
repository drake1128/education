# 工作記錄 | Changelog

**專案**: 內科部 EPA 評核系統
**機構**: 台大醫院新竹分院
**負責人**: 謝慕揚 副主任

---

## 2026-03-10 — Quarto EPA 網站建置與根目錄重整

### 1. Quarto 網站建置

將所有內科次專科 EPA（原 LaTeX 檔案）轉換為 Quarto 靜態網站，部署於 GitHub Pages。

**產出內容（24 頁）**：

| 分類 | 頁面 | 來源 |
|------|------|------|
| 首頁 | `index.qmd` | 新建 |
| 次專科 EPA（12 頁） | `subspecialty/*.qmd` | 由 LaTeX 轉換 |
| 一般 EPA（5 頁） | `general/*.qmd` | 由 HTML 表單轉換 |
| REDCap（2 頁） | `redcap/*.qmd` | 由 CSV + Markdown 彙整 |
| CCC 委員會 | `about.qmd` | 新建 |
| 臨床技能對照表 | `clinical-skills.qmd` | 新建 |
| 排程規劃 | `schedule.qmd` | 新建 |

**次專科 EPA 涵蓋範圍**：

| 次專科 | EPA 數量 | 來源檔案 |
|--------|:--------:|----------|
| 心臟科 Cardiology | 11 | `EPA CV 11.tex` |
| 心臟超音波 Echo | 10 | `EPA CV echo.tex` |
| 胸腔科 Pulmonology | 14 | `EPA Chest 14.tex` |
| 腸胃科 GI | 11 | `EPA GI 11.tex` |
| 內分泌科 Endocrinology | 10 | `EPA Endocrine 10.tex` |
| 血液科 Hematology | 10 | `EPA Hema 10.tex` |
| 感染科 ID | 10 | `EPA ID 10.tex` |
| 腎臟科 Nephrology | 10 | `EPA Nephro 10.tex` |
| 神經科 Neurology | 10 | `EPA Neuro 10.tex` |
| 神經科（內科版） | 7 | `EPA Neuro 7 for IM.tex` |
| 腫瘤科 Oncology | 10 | `EPA Onco 10.tex` |
| 風濕免疫科 Rheumatology | 10 | `EPA Rheuma 10.tex` |

**技術細節**：
- Quarto 版本：1.9.31
- 主題：`default`（因 Chinese path 導致 Sass 編譯問題，無法使用 `cosmo`）
- 語言：`zh-TW`（有非致命性翻譯警告）
- 渲染 workaround：因工作目錄含中文路徑，需複製至 `C:\tmp\epa-render\` 渲染後再複製回 `docs/`

### 2. 學員層級標註系統

每個 EPA 項目皆標註適用的學員層級 badge：

| Badge | 適用 EPA 範圍 |
|-------|:-------------:|
| Clerk 見習醫師 | EPA 1–3 |
| PGY 醫師 | EPA 1–5 |
| NP 專科護理師 | EPA 1–5 |
| Resident 住院醫師 | 全部 |
| Chief 總醫師 | 全部 |

例外：神經科內科版（`neuro-im.qmd`）所有 7 項 EPA 皆適用全部層級。

### 3. REDCap 整合

- 彙整 `EPA_DataDictionary_v2_2026-03-09.csv`（338 欄位、11 instruments）至網站
- 撰寫 8 步驟 REDCap survey 發送流程說明
- 網站為唯讀參考；正式評核透過 REDCap survey 邀請進行

### 4. 根目錄重整

將原本散落在根目錄的 70+ 個檔案整理為以下結構：

```
education/
├── index.html              # GitHub Pages 入口（已更新連結）
├── README.md               # 專案說明（已更新）
├── CHANGELOG.md            # 本工作記錄
├── .gitignore
│
├── docs/                   # Quarto 渲染輸出（GitHub Pages 部署）
├── epa-website/            # Quarto 原始碼（.qmd + _quarto.yml + styles.css）
│
├── html-forms/             # HTML 直接觀察評估表單
│   ├── EPA_見習醫師.html
│   ├── EPA_PGY醫師.html
│   ├── EPA_住院醫師.html
│   ├── EPA_NP專科護理師.html
│   ├── OSCE評估表.html
│   └── troponin-kinetics.html
│
├── planning/               # 規劃文件與資料字典
│   ├── EPA_DataDictionary_v2_2026-03-09.csv
│   ├── @@ REDCap_EPA_Survey_流程說明.md
│   ├── EPA_排程規劃.xlsx
│   └── EPA_HTML_CONVERSION_PLAN.md
│
├── latex/                  # 所有 LaTeX 原始檔（保持平面結構以相容編譯路徑）
│   ├── figure/             # LaTeX 引用圖片
│   ├── EPA *.tex           # 次專科 EPA 內容與投影片
│   ├── Education *.tex     # 教育計畫與報告
│   ├── reading *.tex       # 文獻閱讀筆記
│   ├── tutorial *.tex      # 教學教案
│   ├── Drake_preamble.tex  # 共用 preamble
│   ├── reference.bib       # 共用參考文獻
│   └── *.cls, *.sty, *.bst # LaTeX 類別與樣式檔
│
└── 115 研究計畫 教學部 內科部 EPA and NEJM/
    └── （研究計畫書與 REDCap 資料字典）
```

### 5. index.html 更新

- 新增「次專科 EPA 完整查詢」區塊，連結至 `docs/index.html`
- 顯示 11 個次專科色塊與 EPA 數量
- 保留原有 4 個一般 EPA 表單連結（路徑更新為 `html-forms/`）
- 保留 OSCE 評估表連結
- 統一紫色主題（`#4a148c`）

---

## 2026-02-14 — 初始建立

- 建立 GitHub repository `drake1128/education`
- 上傳 LaTeX 教材（EPA、教育計畫、CCC 文件）
- 建立 4 個一般 EPA HTML 評估表（見習醫師、PGY、住院醫師、NP）
- 建立 OSCE 評估表與 Troponin Kinetics 工具
- 撰寫 README.md

---

*本記錄由 Claude Code 協助撰寫*
