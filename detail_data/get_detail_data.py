import requests


url = 'https://coinfarm.online/public/api/ajax_mex_btc_en.asp'

results = requests.post(url)
data = results.content.decode()  # str
dict_data = eval(data)  # dict

print(dict_data,type(dict_data))


