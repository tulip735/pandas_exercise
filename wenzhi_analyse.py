#! -*- encoding: utf-8 -*-

import pandas as pd

def read_file(file_name):
    data = pd.read_excel(file_name)
    print(data.describe())
    print('ok') 









if __name__ == '__main__':
    file_name = "/Users/blacktulip/test/pandas_exercise/wenzhi_data.xlsx"
    read_file(file_name)
    print('main')