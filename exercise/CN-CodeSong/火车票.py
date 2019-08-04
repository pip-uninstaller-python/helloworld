
import requests
import re
import os
import time
from easygui import multenterbox

qishi,mudi,date = '','',''

today = time.strftime("%Y-%m-%d", time.localtime())
while qishi == '' or mudi == '':
    qishi,mudi,date = multenterbox(msg='请选择输入火车票的信息。', title='火车票', fields=['出发地','目的地','出发时间'], values=['','',today], callback=None, run=True)



header = {'Accept': 'application/json',
          'Accept-Encoding': 'gzip, deflate',
          'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ru;q=0.7',
          'Connection': 'keep-alive',
          'Cookie': 'QN48=tc_8caf63a5191e513b_166da0a434b_346d; QN235=2018-11-03; QN1=O5cv7FvdtM2ZGwY0EUGHAg==; QN66=qunar; QN300=qunar; _i=VInJOm6vru6qH3U1ZElVuZVlsL2q; _vi=wpBsU0KDkvuRM6Tz7w3w303Xxjgoi8ydNn04cS7HLtF5gLtilq-PSCMfHIHVhp_hRvNOW2lxcwRoYNPBCiP7FNJ9HHfW1kpI764vc3Zf9-O8ShmPmUG9Brbqm-BzlrbNyC-qdDViOm5qNy_NL6-v32EGxZImh1CHto4Wy98VbZ89; QN269=496D6B10DF7711E8B269FA163E3D4D9E; fid=dbeb67c9-77d3-4418-9df9-3ca4e157e055; QunarGlobal=10.86.213.149_-28243bd6_166da0466bb_-1bfd|1541256407348; QN99=9839; QN10=startStation%3D%E9%9D%92%E5%B2%9B%26endStation%3D%E5%8C%97%E4%BA%AC%26searchType%3Dstasta%26date%3D2018-11-05',
          'DNT': '1',
          'Host': 'touch.qunar.com',
          'Referer': 'http://touch.qunar.com/h5/train/trainList?startStation=%E9%9D%92%E5%B2%9B&endStation=%E5%8C%97%E4%BA%AC&searchType=stasta&date=2018-11-05&sort=3&wakeup=1&scheme=9ba0d4a5501039c836e0f6ebd7591c3cdf530395e34774be803ca3aa5d8d7dd8cf88613cfc8df070ec4e3b634fadd55e5d2b3c5e92a67cf5b9ad2b2ca2ee2fbeaaaaf8d32f72b48d3195532f9c31363ab1cdf31734bf69946633d45fd62711279bb591494637864aa80089a15ef4dc4c823dadfcf4b93547ce15b49a1d54cb3f',
          'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
          'X-Requested-With': 'XMLHttpRequest'}

while True:
    html = "http://touch.qunar.com/h5/train/trainList?startStation=" + qishi + "&endStation=" + mudi + "&searchType=stasta&date=" + date + "&sort=3&wakeup=1"
    print(html)

    neirong0 = requests.get(url=html, headers=header)
    neirong0 = neirong0.text

    neirong1 = re.findall(r"""<li class="qn_arrow_grey r">(.*)<div class="more">点击查看更多</div>""", neirong0, re.S)
    if len(neirong1) == 0:
        pass
    else:
        neirong1 = neirong1[0]
        # print(neirong1)

        # duan = re.findall(r"""<a.*?</div>
        # """,neirong1,re.S)
        # print(duan)

        print("\t车次\t   类型\t\t出发地点\t\t目的地\t\t出发时间\t行驶时间\t\t抵达时间\t座位型号\t票数\t售价")

        che_ci = re.findall(r'''<span class="qn_fl">(.*)<span class="qn_grey">''', neirong1)
        duan_shu = len(neirong1) / len(che_ci)
        for a in range(len(che_ci)):

            lei_xing = re.findall(r'''qn_grey">(.*?)</span></sp''', neirong1)[a]
            chu_fa_time0 = re.findall(u"""tant">(.*)</""", neirong1)
            for hh in chu_fa_time0:
               if "yen" == hh[1:4]:
                   # chu_fa_time = hh
                    chu_fa_time0.remove(hh)
            chu_fa_time = chu_fa_time0[a]
            chu_fa_di = re.findall(r"""startStation=(.*?)&""", neirong1)[a]
            mu_di_di = re.findall(r"""endStation=(.*?)&""", neirong1)[a]
            xing_shi_time = re.findall(r"""<span class="time">(.*?)</span>""", neirong1, re.S)[a]
            di_da_time = re.findall(r"""<span class="qn_grey">(.*?)</span>""", neirong1, re.S)[a * 2 + 1]
            zuo_wei_lei_xing = re.findall(r"""seatType=(.*?)'>""", neirong1, re.S)[a]
            yu_ding = re.findall
            piao_shu = re.findall(r'\d+张', neirong1)
            shou_jia0 = re.findall(u"""tant">(.*)</""", neirong1)
            if "yen" not in shou_jia0[-1]:
                shou_jia0.append("已售空")
            for d in range(len(che_ci) * 2 - 2):
                if ":" in shou_jia0[d] and "yen" not in shou_jia0[d + 1]:
                    shou_jia0.insert(d + 1, "已售空")
            for b in range(len(che_ci)):
                shi = int(b * duan_shu)
                zhong = int((b + 1) * duan_shu)
                duan = neirong1[shi:zhong]
                if "可预订" in duan:
                    del shou_jia0[b * 2 + 1]
                    shou_jia0.insert(b * 2 + 1, "可预订")
                    piao_shu.insert(b, "预订")
            shou_jia = shou_jia0[a * 2 + 1]
            # print(piao_shu)
            # print(shou_jia0)
            # print(chu_fa_time0)

            print(a, end="\t")
            print(che_ci[a], end="\t")
            if len(lei_xing) == 4:
                print(lei_xing, "    ", end="\t")
            else:
                print(lei_xing, end="\t")
            if len(chu_fa_di) < 4:
                p = 4 - len(chu_fa_di)
                print(chu_fa_di, end="")
                print("  " * p, end="\t\t")
            else:
                print(chu_fa_di, end="\t\t")
            print(mu_di_di, end="\t\t")
            print(chu_fa_time, end="\t\t")
            if len(xing_shi_time) < 6:
                print(xing_shi_time, end="")
                shu0 = 6 - len(xing_shi_time)
                print("  " * shu0, end="\t\t")
            else:
                print(xing_shi_time, end="\t\t")
            print(di_da_time[:5], end="\t\t")
            print(zuo_wei_lei_xing, end="\t\t")
            try:
                print(piao_shu[a], end='\t')
            except IndexError:
                print("0张", end='\t')
            if "可预订" in shou_jia or "已售空" in shou_jia:
                print(shou_jia, end="\t")
            else:
                print(shou_jia[5:], end="\t")

            print('\n')
        time.sleep(4)
        os.system('cls')
        os.system('clear')
