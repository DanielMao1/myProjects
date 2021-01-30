# -*- coding:utf-8 -*-
import os
from os.path import join, getsize


# 版本：提取指定盘和大小的文件及文件夹


def get_paths_size(dirs, maxnum):
    # 提取指定文件夹和大小的函数
    print(f"{dirs} -> 文件夹内文件占用空间：")
    size = 0
    for root, dirs, files in os.walk(dirs):
        try:
            sums = sum([getsize(join(root, file)) for file in files]) // 1024 // 1024
            if sums > maxnum:
                print(f'{sums:>8,d} MB -> {root}')
            size += sums
        except:
            print("error in",files)
            pass

    print(f'{size:>8,d} MB -> 总大小')


def get_files_size(dirs, maxnum):
    # 提取指定文件夹内文件和大小的函数
    print(f"{dirs} -> 文件占用空间：")
    size = 0
    for root, dirs, files in os.walk(dirs):
        for file in files:
            try:
                fpth = join(root, file)
                sums = getsize(fpth) // 1024 // 1024
                if sums > maxnum:
                    print(f'{sums:>8,d} MB -> {fpth}')
                size += sums
            except:
                print("error in", file)
                pass

    print(f'{size:>8,d} MB -> 总大小')


def main():
    paths = r'C:\Users\Zun'
    numbs = 50  # -> MB
    # paths = input(r'请输入盘符(如：D:\Python\Python38：')
    # numbs = int(input(r'请)输入大小单位MB(如：1000)：'))
    get_paths_size(paths, numbs)
    get_files_size(paths, numbs)


if __name__ == '__main__':
    main()