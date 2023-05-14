
import matplotlib.pyplot as plt
import numpy as np
import option

# def Model_ScatterChart(filename):
#     # Palette = ['#FFAE4E', '#B01A5B', '#EFEDE8', '#F41F15']
#     Palette = ['#706d94', '#ecd09c', '#79b4a0', '#d4daa1', '#b96570']
#     fig, ax = plt.subplots(figsize=(8.5, 6))
#     ax.grid(linestyle='--', linewidth=1.0)
#     ax.set_axisbelow(True)  # grid lines are behind the rest
#     plt.xlim(0.2, 5.6)  # 调整刻度左右界
#     plt.ylim(77, 87)  # 调整刻度上下界
#
#     label = ['RTFM†', 'Wu et al.', 'Pang et al.', 'MACIL-SD', 'Ours']
#     x1 = np.array([1])
#     x2 = np.array([2])
#     x3 = np.array([3])
#     x4 = np.array([4])
#     x5 = np.array([5])
#     y1 = np.array([78.54])
#     y2 = np.array([78.64])
#     y3 = np.array([81.69])
#     y4 = np.array([83.4])
#     y5 = np.array([85.67])
#
#     sizes1 = np.array([13.190])
#     sizes2 = np.array([0.843])
#     sizes3 = np.array([1.876])
#     sizes4 = np.array([0.678])
#     sizes5 = np.array([0.607])
#
#     plt.scatter(x1, y1, s=sizes1* 500, c=Palette[0], label=label[0])
#     plt.scatter(x2, y2, s=sizes2* 500, c=Palette[1], label=label[1])
#     plt.scatter(x3, y3, s=sizes3* 500, c=Palette[2], label=label[2])
#     plt.scatter(x4, y4, s=sizes4* 500, c=Palette[3], label=label[3])
#     plt.scatter(x5, y5, s=sizes5* 500, c=Palette[4], label=label[4])
#     lgnd = plt.legend(loc='center left', bbox_to_anchor=(0.02, 0.8), ncol=1,
#                       prop={"family": "Times New Roman", "size": 14}, shadow=True)
#
#     lgnd.legendHandles[0]._sizes = [60]  # 将legend中每个图标大小设置成一样
#     lgnd.legendHandles[1]._sizes = [60]
#     lgnd.legendHandles[2]._sizes = [60]
#     lgnd.legendHandles[3]._sizes = [60]  # 将legend中每个图标大小设置成一样
#     lgnd.legendHandles[4]._sizes = [60]
#
#     for i, txt in enumerate(sizes1):  # 添加备注在点旁边并设置偏移量
#         ax.annotate(str(txt) + 'M', (x1[i] - 0.3, y1[i] + 1.5), fontsize=14)
#     for i, txt in enumerate(sizes2):
#         ax.annotate(str(txt) + 'M', (x2[i] - 0.3, y2[i] + 0.6), fontsize=14)
#     for i, txt in enumerate(sizes3):
#         ax.annotate(str(txt) + 'M', (x3[i] - 0.3, y3[i] +  0.75), fontsize=14)
#     for i, txt in enumerate(sizes4):  # 添加备注在点旁边并设置偏移量
#         ax.annotate(str(txt) + 'M', (x4[i] - 0.3, y4[i] + 0.5), fontsize=14)
#     for i, txt in enumerate(sizes5):
#         ax.annotate(str(txt) + 'M', (x5[i] - 0.3, y5[i] + 0.5), fontsize=14)
#
#     ax.set_ylabel("AP (%)", fontsize=15)
#     ax.set_xticks(range(1, len(label) + 1), label, fontfamily="Times New Roman", fontsize=15)
#     fig.savefig(filename, dpi=300)
#     plt.show()


def Smooth_LineChart2(filename):
    args = option.parser.parse_args()
    # 数据设置部分
    x = np.arange(0, 50)
    y1 = [0.7417, 0.7802, 0.8025, 0.8238, 0.8167, 0.8161, 0.8123, 0.8198, 0.8224, 0.8303,
          0.8385, 0.8234, 0.8263, 0.8219, 0.8325, 0.8240, 0.8191, 0.8299, 0.8249, 0.8295,
          0.8268, 0.8305, 0.8383, 0.8375, 0.8567, 0.8502, 0.8534, 0.8428, 0.8307, 0.8388,
          0.8363, 0.8317, 0.8306, 0.8261, 0.8251, 0.8280, 0.8213, 0.8285, 0.8336, 0.8249,
          0.8291, 0.8262, 0.8240, 0.8234, 0.8241, 0.8227, 0.8255, 0.8228, 0.8207, 0.8244]

    y2 = [0.7134, 0.7441, 0.7879, 0.7997, 0.7443, 0.7716, 0.7861, 0.8135, 0.7877, 0.8077,
          0.8028, 0.8092, 0.8050, 0.8141, 0.7953, 0.8113, 0.7762, 0.8288, 0.7939, 0.7778,
          0.7780, 0.8014, 0.7904, 0.798, 0.7829, 0.7935, 0.8074, 0.7857, 0.7916, 0.8191,
          0.7895, 0.7973, 0.8086, 0.8120, 0.7950, 0.7981, 0.8056, 0.8135, 0.8005, 0.7939,
          0.7924, 0.7934, 0.7960, 0.8003, 0.7945, 0.7960, 0.8006, 0.8000, 0.7961, 0.8044]

    y3 = [0.7737, 0.7729, 0.7874, 0.7900, 0.7672, 0.7812, 0.7966, 0.7931, 0.7385, 0.7982,
          0.7837, 0.7804, 0.7651, 0.7894, 0.7933, 0.7721, 0.7247, 0.7661, 0.7761, 0.7982,
          0.7613, 0.7821, 0.7721, 0.7728, 0.7706, 0.7573, 0.7772, 0.7682, 0.7953, 0.7732,
          0.7608, 0.7701, 0.7674, 0.7733, 0.7663, 0.7682, 0.7821, 0.7979, 0.7602, 0.7800,
          0.7800, 0.7879, 0.7624, 0.7832, 0.7788, 0.7741, 0.7761, 0.7789, 0.7985, 0.7822]

    plt.figure()
    font = {"family": "Times New Roman",  "size": 14}
    font2 = {"family": "Times New Roman", "size": 10}
    colors = ['#CF1E18', '#009C96', '#FDAD52']
    A,= plt.plot(x, [item * 100 for item in y1], '-', label='FHGCN', color=colors[0], linewidth =2.0, markersize=10)
    B,= plt.plot(x,  [item * 100 for item in y2], '.--', label='HGCN', color=colors[1], linewidth =2.0, markersize=10)
    C,= plt.plot(x,  [item * 100 for item in y3], '.-', label='GCN', color=colors[2], linewidth =2.0, markersize=10)

    plt.legend(handles=[A, B, C], prop=font2, loc='upper right')

    plt.ylim(70, 87)  # 设置纵轴上下界
    # plt.title('Loss & Epoch')
    plt.ylabel('Accuracy (AP %)', font, fontweight='bold')
    plt.xlabel('Epoch', font, fontweight='bold')
    plt.xticks(rotation=0)
    plt.grid(True)
    plt.savefig(filename, dpi=300)
    plt.show()


if __name__ == '__main__':

    Smooth_LineChart2(filename='gcn_ap_ablation')