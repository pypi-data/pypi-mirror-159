# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 10:04:47 2022

@author: zmdsn
"""

import read_file as rf

def test_read_file():
    rf.read_file('./test/test_gbk.csv')
    rf.read_file('./test/test_utf8.csv')
    rf.read_file(file_name = './test/test_gbk.csv')
    # assert not rf.read_file(file_names = './test/test_gbk.csv')
    A = rf.read_file('./test/test.xlsx')
    assert  'A' in A
    B = rf.read_file('./test/test.xlsx',sheet_name='test2')
    assert  'test2' in B
    # 长编码
    A = rf.read_file('./test/test.xlsx',dtype={'长编码':str})
    assert  isinstance(A.长编码[0], str)
    B = rf.read_file('./test/test.xlsx',sheet_name='test2',dtype={'长编码':str})
    assert  isinstance(B.长编码[0], str)
    # 日期编码
    A = rf.read_file('./test/test.xlsx',parse_dates = ['日期_1'])
    assert  A.日期_1.dtypes == 'datetime64[ns]'
    # 日期编码
    A = rf.read_file('./test/test.xlsx',parse_dates = ['日期_1'])
    assert  A.日期_1.dtypes == 'datetime64[ns]'
    # A.to_pickle('./test/test_pkl.pkl')
    A = rf.read_file('./test/test_pkl.pkl',parse_dates = ['日期'],dtype={'长编码':str})
    assert  A.日期.dtypes == 'datetime64[ns]'
    assert  isinstance(A.长编码[0], str)
    A = rf.read_file('./test/test.xlsx',sheet_name='test3',index_col=[0,1],header=1).reset_index()
    assert  A.idx[1] == 1
    assert  A.test2[2] == 2
    # 大文件读取相关
    A = rf.read_file('./test/test.xlsx',nrows=1)
    assert  A.shape[0] == 1
    A = rf.read_file('./test/test.xlsx',skiprows= 7)
    assert  A.shape[0] == 1
