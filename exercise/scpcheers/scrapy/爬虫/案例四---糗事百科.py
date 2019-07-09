import requests
import re

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}  # 定义请求头

info_lists = []  # 初始化信息，用于装载信息列表


def judgement_sex(class_name):
    if class_name == 'womanIcon':
        return '女'
    else:
        return '男'


def get_info(url):
    res = requests.get(url)  # 获取网页信息
    ids = re.findall('<h2>(.*?)</h2>', res.text, re.S)
    levels = re.findall('<div class="articleGender \D+Icon">(.*?)'
                        '</div>', res.text, re.S)
    sexs = re.findall('<div class="articleGender (.*?)">', res.text, re.S)
    contents = re.findall('<div class="content">.*?<span>(.*?)</span>', res.text, re.S)
    laughs = re.findall('<span class="stats-vote"><i class="number">(\d+)'
                        '</i>', res.text, re.S)
    comments = re.findall('<i class="number">(\d+)</i>', res.text, re.S)
    for id, level, sex, content, laugh, comment in zip(
            ids, levels, sexs, contents, laughs, comments):
        info = {
            'id': id.strip(),
            'level': level,
            'sex': judgement_sex(sex),
            'content': content.strip(),
            'laugh': laugh,
            'comment': comment
        }
        info_lists.append(info)


if __name__ == '__main__':
    urls = ['https://www.qiushibaike.com/text/page/{}/'.format(str(i))
            for i in range(1, 36)]
    for single_url in urls:
        # print(single_url)
        get_info(single_url)
    for info_list in info_lists:
        f = open('F:/qiushi.txt', 'a+')
        try:
            f.write(info_list['id'] + '\n'),
            f.write(info_list['level'] + '\n'),
            f.write(info_list['sex'] + '\n'),
            f.write(info_list['content'] + '\n')
            f.write(info_list['laugh'] + '\n')
            f.write(info_list['comment'] + '\n\n')  # 写入txt文件
        except UnicodeEncodeError:
            pass  # pass掉错误编码

