# HAPPY CODING
#******* Y༺࿈༻Y ******************************************
#       /  ♅  \     Author        :  zmdsn
#  *    )0 ^ 0(     Last modified :  2022-01-26 09:33
#   \    \ - /      Email         :  zmdsn@126.com
#    \___ | | ___   Filename      :  read_file.py
#        \ ∵ /   L  Description   :
#        / ∴ \  }O{    
#       / | \ \  T       
# ******* |  \ ******************************************/
#!/usr/bin/python
# -*- coding: utf-8 -*- 
import pandas as pd
import chardet 
import time
import numpy as np 
import os
import sys
Debug = 1 

def run_time(func):
    def time_second(*args,**kwargs):
        start_time = time.time()
        res = func(*args,**kwargs)
        end_time = time.time()
        if Debug == 1:
            print( func.__name__, ' time used: ' ,end_time - start_time)
        return res
    return time_second

# @run_time
# def get_encoding(file):     
#     # 验证基本没有用
#     with open(file,'rb') as f:         
#         tmp = chardet.detect(f.read(100))         
#         print(tmp,tmp['encoding'])
#         encoding = tmp['encoding']
#         print(encoding)
#         if tmp['confidence']<0.5 : 
#             encoding = 'utf8'
#         if encoding == 'ascii':
#             encoding = 'utf8'
#         if 'Windows' in encoding:
#             encoding = 'gbk'
#         return encoding

# @run_time
def get_csv(file_name,**kargs): #,skiprows=0, nrows=-1
    # read_csv for different encoding, maybe rewite
    # encoding = get_encoding(fullPath)    
    # print(kargs)
    try:
        data = pd.read_csv(file_name,**kargs)
    except:             
        try:                 
            data = pd.read_csv(file_name,encoding='gbk',**kargs)
        except:                 
            data = pd.read_csv(file_name,encoding='gb2312',**kargs)
    return data
    # if nrows < 0:
    #     try:
    #         data = pd.read_csv(file_name,skiprows=skiprows,**kargs)
    #     except:             
    #         try:                 
    #             data = pd.read_csv(file_name,skiprows=skiprows,
    #                     encoding='gbk',**kargs)
    #         except:                 
    #             data = pd.read_csv(file_name,skiprows=skiprows,
    #                     encoding='gb2312',**kargs)
    # else :
    #     # print(nrows)
    #     try:
    #         data = pd.read_csv(file_name,skiprows=skiprows,nrows=nrows,**kargs)
    #     except:             
    #         try:                 
    #             data = pd.read_csv(file_name,skiprows=skiprows,
    #                     nrows=nrows,encoding='gbk',**kargs)
    #         except:                 
    #             data = pd.read_csv(file_name,skiprows=skiprows,
    #                     nrows=nrows,encoding='gb2312',**kargs)
    # return data

# @run_time
def get_excel(file_name,**kargs):
    print(len(kargs))
    res = pd.read_excel(file_name,**kargs)
    # if sheet_name == 0:
    #     res = pd.read_excel(file_name,**kargs)
    # else:
    #     res = pd.read_excel(file_name,sheet_name,**kargs)
    return res

def get_file_size(file_name):
    # size = sys.getsizeof(file_name)
    file_size = os.path.getsize(file_name)
    return file_size 

def print_file_size(file_name) :
    num = get_file_size(file_name)
    num_len = len(str(num))
    if (num_len<=3):
        print(str(num_len) )
    elif num_len>3 and (num_len<=6):
        print(str(round(num/1024,2)) + 'K')
    elif num_len>6 and (num_len<=9):
        print(str(round(num/1024**2,2)) + 'M')
    elif num_len>9 and (num_len<=12):
        print(str(round(num/1024**3,2)) + 'G')
    elif num_len>12 :
        print(str(round(num/1024**4,2)) + 'T')

@run_time
def read_file(file_name,**kargs):  #,sheet=0,key=0,nrows=-1,
    # filename,type = os.path.splitext(path) 
    # print(kargs)
    if 'file_name' in kargs:
        file_name = kargs['file_name']
    if 'csv' in file_name:
        data = get_csv(file_name,**kargs)
    elif '.xlsx' in file_name or ('.xls' in file_name) :
        data = get_excel(file_name,**kargs)
    elif '.pkl' in file_name:
        data = pd.read_pickle(file_name)
    elif 'h5' in file_name:
        if key == 0:
            data = pd.read_hdf(file_name)
        else:
            data = pd.read_hdf(file_name,key=key)
    return data

def name2pkl(file_name,sheet=0):
    # filename,type = os.path.splitext(path) 
    if '.csv' in file_name:
        return file_name.replace('.csv','_') + str(sheet)+ '.pkl' 
    elif '.xlsx' in file_name:
        return file_name.replace('.xlsx','_') + str(sheet)+ '.pkl' 
    elif '.xls' in file_name:
        return file_name.replace('.xls','_') + str(sheet) + '.pkl' 
    elif '.pkl' in file_name:
        # return file_name.replace('.pkl','.pkl')
        return file_name
    elif '.h5' in file_name:
        return file_name.replace('.h5','.pkl')

def name2csv(file_name,sheet=0):
    # filename,type = os.path.splitext(path) 
    if '.csv' in file_name:
        return file_name
    elif '.xlsx' in file_name:
        return file_name.replace('.xlsx','_') + str(sheet)+ '.csv' 
    elif '.xls' in file_name:
        return file_name.replace('.xls','_') + str(sheet) + '.csv' 
    elif '.pkl' in file_name:
        return file_name.replace('.pkl','.csv')
    elif '.h5' in file_name:
        return file_name.replace('.h5','.csv')

def excel_to_csv(file_name, sheet_name=0, header=0,**kargs):
    file_name_csv = self.change_name(self,file_name, sheet_name=0, header=0)
    pd.read_excel(file_name,sheet_name=sheet_name,
                  header=header,converters={'楼栋编码':str}).to_csv(file_name_csv,index=False,**kargs) #,dtype=str

def pickle_to_csv(file_name):
    pd.read_pickle(file_name).to_csv(file_name.replace('.pkl','.csv'),index=False)

# @run_time
# def read_data(file_name,**kargs):
#     # get_csv
#     if 'file_name' in kargs:
#         file_name = kargs['file_name']
#     file_size = get_file_size(file_name)
#     if (file_size > 100000000) and ('.pkl' not in file_name):
#         print(file_name + ' 文件过大,建议转存为pkl文件')
#     csv_name = name2csv(file_name,kargs)
#     # csv_name = name2pkl(file_name,kargs)
#     to_csv =  kargs['to_csv'] if 'replace' in kargs else 0
#     if os.path.exists(csv_name) and to_csv==0 :
#         data = read_file(csv_name,**kargs)
#         return data
#     elif os.path.exists(csv_name) and to_csv==0 :
#         data = read_file(csv_name,**kargs)
#         return data
#     elif os.path.exists(file_name):
#         data = read_file(file_name,**kargs)
#         if to_csv:
#             data.to_csv(csv_name,index=False)
#         return data
#     raise Exception("No this file",file_name)

def pickle_to_excel(file_name):
    pd.read_pickle(file_name).to_excel(file_name.replace('.pkl','.xlsx'))

def csv_to_excel(file_name,**kargs):
    get_csv(file_name,**kargs).to_excel(file_name.replace('.csv','.xlsx'))

if __name__ == '__main__':
    fpath = "../" 
    # fname = "标记是否异常值剔除.csv"     
    # fname = "poi未匹配.csv"     
    # fname = "重复村名.xlsx"     
    fname = "重复村名.xlsx"     
    fullPath = fpath + fname     
    # print(get_encoding(fullPath) )    
    # print(get_encoding('test.csv') )    
    # df = get_csv(fullPath)
    # size = os.path.getsize('test.csv')
    # print(size)
    # df = get_csv('test.csv')
    # print(df.memory_usage().sum())
    # df . to_pickle('test.pkl')
    # df = pd.read_pickle('test.pkl')
    # print(df.memory_usage().sum())
    # print(get_file_size(fullPath))
    print_file_size(fullPath)
    # read_data('test.csv',nrows=2200)
    # read_data(fullPath)
    # df = get_csv('test.gz')
    # combine = np.random.rand(2000000,100)
    # print(sys.getsizeof(combine))
    # a = pd.DataFrame(combine)
    # # a.to_csv('test.csv')
    # a.to_csv('test.gz', compression='gzip', index=False)
