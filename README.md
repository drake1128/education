# 內科部 EPA 評核系統

**機構**: 台大醫院新竹分院 NTUH Hsinchu Branch
**負責人**: 謝慕揚 副主任（內科部 / 心臟內科）
**網址**: https://drake1128.github.io/education/

---

## 系統架構

本系統整合三大評核管道：

| 管道 | 用途 | 位置 |
|------|------|------|
| **Quarto 網站** | 次專科 EPA 完整定義查詢（115+ 項目） | `docs/` → [線上版](https://drake1128.github.io/education/docs/) |
| **HTML 表單** | 一般 EPA 直接觀察即時評核 | `html-forms/` → [入口頁](https://drake1128.github.io/education/) |
| **REDCap Survey** | 正式半年度主治醫師評核 | 院內 REDCap 系統 |

---

## 資料夾結構

```
education/
├── index.html              # 入口頁面（GitHub Pages）
├── README.md               # 本文件
├── CHANGELOG.md            # 工作記錄
│
├── docs/                   # Quarto 渲染輸出（GitHub Pages 部署用）
│   ├── index.html          # Quarto 首頁
│   ├── subspecialty/       # 12 個次專科 EPA 頁面
│   ├── general/            # 4 個學員層級 EPA 頁面
│   └── redcap/             # REDCap 流程與資料字典
│
├── epa-website/            # Quarto 原始碼
│   ├── _quarto.yml         # 網站設定
│   ├── styles.css          # 自訂樣式
│   ├── subspecialty/       # 次專科 .qmd 檔
│   ├── general/            # 一般 EPA .qmd 檔
│   └── redcap/             # REDCap .qmd 檔
│
├── html-forms/             # HTML 直接觀察評估表單
│   ├── EPA_見習醫師.html
│   ├── EPA_PGY醫師.html
│   ├── EPA_住院醫師.html
│   ├── EPA_NP專科護理師.html
│   ├── OSCE評估表.html
│   └── troponin-kinetics.html
│
├── planning/               # 規劃文件
│   ├── EPA_DataDictionary_v2_2026-03-09.csv
│   ├── EPA_排程規劃.xlsx
│   └── EPA_HTML_CONVERSION_PLAN.md
│
├── latex/                  # LaTeX 教材原始檔
│   ├── figure/             # 圖片資源
│   ├── EPA *.tex           # 次專科 EPA（10 科）
│   ├── EPA 0 *.tex         # CCC 委員會文件
│   ├── Education *.tex     # 教育計畫與報告
│   ├── reading *.tex       # NEJM / AMEE 文獻筆記
│   ├── tutorial *.tex      # 教學教案
│   └── *.cls, *.sty, *.bst # LaTeX 支援檔
│
└── 115 研究計畫 教學部 內科部 EPA and NEJM/
    └── 研究計畫書與 REDCap 資料字典
```

---

## 次專科 EPA 總覽

| 次專科 | EPA 數 | Quarto 頁面 | LaTeX 來源 |
|--------|:------:|-------------|------------|
| 心臟科 Cardiology | 11 | `subspecialty/cv.qmd` | `EPA CV 11.tex` |
| 心臟超音波 Echo | 10 | `subspecialty/cv-echo.qmd` | `EPA CV echo.tex` |
| 胸腔科 Pulmonology | 14 | `subspecialty/chest.qmd` | `EPA Chest 14.tex` |
| 腸胃科 GI | 11 | `subspecialty/gi.qmd` | `EPA GI 11.tex` |
| 內分泌科 Endocrinology | 10 | `subspecialty/endocrine.qmd` | `EPA Endocrine 10.tex` |
| 血液科 Hematology | 10 | `subspecialty/hema.qmd` | `EPA Hema 10.tex` |
| 感染科 ID | 10 | `subspecialty/id.qmd` | `EPA ID 10.tex` |
| 腎臟科 Nephrology | 10 | `subspecialty/nephro.qmd` | `EPA Nephro 10.tex` |
| 神經科 Neurology | 10 + 7 | `subspecialty/neuro.qmd`, `neuro-im.qmd` | `EPA Neuro 10.tex`, `EPA Neuro 7 for IM.tex` |
| 腫瘤科 Oncology | 10 | `subspecialty/onco.qmd` | `EPA Onco 10.tex` |
| 風濕免疫科 Rheumatology | 10 | `subspecialty/rheuma.qmd` | `EPA Rheuma 10.tex` |

---

## 學員適用層級

| 學員 | 次專科 EPA 範圍 | 一般 EPA |
|------|:--------------:|:--------:|
| 見習醫師 Clerk | EPA 1–3 | 5 項 |
| PGY 醫師 | EPA 1–5 | 6 項 |
| NP 專科護理師 | EPA 1–5 | 7 項 |
| 住院醫師 Resident | 全部 | 7 項 |
| 總醫師 Chief | 全部 | — |

---

## 重要時程 2026

| 時間 | 里程碑 |
|------|--------|
| **2026/03/29** | CCC Workshop — 內科部講師訓練 |
| 2026 Q2 | 試行階段 — 2–3 次專科試行 EPA |
| 2026 Q3 | 擴展階段 — 全面推廣 |
| **2026/10** | 正式實施 — EPA 評核制度上線 |

---

## 技術備註

### Quarto 渲染

因工作目錄含中文路徑，Quarto Sass 編譯會失敗。需使用以下 workaround：

```bash
cp -r epa-website/* /c/tmp/epa-render/
cd /c/tmp/epa-render && quarto render
cp -r _site/* "<原始路徑>/docs/"
```

### LaTeX 編譯

所有 `.tex` 檔案保持在 `latex/` 目錄的平面結構，以相容 `\input{Drake_preamble.tex}` 和 `figure/` 等相對路徑。

```bash
cd latex && xelatex "EPA CV 11.tex"
```

---

© 2025–2026 台大醫院新竹分院 教學部 | 本系統僅供醫療教育使用
