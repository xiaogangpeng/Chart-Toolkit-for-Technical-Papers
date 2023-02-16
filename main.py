from fileinput import filename

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib as mpl

import option


def Smooth_LineChart(filename):
    mpl.rcParams['font.sans-serif'] = 'Times New Roman'

    pred = [0., 0., 0.1, 0.2, 0., 0.3, 0.35, 0.5, 0.4, 0.7, 0.2, 0.5, 0.6, 0.65, 0.24, 0.76, 0.9, 0.67, 0.78, 0.76, 0.87, 0.45, 0.2, 0.,
            0.1, 0.34, 0.24, 0.14, 0.1, 0.4, 0., 0., 0., 0., 0., 0., 0., 0., 0.]

    gt = [0., 0., 0., 0., 0., 0.14, 0.1, 0.4, 0., 0., 0., 0., 0., 0.35, 0.5, 0.4, 0.2, 0.1, 0., 0., 0., 0., 0., 0.,
          0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]

    pred = np.repeat(pred, 20)
    gt = np.repeat(gt, 20)

    x_axis = np.arange(0, len(pred))
    x_smooth = np.linspace(x_axis.min(), x_axis.max(), 300)

    y_smooth = make_interp_spline(x_axis, pred)(x_smooth)
    y_smooth2 = make_interp_spline(x_axis, gt)(x_smooth)

    plt.figure(figsize=(12, 6))                  # 定义图像大小
    plt.plot(x_smooth, y_smooth, linewidth=2.5, color='b')  # 线条属性
    plt.plot(x_smooth, y_smooth2, linewidth=2.5, color='r')
    plt.ylim(-0.05, 1.05)    # y轴0刻度和最高值各留出一些边缘空间
    ax = plt.subplot(111)

    plt.legend(['Predicted Score', 'Ground Truth'])  # 右上角加图标提示

    ax.set_xlabel(..., fontsize=14)
    ax.set_ylabel(..., fontsize=14)
    plt.xlabel("X - Axis (Time or others)")
    plt.ylabel("Y - Axis (Scores or other values)")
    plt.title('Line Chart for Output and Ground Truth', fontsize=14)
    plt.savefig(filename, dpi=200)
    plt.show()




def Multi_LineChart(legend_mode, palette, filename):
    #  多条折线图， 可用于多模型准确率比较
    config = {
        "font.family": 'serif',  # sans-serif/serif/cursive/fantasy/monospace
        # "font.size": 14,  # medium/large/small
        'font.style': 'normal',  # normal/italic/oblique
        'font.weight': 'normal',  # bold
        "mathtext.fontset": 'cm',  # 'cm' (Computer Modern)
        "font.serif": ['cmb10'],  # 'Simsun'宋体
        "axes.unicode_minus": False,  # 用来正常显示负号
    }
    plt.rcParams.update(config)

    x_data = [{'Param': 20},{'Param': 40},{'Param': 60},{'Param': 80} ]

    data1 = [{'Param': 18, 'Acc':14.5},
             {'Param': 30, 'Acc': 36.9},
             {'Param': 45, 'Acc': 67.9},
             {'Param': 70, 'Acc': 78.6},
            ]

    data2 = [{'Param': 25, 'Acc': 24.5},
            {'Param': 36, 'Acc': 57},
            {'Param': 55, 'Acc': 73},
            {'Param': 68, 'Acc': 83},
            ]

    data3 = [{'Param': 20, 'Acc': 31},
             {'Param': 36, 'Acc': 67.5},
             {'Param': 52, 'Acc': 78.5},
            {'Param': 69, 'Acc': 88.6},
            ]
    data4 = [{'Param': 15, 'Acc': 34.5},
            {'Param': 40, 'Acc': 70.6},
             {'Param': 60, 'Acc': 82.5},
            {'Param': 75, 'Acc': 92.9},
            ]

    param = [str(item['Param']) for item in x_data]
    acc1 = [item['Acc'] for item in data1]
    acc2 = [item['Acc'] for item in data2]
    acc3 = [item['Acc'] for item in data3]
    acc4 = [item['Acc'] for item in data4]

    # ‘.’：点(point marker)
    # ‘, ’：像素点(pixel marker)
    # ‘o’：圆形(circle marker)
    # ‘v’：朝下三角形(triangle_down marker)
    # ‘ ^ ’：朝上三角形(triangle_up marker)
    # ‘ < ’：朝左三角形(triangle_left marker)
    # ‘ > ’：朝右三角形(triangle_right marker)
    # ‘1’：(tri_down marker)
    # ‘2’：(tri_up marker)
    # ‘3’：(tri_left marker)
    # ‘4’：(tri_right marker)
    # ‘s’：正方形(square marker)
    # ‘p’：五边星(pentagon marker)
    # ‘ * ’：星型(star marker)
    # ‘h’：1号六角形(hexagon1 marker)
    # ‘H’：2号六角形(hexagon2 marker)
    # ‘+’：+号标记(plus marker)
    # ‘x’：x号标记(x marker)
    # ‘D’：菱形(diamond marker)
    # ‘d’：小型菱形(thin_diamond marker)
    # ‘ | ’：垂直线形(vline marker)
    # ‘_’：水平线形(hline marker)

    plt.plot(param, acc1, color=palette[0], marker='o', linewidth=2.0, linestyle='solid', markerfacecolor='white', markeredgewidth=2.0)  # 圆点+实线  markerfacecolor 调整成空心点
    plt.plot(param, acc2, color=palette[1], marker='s', linewidth=2.0, linestyle='dashed', markerfacecolor='white', markeredgewidth=2.0)  # 正方点+虚线
    plt.plot(param, acc3, color=palette[2], marker='^', linewidth=2.0, linestyle='dashdot', markerfacecolor='white', markeredgewidth=2.0)  # 上三角+实线
    plt.plot(param, acc4, color=palette[3], marker='D', linewidth=2.0, linestyle='dotted', markerfacecolor='white', markeredgewidth=2.0)  # 星星+虚线
    ax = plt.subplot(111)
    # plt.title('Income')

    if legend_mode == 0:   # legend 模式调整，放外面，还是放里面
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width, box.height * 0.98])  #  height 调整图高低
        ax.legend(['Model 1', 'Model 2', 'Model 3', 'Model 4'], loc='center left', bbox_to_anchor=(0.25, 1.08), ncol=2,  prop={"family": "Times New Roman", "size": 18})
        # 1.08 调整legend与主图之间的上下间距， 0.2 调整legend的左右边距  ncol 一行图标的个数
    elif legend_mode == 1:
        # loc = 'best', 'upper right', 'upper left', 'lower left', 'lower right',
        # 'right', 'center left', 'center right', 'lower center', 'upper center', 'center'
        ax.legend(['Model 1', 'Model 2', 'Model 3', 'Model 4'], loc='lower right', prop={"family": "Times New Roman", "size": 10})

    plt.xlabel('Model Parameters (M)', fontdict={"family": "Times New Roman", "size": 10})
    plt.ylabel('Accuracy (%)', fontdict={"family": "Times New Roman", "size": 10})
    plt.grid(color='#929292', linestyle='--', linewidth=0.5)  # 添加网格线
    plt.savefig(filename, dpi=200)
    plt.show()



def Single_BarChart(data, label, legend_mode, pallete, bar_width, filename):
    rect = plt.bar(range(len(data)), data, color=pallete, width=bar_width)
    plt.grid(color='#929292', linestyle='--', linewidth=0.5, axis='y')
    ax = plt.subplot(111)

    if legend_mode == 0:   # legend 模式调整，放外面，还是放里面
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width, box.height * 0.98])  #  height 调整图高低
        ax.legend(rect, label, loc='center left', bbox_to_anchor=(0.25, 1.08), ncol=2)
        # 1.08 调整legend与主图之间的上下间距， 0.2 调整legend的左右边距  ncol 一行图标的个数
    elif legend_mode == 1:
        # loc = 'best', 'upper right', 'upper left', 'lower left', 'lower right',
        # 'right', 'center left', 'center right', 'lower center', 'upper center', 'center'
        ax.legend(rect, label, loc='lower right', prop={"family": "Times New Roman", "size": 10})

    ax.set_xticks(range(len(label)), label)

    plt.savefig(filename, dpi=200)
    plt.show()


def Grouped_BarChart(data, group_item, group_label, legend_mode, pallete, bar_width, filename):

    import matplotlib.ticker as mticker

    pos = list(range(len(group_label)))
    ind = np.arange(len(group_label))
    fig,ax = plt.subplots(figsize=(16, 7))
    plt.figure(dpi=200)

    for i in range(len(data)):
        ax.bar([p + i*bar_width for p in pos], data[i], bar_width, color=pallete[i], edgecolor='black')
        for x, y in zip([p + i*bar_width for p in pos], data[i]):
            # 把数据加在注条上面，不需要可注释掉这个循环
            ax.annotate(str(y) + '%', (x, y + 0.3), fontsize=14, horizontalalignment='center')

    if legend_mode == 0:  # legend 模式调整，放外面，还是放里面
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width, box.height * 0.98])  # height 调整图高低
        ax.legend(group_item, loc='center left', bbox_to_anchor=(0.22, 1.08), ncol=4,  prop={"family": "Times New Roman", "size": 18})
        # 1.08 调整legend与主图之间的上下间距， 0.22 调整legend的左右边距  ncol 一行图标的个数
    elif legend_mode == 1:
        # loc = 'best', 'upper right', 'upper left', 'lower left', 'lower right',
        # 'right', 'center left', 'center right', 'lower center', 'upper center', 'center'
        ax.legend(group_item, loc='upper right', prop={"family": "Times New Roman", "size": 18})

    ax.tick_params(labelsize=18)
    ax.set_xticks(ind+bar_width*1.5, group_label, fontsize=18)
    ax.set_ylabel("Accuracy (%)", loc='center', fontsize=18)
    ax.yaxis.set_major_formatter(mticker.FormatStrFormatter('%.0f'))

    fig.savefig(filename, dpi=200)
    fig.show()


if __name__ == '__main__':
    args = option.parser.parse_args()

    # ======= # 普通折线图（平滑线条）
    if args.chart_mode == 'smooth_line_chart':
        filename = 'smooth_lc'
        Smooth_LineChart(filename=filename)
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
    # ======= # 组合条形图
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



