"""
Demo: Publication-quality Kaplan-Meier survival curve
Simulated clinical trial comparing Treatment A vs Treatment B
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.gridspec import GridSpec

np.random.seed(42)

# --- Simulate survival data ---
n_per_group = 120

# Treatment A: median survival ~24 months (better)
times_a = np.random.exponential(scale=30, size=n_per_group)
events_a = np.random.binomial(1, 0.75, size=n_per_group)  # 75% event rate

# Treatment B: median survival ~16 months (worse)
times_b = np.random.exponential(scale=18, size=n_per_group)
events_b = np.random.binomial(1, 0.80, size=n_per_group)

# Cap follow-up at 48 months
max_time = 48
times_a = np.minimum(times_a, max_time)
times_b = np.minimum(times_b, max_time)

# Where time hits cap, mark as censored
events_a[times_a >= max_time] = 0
events_b[times_b >= max_time] = 0


def kaplan_meier(times, events):
    """Compute KM survival estimate with Greenwood CI."""
    order = np.argsort(times)
    t = times[order]
    e = events[order]

    unique_times = np.unique(t[e == 1])
    unique_times = np.sort(unique_times)

    n_at_risk_list = []
    n_events_list = []

    for ti in unique_times:
        at_risk = np.sum(t >= ti)
        died = np.sum((t == ti) & (e == 1))
        n_at_risk_list.append(at_risk)
        n_events_list.append(died)

    n_at_risk_arr = np.array(n_at_risk_list)
    n_events_arr = np.array(n_events_list)

    survival = np.cumprod(1 - n_events_arr / n_at_risk_arr)

    # Greenwood variance
    greenwood = np.cumsum(n_events_arr / (n_at_risk_arr * (n_at_risk_arr - n_events_arr + 1e-10)))
    se = survival * np.sqrt(greenwood)

    ci_lower = np.maximum(survival - 1.96 * se, 0)
    ci_upper = np.minimum(survival + 1.96 * se, 1)

    # Prepend time 0
    unique_times = np.concatenate([[0], unique_times])
    survival = np.concatenate([[1.0], survival])
    ci_lower = np.concatenate([[1.0], ci_lower])
    ci_upper = np.concatenate([[1.0], ci_upper])

    return unique_times, survival, ci_lower, ci_upper


def n_at_risk(times, checkpoints):
    """Number at risk at given time points."""
    return [int(np.sum(times >= cp)) for cp in checkpoints]


def log_rank_test(times_a, events_a, times_b, events_b):
    """Simple log-rank test (Mantel-Cox)."""
    all_times = np.unique(np.concatenate([
        times_a[events_a == 1], times_b[events_b == 1]
    ]))
    all_times = np.sort(all_times)

    numerator = 0.0
    denominator = 0.0

    for ti in all_times:
        na = np.sum(times_a >= ti)
        nb = np.sum(times_b >= ti)
        n_total = na + nb
        if n_total == 0:
            continue
        da = np.sum((times_a == ti) & (events_a == 1))
        db = np.sum((times_b == ti) & (events_b == 1))
        d_total = da + db

        expected_a = na * d_total / n_total
        numerator += da - expected_a

        if n_total > 1:
            denominator += (na * nb * d_total * (n_total - d_total)) / (n_total ** 2 * (n_total - 1))

    if denominator <= 0:
        return 1.0

    chi2 = numerator ** 2 / denominator

    # chi2 with 1 df -> p-value via survival function approximation
    from scipy.stats import chi2 as chi2_dist
    p_value = chi2_dist.sf(chi2, df=1)
    return p_value


# Compute KM curves
t_a, s_a, ci_lo_a, ci_hi_a = kaplan_meier(times_a, events_a)
t_b, s_b, ci_lo_b, ci_hi_b = kaplan_meier(times_b, events_b)

# Log-rank p-value
p_val = log_rank_test(times_a, events_a, times_b, events_b)

# --- Plot ---
fig = plt.figure(figsize=(8, 6.5), dpi=300)
gs = GridSpec(2, 1, height_ratios=[4, 1], hspace=0.08, figure=fig)

ax_main = fig.add_subplot(gs[0])
ax_table = fig.add_subplot(gs[1])

color_a = '#2166AC'  # blue
color_b = '#B2182B'  # red

# Step curves
ax_main.step(t_a, s_a, where='post', color=color_a, linewidth=2, label='Treatment A (n=120)')
ax_main.step(t_b, s_b, where='post', color=color_b, linewidth=2, label='Treatment B (n=120)')

# Confidence intervals
ax_main.fill_between(t_a, ci_lo_a, ci_hi_a, step='post', alpha=0.15, color=color_a)
ax_main.fill_between(t_b, ci_lo_b, ci_hi_b, step='post', alpha=0.15, color=color_b)

# Censoring tick marks
cens_t_a = times_a[events_a == 0]
cens_s_a = []
for ct in cens_t_a:
    idx = np.searchsorted(t_a, ct, side='right') - 1
    idx = min(idx, len(s_a) - 1)
    cens_s_a.append(s_a[idx])
ax_main.plot(cens_t_a, cens_s_a, '|', color=color_a, markersize=8, markeredgewidth=1.2)

cens_t_b = times_b[events_b == 0]
cens_s_b = []
for ct in cens_t_b:
    idx = np.searchsorted(t_b, ct, side='right') - 1
    idx = min(idx, len(s_b) - 1)
    cens_s_b.append(s_b[idx])
ax_main.plot(cens_t_b, cens_s_b, '|', color=color_b, markersize=8, markeredgewidth=1.2)

# P-value annotation
if p_val < 0.001:
    p_text = 'Log-rank P < 0.001'
else:
    p_text = f'Log-rank P = {p_val:.3f}'
ax_main.text(0.98, 0.95, p_text, transform=ax_main.transAxes,
             ha='right', va='top', fontsize=11,
             bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='gray', alpha=0.8))

# Formatting
ax_main.set_xlim(0, max_time)
ax_main.set_ylim(0, 1.05)
ax_main.set_ylabel('Survival Probability', fontsize=13)
ax_main.set_title('Kaplan-Meier Estimate: Treatment A vs Treatment B\n(Simulated Randomized Controlled Trial, N=240)',
                  fontsize=13, fontweight='bold', pad=10)
ax_main.legend(loc='lower left', fontsize=11, frameon=True, framealpha=0.9)
ax_main.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1.0))
ax_main.set_xticklabels([])
ax_main.grid(axis='y', alpha=0.3, linestyle='--')
ax_main.spines['top'].set_visible(False)
ax_main.spines['right'].set_visible(False)

# --- Number at risk table ---
checkpoints = np.arange(0, max_time + 1, 6)
nar_a = n_at_risk(times_a, checkpoints)
nar_b = n_at_risk(times_b, checkpoints)

ax_table.set_xlim(ax_main.get_xlim())
ax_table.set_ylim(-0.5, 1.5)
ax_table.set_xlabel('Time (Months)', fontsize=13)
ax_table.set_xticks(checkpoints)

for i, cp in enumerate(checkpoints):
    ax_table.text(cp, 1, str(nar_a[i]), ha='center', va='center', fontsize=10, color=color_a, fontweight='bold')
    ax_table.text(cp, 0, str(nar_b[i]), ha='center', va='center', fontsize=10, color=color_b, fontweight='bold')

ax_table.text(-3.5, 1, 'Trt A', ha='right', va='center', fontsize=10, color=color_a, fontweight='bold')
ax_table.text(-3.5, 0, 'Trt B', ha='right', va='center', fontsize=10, color=color_b, fontweight='bold')

ax_table.set_yticks([])
ax_table.spines['top'].set_visible(False)
ax_table.spines['right'].set_visible(False)
ax_table.spines['left'].set_visible(False)
ax_table.tick_params(left=False)
ax_table.set_title('Number at Risk', fontsize=10, loc='left', pad=2)

plt.savefig(
    'G:/我的雲端硬碟/004 教學資料 at Hsinchu 院內/Teaching materials CV education web at github/IM CCC EPA/planning/analysis/demo_kaplan_meier.png',
    dpi=300, bbox_inches='tight', facecolor='white'
)
print(f"Figure saved. Log-rank p-value = {p_val:.6f}")
print("Done.")
