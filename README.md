# Chart Toolkit for Technical Paper
## Motivation
为了在写作画图时更加方便和快捷，本工具包整合了常用制图代码以方便调用并快速出图。

## Color Palette 颜色版


## Line Chart
### Smooth Line Chart
```shell
python main.py --chart-mode=smooth_line_chart  
```
<div style="align: center"><img src="./images/smooth_lc.png" width="50%"></div>>

### Line Chart of Multiple Lines
```shell
python main.py --chart-mode=multi_line_chart
```

<div style="align: center">
<img src="./images/multi_lc_m1_p1.png" width="40%">
<img src="./images/multi_lc_m2_p1.png" width="40%">
<img src="./images/multi_lc_m2_p2.png" width="40%">
<img src="./images/multi_lc_m2_p3.png" width="40%">
</div>

## Bar Chart
### Single Bar Chart
```shell
python main.py --chart-mode=single_bar_chart  
```
<div style="align: center"><img src="./images/single_bc.png" width="50%"></div>

### Grouped Bar Chart
```shell
python main.py --chart-mode=grouped_bar_chart  
```
<div style="align: center">
<img src="./images/grouped_bc.png" width="50%">
<img src="./images/grouped_bc2.png" width="40%">
</div>>
根据自己的需求来调整画布尺寸(figsize)和柱状宽度(bar_width)达到以上效果