# coding:utf-8
import time
import os


def locattime():
    """ 返回当前时间，格式%Y-%m-%d %H:%M:%S """
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def locatdate():
    """ 返回当前日期，格式%Y-%m-%d """
    return time.strftime("%Y-%m-%d", time.localtime())

    
def cat(path, encoding='utf-8'):
    """ 同linux下的cat """
    import codecs
    file = codecs.open(path, encoding=encoding, errors='ignore')
    text = file.read()
    file.close()
    return text


def sql_remove_comments(text):
    """ sql中有--注释，直接带入可能会不识别，通过此方法去掉注释 """
    sql = ''
    for line in text.split('\n'):
        if '--' in line:
            sql_line = line.split('--')[0]
        else:
            sql_line = line
        sql = sql + ' ' + sql_line
    sql = spacesmerge(sql.replace('\n',' '))
    return sql


def echo(text, path, mode='a'): 
    """ 把text输出到指定路径文件，不存在会创建（包括文件夹），mode默认是a，表示追加写，设为w表示覆写 """
    try:
        mkdir(os.path.dirname(path))
    except:
        pass
    path = path.replace('\u202a', '')
    file = open(path, mode, encoding='utf-8', errors='ignore')
    file.write(str(text) + '\n')
    file.close()
    
    
def mkdir(path):
    """ 不存在则创建文件夹，逐层创建 """
    if not os.path.exists(path):
        os.makedirs(path)

        
def rm(path):
    """ 同linux下的rm -rf """
    import shutil
    path = path.replace('\\', '/')
    if os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)


def spacesmerge(s):
    """ 空格合并，直到不存在多个连续空格 """
    s2 = ''
    for line in s.split('\n'):
        s2 = s2 + ' '.join(line.split()) + '\n'
    return s2.strip()


def nvl(strVal, defaultVal):
    """ 同Oracle下的nvl """
    if strVal is None or strVal == '':
        return defaultVal
    else:
        return strVal
    
    
def round_(num, format_):
    """ round无异常 """
    import builtins
    try:
        return builtins.round(num, format_)
    except:
        return None


def timeformat(timeStr, srcformat, dstformat):
    """ 自由的时间格式转换
    %y 两位数的年份表示（00-99）
    %Y 四位数的年份表示（000-9999）
    %m 月份（01-12）
    %d 月内中的一天（0-31）
    %H 24小时制小时数（0-23）
    %I 12小时制小时数（01-12）
    %M 分钟数（00-59）
    %S 秒（00-59）
    %a 本地简化星期名称
    %A 本地完整星期名称
    %b 本地简化的月份名称
    %B 本地完整的月份名称
    %c 本地相应的日期表示和时间表示
    %j 年内的一天（001-366）
    %p 本地A.M.或P.M.的等价符
    %U 一年中的星期数（00-53）星期天为星期的开始
    %w 星期（0-6），星期天为 0，星期一为 1，以此类推。
    %W 一年中的星期数（00-53）星期一为星期的开始
    %x 本地相应的日期表示
    %X 本地相应的时间表示
    %Z 当前时区的名称
    %% %号本身 """
    import datetime
    return datetime.datetime.strptime(timeStr, srcformat).strftime(dstformat)


class Log():
    """ 简单的日志类 """

    def __init__(self, filepath):
        self.filepath = filepath

    def info(self, *text):
        print(locattime(), 'info', str(text))
        echo((locattime(), 'info', str(text)), self.filepath)
        
    def warning(self, *text):
        print(locattime(), 'warning', str(text))
        echo((locattime(), 'warning', str(text)), self.filepath)
        
    def error(self, *text):
        print(locattime(), 'error', str(text))
        echo((locattime(), 'error', str(text)), self.filepath)
        

def zipfolder(dirpath, outFullName):
    """ 压缩指定文件夹
    :param dirpath: 目标文件夹路径
    :param outFullName: 压缩文件保存路径+xxxx.zip
    :return: 无
    """
    import zipfile
    zip_ = zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED)
    for path, _, filenames in os.walk(dirpath):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dirpath, '')

        for filename in filenames:
            zip_.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zip_.close()

    
def linemergealign(str_1, str_2, iscompare=False):
    """ 两个字符串的同一行合并成新的一行，并且对齐（用于方便左右比较）
    iscompare为真时，左右不一致会在最右边提示*号 """
    str1s = str_1.split('\n')
    str2s = str_2.split('\n')
    strlennum = 0  # 最大字符长度
    for str_ in str1s:
        if strlennum < len(str_):
            strlennum = len(str_)
    for str_ in str2s:
        if strlennum < len(str_):
            strlennum = len(str_)
    linenum = len(str1s) if len(str1s) > len(str2s) else len(str2s)  # 最大行数
    str_ = ''
    for idx in range(0, linenum):
        try:
            str1 = str1s[idx]
        except:
            str1 = ''
        try:
            str2 = str2s[idx]
        except:
            str2 = ''
        if iscompare:
            if spacesmerge(str1.strip()) != spacesmerge(str2.strip()):
                str_ = str_ + str1 + ' ' * (strlennum - len(str1) + 1) + str2 + '\t*\n'
            else:
                str_ = str_ + str1 + ' ' * (strlennum - len(str1) + 1) + str2 + '\n'
        else:
            str_ = str_ + str1 + ' ' * (strlennum - len(str1) + 1) + str2 + '\n'
    return str_.strip()
