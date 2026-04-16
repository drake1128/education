"""
EPA 第 1 週 Pilot 分析
======================
資料來源: planning/EPA_DATA_LABELS_2026-04-11_1344.csv
匯出時間: 2026-04-11 13:44

清理規則 (依 2026-04-09 與謝慕揚副主任討論):
  1. 心臟科 VS「呂欣瑜」不存在 -> 從媒合表移除 (本檔不影響, 因無資料)
  2. 風濕免疫 6 位 VS 改列第二批, Pilot 不分析 rheuma_epa
  3. 胸腔科 4 筆 2025 年舊測試資料 (學員類別非「專科護理師」) 全部排除
  4. 神經內科 neuro_epa 尚未啟動, 不分析

Pilot 分析對象 (VS 100% 回收的 4 科):
  - 腸胃內科 gi_epa     (8 VS, 2 NP, 16 評核)
  - 內分泌科 endocrine  (4 VS, 4 NP, 12 評核)
  - 腎臟內科 nephro     (4 VS, 3 NP, 12 評核)
  - 感染科   id_epa     (2 VS, 4 NP,  4 評核)
"""

import re
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# --- 中文字型 (Windows) ---
mpl.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'Microsoft YaHei', 'SimHei']
mpl.rcParams['axes.unicode_minus'] = False

BASE = Path(r"G:\我的雲端硬碟\004 教學資料 at Hsinchu 院內\Teaching materials CV education web at github\IM CCC EPA\planning")
CSV  = BASE / "EPA_DATA_LABELS_2026-04-14_1208.csv"
DATE_TAG = "2026-04-14"
OUT  = BASE / "analysis"
OUT.mkdir(exist_ok=True)

# ---------------------------------------------------------------
# 1. 讀檔 (寬表: 每個 instrument 各有一組 EPA 欄位, pandas 會自動加 .1 .2 ...)
# ---------------------------------------------------------------
df = pd.read_csv(CSV, dtype=str, keep_default_na=False)
df = df.replace("", np.nan)

INSTRUMENTS = {
    "Chest Epa":     "胸腔內科",
    "Cv Epa":        "心臟內科",
    "Gi Epa":        "腸胃內科",
    "Nephro Epa":    "腎臟內科",
    "Endocrine Epa": "內分泌科",
    "Hema Epa":      "血液科",
    "Id Epa":        "感染科",
    "Onco Epa":      "腫瘤科",
    "Rheuma Epa":    "風濕免疫",
    "Neuro Epa":     "神經內科",
}

# 對每個 instrument, 找出它對應的欄位區段 (header 重複出現的那一段)
def cols_for(prefix):
    """回傳該 instrument 的欄位 dict (重複欄位 pandas 加 .1 .2 ...)"""
    # 所有評核欄位重複 10 次, 順序: chest, cv, gi, nephro, endocrine, hema, id, onco, rheuma, neuro
    return None

INST_ORDER = ["Chest Epa","Cv Epa","Gi Epa","Nephro Epa","Endocrine Epa",
              "Hema Epa","Id Epa","Onco Epa","Rheuma Epa","Neuro Epa"]
SUFFIX = {name: ("" if i == 0 else f".{i}") for i, name in enumerate(INST_ORDER)}
# 每個 instrument 的 EPA 題數 (依 header 順序)
EPA_COUNTS = {"Chest Epa":14,"Cv Epa":11,"Gi Epa":11,"Nephro Epa":10,
              "Endocrine Epa":10,"Hema Epa":10,"Id Epa":10,"Onco Epa":10,
              "Rheuma Epa":10,"Neuro Epa":7}
# 依 header 出現順序切出每個 instrument 的 EPA 欄位
ALL_EPA_COLS = [c for c in df.columns if re.match(r"^EPA \d+:", c)]
INST_EPA_COLS = {}
_idx = 0
for _inst in INST_ORDER:
    n = EPA_COUNTS[_inst]
    INST_EPA_COLS[_inst] = ALL_EPA_COLS[_idx:_idx+n]
    _idx += n
assert _idx == len(ALL_EPA_COLS), f"EPA col count mismatch: {_idx} vs {len(ALL_EPA_COLS)}"

KEY_COLS = ["評核日期","評核教師姓名","被評核學員姓名","被評核學員類別","受評者姓名","評核科別",
            "整體質性評語","優點與具體表現","需改進之處與學習建議","是否建議進入下階段訓練"]

def long_form():
    rows = []
    for inst in INST_ORDER:
        sub = df[df["Repeat Instrument"] == inst].copy()
        if sub.empty:
            continue
        suf = SUFFIX[inst]
        epa_cols = INST_EPA_COLS[inst]
        for _, r in sub.iterrows():
            base = {"instrument": inst, "subspec": INSTRUMENTS[inst],
                    "rid": r["Record ID"], "rinst": r["Repeat Instance"]}
            for k in KEY_COLS:
                col = k + suf
                base[k] = r.get(col)
            for ec in epa_cols:
                epa_name = re.sub(r"^EPA (\d+):\s*", r"EPA\1: ", ec.split(suf)[0] if suf else ec)
                val = r.get(ec)
                rows.append({**base, "epa": epa_name, "level_text": val})
    return pd.DataFrame(rows)

L = long_form()

# 解析 Level 數字
def parse_level(s):
    if pd.isna(s): return np.nan
    m = re.search(r"Level\s*(\d)", str(s))
    return int(m.group(1)) if m else np.nan

L["level"] = L["level_text"].apply(parse_level)

# 區分 stub vs 已填寫: 一筆 (rid, instrument, rinst) 至少有一個 Level 才算 completed
has_level = (L.dropna(subset=["level"])
               .groupby(["rid","instrument","rinst"]).size()
               .reset_index(name="n_levels"))
L = L.merge(has_level, on=["rid","instrument","rinst"], how="left")
L["is_completed"] = L["n_levels"].notna()

# ---------------------------------------------------------------
# 2. 套用清理規則
# ---------------------------------------------------------------
before = len(L)
# (a) 胸腔科只保留 NP
mask_chest_test = (L["instrument"] == "Chest Epa") & (L["被評核學員類別"] != "專科護理師")
L = L[~mask_chest_test].copy()
removed_chest = before - len(L)

# (b) 排除尚未啟動的科
L = L[~L["instrument"].isin(["Rheuma Epa","Neuro Epa"])].copy()

# (c) 心臟科呂欣瑜不存在 -> 資料中本來就沒有, 這裡只是 sanity check
assert (L[(L["instrument"]=="Cv Epa") & (L["評核教師姓名"]=="呂欣瑜")].empty)

print(f"[清理] 移除胸腔科舊測試 EPA 列數: {removed_chest}")
print(f"[清理] 清理後總 EPA 評分列數: {len(L)}")
print(f"[清理] 評核件數 (record-level): {L.groupby(['instrument','rid','rinst']).ngroups}")

# 存出長表, 後續可在 R/Excel 內再用
L.to_csv(OUT / f"epa_long_clean_{DATE_TAG}.csv", index=False, encoding="utf-8-sig")

# ---------------------------------------------------------------
# 3. 各科回收摘要 (區分 stub 與真正完成)
# ---------------------------------------------------------------
def n_unique_records(g):
    return g[["rid","rinst"]].drop_duplicates().shape[0]

rows = []
for (inst, sub), g in L.groupby(["instrument","subspec"]):
    g_done = g[g["is_completed"]]
    rows.append({
        "instrument": inst, "subspec": sub,
        "n_records_total": n_unique_records(g),
        "n_records_completed": n_unique_records(g_done),
        "n_vs_total": g["評核教師姓名"].nunique(),
        "n_vs_completed": g_done["評核教師姓名"].nunique(),
        "n_np": g_done["被評核學員姓名"].nunique(),
        "level_mean": round(g_done["level"].mean(), 2) if not g_done.empty else np.nan,
        "level_median": g_done["level"].median() if not g_done.empty else np.nan,
    })
recs = pd.DataFrame(rows).sort_values("n_records_completed", ascending=False)
recs["level_mean"] = recs["level_mean"].round(2)
recs.to_csv(OUT / f"summary_by_subspec_{DATE_TAG}.csv", index=False, encoding="utf-8-sig")
print("\n=== 各科回收摘要 ===")
print(recs.to_string(index=False))

# ---------------------------------------------------------------
# 4. Pilot 分析: 有實際完成資料的 5 科
# ---------------------------------------------------------------
PILOT = ["Cv Epa","Gi Epa","Nephro Epa","Id Epa","Chest Epa"]   # 2026-04-11 胸腔科加入
P = L[L["instrument"].isin(PILOT) & L["is_completed"]].copy()

# 2x3 格 (留 1 格空白)
def _pilot_axes():
    fig, axes = plt.subplots(2, 3, figsize=(15, 9))
    used = list(axes.flat)[:len(PILOT)]
    for ax in list(axes.flat)[len(PILOT):]:
        ax.axis("off")
    return fig, used

# (a) Level 分布長條圖
fig, used = _pilot_axes()
for ax, inst in zip(used, PILOT):
    sub = P[P["instrument"] == inst]
    counts = sub["level"].value_counts().reindex([1,2,3,4,5], fill_value=0)
    bars = ax.bar(counts.index.astype(str), counts.values,
                  color=["#d73027","#fc8d59","#fee08b","#91cf60","#1a9850"])
    ax.set_title(f"{INSTRUMENTS[inst]} ({inst})  n={int(counts.sum())}")
    ax.set_xlabel("信賴等級 (Level)")
    ax.set_ylabel("評分次數")
    for b in bars:
        h = b.get_height()
        if h > 0:
            ax.text(b.get_x()+b.get_width()/2, h, str(int(h)),
                    ha="center", va="bottom", fontsize=9)
fig.suptitle(f"EPA Pilot — {len(PILOT)} 科信賴等級分布 ({DATE_TAG})", fontsize=14, fontweight="bold")
fig.tight_layout()
fig.savefig(OUT / "fig1_level_distribution.png", dpi=160, bbox_inches="tight")
plt.close(fig)

# (b) 每位 NP 的平均 Level (橫條圖)
fig, used = _pilot_axes()
for ax, inst in zip(used, PILOT):
    sub = P[P["instrument"] == inst]
    np_mean = (sub.groupby("被評核學員姓名")["level"]
                  .mean().sort_values())
    ax.barh(np_mean.index, np_mean.values, color="#4575b4")
    ax.set_xlim(0, 5)
    ax.axvline(3, color="grey", ls="--", lw=0.8)
    ax.set_title(f"{INSTRUMENTS[inst]}")
    ax.set_xlabel("平均信賴等級")
    for i,(name,v) in enumerate(np_mean.items()):
        ax.text(v+0.05, i, f"{v:.2f}", va="center", fontsize=9)
fig.suptitle(f"EPA Pilot — 各 NP 平均信賴等級 ({DATE_TAG})", fontsize=14, fontweight="bold")
fig.tight_layout()
fig.savefig(OUT / "fig2_np_mean_level.png", dpi=160, bbox_inches="tight")
plt.close(fig)

# (c) 是否建議進入下階段訓練 — 統計
adv = (P.groupby(["instrument","是否建議進入下階段訓練"])
         .size().unstack(fill_value=0))
adv.to_csv(OUT / "advance_recommendation.csv", encoding="utf-8-sig")
print(f"\n=== 是否建議進入下階段 (Pilot {len(PILOT)} 科) ===")
print(adv)

# (d) 每科 EPA 題目層級的平均 (heatmap-like 表)
for inst in PILOT:
    sub = P[P["instrument"] == inst]
    pv = (sub.groupby(["epa","被評核學員姓名"])["level"]
            .mean().unstack())
    pv.to_csv(OUT / f"epa_x_np_{inst.replace(' ','_').lower()}.csv",
              encoding="utf-8-sig")

print(f"\n所有輸出已寫入: {OUT}")
