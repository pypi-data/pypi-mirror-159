# HAPPY CODING
#******* Y༺࿈༻Y ******************************************
#       /  ♅  \     Author        :  zmdsn
#  *    )0 ^ 0(     Last modified :  2022-02-08 14:54
#   \    \ - /      Email         :  zmdsn@126.com
#    \___ | | ___   Filename      :  origin_file.py
#        \ ∵ /   L  Description   :
#        / ∴ \  }O{    
#       / | \ \  T       
# ******* |  \ ******************************************/
#!/usr/bin/python
# -*- coding: utf-8 -*- 
import pandas as pd
# import rainpy
from read_file import *
# from common import *
import logging

class OriginFile():
    def __init__(self,*args, **kargs):
        '''
            OriginFile(,*args, **kargs)
        '''
        if 'log_file' in kargs:
            self.log_file = kargs['columns_map']
            del kargs['columns_map']
        else:
            self.log_file = "sys.log"
        if 'features' in kargs:
            self.features = kargs['features']
            del kargs['features']
        if 'data' in kargs:
            self.data = kargs['data']
            del kargs['data']
        else:
            self.data = read_file(*args, **kargs)
        # if len(args)>0 and isinstance(args[0],str):
        #     self.file_name = args[0]
        #     if 'features' in kargs:
        #         self.features = kargs['features']
        #         del kargs['features']
        #     self.data = read_file(file_name=self.file_name,**kargs)
        # else:
        #     self.data = read_file(*args, **kargs)
        # 特殊表处理
        if 'index_col' in kargs:
            self.data = self.data.reset_index()
        # 根据features提取数据
        if hasattr(self, 'features'):
            self.origin_data = self.data
            self.data = self.data[self.features]
        self.init_logger()

            
    def rename(self,columns:dict):
        # 更换列名
        # self.set_mapping_col(*columns)
        self.columns = columns
        self.data = self.data.rename(columns=self.columns)
 
    def column_split(self,column,reg_pat):
        D = self.data[column].str.extract(pat = reg_pat)
        self.data = pd.concat([self.data,D],axis=1)
        
    # def huxing_split(self,column='户型'):
    #     # before split, change to 房 厅
    #     self.data[column] = self.data[column].str.replace('居室','室')
    #     self.data[column] = self.data[column].str.replace('居','室')
    #     self.data[column] = self.data[column].str.replace('房','室')
    #     self.data[column] = self.data[column].str.replace('居','室')
    #     self.data[column] = self.data[column].str.replace('居','室')
    #     D = self.data['户型'].str.extract(pat = '(?P<房>\d)室.*(?P<厅>\d)厅')
    #     D['房'] = D['房'].fillna(0)
    #     D['厅'] = D['厅'].fillna(0)
    #     if('房' not in self.data.columns)and('厅' not in self.data.columns):
    #         self.data = pd.concat([self.data,D],axis=1)
    #     if '房' in self.data.columns:
    #         self.data['房'] = D['房']
    #     if '厅' in self.data.columns:
    #         self.data['厅'] = D['厅']
    def str_time_format(self,str_): 
        if '-' in str_:
            sp = '-'
        elif '/' in str_:
            sp = '/'
        else:
            sp = ''
        str_s = str_.replace('-','')
        str_s = str_s.replace('/','')
        if len(str_s) == 8:
            return '%Y'+sp+'%m'+sp+'%d'
        if len(str_s) == 6:
            if sp == '':
                return '%Y'+sp+'%m'
            elif str_.count(sp)==2:
                return '%Y'+sp+'%m'+sp+'%d'
            else:
                return '%Y'+sp+'%m'
        if len(str_s) == 4:
            if sp == '':
                return '%Y'
            else:
                return '%y'+sp+'%m'
            
    def drop_Unnamed(self): 
        r = self.data.columns[['Unnamed' in x for x in self.data.columns]] 
        self.data = self.data.drop(columns=r)

    def append(self,other): 
        # 数据合并
        row_before = self.data.shape[0]
        if hasattr(self, 'data') and hasattr(other, 'data'):
            self.data = self.data.append(other.data)
        # 列名合并
        row_after = self.data.shape[0]
        if row_before >= row_after:
            print("\033[0;31m执行 'append' 可能有错误 %d 变为 %d\033[0m",row_before,row_after)
        return self
    
    # 定义获取容器中指定元素的行为，相当于 self[key]
    def __getitem__(self, item):
        return self.data[item]

    # 定义设置容器中指定元素的行为，相当于 self[key] = value
    def __setitem__(self, key, value):
        self.data[key] = value

    # 定义当迭代容器中的元素的行为
    def __iter__(self):
        return self.data
    
    def __call__(self):
        print('call is called')
        
    # 定义赋值加法的行为：+= 
    def __iadd__(self, other):            
        try:
            self.data = self.data.merge(other.data,how='left')
        except :
            print("\033[0;31m 请检查数据类型,或删除相应的pkl文件使其重新生成 \033[0m" )
            print("需要比较相同字段 ",set(self.data.columns).intersection(
                set(other.data.columns) ) )
        return self

    # 定义当使用成员测试运算符（in 或 not in）时的行为
    def __contains__(self, item):
        return item in self.data
  
    def init_logger(self,log_tag='OriginFile'):
        self.logger = logging.getLogger(log_tag)
        self.logger.setLevel(logging.DEBUG)
        if (not self.logger.handlers) or ((not os.path.exists(self.log_file))):
            filehandler = logging.FileHandler(filename=self.log_file,encoding="utf-8",mode='a')
            # filehandler.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s & %(funcName)s & %(levelname)s & %(name)s & %(message)s')
            filehandler.setFormatter(formatter)
            self.logger.addHandler(filehandler)

      
if __name__ == '__main__':
    Cases = OriginFile('./test.csv')
    Cases1 = OriginFile('./test.csv')
    # print(Cases.append(Cases1))
    # print(Cases.set_mapping_col({'A':'AA'})) 
    print(Cases.mapping_col({'A':'AA','C':'CC'})) 
    Cases = Cases+Cases1
    print(Cases.data)
    # print(Cases.column_split('C','(?P<E>\d)_(?P<F>\d)') )
    # print(Cases.data) 
    # print(Cases.set_mapping_col({'A':'AA'})) 
    # print(Cases.mapping_col({'A':'AA','C':'CC'})) 
    # print(Cases.mapping_col({'A':'AA'})) 
    # print(Cases.mapping_col({'C':'CA'})) 
    # print(Cases.select_nan('C')) 
    # print(Cases.select('A',3)) 
    # print(Cases.select('A',[1,2])) 
    # Cases.sel_columns(['A','B'])
    # print(Cases.data)

