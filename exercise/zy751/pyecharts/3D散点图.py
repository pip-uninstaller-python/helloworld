from pyecharts.charts import Scatter3D
import random
from example.commons import Faker
from pyecharts import options as op

def a_scatter():
    data=[[random.randint(0,100),random.randint(0,80),random.randint(0,70)] for i in range(80)]
    sc=(
        Scatter3D()
        .add('',data,grid3d_opts=op.Grid3DOpts(rotate_speed=150,is_rotate=True))
        .set_global_opts(title_opts={'text':'3D散点图'},visualmap_opts=op.VisualMapOpts(range_color=Faker.visual_color))
    )
    return  sc
sc=a_scatter()
sc.render('4.html')