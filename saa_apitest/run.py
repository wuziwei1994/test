# -*- coding: utf-8 -*-
# File Name：   run.py
# Author   :  tenghaiqin
# Date     ：  2020/3/14 0014
# Email    : haiqinteng@saa.com.cn

import  unittest
from test_case import test_login #引入测试用例模块
from test_case import test_carInfo
from common.publice import project_path
import HTMLTestRunnerNew
from BeautifulReport import BeautifulReport


#测试集对象
suite = unittest.TestSuite()

#加载用例
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(test_login)) #单个添加测试用例 使用的是导入模块
# suite.addTest(loader.loadTestsFromModule(test_carInfo))



# 执行测试,并生成测试报告 使用 HTMLTestRunnerNew  方法一
# with open(project_path.report_path,'wb') as file:
#     runner  = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
#                                                verbosity=2,
#                                                title='20200314的接口测试报告',
#                                                description='这是一个注释呢',
#                                                tester='测试员滕海琴')
#     runner.run(suite)



# 一个好看的测试报告模板 可视化测试报告 pip BeautifulReport 并引入 方法二
# from BeautifulReport import BeautifulReport
result = BeautifulReport(suite)
result.report(description= '20200316自动化测试报告', filename= 'test_report', report_dir=project_path.report_path)
'''report_dir:路径 只到文件夹下
filename :文件名，不需要后缀
descriptio：描述，说明'''
#把之前的报告删除，看看是否生成  现在来运行看一下  报告已生成