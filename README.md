# Chart Toolkit for Technical Paper
## Motivation
为了在写作画图时更加方便和快捷，本工具包整合了常用制图代码以方便调用并快速出图。

## Color Palette 颜色版
#
    ‘.’：点(point marker)
    ‘, ’：像素点(pixel marker)
    ‘o’：圆形(circle marker)
    ‘v’：朝下三角形(triangle_down marker)
    ‘ ^ ’：朝上三角形(triangle_up marker)
    ‘ < ’：朝左三角形(triangle_left marker)
    ‘ > ’：朝右三角形(triangle_right marker)
    ‘1’：(tri_down marker)
    ‘2’：(tri_up marker)
    ‘3’：(tri_left marker)
    ‘4’：(tri_right marker)
    ‘s’：正方形(square marker)
    ‘p’：五边星(pentagon marker)
    ‘ * ’：星型(star marker)
    ‘h’：1号六角形(hexagon1 marker)
    ‘H’：2号六角形(hexagon2 marker)
    ‘+’：+号标记(plus marker)
    ‘x’：x号标记(x marker)
    ‘D’：菱形(diamond marker)
    ‘d’：小型菱形(thin_diamond marker)
    ‘ | ’：垂直线形(vline marker)
    ‘_’：水平线形(hline marker)
#

## Line Chart
### Smooth Line Chart
```shell
python main.py --chart-mode=smooth_line_chart  
```
<div style="align: center">
<ul><img src="./images/smooth_lc.png" width="50%"></ul>
</div>

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