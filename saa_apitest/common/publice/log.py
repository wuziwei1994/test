
#创建一个日志类
import logging
from common.publice import project_path #引入路径模块

class Log:

    def log(self,level,msg):
        '''level：日志等级
        msg:日志信息'''
        logger = logging.getLogger('saa接口自动化')#接口自动化日志收集器名称
        logger.setLevel('DEBUG') #设置默认日志等级  debug-info-warning-error-critical

        #设置日志输出格式
        formatter = logging.Formatter('[%(asctime)s]-[%(levelname)s]-%(filename)s-%(name)s-[日志信息]:%(message)s')

        ch = logging.StreamHandler() #输出到控制台
        ch.setLevel('INFO')#设置等级
        ch.setFormatter(formatter) #设置日志格式

        fh = logging.FileHandler(project_path.log_path,encoding='utf-8') #日志文件存在 路径 ，设置编码格式
        fh.setFormatter(formatter)
        fh.setLevel('INFO')

        #添加输出渠道
        logger.addHandler(ch)
        logger.addHandler(fh)

        if level == 'DEBUG':
            logger.debug(msg)
        elif level == 'INFO':
            logger.info(msg)
        elif level == 'WARNING':
            logger.warning(msg)
        elif level == 'ERROR':
            logger.error(msg)
        else:
            logger.critical(msg)

        #移除渠道
        logger.removeHandler(fh)
        logger.removeHandler(ch)

    def debug(self,msg):
        self.log('DEBUG',msg) #调用 上面的log方法，进行传等级参数
    def info(self,msg):
        self.log('INFO',msg)
    def warning(self,msg):
        self.log('WARNING',msg)
    def error(self,msg):
        self.log('ERROR',msg)
    def critical(self,msg):
        self.log('CRITICAL',msg)

if __name__ == '__main__':
    Log().debug('这是一个debug的日志记录') #为什么没有输出到控制台？也没有输出到日志文件呢？
    Log().info('这是一个info的日志记录') #因为，设置的等级是INFO，所以低于info的等级的日志不会输出，日志类已经写好，接下来，运行起来

