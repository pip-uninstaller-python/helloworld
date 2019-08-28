import math
from example.commons import Faker
from  pyecharts.charts import Line3D
import pyecharts.options  as op
def line_3d():
    data=[]
    for t in range(0,25000):
        _t=t/1000
        x=(1+0.25*math.cos(75*_t))*math.cos(_t)
        y=(1+0.25*math.cos(75*_t))*math.sin(_t)
        z=_t+2.0*math.sin(75*_t)
        data.append([x,y,z])
    c=(
        Line3D()
        .add(
            '',
            data,
            xaxis3d_opts=op.Axis3DOpts(Faker.clock,type_='value'),
            yaxis3d_opts=op.Axis3DOpts(Faker.week_en,type_='value'),
            grid3d_opts=op.Grid3DOpts(width=100,height=100,depth=100,rotate_speed=100,is_rotate=True),
        )
       .set_global_opts(
        visualmap_opts=op.VisualMapOpts(
            max_=30,min_=0,range_color=Faker.visual_color
        ),
        title_opts=op.TitleOpts(title='line3d'),
    )
    )
    return c
c=line_3d()
c.render('3.html')