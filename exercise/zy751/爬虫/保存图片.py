import requests
#url="https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1561244479&di=b5e20358867355ec44a575f3355da740&src=http://aliyunzixunbucket.oss-cn-beijing.aliyuncs.com/jpg/bd57395940e68c946be5eb6db75c4f75.jpg?x-oss-process=image/resize,p_100/auto-orient,1/quality,q_90/format,jpg/watermark,image_eXVuY2VzaGk=,t_100"
url="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p712241453.webp"
e=requests.get(url)
with open('图片1.png','wb') as f:
    f.write(e.content)