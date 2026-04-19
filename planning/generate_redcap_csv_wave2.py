# -*- coding: utf-8 -*-
"""
Wave 2 REDCap import generator — 2026-04-18 (v2: all VS in spec evaluate each PGY)
- Add 呂菁 as 2nd evaluator for 王心妍 + 陳逵蓉 (endocrine_epa)
  (邱玉婷 already assigned to 呂菁 in Wave 1 — skipped to avoid duplicate)
- Add 7 PGY, each rotating 3 subspecialties
- For each PGY-rotation: EVERY VS in that specialty evaluates the PGY
- Blood/tumor rotations expand to hema_epa + onco_epa per VS (2 rows each)
- 5-7月 PGY (李宗翰, 吳定衡) records included; all surveys sent together

Record IDs start at 102 (wave 1 used 1-101).
"""
import sys, io, csv
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

form_names = {
    'cv': 'cv_epa', 'chest': 'chest_epa', 'gi': 'gi_epa',
    'endocrine': 'endocrine_epa', 'nephro': 'nephro_epa',
    'hema': 'hema_epa', 'onco': 'onco_epa', 'id': 'id_epa',
}
dept_labels = {
    'cv': '心臟內科', 'chest': '胸腔內科', 'gi': '腸胃內科', 'endocrine': '內分泌科',
    'nephro': '腎臟內科', 'hema': '血液科', 'onco': '腫瘤科', 'id': '感染科',
}

vs_by_spec = {
    'chest':  ['吳常瑋', '林振傑', '耿立達', '張建仁', '陳詩宇', '楊漢清', '溫岳峯', '鄒秉誠'],
    'gi':     ['林宣合', '胡文皓', '孫宜禎', '高健能', '郭怡男', '蔡明宏', '魏平雅', '陳聲旺'],
    'nephro': ['陳長江', '楊忠煒', '楊為舜', '趙政漢'],
    'hema':   ['吳尚儒', '呂欣瑜', '呂亭緯', '陳成曄'],
    'id':     ['郭漢岳', '邊建榮'],
}

vs_emails = {
    '呂菁': 'luching@hotmail.com.tw',
    '吳常瑋': 'sinceadidas@hotmail.com', '林振傑': 'B97401095@ntu.edu.tw',
    '耿立達': 'ltkeng@gmail.com', '張建仁': 'cjchangone@yahoo.com.tw',
    '陳詩宇': 'seakmax11078@hotmail.com', '楊漢清': 'yang760701@yahoo.com.tw',
    '溫岳峯': 'freeman0509@gmail.com', '鄒秉誠': 'anskyluker@gmail.com',
    '林宣合': 'tostart21@gmail.com', '胡文皓': 'wenhaohu120@gmail.com',
    '孫宜禎': 'clotilde.s@yahoo.com.tw', '高健能': 'neil855011@msn.com',
    '郭怡男': 'kuo5412@ms9.hinet.net', '蔡明宏': 'ybpptats@gmail.com',
    '魏平雅': 'pywei0526@gmail.com', '陳聲旺': 'tansiawang@gmail.com',
    '陳長江': 'cck85515@yahoo.com.tw', '楊忠煒': 'yang.chung.wei@gmail.com',
    '楊為舜': 'weishun.yang@gmail.com', '趙政漢': 'alex938235@gmail.com',
    '吳尚儒': 'wushangju@gmail.com', '呂欣瑜': 'sgps70632@gmail.com',
    '呂亭緯': 'twlyu29@gmail.com', '陳成曄': 'sammychen95@gmail.com',
    '郭漢岳': 'hykuo1289@gmail.com', '邊建榮': 'aries0713@yahoo.com.tw',
}

# ---- Wave 2 NP additions (呂菁 as 2nd evaluator) ----
np_assignments = [
    # (spec, vs_name, np_name, np_email)
    ('endocrine', '呂菁', '王心妍', 'lukesimoningrid@yahoo.com.tw'),
    ('endocrine', '呂菁', '陳逵蓉', 'kuei142@yahoo.com.tw'),
]

# ---- PGY rotations (each gets evaluated by ALL VS in each rotation spec) ----
# (pgy_name, pgy_email, [spec1, spec2, spec3])
pgy_rotations = [
    ('王閎毅', 'allan.wang880@gmail.com', ['hema', 'id', 'gi']),
    ('藍子宸', '456281379s@gmail.com',    ['gi', 'hema', 'chest']),
    ('陳擎',   'chingchen87@gmail.com',   ['chest', 'nephro', 'hema']),
    ('陳昱安', 'a0912023690@gmail.com',   ['id', 'gi', 'nephro']),
    ('李治蘊', 'jiueng50919@gmail.com',   ['nephro', 'chest', 'id']),
    ('李宗翰', 'kevin07009@gmail.com',    ['nephro', 'gi', 'chest']),   # 115年5-7月
    ('吳定衡', '900222timmy@gmail.com',   ['chest', 'nephro', 'gi']),   # 115年5-7月
]

# ---- CSV Generation ----
all_fields = ['eval_date', 'assessor_name', 'assessor_email', 'assessor_title',
              'evaluated_id', 'evaluated_name', 'evaluated_type',
              'trainee_type', 'trainee_name', 'dept']
prefix_order = ['cv', 'chest', 'gi', 'endocrine', 'nephro', 'hema', 'onco', 'id']

header = ['record_id', 'redcap_repeat_instrument', 'redcap_repeat_instance']
for pfx in prefix_order:
    for f in all_fields:
        header.append(f"{pfx}_{f}")

csv_rows = []
record_id = 102  # Wave 1 used 1-101

# --- NP rows (呂菁) ---
for spec, vs_name, np_name, np_email in np_assignments:
    row = {
        'record_id': str(record_id),
        'redcap_repeat_instrument': form_names[spec],
        'redcap_repeat_instance': '1',
        f'{spec}_assessor_name': vs_name,
        f'{spec}_assessor_email': vs_emails[vs_name],
        f'{spec}_assessor_title': '1',
        f'{spec}_evaluated_name': np_name,
        f'{spec}_evaluated_id': '',
        f'{spec}_evaluated_type': '4',  # 4 = 專科護理師
        f'{spec}_trainee_type': '4',
        f'{spec}_trainee_name': np_name,
        f'{spec}_dept': dept_labels[spec],
        f'{spec}_eval_date': '',
    }
    csv_rows.append(row)
    record_id += 1

# --- PGY rows: every VS in each rotation spec evaluates the PGY ---
for pgy_name, pgy_email, specs in pgy_rotations:
    for spec in specs:
        for vs_name in vs_by_spec[spec]:
            # Blood/tumor expands to 2 forms per VS
            forms = ['hema', 'onco'] if spec == 'hema' else [spec]
            for form in forms:
                row = {
                    'record_id': str(record_id),
                    'redcap_repeat_instrument': form_names[form],
                    'redcap_repeat_instance': '1',
                    f'{form}_assessor_name': vs_name,
                    f'{form}_assessor_email': vs_emails[vs_name],
                    f'{form}_assessor_title': '1',
                    f'{form}_evaluated_name': pgy_name,
                    f'{form}_evaluated_id': '',
                    f'{form}_evaluated_type': '2',  # 2 = PGY
                    f'{form}_trainee_type': '2',
                    f'{form}_trainee_name': pgy_name,
                    f'{form}_dept': dept_labels[form],
                    f'{form}_eval_date': '',
                }
                csv_rows.append(row)
            record_id += 1  # one record_id per (PGY × spec × VS), hema double-rows share id

output_path = 'G:/我的雲端硬碟/004 教學資料 at Hsinchu 院內/Teaching materials CV education web at github/IM CCC EPA/planning/REDCap_Import_EPA_Wave2_2026-04-18.csv'
with open(output_path, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, fieldnames=header, restval='')
    writer.writeheader()
    writer.writerows(csv_rows)

# ---- Summary ----
spec_labels_zh = {'chest':'胸腔內科','gi':'腸胃內科','nephro':'腎臟內科','hema':'血液腫瘤科','id':'感染科'}
print("=== Wave 2 REDCap Import — 2026-04-18 (v2: all VS) ===\n")
print(f"NP additions (呂菁 as 2nd evaluator): {len(np_assignments)}")
for spec, vs, np, _ in np_assignments:
    print(f"  {np} ← {vs} ({spec}_epa)")

print(f"\nPGY: {len(pgy_rotations)} residents")
for pgy_name, pgy_email, specs in pgy_rotations:
    print(f"  {pgy_name} ({pgy_email}):")
    for spec in specs:
        n_vs = len(vs_by_spec[spec])
        ext = f" × 2 forms (hema+onco) = {n_vs * 2} rows" if spec == 'hema' else f" = {n_vs} rows"
        print(f"    - {spec_labels_zh[spec]}: {n_vs} VS ({', '.join(vs_by_spec[spec])}){ext}")

# VS load
vs_load = {}
for row in csv_rows:
    for pfx in ['cv', 'chest', 'gi', 'endocrine', 'nephro', 'hema', 'onco', 'id']:
        name = row.get(f'{pfx}_assessor_name')
        if name:
            vs_load[name] = vs_load.get(name, 0) + 1
            break
print(f"\n--- VS survey count this wave ---")
for v, n in sorted(vs_load.items(), key=lambda x: -x[1]):
    print(f"  {v}: {n}")

print(f"\nTotal record_ids: {record_id - 102} (102 ~ {record_id - 1})")
print(f"Total CSV rows: {len(csv_rows)}")
print(f"\nOutput: {output_path}")
