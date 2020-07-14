
import unittest
from common.publice.log import Log #引入日志类
from common.publice import project_path #引入路径模块
from common.publice.read_config import ReadConfig #引入读取配置文件类
from common.publice.do_excel import Do_Excel #引入读取测试用例类
from ddt import ddt,data #引入DDT进行参数化
from common.publice.http_request import HttpRequest

#读取测试用例
test_data = Do_Excel(project_path.case_path,'login').read_data('LoginCaseId')
log = Log() #日志记录


@ddt #装饰测试用例
class Test_Login(unittest.TestCase):#模块、类、函数名都要test开头，否则不会执行 这是python默认规则，也可以自己修改规则，自行百度扩展
    '''登录测试'''
    def setUp(self) : #相关于预置条件
        log.info('------------开始执行测试----------')
        try:
            '''创建写入测试用例的对象，用来回写测试结果'''
            self.t = Do_Excel(project_path.case_path,'login')
        except Exception as e :
            log.error('测试用例文件打开失败{}'.format(e))
            raise e
    def tearDown(self) :#相当于测试完的清场工作，可用，可不用，为了好看，我就用了，一般可用于，如为了下次测试，需要清数据的时候
        log.info('------------测试结束-------------')

    @data(*test_data)
    def test_login(self,case):#使用case 作为接收参数数据的变量名
        global TestResult
        #获取测试参数，根据key取值
        url = case['Url']
        param = eval(case['Param']) #eval 转成字典
        method = case['Method']
        header = eval(case['Headers'])
        log.info('正在执行{}模块第{}条用例:{}'.format(case['Module'],case['CaseId'],case['Title']))
        log.info('测试数据是:{}'.format(param))


        #发起请求，开始测试
        try:
            resp = HttpRequest().http_request(url=url,param=param,method=method,header=header)
            print(type(resp))
            log.info('{}模块第{}条用例的测试返回结果:{}'.format(case['Module'],case['CaseId'],resp.text)) #resp.text 是str类型
        except Exception as e:
            log.error('{}模块第{}条用例的接口请求错误，错误是:{}'.format(case['Module'],case['CaseId'],e))
            raise e

        #断言并讲测试结果写回excel中
        try:
            self.assertEqual(resp.json()['msg'],eval(case['ExpectedResult'])['msg'])  #判断 实际结果和预期结果是否相等
            # #因为每次的响应结果都不一样，所以，我这边只获取他的一个msg
            # #这是预期结果的值：如
            # a = {'phone':'15382876192','msg':'获取成功'}
            # #这是实际的返回响应结果
            # b = {'phone':'18978546292','msg':'获取成功'}
            # #判断他们2个是否相等，就取相同的key msg  assertEqual（a,b）判断是否相等
            # #resp.json() 是因为获取到是json格式的返回结果才是dict，才能取到key ：msg
            log.info('预期结果与实际测试结果一致！')
            TestResult = 'pass' #定义一个变量，如果一致就pass
        except Exception as e :
            TestResult = 'failed'
            log.error('预期结果与实际测试结果不一致！')
            log.error('{}模块第{}条用例的返回测试结果:{}'.format(case['Module'], case['CaseId'],e)) #这个不要也可以，要的话好定位
            # log.info('{}模块第{}条用例的预期结果:{}'.format(case['Module'],case['CaseId'],eval(case['ExpectedResult'])) # 这个不要也可以，要的话好定位
            raise e

        finally:#不管是pass还是fail最终写入结果到excel中
            #使用前面创建的对象
            #写入测试结果
            self.t.write_back(case['CaseId']+1,9,resp.text) #写入结果要text  参数1是行，参数2 是列 ，参数3是写入的值 9是列数一下，测试结果在第几列
            # 行 当我们要写入caseId为1的用例结果时，我们的这条用例 是在第二行，caseId为2时，用例实际是在第三行，标题是第1行，所以要加1
            self.t.write_back(case['CaseId']+1,10,TestResult)#写入测试结果 pass fail
        #记录是pass还是fail，
        log.info('{}模块第{}条用例的测试结果是:{}'.format(case['Module'], case['CaseId'], TestResult))






