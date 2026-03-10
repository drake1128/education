# EPA LaTeX → 教學性質 HTML 整合轉換計劃

## 一、現況盤點

### 1.1 LaTeX 檔案清單（共 22 個 .tex 檔）

#### 專科 EPA 教學文件（12 個）

| 檔案名稱 | 科別 | EPA 數量 | 目標對象 |
|----------|------|----------|---------|
| EPA GI 11.tex | 腸胃內科 (Gastroenterology) | 11 | 住院醫師 R1-R3 |
| EPA Chest 10.tex | 胸腔內科 (Pulmonology) | 10 | 住院醫師 R1-R3 |
| EPA Chest 14.tex | 胸腔內科 (Pulmonology) | 14 | 住院醫師 R1-R3 |
| EPA CV 11.tex | 心臟內科 (Cardiology) | 11 | 住院醫師 R1-R3 |
| EPA CV echo.tex | 心臟內科-心超 (Echo) | 專項 | 住院醫師 R1-R3 |
| EPA Neuro 10.tex | 神經科 (Neurology) | 10 | 住院醫師 R1-R3 |
| EPA Neuro 7 for IM.tex | 神經科-內科適用版 | 7 | 內科住院醫師 |
| EPA Endocrine 10.tex | 內分泌科 (Endocrinology) | 10 | 住院醫師 R1-R3 |
| EPA Hema 10.tex | 血液腫瘤科 (Hematology) | 10 | 住院醫師 R1-R3 |
| EPA ID 10.tex | 感染科 (Infectious Diseases) | 10 | 住院醫師 R1-R3 |
| EPA Nephro 10.tex | 腎臟科 (Nephrology) | 10 | 住院醫師 R1-R3 |
| EPA Onco 10.tex | 腫瘤科 (Oncology) | 10 | 住院醫師 R1-R3 |
| EPA Rheuma 10.tex | 風濕免疫科 (Rheumatology) | 10 | 住院醫師 R1-R3 |

#### 簡報版（Beamer Slide，4 個）

| 檔案名稱 | 用途 |
|----------|------|
| EPA CV 10 slide.tex | 心臟內科教學簡報 |
| EPA CV 11 slide.tex | 心臟內科教學簡報（更新版） |
| EPA Chest 10 slide.tex | 胸腔內科教學簡報 |
| EPA Chest 14 slide.tex | 胸腔內科教學簡報（更新版） |

#### 行政框架文件（4 個）

| 檔案名稱 | 用途 |
|----------|------|
| EPA 0 internal medicine CCC.tex | 內科部 CCC 評量委員會章程（1,063 行） |
| EPA 0 internal medicine CCC meeting 01.tex | CCC 會議紀錄範本 |
| EPA 0 internal medicine CCC slide.tex | CCC 制度簡報 |
| EPA 0 slide introduction.tex | EPA 制度總論簡報 |

#### 技能清單（1 個）

| 檔案名稱 | 用途 |
|----------|------|
| EPA Clinical Skills Internal Medicine.tex | 內科臨床技能檢核清單（跨訓練階段） |

### 1.2 已存在的 HTML 檔案（4 個）

| 檔案名稱 | 對象 | 性質 | 配色 |
|----------|------|------|------|
| EPA_見習醫師.html | 見習醫師 (Clerk) | 評估表單 | 紫色漸層 #667eea → #764ba2 |
| EPA_PGY醫師.html | PGY 醫師 | 評估表單 | 綠色漸層 #11998e → #38ef7d |
| EPA_住院醫師.html | 住院醫師 (Resident) | 評估表單 | 粉紅漸層 #f093fb → #f5576c |
| EPA_NP專科護理師.html | 專科護理師 (NP) | 評估表單 | 藍色漸層 #4facfe → #00f2fe |

> **重要發現**：現有 HTML 是「評估表單」（form-based），僅有 EPA 標題 + 信任等級選項 + 評語欄位。LaTeX 文件中的豐富教學內容（描述、核心能力、里程碑）**完全沒有**出現在 HTML 中。

---

## 二、核心挑戰分析

### 2.1 分類維度複雜

目前內容同時涉及**三個分類軸**：

```
軸一：科別（Specialty）
├── 腸胃內科 (GI)
├── 胸腔內科 (Chest)
├── 心臟內科 (CV)
├── 神經科 (Neuro)
├── 內分泌科 (Endo)
├── 血液腫瘤科 (Hema)
├── 感染科 (ID)
├── 腎臟科 (Nephro)
├── 腫瘤科 (Onco)
└── 風濕免疫科 (Rheuma)

軸二：訓練層級（Training Level）
├── 見習醫師 (Clerk / M5-M6)
├── PGY 醫師 (PGY1-PGY2)
├── 住院醫師 (R1-R3)
├── 專科護理師 (NP1-NP3+)
└── 主治醫師 / 教師（評估者角色）

軸三：內容類型（Content Type）
├── 教學內容（描述 + 核心能力 + 里程碑）
├── 評估表單（信任等級評分）
├── 行政框架（CCC 制度、會議紀錄）
└── 技能清單（程序性技能檢核）
```

### 2.2 內容量龐大

- 10 個科別 × 平均 10 個 EPA × 每個 EPA 約 5 個核心能力 + 5 個里程碑等級 = **~1,000 個知識單元**
- 每個 LaTeX 檔約 400-700 行，全部內容約 **6,000+ 行的結構化教學內容**

### 2.3 現有 HTML 與 LaTeX 脫節

- HTML 只做「評估工具」，缺乏教學引導內容
- LaTeX 有完整的里程碑描述，但沒有互動性
- 兩者之間沒有資料共享機制

---

## 三、分類架構建議

### 3.1 建議的二維導航架構

**主軸：依訓練層級分流**（因為不同層級的使用者進入系統後，只需要看自己的內容）

```
首頁入口（Portal）
│
├── 🟣 見習醫師 (Clerk) 專區
│   └── 通用臨床技能 EPA（跨科共用）
│
├── 🟢 PGY 醫師專區
│   └── 通用核心 EPA（跨科共用）
│
├── 🔴 住院醫師 (Resident) 專區 ← 主力內容
│   ├── 📂 腸胃內科 (11 EPAs)
│   ├── 📂 胸腔內科 (14 EPAs)
│   ├── 📂 心臟內科 (11 EPAs + Echo)
│   ├── 📂 神經科 (10 EPAs)
│   ├── 📂 內分泌科 (10 EPAs)
│   ├── 📂 血液腫瘤科 (10 EPAs)
│   ├── 📂 感染科 (10 EPAs)
│   ├── 📂 腎臟科 (10 EPAs)
│   ├── 📂 腫瘤科 (10 EPAs)
│   └── 📂 風濕免疫科 (10 EPAs)
│
├── 🔵 專科護理師 (NP) 專區
│   └── NP 核心 EPA（跨科共用 + 專科特化）
│
└── ⚙️ 教師 / CCC 委員專區
    ├── CCC 制度說明
    ├── 評量工具使用指引
    └── 會議範本
```

### 3.2 為什麼用「訓練層級」當主軸？

1. **使用者明確**：每個人很清楚自己是哪個層級，不會搞混
2. **科別是次級篩選**：住院醫師輪訓時才需選科，見習/PGY/NP 用通用版
3. **內容複雜度分層**：見習醫師看基礎版，住院醫師才看專科深入版
4. **權限控制友善**：未來若需差異化存取，以層級為單位最自然

---

## 四、HTML 教學頁面設計方案

### 4.1 每個 EPA 的教學 HTML 頁面結構

```
┌──────────────────────────────────────────────────┐
│ Header: 科別名稱 + EPA 編號 + 標題              │
│ 配色: 沿用 LaTeX 各科主題色                      │
├──────────────────────────────────────────────────┤
│ 📖 EPA 描述                                      │
│   完整敘述這個 EPA 的定義與範疇                   │
├──────────────────────────────────────────────────┤
│ 🎯 核心能力要素（可展開/收合）                    │
│   ├── 能力 1: 說明                               │
│   ├── 能力 2: 說明                               │
│   ├── 能力 3: 說明                               │
│   └── ...                                        │
├──────────────────────────────────────────────────┤
│ 📊 里程碑進度（互動式進度條/階梯圖）              │
│   Level 1 [Novice]     ████░░░░░░ 描述...        │
│   Level 2 [Adv Begin]  ██████░░░░ 描述...        │
│   Level 3 [Competent]  ████████░░ 描述...        │
│   Level 4 [Proficient] █████████░ 描述...        │
│   Level 5 [Expert]     ██████████ 描述...        │
├──────────────────────────────────────────────────┤
│ 📝 自我評估區                                    │
│   「我目前在哪個等級？」互動選擇                   │
│   + 觀察評語文字輸入                              │
├──────────────────────────────────────────────────┤
│ 📚 建議學習資源（連結）                           │
│ ← 上一個 EPA    回到科別總覽    下一個 EPA →      │
└──────────────────────────────────────────────────┘
```

### 4.2 科別配色方案（延續 LaTeX 主題色）

| 科別 | 主色 | 輔色 | CSS 變數名稱 |
|------|------|------|-------------|
| 腸胃內科 | #228B22 (gi_green) | #1E90FF (gi_blue) | --gi-primary / --gi-accent |
| 胸腔內科 | #BA181B (chest_red) | #0072BC (chest_blue) | --chest-primary / --chest-accent |
| 心臟內科 | #BA181B (cv_red) | #0072BC (cv_blue) | --cv-primary / --cv-accent |
| 神經科 | #2E5090 (neuro_blue) | #C0C0C0 (neuro_silver) | --neuro-primary / --neuro-accent |
| 內分泌科 | #1565C0 (endo_blue) | #00897B (endo_teal) | --endo-primary / --endo-accent |
| 血液腫瘤科 | 各科自定 | - | --hema-primary / --hema-accent |
| 感染科 | 各科自定 | - | --id-primary / --id-accent |
| 腎臟科 | 各科自定 | - | --nephro-primary / --nephro-accent |
| 腫瘤科 | 各科自定 | - | --onco-primary / --onco-accent |
| 風濕免疫科 | 各科自定 | - | --rheuma-primary / --rheuma-accent |

### 4.3 技術架構選擇

#### 方案 A：純靜態 HTML（建議優先）

```
/epa-html/
├── index.html                      ← 入口首頁（選層級）
├── css/
│   ├── common.css                  ← 共用樣式
│   └── themes/
│       ├── gi.css                  ← 腸胃內科主題色
│       ├── cv.css                  ← 心臟內科主題色
│       └── ...
├── js/
│   ├── navigation.js               ← 導航/篩選邏輯
│   ├── assessment.js               ← 自我評估互動
│   └── export.js                   ← 匯出 PDF/列印
├── data/
│   ├── epa-gi.json                 ← GI 的 11 個 EPA 結構化資料
│   ├── epa-cv.json                 ← CV 的 11 個 EPA 結構化資料
│   └── ...                         ← 每科一個 JSON
├── clerk/                          ← 見習醫師
│   └── index.html
├── pgy/                            ← PGY 醫師
│   └── index.html
├── resident/                       ← 住院醫師
│   ├── index.html                  ← 科別選擇
│   ├── gi/
│   │   ├── index.html              ← GI EPA 總覽
│   │   ├── epa-01.html             ← 各 EPA 教學頁
│   │   ├── epa-02.html
│   │   └── ...
│   ├── cv/
│   ├── chest/
│   └── ...
├── np/                             ← 專科護理師
│   └── index.html
└── admin/                          ← CCC/教師
    └── index.html
```

**優點**：
- 零後端依賴，GitHub Pages 即可部署
- 每個頁面可獨立離線使用（教學現場友善）
- LaTeX 到 JSON 的轉換可自動化

#### 方案 B：Single Page Application (SPA)

- 用 React/Vue 做成一個應用，JSON 資料驅動
- 適合將來需要登入、追蹤進度等功能
- 初期較重，但擴展性佳

**建議**：先用方案 A 完成教學內容上線，再視需求升級為方案 B。

---

## 五、轉換工作流程

### Phase 1：資料結構化（LaTeX → JSON）

將每個 LaTeX 的 EPA 內容萃取為結構化 JSON：

```json
{
  "specialty": "GI",
  "specialty_zh": "腸胃內科",
  "specialty_en": "Gastroenterology",
  "target_audience": "住院醫師 R1-R3",
  "version": "1.0",
  "total_epas": 11,
  "theme_colors": {
    "primary": "#228B22",
    "accent": "#1E90FF",
    "gray": "#787878"
  },
  "epas": [
    {
      "number": 1,
      "title_zh": "消化系統病史詢問與風險評估",
      "title_en": "GI History Taking and Risk Assessment",
      "description": "能夠獨立進行消化系統疾病相關的完整病史詢問...",
      "core_competencies": [
        {
          "name": "症狀評估",
          "detail": "腹痛、噁心嘔吐、腹瀉便秘、吞嚥困難的詳細詢問"
        }
      ],
      "milestones": {
        "level_1": { "label": "Novice", "description": "能詢問基本消化系統症狀..." },
        "level_2": { "label": "Advanced Beginner", "description": "能系統性完成..." },
        "level_3": { "label": "Competent", "description": "能獨立完成複雜..." },
        "level_4": { "label": "Proficient", "description": "能在困難情況下..." },
        "level_5": { "label": "Expert", "description": "能指導他人..." }
      },
      "assessment_tools": ["Mini-CEX", "CbD"]
    }
  ]
}
```

### Phase 2：HTML 模板建構

1. 建立共用 CSS 框架（響應式設計）
2. 建立科別主題色 CSS 變數系統
3. 建立 EPA 教學頁面模板
4. 建立科別總覽頁面模板
5. 建立入口首頁（層級選擇器）

### Phase 3：內容填充

- 將 10 個科別的 JSON 資料注入模板
- 逐科檢核內容正確性
- 整合現有 4 個 HTML 評估表單的元素

### Phase 4：增值功能

- 里程碑互動視覺化（進度條/階梯圖）
- 自我評估功能（localStorage 暫存）
- 匯出為 PDF / 列印友善版本
- 跨科 EPA 比對搜尋

---

## 六、處理特殊案例

### 6.1 胸腔內科有兩個版本（10 vs 14 EPAs）

**建議**：以 14 EPAs 為主版本（較完整），10 EPAs 版標記為「精簡版」，兩者並存。

### 6.2 神經科有完整版與內科適用版（10 vs 7 EPAs）

**建議**：
- 完整版 (10 EPAs) → 放在「住院醫師/神經科」路徑
- 內科適用版 (7 EPAs) → 放在「住院醫師/神經科」下的獨立子頁面，標示為「內科住院醫師輪訓適用」

### 6.3 心臟內科有 Echo 專項 EPA

**建議**：以獨立子頁面呈現，在心臟內科總覽中加入「進階：心臟超音波 EPA」入口。

### 6.4 見習醫師/PGY/NP 的 EPA 來源

目前 LaTeX 僅針對住院醫師。見習醫師/PGY/NP 的 EPA 內容來自現有 HTML。

**建議**：
- 先保留現有 HTML 的 EPA 條目
- 未來補充 LaTeX 級的教學內容（描述 + 里程碑）
- 統一格式後整合進新系統

---

## 七、產出物清單

完成此計劃後，預期產出：

| # | 產出物 | 數量 | 說明 |
|---|--------|------|------|
| 1 | 入口首頁 | 1 | 層級選擇 Portal |
| 2 | 層級首頁 | 5 | 見習/PGY/住院/NP/教師 |
| 3 | 科別總覽頁 | 10 | 每個次專科一頁 |
| 4 | EPA 教學頁 | ~110 | 每個 EPA 獨立頁面 |
| 5 | 結構化 JSON | 10 | 每科一個資料檔 |
| 6 | 共用 CSS | 1+10 | 1 通用 + 10 科別主題 |
| 7 | 互動 JS | 3-4 | 導航/評估/匯出/搜尋 |

**總計約 140 個檔案**

---

## 八、建議執行順序

```
Step 1 → 選一個科別做 Pilot（建議 GI 腸胃內科，有 11 個 EPA 且結構最清楚）
         ├── 萃取 JSON
         ├── 建立 HTML 模板
         └── 完成該科 11 頁 + 總覽頁

Step 2 → 確認模板與互動設計滿意後，批次轉換其餘 9 科

Step 3 → 建立入口首頁與各層級首頁

Step 4 → 整合現有 4 個 HTML 評估表

Step 5 → 加入增值互動功能

Step 6 → 整體測試與部署
```

---

## 九、待確認事項（需您決定）

1. **是否需要登入系統？** → 影響選用方案 A 或 B
2. **是否需要儲存評估結果到後端？** → 目前 HTML 表單資料不會被保存
3. **Beamer 簡報版是否也要轉 HTML？** → 可用 reveal.js 或直接轉 PDF
4. **CCC 行政文件是否需要教學 HTML 化？** → 或維持 PDF 即可
5. **胸腔內科以 10 還是 14 EPAs 為主？** → 建議 14
6. **是否有額外科別（例如外科、急診）的 EPA 需要未來擴充？** → 影響模板設計的通用性
