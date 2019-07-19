from example.commons import Faker
from pyecharts import options as op
from  pyecharts.charts import Bar3D
import random
def bar3d():
    data=[(i,j,random.randint(0,12))for i in range(6) for j in range(12)]
    c=(
        Bar3D()
        .add(
            '',
            [[d[1],d[0],d[2]] for d in data],
            xaxis3d_opts=op.Axis3DOpts(Faker.color,type_='category'),
            yaxis3d_opts=op.Axis3DOpts(Faker.week_en,type_='category'),
            zaxis3d_opts=op.Axis3DOpts(type_='value')
        )
        .set_global_opts(
            visualmap_opts=op.VisualMapOpts(max_=20),
            title_opts={'text':'三维'}
        )
    )
    return c
c=bar3d()
c.render('2.html')