"""
Generate EPA Assessment Workflow Diagram
Clinical workflow showing the Entrustable Professional Activity assessment process.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# --- Configuration ---
fig, ax = plt.subplots(1, 1, figsize=(14, 18), dpi=200)
ax.set_xlim(0, 14)
ax.set_ylim(0, 18)
ax.axis('off')
fig.patch.set_facecolor('white')

# Color palette (colorblind-friendly)
colors = {
    'title_bg': '#2C3E50',
    'step_blue': '#3498DB',
    'step_blue_light': '#D6EAF8',
    'step_green': '#27AE60',
    'step_green_light': '#D5F5E3',
    'step_orange': '#E67E22',
    'step_orange_light': '#FDEBD0',
    'step_red': '#E74C3C',
    'step_red_light': '#FADBD8',
    'arrow': '#5D6D7E',
    'level_colors': ['#1B4F72', '#2874A6', '#2E86C1', '#5DADE2', '#85C1E9'],
    'level_text': ['white', 'white', 'white', '#1B4F72', '#1B4F72'],
}

# --- Helper functions ---
def draw_rounded_box(ax, x, y, w, h, facecolor, edgecolor, linewidth=2, alpha=1.0):
    box = FancyBboxPatch(
        (x - w/2, y - h/2), w, h,
        boxstyle="round,pad=0.15",
        facecolor=facecolor, edgecolor=edgecolor,
        linewidth=linewidth, alpha=alpha,
        zorder=2
    )
    ax.add_patch(box)
    return box

def draw_arrow(ax, x1, y1, x2, y2):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(
                    arrowstyle='->', color=colors['arrow'],
                    lw=2.5, mutation_scale=20
                ), zorder=1)

def draw_step_number(ax, x, y, num):
    circle = plt.Circle((x, y), 0.35, facecolor=colors['title_bg'],
                         edgecolor='white', linewidth=2, zorder=4)
    ax.add_patch(circle)
    ax.text(x, y, str(num), fontsize=14, fontweight='bold', color='white',
            ha='center', va='center', zorder=5)

# --- Title ---
draw_rounded_box(ax, 7, 17.0, 10, 1.0, colors['title_bg'], colors['title_bg'], linewidth=0)
ax.text(7, 17.05, 'EPA Assessment Workflow', fontsize=22, fontweight='bold',
        color='white', ha='center', va='center', fontfamily='sans-serif', zorder=3)
ax.text(7, 16.6, 'Entrustable Professional Activity', fontsize=12,
        color='#AEB6BF', ha='center', va='center', fontfamily='sans-serif', zorder=3)

# --- Step positions (center x=7, descending y) ---
steps = [
    {
        'num': 1, 'y': 15.2, 'label': 'Trainee Performs\nClinical Activity',
        'desc': 'History taking, physical exam, procedures,\npatient management, clinical reasoning',
        'bg': colors['step_blue_light'], 'edge': colors['step_blue'],
        'icon': '\u2695'  # medical symbol
    },
    {
        'num': 2, 'y': 13.2, 'label': 'Supervisor Observes',
        'desc': 'Direct observation or indirect assessment\n(chart review, case discussion, handover)',
        'bg': colors['step_blue_light'], 'edge': colors['step_blue'],
        'icon': '\U0001F441'
    },
    {
        'num': 3, 'y': 11.2, 'label': 'Assessment Form Completed\nvia REDCap',
        'desc': 'Electronic data capture of EPA ratings,\ncomments, and clinical context',
        'bg': colors['step_green_light'], 'edge': colors['step_green'],
        'icon': '\U0001F4CB'
    },
    {
        'num': 4, 'y': 9.2, 'label': 'Feedback Discussion',
        'desc': 'Bidirectional dialogue: strengths identified,\nareas for improvement, action plan agreed',
        'bg': colors['step_orange_light'], 'edge': colors['step_orange'],
        'icon': '\U0001F4AC'
    },
    {
        'num': 5, 'y': 7.0, 'label': 'Entrustment Decision',
        'desc': 'Supervisor determines the level of\nsupervision required for the activity',
        'bg': colors['step_red_light'], 'edge': colors['step_red'],
        'icon': '\u2714'
    },
]

box_w = 8.0
box_h = 1.4

for step in steps:
    y = step['y']
    draw_rounded_box(ax, 7, y, box_w, box_h, step['bg'], step['edge'], linewidth=2.5)
    draw_step_number(ax, 7 - box_w/2 + 0.6, y + 0.15, step['num'])

    ax.text(7 + 0.3, y + 0.3, step['label'], fontsize=13, fontweight='bold',
            color='#2C3E50', ha='center', va='center', fontfamily='sans-serif', zorder=3)
    ax.text(7 + 0.3, y - 0.35, step['desc'], fontsize=9,
            color='#566573', ha='center', va='center', fontfamily='sans-serif',
            style='italic', zorder=3)

# --- Arrows between steps ---
for i in range(len(steps) - 1):
    y_from = steps[i]['y'] - box_h/2 - 0.05
    y_to = steps[i+1]['y'] + box_h/2 + 0.05
    draw_arrow(ax, 7, y_from, 7, y_to)

# --- Arrow from step 5 down to levels ---
draw_arrow(ax, 7, steps[-1]['y'] - box_h/2 - 0.05, 7, 5.6)

# --- Entrustment Levels section ---
# Section header
draw_rounded_box(ax, 7, 5.3, 12.5, 0.5, '#F2F3F4', '#BDC3C7', linewidth=1)
ax.text(7, 5.3, 'Entrustment Levels', fontsize=14, fontweight='bold',
        color='#2C3E50', ha='center', va='center', fontfamily='sans-serif', zorder=3)

# Level boxes
levels = [
    {'num': 1, 'title': 'Level 1', 'desc': 'Observe\nOnly',
     'detail': 'Not allowed to\npractice activity'},
    {'num': 2, 'title': 'Level 2', 'desc': 'Direct\nSupervision',
     'detail': 'Supervisor in\nroom / present'},
    {'num': 3, 'title': 'Level 3', 'desc': 'Indirect\nSupervision',
     'detail': 'Supervisor\navailable nearby'},
    {'num': 4, 'title': 'Level 4', 'desc': 'Distant\nSupervision',
     'detail': 'Supervisor\navailable by phone'},
    {'num': 5, 'title': 'Level 5', 'desc': 'Unsupervised\nPractice',
     'detail': 'Can supervise\nothers'},
]

level_w = 2.2
level_h = 2.8
level_y = 3.2
start_x = 1.5
spacing = 2.5

# Draw progress arrow underneath
ax.annotate('', xy=(start_x + 4*spacing + level_w/2 + 0.3, level_y - level_h/2 - 0.4),
            xytext=(start_x - level_w/2 - 0.3, level_y - level_h/2 - 0.4),
            arrowprops=dict(arrowstyle='->', color='#ABB2B9', lw=3, mutation_scale=25),
            zorder=0)
ax.text(7, level_y - level_h/2 - 0.7, 'Increasing Autonomy',
        fontsize=11, color='#7F8C8D', ha='center', va='center',
        fontfamily='sans-serif', style='italic', zorder=1)

for i, level in enumerate(levels):
    x = start_x + i * spacing
    bg_color = colors['level_colors'][i]
    text_color = colors['level_text'][i]

    draw_rounded_box(ax, x, level_y, level_w, level_h, bg_color, bg_color, linewidth=0)

    # Level number circle
    circle = plt.Circle((x, level_y + level_h/2 - 0.45), 0.28,
                         facecolor='white', edgecolor=bg_color, linewidth=2, zorder=4, alpha=0.9)
    ax.add_patch(circle)
    ax.text(x, level_y + level_h/2 - 0.45, str(level['num']),
            fontsize=12, fontweight='bold', color=bg_color,
            ha='center', va='center', zorder=5)

    # Title
    ax.text(x, level_y + 0.25, level['desc'], fontsize=11, fontweight='bold',
            color=text_color, ha='center', va='center', fontfamily='sans-serif',
            zorder=3, linespacing=1.3)

    # Detail
    ax.text(x, level_y - 0.7, level['detail'], fontsize=8,
            color=text_color, ha='center', va='center', fontfamily='sans-serif',
            zorder=3, alpha=0.85, linespacing=1.3)

# --- Footer ---
ax.text(7, 0.8, 'EPA = Entrustable Professional Activity  |  REDCap = Research Electronic Data Capture',
        fontsize=9, color='#95A5A6', ha='center', va='center', fontfamily='sans-serif')
ax.text(7, 0.4, 'IM CCC EPA Program  |  Generated 2026-04-12',
        fontsize=8, color='#BDC3C7', ha='center', va='center', fontfamily='sans-serif')

plt.tight_layout(pad=0.5)
output_path = r"G:\我的雲端硬碟\004 教學資料 at Hsinchu 院內\Teaching materials CV education web at github\IM CCC EPA\planning\analysis\EPA_assessment_workflow.png"
plt.savefig(output_path, dpi=200, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.close()
print(f"Diagram saved to: {output_path}")
