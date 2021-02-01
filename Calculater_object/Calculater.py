# -*- coding:utf-8 -*-
# 计算器
class Calculater:
    # 加
    def add(self,a,b):
        return a+b
    # 除
    def div(self,a,b):
        if b==0:
            print("除数不能为0")
            return
        else:
            return a/b
    #     减
    def sub(self,a,b):
        return a-b
    # 乘
    def mul(self,a,b):
        return a*b