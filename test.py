
import matplotlib.pyplot as plt
import numpy as np


def Smooth_LineChart2(filename):
    Palette5 = ['#FFAE4E', '#B01A5B', '#EFEDE8', '#F41F15']
    fig,ax = plt.subplots(figsize=(6, 6))
    ax.grid(linestyle = '--', linewidth = 1.0)
    ax.set_axisbelow(True)  # grid lines are behind the rest
    plt.xlim(0.5, 3.5)   #调整刻度左右界
    plt.ylim(79, 88)  #调整刻度上下界

    label = ['Model 1', 'Model 2', 'Model 3']
    x1 = np.array([1, 1, 1])
    x2 = np.array([2, 2])
    x3 = np.array([3, 3])
    y1 = np.array([83, 85, 87])
    y2 = np.array([84, 85.2])
    y3 = np.array([80, 85.9])

    sizes1 = np.array([20, 32, 277])*4
    sizes2 = np.array([86, 307])*4
    sizes3 = np.array([25, 928])*4
    plt.scatter(x1, y1, s=sizes1, c=Palette5[0], label=label[0])
    plt.scatter(x2, y2, s=sizes2, c=Palette5[1], label=label[1])
    plt.scatter(x3, y3, s=sizes3, c=Palette5[3], label=label[2])
    lgnd = plt.legend(loc='center left', bbox_to_anchor=(0.05, 1.08), ncol=3,
              prop={"family": "Times New Roman", "size": 12}, shadow=True)

    lgnd.legendHandles[0]._sizes = [60]  # 将legend中每个图标大小设置成一样
    lgnd.legendHandles[1]._sizes = [60]
    lgnd.legendHandles[2]._sizes = [60]

    for i, txt in enumerate(sizes1):   # 添加备注在点旁边并设置偏移量
        ax.annotate(str(txt)+'M', (x1[i]-0.15*(i+1), y1[i] +0.2))
    for i, txt in enumerate(sizes2):
        ax.annotate(str(txt)+'M', (x2[i]-0.25*(i+1), y2[i]+0.3))
    for i, txt in enumerate(sizes3):
        ax.annotate(str(txt)+'M', (x3[i]-0.25*(i+1), y3[i]+(i+1)*0.3))

    plt.ylabel("Accuracy (%)")
    ax.set_xticks(range(1, len(label)+1), label, fontsize=12)
    plt.show()


if __name__ == '__main__':
    Smooth_LineChart2(filename='test')