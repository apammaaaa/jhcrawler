import re
import asyncio
from concurrent.futures import ThreadPoolExecutor

def asyncrun(ls, func):
    '''
    ls: 需要遍历的列表
    func: 函数
    '''
    loop = asyncio.get_event_loop()
    tasks = []
    executor = ThreadPoolExecutor(25)
    for i in ls:
        futures = loop.run_in_executor(executor, func, i)
        tasks.append(futures)
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

def get_m3u8_ls(m3u8file):
    '''
    m3u8file: m3u8文件
    '''
    with open(m3u8file, 'r') as fp:
        t = fp.read()
    ls = re.findall(r"\n([^\n]+ts)\n", t)
    return ls
