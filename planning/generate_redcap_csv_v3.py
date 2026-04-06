# -*- coding: utf-8 -*-
"""
v3: 呂欣瑜 moved from 心臟內科 to 血液腫瘤科 (now 4 VS in hema)
"""
import sys, io, csv
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

form_names = {
    'cv': 'cv_epa', 'chest': 'chest_epa', 'gi': 'gi_epa',
    'endo': 'endocrine_epa', 'nephro': 'nephro_epa',
    'hema': 'hema_epa', 'onco': 'onco_epa', 'id': 'id_epa',
}
form_prefix = {
    'cv': 'cv', 'chest': 'chest', 'gi': 'gi', 'endo': 'endocrine',
    'nephro': 'nephro', 'hema': 'hema', 'onco': 'onco', 'id': 'id',
}
dept_labels = {
    'cv': '心臟內科', 'chest': '胸腔內科', 'gi': '腸胃內科', 'endo': '內分泌科',
    'nephro': '腎臟內科', 'hema': '血液科', 'onco': '腫瘤科', 'id': '感染科',
}
spec_labels = {
    'cv':'心臟內科','chest':'胸腔內科','gi':'腸胃內科','endo':'內分泌科',
    'nephro':'腎臟內科','hema':'血液腫瘤科','id':'感染科'
}

# UPDATED: 呂欣瑜 moved to hema
vs_by_spec = {
    'cv': ['呂忠穎','李志國','洪國軒','張恕桓','許如瑩','楊欽文','潘恆宇','蕭喻中','謝慕揚'],
    'chest': ['吳常瑋','林振傑','耿立達','張建仁','陳詩宇','楊漢清','溫岳峯','鄒秉誠'],
    'gi': ['林宣合','胡文皓','孫宜禎','高健能','郭怡男','蔡明宏','魏平雅','陳聲旺'],
    'endo': ['呂菁','李宜鴻','林以茀','范綱志'],
    'nephro': ['陳長江','楊忠煒','楊為舜','趙政漢'],
    'hema': ['吳尚儒','呂欣瑜','呂亭緯','陳成曄'],  # 4 VS now
    'id': ['郭漢岳','邊建榮'],
}

emails = {
    '呂忠穎':'shadowinlx@gmail.com','呂欣瑜':'sgps70632@gmail.com','李志國':'keitheva2009@gmail.com',
    '洪國軒':'hong113871@gmail.com','張恕桓':'shujames921@gmail.com','許如瑩':'roxannehsu5057@gmail.com',
    '楊欽文':'jgboon0407@gmail.com','潘恆宇':'phy20633@gmail.com','蕭喻中':'addieb7bz@gmail.com',
    '謝慕揚':'drake1128@gmail.com',
    '吳常瑋':'sinceadidas@hotmail.com','林振傑':'B97401095@ntu.edu.tw','耿立達':'ltkeng@gmail.com',
    '張建仁':'cjchangone@yahoo.com.tw','陳詩宇':'seakmax11078@hotmail.com','楊漢清':'yang760701@yahoo.com.tw',
    '溫岳峯':'freeman0509@gmail.com','鄒秉誠':'anskyluker@gmail.com',
    '林宣合':'tostart21@gmail.com','胡文皓':'wenhaohu120@gmail.com','孫宜禎':'clotilde.s@yahoo.com.tw',
    '高健能':'neil855011@msn.com','郭怡男':'kuo5412@ms9.hinet.net','蔡明宏':'ybpptats@gmail.com',
    '魏平雅':'pywei0526@gmail.com','陳聲旺':'tansiawang@gmail.com',
    '呂菁':'luching@hotmail.com.tw','李宜鴻':'b98401022@gmail.com','林以茀':'b98401002@gmail.com',
    '范綱志':'ntuhendocrine@gmail.com',
    '陳長江':'cck85515@yahoo.com.tw','楊忠煒':'yang.chung.wei@gmail.com','楊為舜':'weishun.yang@gmail.com',
    '趙政漢':'alex938235@gmail.com',
    '吳尚儒':'wushangju@gmail.com','呂亭緯':'twlyu29@gmail.com','陳成曄':'sammychen95@gmail.com',
    '郭漢岳':'hykuo1289@gmail.com','邊建榮':'aries0713@yahoo.com.tw',
}

hema_fixed = {'林乃莉','彭琛玉','蘇韻珊'}
hema_mobile_only = {'林文茹','張月梅','陳秀如','羅彩鳳'}

nps_raw = [
    ('丁虹文','sharon3458@gmail.com',['nephro'],False),
    ('孔令潔','kongpaopao@gmail.com',['id'],True),
    ('王心妍','lukesimoningrid@yahoo.com.tw',['chest'],False),
    ('吳惠如','jk5201123@yahoo.com.tw',['chest'],True),
    ('李雅丞','pomy103@hotmail.com',['chest'],True),
    ('林乃莉','yanai246@gmail.com',['hema'],False),
    ('林子甯','zizing@gmail.com',['chest'],True),
    ('林文茹','a90050636@gmail.com',['hema'],True),
    ('林秋蓉','G00511@hch.gov.tw',['chest'],False),
    ('邱玉婷','emily55660@gmail.com',['endo'],False),
    ('洪韻新','a20030617@yahoo.com.tw',['gi','chest'],True),
    ('紀怡如','tang50545@gmail.com',['endo'],True),
    ('張月梅','yuehmei1012@gmail.com',['hema'],True),
    ('張惠婷','h9856437@gmail.com',['cv'],True),
    ('許依穎','juliahsu0603@hotmail.com',['id','chest'],True),
    ('陳秀如','p751172002@gmail.com',['hema'],True),
    ('陳品志','rtyu2583@gmail.com',['chest'],True),
    ('陳逵蓉','kuei142@yahoo.com.tw',['endo'],True),
    ('廖筱芸','mmiris0815@gmail.com',['endo'],True),
    ('劉妤珊','t760it7601@gmail.com',['chest'],True),
    ('彭瓊瑤','joana4009@yahoo.com.tw',['id'],False),
    ('彭琛玉','G00522@hch.gov.tw',['hema'],False),
    ('黃秋燕','alice511091@yahoo.com.tw',['cv'],False),
    ('葉佩珊','kelly.yeh1980@gmail.com',['nephro'],False),
    ('盧麗玉','takki730629@yahoo.com.tw',['chest'],False),
    ('戴聿晨','Tin6392@yahoo.com.tw',['chest'],False),
    ('謝瑞玲','lady80410@gmail.com',['chest'],False),
    ('蔡佳辰','nnww37@yahoo.com.tw',['gi'],True),
    ('蘇怡文','jagawife515@gmail.com',['id'],False),
    ('蘇韻珊','G80996@hch.gov.tw',['hema'],False),
    ('許家晟','G03170@hch.gov.tw',['nephro','chest'],True),
    ('羅彩鳳','tsaifenglio@gmail.com',['hema'],True),
    ('鍾恬菁','G81220@hch.gov.tw',['cv'],False),
    ('楊芝筠','G81055@hch.gov.tw',['chest'],False),
]

# ---- Assignment ----
# Rules: each VS max 3 surveys (hema max 5), each NP min 1 VS per spec
# Fill up VS capacity to maximize evaluations per NP

spec_nps = {}
for np_name, np_email, specs, is_mobile in nps_raw:
    for spec in specs:
        if spec == 'hema':
            if np_name in hema_fixed:
                spec_nps.setdefault(spec, []).append((np_name, 4))  # all 4 VS now
            elif np_name in hema_mobile_only:
                spec_nps.setdefault(spec, []).append((np_name, 1))
        else:
            spec_nps.setdefault(spec, []).append((np_name, 1))

# Maximize VS per NP within capacity (max 3 per VS)
for spec in ['cv','chest','gi','endo','nephro','id']:
    np_list = spec_nps.get(spec, [])
    vs_list = vs_by_spec[spec]
    if not np_list or not vs_list:
        continue
    total_capacity = len(vs_list) * 3
    np_count = len(np_list)
    max_vs_per_np = min(total_capacity // np_count, len(vs_list))
    max_vs_per_np = max(max_vs_per_np, 1)
    spec_nps[spec] = [(n, max_vs_per_np) for n, _ in np_list]

raw_assignments = []

for spec in ['cv','chest','gi','endo','nephro','hema','id']:
    np_list = spec_nps.get(spec, [])
    vs_list = vs_by_spec[spec]
    if not np_list or not vs_list:
        continue
    vs_load = {v: 0 for v in vs_list}
    survey_mult = 2 if spec == 'hema' else 1
    max_load = 8 if spec == 'hema' else 3  # hema needs 8 to fit 3 fixed(x4 VS) + 4 mobile(x1 VS)

    for np_name, target in np_list:
        t = min(target, len(vs_list))
        available = [v for v in vs_list if vs_load[v] + survey_mult <= max_load]
        if not available:
            available = sorted(vs_list, key=lambda v: vs_load[v])
        else:
            available = sorted(available, key=lambda v: (vs_load[v], vs_list.index(v)))
        assigned = available[:t]
        for v in assigned:
            vs_load[v] += survey_mult
            raw_assignments.append((spec, v, np_name))

# Ensure 謝慕揚 is included in CV
cv_vs = [v for s,v,n in raw_assignments if s == 'cv']
if '謝慕揚' not in cv_vs:
    cv_np_count = {}
    for s,v,n in raw_assignments:
        if s == 'cv':
            cv_np_count[n] = cv_np_count.get(n, 0) + 1
    if cv_np_count:
        min_np = min(cv_np_count.items(), key=lambda x: x[1])[0]
        raw_assignments.append(('cv', '謝慕揚', min_np))

# ---- Print assignment summary ----
print("=== ASSIGNMENT SUMMARY (v3) ===\n")

for spec in ['cv','chest','gi','endo','nephro','hema','id']:
    recs = [(v,n) for s,v,_,n in [(s,v,emails[v],n) for s,v,n in raw_assignments] if s == spec]
    # Simpler:
    recs = [(v,n) for s,v,n in raw_assignments if s == spec]
    if not recs:
        continue
    np_vs = {}
    for v, n in recs:
        np_vs.setdefault(n, []).append(v)
    label = spec_labels[spec]
    note = ' (x2: hema+onco)' if spec == 'hema' else ''
    print(f"--- {label}: {len(recs)} records{note} ---")
    for n, vlist in np_vs.items():
        tag = ''
        if spec == 'hema':
            if n in hema_fixed: tag = ' [fixed]'
            elif n in hema_mobile_only: tag = ' [mobile]'
        print(f"  {n}{tag} <- {', '.join(vlist)} ({len(vlist)} VS)")
    vl = {}
    for v, n in recs:
        mult = 2 if spec == 'hema' else 1
        vl[v] = vl.get(v, 0) + mult
    print(f"  VS load: {', '.join(f'{v}({c})' for v,c in sorted(vl.items(), key=lambda x:-x[1]))}")
    print()

# Total
total_records = len(set(i for i,_ in enumerate(raw_assignments)))
hema_cnt = sum(1 for s,_,_ in raw_assignments if s == 'hema')
print(f"=== TOTALS ===")
print(f"Records: {len(raw_assignments)}")
print(f"CSV rows: {len(raw_assignments) + hema_cnt} (hema records have 2 rows)")
print(f"Surveys: {len(raw_assignments) + hema_cnt}")

print(f"\n--- VS total survey load ---")
vt = {}
for s, v, _ in raw_assignments:
    m = 2 if s == 'hema' else 1
    vt[v] = vt.get(v, 0) + m
for v, load in sorted(vt.items(), key=lambda x: -x[1]):
    sp = ''
    for s, vl in vs_by_spec.items():
        if v in vl:
            sp = spec_labels[s]
            break
    print(f"  {v} ({sp}): {load}")

# ---- Generate CSV ----
all_fields = ['eval_date', 'assessor_name', 'assessor_email', 'assessor_title',
              'evaluated_id', 'evaluated_name', 'evaluated_type',
              'trainee_type', 'trainee_name', 'dept']

prefix_order = ['cv','chest','gi','endocrine','nephro','hema','onco','id']
all_prefixes = set()
for spec, vs, np in raw_assignments:
    if spec == 'hema':
        all_prefixes.add('hema')
        all_prefixes.add('onco')
    else:
        all_prefixes.add(form_prefix[spec])

header = ['record_id', 'redcap_repeat_instrument', 'redcap_repeat_instance']
for pfx in prefix_order:
    if pfx in all_prefixes:
        for f in all_fields:
            header.append(f"{pfx}_{f}")

csv_rows = []
record_id = 1

for spec, vs_name, np_name in raw_assignments:
    if spec == 'hema':
        for form_key in ['hema', 'onco']:
            pfx = form_prefix[form_key]
            row = {
                'record_id': str(record_id),
                'redcap_repeat_instrument': form_names[form_key],
                'redcap_repeat_instance': '1',
            }
            row[f"{pfx}_assessor_name"] = vs_name
            row[f"{pfx}_assessor_email"] = emails[vs_name]
            row[f"{pfx}_assessor_title"] = '1'
            row[f"{pfx}_evaluated_name"] = np_name
            row[f"{pfx}_evaluated_id"] = ''
            row[f"{pfx}_evaluated_type"] = '4'
            row[f"{pfx}_trainee_type"] = '4'
            row[f"{pfx}_trainee_name"] = np_name
            row[f"{pfx}_dept"] = dept_labels[form_key]
            row[f"{pfx}_eval_date"] = ''
            csv_rows.append(row)
        record_id += 1
    else:
        pfx = form_prefix[spec]
        row = {
            'record_id': str(record_id),
            'redcap_repeat_instrument': form_names[spec],
            'redcap_repeat_instance': '1',
        }
        row[f"{pfx}_assessor_name"] = vs_name
        row[f"{pfx}_assessor_email"] = emails[vs_name]
        row[f"{pfx}_assessor_title"] = '1'
        row[f"{pfx}_evaluated_name"] = np_name
        row[f"{pfx}_evaluated_id"] = ''
        row[f"{pfx}_evaluated_type"] = '4'
        row[f"{pfx}_trainee_type"] = '4'
        row[f"{pfx}_trainee_name"] = np_name
        row[f"{pfx}_dept"] = dept_labels[spec]
        row[f"{pfx}_eval_date"] = ''
        csv_rows.append(row)
        record_id += 1

output_path = 'G:/我的雲端硬碟/004 教學資料 at Hsinchu 院內/Teaching materials CV education web at github/IM CCC EPA/planning/REDCap_Import_EPA_2026-04-06_v3.csv'
with open(output_path, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, fieldnames=header, restval='')
    writer.writeheader()
    writer.writerows(csv_rows)

print(f"\nCSV written: {output_path}")
print(f"CSV rows: {len(csv_rows)}, Columns: {len(header)}")
