import requests
import threading
# from bs4 import BeautifulSoup
# https://cn.tradingview.com/
# https://coinfarm.online，此网站一部分数据是从上面网站使用websockt获取的


def get_data(url):
    '''获取long，short图表数据，返回字典格式数据'''

    results = requests.post(url)
    data = results.content.decode()  # str
    dict_data = eval(data)  # dict

    return dict_data


if __name__ == '__main__':
    '''获取long，short百分比图表数据，返回字典格式数据'''
    url_1 = 'https://coinfarm.online/public/api/mex_trade_usd.asp'
    t = threading.Thread(target=get_data, args=(url_1,))
    t.start()
    # 数据分别代表五分钟，十分钟对应的数据

    '''获取折线图数据'''
    url_2 = 'https://coinfarm.online/public/ws/gr_json_0030.asp'
    t = threading.Thread(target=get_data, args=(url_2,))
    t.start()
