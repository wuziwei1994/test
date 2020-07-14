

import  os  #文件处理的类OS
'''先来看一下当前文件路径
'''
#现在已经获取到common我们按取他的索引值为0
path = os.path.split(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0])[0]
# print(path) #D:\吉诺SAA\saa_apitest\common 已获取到，现在进行接接

#配置文件路径
conf_path = os.path.join(path,'common','conf','config.conf')
# print(conf_path) #目前的拼接出来的路径就是当前配置文件下的路径，其他路径一样的拼接

#日志文件路径
log_path = os.path.join(path,'test_log','test_log.log')
# print(log_path)

#测试用例文件路径
case_path = os.path.join(path,'test_case','test_api.xlsx') #文件名写错了，失误失误--||
# print(case_path)

#测试报告的路径
report_path = os.path.join(path,'test_result') # 方法二 报告需要改一下路径，只需要到文件夹下即可，,'test_report.html' 文件名不要了
# print(report_path)

