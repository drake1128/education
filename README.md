# 內科部臨床能力委員會與 EPA 教學資源
# Internal Medicine CCC and EPA Teaching Resources

**建立日期 | Created**: 2026-02-14
**負責人 | Owner**: 謝慕揚 副主任
**最後更新 | Last Updated**: 2026-02-14

---

## 最新公告 | Announcements

### CCC Workshop 報名通知 | CCC Workshop Registration

**【重要】內科部 CCC Workshop 即將舉辦！**

| 項目 | 內容 |
|------|------|
| **日期 Date** | 2026年3月29日 (週日) |
| **時間 Time** | 09:10 - 12:30 |
| **地點 Venue** | 生醫大樓 5F 第一會議室 |
| **對象 Target** | 內科部全體講師 |

**議程 Agenda**:
1. CBME 與 EPA 概念介紹 (30 min)
2. CCC 委員會章程說明 (30 min)
3. 各次專科 EPA 講義導讀 (60 min)
4. 討論與 Q&A (60 min)

---

## 資料夾結構 | Folder Structure

```
Education internal medicine CCC and EPA/
│
├── README.md                          # 本文件
│
├── [CCC 核心文件 | CCC Core Documents]
│   ├── EPA 0 internal medicine CCC.tex         # CCC 委員會章程
│   ├── EPA 0 internal medicine CCC slide.tex   # CCC 簡報
│   ├── EPA 0 internal medicine CCC meeting 01.tex  # 會議紀錄
│   └── EPA 0 slide introduction.tex            # EPA 概念介紹
│
├── [各次專科 EPA | Subspecialty EPAs]
│   ├── EPA CV *.tex                   # 心臟科
│   ├── EPA Chest *.tex                # 胸腔科
│   ├── EPA GI *.tex                   # 腸胃科
│   ├── EPA Nephro *.tex               # 腎臟科
│   ├── EPA ID *.tex                   # 感染科
│   ├── EPA Endocrine *.tex            # 內分泌科
│   ├── EPA Rheuma *.tex               # 風濕免疫科
│   ├── EPA Hema *.tex                 # 血液科
│   ├── EPA Onco *.tex                 # 腫瘤科
│   └── EPA Neuro *.tex                # 神經科
│
├── [教育計畫 | Education Plans]
│   ├── Education plan *.tex
│   └── tutorial *.tex
│
├── [LaTeX 支援檔 | LaTeX Support Files]
│   ├── tufte-handout.cls
│   ├── tufte-book.cls
│   ├── Drake_preamble.tex
│   ├── booksprint.sty
│   └── reference.bib
│
└── figure/                            # 圖片資源
```

---

## EPA 講義總覽 | EPA Handouts Overview

### 內科部次專科 EPA 清單 | Subspecialty EPA List

| 次專科 | Subspecialty | EPA 編號 | 檔案名稱 | 狀態 |
|--------|--------------|----------|----------|------|
| 心臟科 | Cardiology (CV) | EPA 10, 11 | `EPA CV 10 slide.tex`, `EPA CV 11.tex`, `EPA CV echo.tex` | 完成 |
| 胸腔科 | Pulmonology (Chest) | EPA 10, 14 | `EPA Chest 10.tex`, `EPA Chest 14.tex` | 完成 |
| 腸胃科 | Gastroenterology (GI) | EPA 11 | `EPA GI 11.tex` | 完成 |
| 腎臟科 | Nephrology | EPA 10 | `EPA Nephro 10.tex` | 完成 |
| 感染科 | Infectious Disease (ID) | EPA 10 | `EPA ID 10.tex` | 完成 |
| 內分泌科 | Endocrinology | EPA 10 | `EPA Endocrine 10.tex` | 完成 |
| 風濕免疫科 | Rheumatology | EPA 10 | `EPA Rheuma 10.tex` | 完成 |
| 血液科 | Hematology | EPA 10 | `EPA Hema 10.tex` | 完成 |
| 腫瘤科 | Oncology | EPA 10 | `EPA Onco 10.tex` | 完成 |
| 神經科 | Neurology | EPA 7, 10 | `EPA Neuro 7 for IM.tex`, `EPA Neuro 10.tex` | 完成 |

### EPA 核心概念 | EPA Core Concepts

**EPA (Entrustable Professional Activities)** = 可信賴專業活動

EPA 是一種以能力為導向的醫學教育評估框架，將傳統「以時間為本」的訓練模式轉變為「以能力為本」的個別化學習路徑。

**Key Features**:
- 可觀察 (Observable)
- 可評估 (Assessable)
- 可信賴 (Entrustable)
- 整合性 (Integrative)

---

## CCC 委員會 | CCC Committee

### Clinical Competency Committee 臨床能力委員會

**章程文件**: `EPA 0 internal medicine CCC.tex`

#### 委員會宗旨 | Mission

因應住院醫師納入勞基法後工時縮減的挑戰，建立以勝任能力為本 (Competency-Based Medical Education, CBME) 的系統性教學評量機制。

#### 評估對象 | Assessment Targets
- 醫學系學生 (Medical Students)
- 畢業後一般醫學訓練醫師 (PGY)
- 住院醫師 R1-R3 (Residents)

#### 六大核心能力 | Six Core Competencies (ACGME)
1. 病患照護 (Patient Care)
2. 醫學知識 (Medical Knowledge)
3. 實務學習與改善 (Practice-based Learning and Improvement)
4. 人際關係與溝通技巧 (Interpersonal and Communication Skills)
5. 專業素養 (Professionalism)
6. 制度下的實務 (Systems-based Practice)

#### 里程碑層級 | Milestone Levels
- **Level 1**: 新手，需直接監督
- **Level 2**: 進階初學者，需間接監督
- **Level 3**: 勝任者，可獨立執行
- **Level 4**: 熟練者，可指導他人
- **Level 5**: 專家，可擔任教學領導

---

## 使用指引 | Usage Guide

### LaTeX 編譯說明 | LaTeX Compilation

本資料夾中的文件使用 XeLaTeX 編譯，需要以下環境：

**必要套件 | Required Packages**:
- `xeCJK` - 中文支援
- `fontspec` - 字型設定
- `tikz` - 圖形繪製
- `tcolorbox` - 文字框
- `beamer` - 簡報製作

**字型需求 | Font Requirements**:
- Noto Serif CJK TC
- Noto Sans CJK TC

**編譯指令 | Compile Command**:
```bash
xelatex filename.tex
```

### 如何修改與更新 | How to Edit

1. 使用任何文字編輯器開啟 `.tex` 檔案
2. 修改內容後存檔
3. 使用 XeLaTeX 重新編譯
4. 檢查 PDF 輸出

---

## 重要日期 | Important Dates

### 2026 年度時程 | 2026 Timeline

| 時間 | 里程碑 | 說明 |
|------|--------|------|
| **2026/03/29** | CCC Workshop | 內科部講師訓練 |
| 2026 Q2 | 試行階段 | 2-3 次專科試行 EPA |
| 2026 Q3 | 擴展階段 | 全面推廣 |
| **2026/10** | 正式實施 | EPA 評核制度上線 |

---

## 相關連結 | Related Links

- [ACGME Milestones](https://www.acgme.org/what-we-do/accreditation/milestones/)
- [醫策會 JCTM](https://www.jct.org.tw/)

---

## 聯絡資訊 | Contact

**負責人 | Contact Person**: 謝慕揚 副主任
**單位 | Department**: 內科部 / 心臟內科
**機構 | Institution**: 新竹台大分院

---

*本文件由 Claude Code 協助建立 | Document created with assistance from Claude Code*
*最後更新 | Last updated: 2026-02-14*
