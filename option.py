import argparse
# 颜色版
Palette1 = ['#315866', '#2A9D8E', '#E9C46B', '#F3A261', '#E66F51']
Palette2 = ['#4E62AB', '#87CFA4', '#FDB96A', '#D6404E']
Palette3 = ['#1A0841', '#4F9DA6', '#FFAD5A', '#FF5959']

parser = argparse.ArgumentParser(description='Vis_tools')
parser.add_argument('--line-width', default=0.5, help='linewidth of line chart')
parser.add_argument('--chart-mode', default='single_bart_chart', help='[smooth_line_chart, multi_line_chart, single_bart_chart, grouped_bar_chart]')
parser.add_argument('--palette', default=Palette3, help='color palette list')