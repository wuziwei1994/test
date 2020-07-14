# -*- coding: utf-8 -*-
# File   :   http_request.PY
# Author :   tenghaiqin
# DATA   ：  2020/3/13 0013

#可以根据传的method、get\postp完成 不同的请求，
import requests
from common.publice.log import Log

log = Log() #创建日志实例


class HttpRequest:
    '''创建一个http的接口请求类'''
    def http_request(self,url,param,header=None,method='get'):
        if method.upper()=='GET':
            try:
                res = requests.get(url,params=param,headers=header)
            except Exception as e:
                log.error('请求错误{}'.format(e))
                raise e
        elif method.upper()=='POST':
            try:
                res = requests.post(url,json=param,headers=header)
            except Exception as e:
                log.error('请求错误{}'.format(e))
                raise e
        else:
            log.error('请求方法错误{}'.format(method))
            res = None
        return res

if __name__ == '__main__':
    url = "http://testssr.saa.com.cn/loginRequest"
    header={"Content-Type":"application/json; charset=UTF-8",}
    param = {"url":"/oauth/token?username=test1&password=123456&grant_type=password"}
    res = HttpRequest().http_request(url, param,method='post',header=header)
    # print(res.json())
    print(res.text)

    # #车辆管理 /carInfo/findByPage? 车辆管理分页查询接口
    url2="http://testssr.saa.com.cn/postRequest"
    header2={"Content-Type":"application/json; charset=UTF-8"}
    param2={"path":"client","url":"/carInfo/findByPage?pageIndex=1&pageSize=50",
            "params":{"carNo":"",#车牌号码
                      "carServiceBelong":None,
                      "companyId":136,
                      "carBrand":"",
                      "carTypeId":"",
                      "gpsDeviceNo":"",
                      "parkingId":"",
                      "dateList":[],
                      "startUpdatedDate":"",
                      "endUpdatedDate":"",
                      "carStatus":1,"pageIndex":1,
                      "pageSize":50,"isLease":"","leaseType":""},
            "name":"b8142069a29e8024940cb8fd6224542b"}
    res2 = HttpRequest().http_request(url2, param2,method='post',header=header2)
    print(res2.json())

    #测试一下是没问题,所以再看一下是哪里错了