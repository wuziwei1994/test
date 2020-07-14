
#读取配置文件的类

from configparser import ConfigParser


class ReadConfig:
    '''读取配置文件信息类'''
    def __init__(self,file_name):
        self.file_name = file_name
        self.cf = ConfigParser() #创建一个实例对象
        #读取文件
        self.cf.read(self.file_name,encoding='utf-8') #第一个参数是配置文件读取路径，第二是设置编码格式，因为内容可能为有中文

    def get_str(self,section,option):
        '''从配置文件里面获取一个字符串'''
        value = self.cf.get(section,option) #源码里面有2个参数必填 片段名 CaseId ，选项名  case_id
        return value #获取后要有返回值

    def get_int(self, section, option):
        '''从配置文件里面获取一个整数'''
        value = self.cf.getint(section, option)
        return value

    def get_float(self, section, option):
        '''从配置文件里面获取一个浮点数'''
        value = self.cf.getfloat(section, option)
        return value

    def get_boolean(self, section, option):
        '''从配置文件里面获取一个布尔值'''
        value = self.cf.getboolean(section, option)
        return value

    def get_data(self, section, option):
        '''从配置文件里面获取一个元组、列表、字典'''
        value = self.cf.get(section, option)
        return eval(value)

if __name__ == '__main__': #这是一个测试入口，在其他地方调用这个模块的时候，下面的测试代码不会被引入
    # value = ReadConfig('D:\吉诺SAA\saa_apitest\common\conf\config.conf').get_str('CaseId','case_id')  #<class 'str'>
    value = ReadConfig('D:\吉诺SAA\saa_apitest\common\conf\config.conf').get_int('CaseId', 'case_id')  #<class 'int'>
    print(value)
    print(type(value))

# 我们在excel读取的地方去调用配置文件，根据配置文件获取指定 的用例数据
