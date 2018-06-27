# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 20:50:25 2018

@author: lius
"""
import os
# function:获得某一目录下特定后缀文件列表
def getx_XX(_path,postfix):
    filelist = os.listdir(_path)
    ret = []
    for file in filelist:
        if os.path.splitext(file)[1]==postfix:
            ret.append(file)
    return ret
    #print('xx')

###funtion:获得某一路径下文件夹列表
def getdir(_path):
    ret = []
    filelist=os.listdir(_path)
    for file in filelist:
        if os.path.isdir(file):
            ret.append(file)
    return ret
   
if __name__=="__main__":
    print('getx_XX:',getx_XX('.','.py'))
    print('getdir:',getdir('.'))
