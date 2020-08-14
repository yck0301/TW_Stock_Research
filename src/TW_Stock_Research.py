# Taiwan Stock Research
#
#
# Author: yck
# Date: 2020-Aug

import requests
import io
from datetime import datetime


def get_day_trading(callback=None):
    """
        synopsis: daily update the Taiwan stock trading information
            * trading: 成交資訊
            * from: data.gov.tw (open data)/ 個股日成交資訊
        args: callback(function)
        return: none
    """
    src_url = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY_ALL?response=open_data'
    resp = requests.get(src_url)
    resp.encoding = 'utf-8'
    if resp.status_code == 200:
        if callback != None:
            callback(resp.text)
    else:
        # todo: error log
        pass

def get_ownership_concentration(callback=None):
    """
        synopsis: weekly update the Taiwan stock ownership concentration
            * ownership concentration: 股權集中度
            * from: data.gov.tw (open data)/ 集保戶股權分散表
        args: callback (function)     
        return: none
    """
    src_url = 'https://smart.tdcc.com.tw/opendata/getOD.ashx?id=1-5'
    # tdcc blocks python's user-agent
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
    resp = requests.get(src_url, headers=headers)
    if resp.status_code == 200:
        if callback != None:
            callback(resp.text)
    else:
        # todo: error log
        pass


def create_write_out(file_path):
    """
        synopsis: create a function to write out a text file with the file path
        args: file_path (string)
        return: write_out (function)
    """
    def write_out(text):
        with io.open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)
    return write_out

if __name__ == '__main__':
    dir_path = '/Users/yck/Projects/TW_Stock_Research/data/{0}'
    current_timestamp = datetime.today().strftime('%Y%m%d')

    file_name_owner_conc = 'owner_conc_{0}.csv'.format(current_timestamp)
    file_name_day_trading = 'day_trading_{0}.csv'.format(current_timestamp)
    get_ownership_concentration(create_write_out(dir_path.format(file_name_owner_conc)))
    get_day_trading(create_write_out(dir_path.format(file_name_day_trading)))