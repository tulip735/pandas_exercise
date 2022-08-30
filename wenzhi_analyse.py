#! -*- encoding: utf-8 -*-

from typing import List
import pandas as pd


def read_file(file_name: str, column_name: List[str]) -> pd.DataFrame:
    data = pd.read_excel(file_name, engine='openpyxl')
    print(data.columns)
    data = data[column_name]
    print(data.shape)
    print(data.head())
    return data


def group_statics(data: pd.DataFrame,column_names: List[str]):

    data[column_names] = data[column_names].astype(str)
    # grouped = data[column_names].groupby(column_names)agg('count')
    grouped = data[column_names].agg('count')
    with pd.option_context('expand_frame_repr', False, 'display.max_rows', None):
        print(grouped)



if __name__ == '__main__':
    # 读取文件
    file_name = "/Users/blacktulip/test/pandas_exercise/wenzhi_data.xlsx"
    column_names = ['岗位代码', '用人单位名称', '岗位类别','学历', '工作地点', '所学专业']
    wenzhi_data = read_file(file_name, column_names)

    # 数量统计
    group_names = ['工作地点']
    group_statics(wenzhi_data, group_names)

    print('main')