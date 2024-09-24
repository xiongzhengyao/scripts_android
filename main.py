import os
import pandas as pd
from tabulate import tabulate



# 定义一个包含多个字典的列表，每个字典包含功能名称和JSON文件目录
features = [
    {"Index":"1" ,  "name": "LogPull",          "directory": "function_list/log_pull.json"},
    {"Index":"2" ,  "name": "OpenLog",          "directory": "function_list/open_log.json"},
    {"Index":"3" ,  "name": "Dump_pull",        "directory": "function_list/dump_pull.json"},
    {"Index":"4" ,  "name": "Dump_push",        "directory": "function_list/dump_push.json"},
    {"Index":"5" ,  "name": "setting_formate",  "directory": "function_list/dump_delete.json"},
    # 可以继续添加更多的功能
]

def main():
    print("Hello world!")
    # 打印第一行第二列
    print(features[0]["name"])
    print(features[0]["directory"])
    # 以表格的形式在终端输出每一行的name
    df = pd.DataFrame(features)
    alignment   = {'Index': 'center',   'name': 'center',     'directory': 'left'}
    space       = {'Index': 5,          'name': 20,         'directory': 40}
    print(df.to_string(index=False,justify=alignment,col_space=space))
    print(tabulate(df, headers='keys', tablefmt='psql'))
    # 再添加序号
    


if __name__ == "__main__":
    main()