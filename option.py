import argparse
# 颜色版
Palette1 = ['#315866', '#2A9D8E', '#E9C46B', '#F3A261', '#E66F51']
Palette2 = ['#4E62AB', '#87CFA4', '#FDB96A', '#D6404E']
Palette3 = ['#1A0841', '#4F9DA6', '#FFAD5A', '#FF5959']
Palette4 = ['#BAB2AC', '#2C5B78', '#4C4D57', '#2A7377']
Palette5 = ['#FFAE4E', '#B01A5B', '#EFEDE8', '#F41F15']
Palette6 = ['#1E1548', '#2E99B0', '#FCD77F', '#FF2E4C']

parser = argparse.ArgumentParser(description='Chart_Toolkit')
parser.add_argument('--line-width', default=0.5, help='linewidth of line chart')
parser.add_argument('--chart-mode', default='smooth_line_chart2', help='[smooth_line_chart, multi_line_chart, single_bart_chart, grouped_bar_chart]')
parser.add_argument('--palette', default=Palette3, help='color palette list')