"""
Demo: Publication-quality EPA assessment scores figure
Simulated data for medical education assessment visualization
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

matplotlib.rcParams['font.family'] = 'Microsoft JhengHei'
matplotlib.rcParams['axes.unicode_minus'] = False

# Set seed for reproducibility
np.random.seed(42)

# --- Simulated Data ---
domains = ['History\nTaking', 'Physical\nExam', 'Clinical\nReasoning', 'Communication', 'Procedures']
domain_labels_heatmap = ['History Taking', 'Physical Exam', 'Clinical Reasoning', 'Communication', 'Procedures']
n_per_group = 60

records = []
# PGY1: generally lower scores; PGY2: higher
for domain_idx, domain in enumerate(domains):
    for pgy, base in [('PGY-1', 2.8), ('PGY-2', 3.6)]:
        # Vary base by domain slightly
        offsets = [0.0, -0.1, -0.3, 0.2, -0.2]
        mu = base + offsets[domain_idx]
        scores = np.clip(np.random.normal(mu, 0.7, n_per_group), 1, 5).round(0).astype(int)
        for s in scores:
            records.append({'Domain': domain, 'PGY Level': pgy, 'Entrustment Score': s})

df = pd.DataFrame(records)

# Heatmap data: average scores by domain and assessor type
assessor_types = ['Attending', 'Fellow', 'NP']
heatmap_data = []
for i, domain in enumerate(domain_labels_heatmap):
    row = {}
    for assessor in assessor_types:
        # Attendings rate slightly lower, NPs slightly higher
        base = 3.2 + 0.15 * i
        if assessor == 'Attending':
            base -= 0.3
        elif assessor == 'NP':
            base += 0.2
        row[assessor] = round(base + np.random.normal(0, 0.15), 2)
    heatmap_data.append(row)

heatmap_df = pd.DataFrame(heatmap_data, index=domain_labels_heatmap)

# --- Figure ---
fig, axes = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={'width_ratios': [1.3, 1]})

# Color palette - medical/professional
palette = {'PGY-1': '#4878A8', 'PGY-2': '#E07B54'}

# Left: Violin plot
ax1 = axes[0]
sns.violinplot(
    data=df, x='Domain', y='Entrustment Score', hue='PGY Level',
    split=True, inner='quartile', palette=palette, ax=ax1,
    linewidth=1.2, cut=0, density_norm='width'
)
ax1.set_ylim(0.5, 5.5)
ax1.set_yticks([1, 2, 3, 4, 5])
ax1.set_yticklabels([
    '1 - Observe only',
    '2 - Direct supervision',
    '3 - Indirect supervision',
    '4 - Distant supervision',
    '5 - Unsupervised'
], fontsize=8.5)
ax1.set_xlabel('')
ax1.set_ylabel('Entrustment Level', fontsize=11, fontweight='bold')
ax1.set_title('EPA Entrustment Scores by Clinical Domain', fontsize=13, fontweight='bold', pad=12)
ax1.legend(title='Training Year', loc='lower right', framealpha=0.9, fontsize=9, title_fontsize=10)
ax1.axhline(y=3, color='gray', linestyle='--', alpha=0.4, linewidth=0.8)
ax1.tick_params(axis='x', labelsize=9.5)
sns.despine(ax=ax1)

# Right: Heatmap
ax2 = axes[1]
cmap = sns.color_palette("YlOrRd", as_cmap=True)
sns.heatmap(
    heatmap_df, annot=True, fmt='.2f', cmap=cmap, ax=ax2,
    linewidths=1.5, linecolor='white',
    vmin=2.5, vmax=4.5,
    cbar_kws={'label': 'Mean Entrustment Score', 'shrink': 0.8},
    annot_kws={'fontsize': 12, 'fontweight': 'bold'}
)
ax2.set_title('Mean Scores by Domain & Assessor', fontsize=13, fontweight='bold', pad=12)
ax2.set_xlabel('Assessor Type', fontsize=11, fontweight='bold')
ax2.set_ylabel('')
ax2.tick_params(axis='y', labelsize=9.5, rotation=0)
ax2.tick_params(axis='x', labelsize=10)

fig.suptitle('Simulated EPA Assessment Analysis — Internal Medicine Residency',
             fontsize=15, fontweight='bold', y=1.02, color='#2C3E50')

plt.tight_layout()

output_path = r"G:/我的雲端硬碟/004 教學資料 at Hsinchu 院內/Teaching materials CV education web at github/IM CCC EPA/planning/analysis/demo_epa_scores.png"
fig.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.close()
print(f"Saved to {output_path}")
