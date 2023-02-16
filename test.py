
import matplotlib.pyplot as plt
import numpy as np


def Smooth_LineChart2(filename):
    # 数据设置部分
    T = 50
    x1 = range(0, T, 1)  # x轴为：0 - 100
    rng = np.random.default_rng()
    y1 = rng.integers(0, np.arange(T, 0, -1))/100
    y2 = 0.95**np.arange(50)  # final_train_loss是一个list

    plt.figure()
    plt.plot(x1, y1, '.-', label='loss1')
    plt.plot(x1, y2, '--', label='loss2')
    plt.ylim(-0.05, 1.05)  # 设置纵轴上下界
    plt.title('Loss & Epoch')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.show()
    plt.savefig(filename, dpi=200)


if __name__ == '__main__':
    Smooth_LineChart2(filename='test')