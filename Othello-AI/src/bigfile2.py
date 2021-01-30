# -*- coding:utf-8 -*-
import os
from os.path import join, getsize
import csv

"""
版本：直接提取C-I盘所有大于1GB的文件及文件夹
并输出CSV文件
盘符不存在则程序执行结束！
文件夹：size_C_path.csv
文件：size_C_file.csv
"""


def get_dirs_size(dirs, maxnum):
    print(dirs)
    # CSV文件名后缀
    fname = dirs.replace('\\', '_').replace(':', '').replace('/', '_')
    path_size = []  # 路径大小列表
    file_size = []  # 文件大小列表
    size = 0  # 合计
    for root, dirs, files in os.walk(dirs):
        for f in files:
            fp = join(root, f)
            su = getsize(fp) // 1024 // 1024
            if su > maxnum:
                file_size.append([su, fp])
                print(f'{su:>8,d} MB --> {fp}')
            pass
        sums = sum([getsize(join(root, file)) for file in files]) // 1024 // 1024
        size += sums
        if sums > maxnum:
            path_size.append([sums, root])
            print(f'{sums:>8,d} MB --> {root}')
            pass
    print(f'{size:>8,d} MB --> {dirs}')
    # 调用导出CSV函数导出CSV文件
    savecsvfile(path_size, ['大小', '文件夹'], f'size_{fname}path.csv')
    savecsvfile(file_size, ['大小', '文件'], f'size_{fname}file.csv')


def savecsvfile(rows, header, csv_name):
    # 导出CSV文件函数
    # if not os.path.exists(csv_name):
    with open(csv_name, 'w', newline='', encoding='utf-8') as f:
        fc = csv.writer(f)
        fc.writerow(header)
        fc.writerows(rows)
        print(csv_name, '导出成功！')


def main():
    # 所有盘符列表推导式：从C盘到I盘
    paths = [F"{x}:/" for x in 'C']
    for p in paths:
        if not os.path.exists(p):
            print(f'盘符 -> {p} 不存在!')
            break
        # 只提取大于1000MB的文件和文件夹
        get_dirs_size(p, 200)


if __name__ == '__main__':
    main()