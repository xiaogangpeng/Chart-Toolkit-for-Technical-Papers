from chart import *


if __name__ == '__main__':
    args = option.parser.parse_args()

    # ======= # 普通折线图（平滑线条）
    if args.chart_mode == 'smooth_line_chart':
        filename = 'smooth_lc'
        Smooth_LineChart(filename=filename)

    # ======= # loss对比折线图（平滑线条）
    elif args.chart_mode == 'smooth_line_chart2':
        filename = 'smooth_lc2'
        Smooth_LineChart2(filename=filename)

    # ======= # 多线折线图
    elif args.chart_mode == 'multi_line_chart':
        filename = 'multi_lc'
        Multi_LineChart(legend_mode=0,palette=args.palette, filename=filename)

    # ======= # 单条形图
    elif args.chart_mode == 'single_bart_chart':
        data = [195, 145, 56, 213]
        label = ['Model 1', 'Model 2', 'Model 3', 'Model 4']
        assert len(data) == len(label) == len(args.palette), 'number of data must be equal to number of labels and colors'
        bar_width = 0.4
        filename = 'single_bc'
        Single_BarChart(data, label, legend_mode=1, pallete=args.palette, bar_width=bar_width, filename=filename)

    # ======= # 组合式条形图
    elif args.chart_mode == 'grouped_bar_chart':
        data = [[36, 25, 17, 12, 15],
                [28, 17, 12, 9, 8],
                [23, 15, 15, 12, 16],
                [23, 15, 15, 12, 16]]
        group_label = ['0.2', '0.4', '0.6', '0.8', '1.0']    # 横轴数据
        group_item = ['Class 1', 'Class 2', 'Class 3', 'Class 4']  # 组合内类别（标签）
        assert len(data) == len(group_item) == len(args.palette), 'number of data must be equal to number of labels and colors'
        bar_width = 0.2
        filename = 'grouped_bc'
        Grouped_BarChart(data, group_item, group_label, legend_mode=1, pallete=args.palette, bar_width=bar_width, filename=filename)

    # ======= # 模型属性对比散点图
    elif args.chart_mode == 'model_scatter_chart':
        Model_ScatterChart(filename='model_sc')

