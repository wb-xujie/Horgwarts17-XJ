# -*- coding: utf-8 -*-
# 这是计算器的测试用例模块
import sys
import yaml
import pytest

sys.path.append('..')
from Calculater_object.Calculater import *

def get_data(key,value = 'value'):
    with open("./data.yml") as file:
        data = yaml.safe_load(file)
        # print(data)
        return data[key][value]

class TestCalculater:

    # 这是加的数据源
    data_add:list = get_data('add')
    # print(data_add)
    # 这是除的数据源
    data_div:list = get_data('div')
    # 这是乘的数据源
    data_mul:list = get_data('mul')
    # 这是减得数据源
    data_sub:list = get_data('sub')
    def setup_class(self):
        print("开始计算机测试")
        self.calc = Calculater()
    def teardown_class(self):
        print("结束计算机测试")

    def setup_method(self):
        print("开始用例执行")

    def teardown_method(self):
        print("用例执行结束")

    # @pytest.mark.test
    # 这是一个标签
    # 数据参数化
    @pytest.mark.parametrize("a,b,answer",data_add)
    # 加法测试用例
    def test_add(self,a,b,answer):
        assert answer == self.calc.add(a,b)
        print("这是加法测试用例")
    # @pytest.mark.dev
    # 这是一个标签
    # 除法测试用例
    @pytest.mark.parametrize("a,b,answer", data_div)
    def test_div(self,a,b,answer):
        print("这是除法测试用例")
        if b == 0:
            assert(self.calc.div(a,b)==None)
        else:
            assert answer == self.calc.div(a,b)

    # 乘法测试用例
    @pytest.mark.parametrize("a,b,answer", data_mul)
    def test_mul(self,a,b,answer):
        print("这是乘法测试用例")
        assert answer == self.calc.mul(a,b)

    # 减法测试用例
    @pytest.mark.parametrize("a,b,answer", data_sub)
    def test_sub(self,a,b,answer):
        print("这是减法测试用例")
        assert answer == self.calc.sub(a,b)