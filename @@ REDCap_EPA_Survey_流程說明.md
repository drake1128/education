# REDCap EPA Survey 發送流程

> 適用情境：多位評核醫師 × 多位被評核專科護理師（多對多）  
> 專案：EPA 評核系統（含各內科次專科）  
> 最後更新：2026-03-09

---

## 前置確認

- [ ] REDCap 專案已啟用 **Use surveys in this project?**
- [ ] Data Dictionary（`EPA_DataDictionary_v2_2026-03-09.csv`）已匯入
- [ ] 各次專科 instrument 已在 **Designer → Enable** 開啟 Survey 功能
- [ ] Survey Settings 各 form 設為 **By Invitation Only**

---

## Step 1｜取得評核配對名單

向助理索取 Excel 或 CSV，需包含以下欄位：

| 欄位 | 說明 | 範例 |
|------|------|------|
| `assessor_name` | 評核醫師姓名 | 王大明 |
| `assessor_email` | 評核醫師 email | wang@ntuh.gov.tw |
| `assessor_title` | 職稱代碼 | `1`＝主治醫師、`2`＝總醫師、`3`＝其他 |
| `evaluated_name` | 被評核護理師姓名 | 李小芬 |
| `evaluated_id` | 護理師員工編號 | N001234 |
| `form_name` | 要填的次專科 form | `cv_epa`、`chest_epa` … |

> **重要**：一位醫師評 N 位護理師 → 該醫師的 email 出現 N 次，對應不同護理師。

---

## Step 2｜轉換成 REDCap Import CSV

將配對名單轉成每列一筆 record 的格式：

| record_id | {prefix}_assessor_name | {prefix}_assessor_email | {prefix}_evaluated_name | {prefix}_evaluated_id | {prefix}_evaluated_type |
|-----------|------------------------|------------------------|-------------------------|-----------------------|------------------------|
| 001 | 王大明 | wang@ntuh.gov.tw | 李小芬 | N001234 | 4 |
| 002 | 王大明 | wang@ntuh.gov.tw | 陳美玲 | N005678 | 4 |
| 003 | 張志偉 | chang@ntuh.gov.tw | 李小芬 | N001234 | 4 |

> `{prefix}` 依次專科替換，例如心臟內科為 `cv`、胸腔內科為 `chest`。  
> `evaluated_type` 代碼：`1`＝醫學生、`2`＝PGY、`3`＝住院醫師、`4`＝專科護理師  
> **可將配對名單傳給 Claude，自動產出此格式。**

---

## Step 3｜匯入 Records 至 REDCap

1. 左側選單 → **Data Import Tool**
2. 上傳 Step 2 產出的 CSV
3. 選擇 **Import Action: Insert new records**
4. 確認預覽無誤 → **Import Data**
5. 至 **Record Status Dashboard** 確認所有 record 已建立

---

## Step 4｜設定各 Form 為 Survey

針對每個次專科 form（`chest_epa`、`cv_epa`、`gi_epa` …）：

1. **Designer** → 找到該 instrument → 點 **Enable**（Survey 欄）
2. 進入 **Survey Settings**：
   - Survey Title：例如「心臟內科 EPA 評核問卷」
   - **Survey Access**：`By Invitation Only`
   - Survey Expiration：視需求設定截止日
3. **Save Survey Settings**

---

## Step 5｜設定 Participant List 並批次寄送

1. 左側 → **Survey Distribution Tools → Participant List**
2. 選擇要發送的 instrument（次專科 form）
3. 點 **Add participants from existing records**
   - REDCap 自動抓取該 record 對應的 `{prefix}_assessor_email`
4. 選取全部 participants → **Compose Invitations**
5. 設定信件內容（可使用範本，見下方）
6. 設定寄送時間：立即 or 排程
7. **Send Invitations**

### 信件範本

```
主旨：【EPA 評核問卷】請填寫您負責評核的護理師問卷

王醫師 您好，

請您針對 [evaluated_name]（員工編號：[evaluated_id]）
填寫本次 EPA 評核問卷：

[survey-url]

若有任何問題請聯繫教學部。感謝您的協助。

臺大新竹分院 教學部
```

> `[survey-url]` 為 REDCap 自動帶入的個人化連結，每封不同。

---

## Step 6｜設定自動提醒（Reminder）

1. **Survey Distribution Tools → Reminders**
2. 建議設定：
   - 第一次提醒：寄出後 **3 天**（未完成者）
   - 第二次提醒：截止前 **2 天**
3. 可自訂提醒信件內容

---

## Step 7｜追蹤回覆狀況

### Participant List 狀態說明

| 狀態 | 說明 |
|------|------|
| `Not yet sent` | 尚未寄出邀請 |
| `Invited` | 已寄出，尚未填寫 |
| `Reminder sent` | 已寄出提醒 |
| `Completed` | 已完成填寫 |

### 查看整體完成率

- **Record Status Dashboard** → 各 form 完成狀況一覽

---

## Step 8｜匯出資料分析

1. 左側 → **Data Exports, Reports, and Stats**
2. 選擇格式：Excel / CSV / SPSS / R / STATA
3. 建議依 `{prefix}_evaluated_name` 分組，計算各護理師的 EPA 平均等級
4. 可在 **Reports** 先建立篩選條件，例如：
   - 僅匯出已完成的 records
   - 依次專科分別匯出

---

## 快速參照：次專科 Form 對照表

| 次專科 | Form Name | Email 欄位 |
|--------|-----------|------------|
| 胸腔內科 | `chest_epa` | `chest_assessor_email` |
| 心臟內科 | `cv_epa` | `cv_assessor_email` |
| 腸胃內科 | `gi_epa` | `gi_assessor_email` |
| 腎臟內科 | `nephro_epa` | `nephro_assessor_email` |
| 內分泌科 | `endocrine_epa` | `endocrine_assessor_email` |
| 血液科 | `hema_epa` | `hema_assessor_email` |
| 感染科 | `id_epa` | `id_assessor_email` |
| 腫瘤科 | `onco_epa` | `onco_assessor_email` |
| 風濕免疫科 | `rheuma_epa` | `rheuma_assessor_email` |
| 神經科 | `neuro_epa` | `neuro_assessor_email` |

---

## 注意事項

- **一筆 record = 一個「評核醫師 × 被評核護理師」配對**，不可混用
- Record ID 為系統自動產生，不需手動填寫
- 若評核醫師跨多個次專科，各次專科需分別建立 record 並發送不同 form
- Survey 連結為一次性個人連結，請勿轉發
- 匯入前請先備份原始配對名單 Excel，以便日後對帳
