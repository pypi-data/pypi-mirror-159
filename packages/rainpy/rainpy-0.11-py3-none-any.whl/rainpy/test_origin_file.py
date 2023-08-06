# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 10:04:47 2022

@author: zmdsn
"""

import origin_file as rf

def test_OriginFile():
    rf.OriginFile('./test/test_gbk.csv')
    rf.OriginFile('./test/test_utf8.csv')
    A = rf.OriginFile('./test/test.xlsx')
    assert  'A' in A
    B = rf.read_file('./test/test.xlsx',sheet_name='test2')
    assert  'test2' in B
    # # 长编码
    A = rf.OriginFile('./test/test.xlsx',dtype={'长编码':str})
    assert  isinstance(A['长编码'][0], str)
    B = rf.OriginFile('./test/test.xlsx',sheet_name='test2',dtype={'长编码':str})
    assert  isinstance(B['长编码'][0], str)
    # # 日期编码
    B = rf.OriginFile('./test/test.xlsx',parse_dates = ['日期_1'])
    assert  B['日期_1'].dtypes == 'datetime64[ns]'
    # # 日期编码
    A = rf.OriginFile('./test/test.xlsx',parse_dates = ['日期_1'])
    assert  A['日期_1'].dtypes == 'datetime64[ns]'
    # # A.to_pickle('./test/test_pkl.pkl')
    A = rf.OriginFile('./test/test_pkl.pkl',parse_dates = ['日期'],dtype={'长编码':str})
    assert  A['日期'].dtypes == 'datetime64[ns]'
    assert  isinstance(A['长编码'][0], str)
    A = rf.OriginFile('./test/test.xlsx',sheet_name='test3',index_col=[0,1],header=1)
    assert  A['idx'][1] == 1
    assert  A['test2'][2] == 2
    mp_dict = {'idx':'AA','长编码1':'BA'}
    A.rename(columns = mp_dict)
    assert 'AA' in A
    assert 'BA' not in A

    A = rf.OriginFile('./test/test.xlsx',dtype={'长编码':str})
    B = rf.OriginFile('./test/test.xlsx',sheet_name='test2',dtype={'长编码':str})
    old_l = len(set(A.data.columns.append(B.data.columns)))
    A += B
    assert len(A.data.columns) == old_l
    
    A = rf.OriginFile('./test/test.xlsx')
    old_l = A.data.shape[0]
    A.append(A)
    assert A.data.shape[0] == old_l*2
    
    A.drop_Unnamed()
    assert A.data.columns.str.contains('Unnamed').sum() == 0
    
    assert A.str_time_format('20180102') == '%Y%m%d'
    assert A.str_time_format('2018-01-02') == '%Y-%m-%d'
    assert A.str_time_format('2018-1-2') == '%Y-%m-%d'
    assert A.str_time_format('2018/01/02') == '%Y/%m/%d'
    assert A.str_time_format('2018-01') == '%Y-%m'
    assert A.str_time_format('18-01') == '%y-%m'
    # assert A.str_time_format('18-01-02') == '%y-%m-%d'
    
    
    
    
    
    