import requests
import threading
import csv
# from bs4 import BeautifulSoup
# https://cn.tradingview.com/
# https://coinfarm.online，此网站一部分数据是从上面网站使用websockt获取的

class GetCoinfarm(object):

    def __init__(self, coin_name, url):
        self.coin_name = coin_name
        self.url = url

    def get_data(self):
        try:
            '''获取long，short图表数据，返回字典格式数据'''
            results = requests.post(self.url)
            data = results.content.decode()  # str
            dict_data = eval(data)  # dict
            # print(dict_data)
            return dict_data
        except Exception:
            print(Exception)

    def line_data_to_csv(self,data_dict):
        # 将折线图数据存入csv文件中
        headers = ['v','l','s']
        rows = data_dict['data']
        with open(self.coin_name+'_line.csv', 'w') as f:
            f_csv = csv.DictWriter(f, headers)
            f_csv.writeheader()
            f_csv.writerows(rows)

    def chart_data_to_csv(self, data_dict):
        # 将百分比图表数据存入csv文件中
        headers = ['b5', 's5', 'b10', 's10', 'b30', 's30', 'b60', 's60', 'b120', 's120', 'b240', 's240', 'b720', 's720', 'b1440', 's1440']
        rows = data_dict
        # print('in_in',data_dict)
        # print(type(data_dict))
        with open(self.coin_name + '_chart.csv', 'w') as f:
            f_csv = csv.DictWriter(f, headers)
            f_csv.writeheader()
            f_csv.writerows(rows)

if __name__ == '__main__':

    coin_url_dict = {'bitmex_XBT_USD':['https://coinfarm.online/public/api/mex_trade_usd.asp','https://coinfarm.online/public/ws/gr_json_0030.asp'],
                     'bitmex_XBT_BTC':['https://coinfarm.online/public/api/mex_trade_btc.asp','https://coinfarm.online/public/ws/btc_gr_json_0030t.asp?gmt=+08:00'],
                     'bitfinex_BTC_USDT':['','https://coinfarm.online/bitfinex/btc_gr_json_0030t.asp?gmt=+08:00'],
                     'bitflyer_BTC_JPY':['https://coinfarm.online/bitflyer/ajax_btc_trade_jpy.asp','https://coinfarm.online/bitflyer/ws/gr_json_0030t.asp?gmt=+08:00'],
                     'bitmex_funding_XBT':['',''],
                     'bitmex_ETH_USD':['https://coinfarm.online/eth/ajax_eth_trade_usd.asp','https://coinfarm.online/eth/ws/gr_json_0030t.asp?gmt=+08:00']

                     }
    for coin_name in coin_url_dict:
        # 创建折线图对象

        if coin_url_dict[coin_name][1] == '':
            print(coin_name,':的line_url是空的')
            continue
        obj_data_line = GetCoinfarm(coin_name, coin_url_dict[coin_name][1])
        data_line_dict = obj_data_line.get_data()
        # print(data_line_dict)
        obj_data_line.line_data_to_csv(data_line_dict)

    for coin_name in coin_url_dict:
        # 创建图表对象
        if coin_url_dict[coin_name][0] == '':
            print(coin_name,':的chart_url是空的')
            continue
        obj_data_chart = GetCoinfarm(coin_name, coin_url_dict[coin_name][0])
        data_chart = obj_data_chart.get_data()
        # print(data_chart)
        # print(type(data_chart))
        obj_data_chart.chart_data_to_csv([data_chart])


    # # USD数据
    # '''获取long，short百分比图表数据，返回字典格式数据'''
    # url_1 = 'https://coinfarm.online/public/api/mex_trade_usd.asp'
    # t = threading.Thread(target=get_data, args=(url_1,))
    # t.start()
    # # 数据分别代表五分钟，十分钟对应的数据
    #
    # '''获取折线图数据'''
    # url_2 = 'https://coinfarm.online/public/ws/gr_json_0030.asp'
    # t = threading.Thread(target=get_data, args=(url_2,))
    # t.start()

