import csv
# BTC_USDT

def process_data(coin_name):
    with open(coin_name+'.csv') as f:
        reader = csv.reader(f)
        data_list = []
        pop_data_list = []
        for row in reader:
            if len(row) == 0:
                continue
            if row[0] == 'v':
                continue
            if row[0] <= ' 18:00':
                pop_data_list.append(row)
                continue
            data_list.append(row)

        with open('perfect_'+coin_name+'.csv', 'w') as f:
            writer = csv.writer(f)
            header = ['v','l','s']
            writer.writerow(header)
            writer.writerows(data_list)

        # for data in data_list:
        #     print(data)

coin_name_list = ['bitfinex_BTC_USDT_line','bitflyer_BTC_JPY_line','bitmex_ETH_USD_line','bitmex_XBT_BTC_line','bitmex_XBT_USD_line']
for coin_name in coin_name_list:
    process_data(coin_name)