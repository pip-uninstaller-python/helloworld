from pyecharts import options as op
from pyecharts.render import make_snapshot
from pyecharts.charts import Bar
from snapshot_selenium import snapshot
def bar_chart():
    bar=(
        Bar()
        .add_xaxis(['苹果','香蕉','黄瓜','石榴'])
        .add_yaxis('A商家',[12,321,213,23])
        .set_global_opts(title_opts={'text':'喜爱的水果销售情况'})
    )
    return bar
a=bar_chart()

make_snapshot(snapshot,a.render(),'aa.png')
