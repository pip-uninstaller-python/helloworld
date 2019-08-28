from pyecharts.charts import Bar#新的pyecharts 导入图形方式
import pyecharts.options as op  #标题选择吧
bar=(Bar()#图形实例化
    .add_xaxis(['毛衣','短袖','衬衫','tt'])#x轴坐标属性名
     # .set_global_opts(title_opts={'text':'销售情况表','subtext':'噢哟'})#表名  text主标题 subtext 副标题
    .set_global_opts(title_opts=op.TitleOpts(title='销售情况表',subtitle='噢哟'))
     .add_yaxis('商家A',[12,43,213,65],stack='stac12')#stack 为柱形图位置，设相同可叠加
     .add_yaxis('商家B',[23,12,54,12],stack='stack1')
     .set_series_opts(label_opts=op.LabelOpts(is_show=False))
     )
bar.render('1.html')
