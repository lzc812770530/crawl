import aiohttp
import asyncio
import time
import threading
import re
import datetime
import pymysql
from config import URL_POOL1, URL_POOL2, BUY, SELL, HEADERS, MYSQLCONFIG, MYSQLCONFIG1, TIME_DELAY, START, PROXY_URL
from util import logFile


class Crawler(threading.Thread):
    '''创建线程爬取不同的区服'''
    def __init__(self, url, *args, **kwargs):
        super(Crawler, self).__init__()
        self.url = url
        self.flag = args[0]


    def run(self):
        '''循环进行爬取，每5分钟爬取一次'''
        while START:
            # proxy = asyncio.run(self.getProxy())
            html = asyncio.run(self.req())
            if html:
                if self.flag == 'buy':
                    gname, data = self.parseHtmlBuy(html)
                    self.connectDBBuy(gname, data)
                elif self.flag == 'sell':
                    gname, data = self.parseHtmlSell(html)
                    self.connectDBSell(gname, data)


            time.sleep(TIME_DELAY)




    def parseHtmlBuy(self, html):
        '''买方页面解析'''
        gname = re.findall('<span class="color999">(.*?)</span>.*?<span class="color999">条</span>', html, re.S)
        gname = gname[0].split('-')
        gname = gname[1] + '/' + gname[2] + '/' + gname[3]

        data = re.findall('<span class="font12 colorFF5">(.*?)</span>.*?<span class="font12 colorFF5">(.*?)</span>.*?'
                          '<p class="font12 colorFF5 m-t9 clear">(.*?)</p>.*?<p class="font12 color666 m-t9">(.*?)</p>.*?'
                          '<span class="font12 colorFF5 f-left">(.*?)</span>.*?<span class="font12 color999 f-left">起收≥</span>.*?'
                          '<span class="font12 color666 f-left">(.*?)</span>.*?<span class="font12 color999 f-left">最高≤</span>.*?'
                          '<span class="font12 color666 f-left">(.*?)</span>.*?<div class="buy-number-box" id="(.*?)">',
                          html, re.S)
        return gname, data





    def parseHtmlSell(self, html):
        '''卖方页面解析'''
        gname = re.findall('<a class="font12 color666" target="_blank" href="/s-eja7u2.html">魔兽世界燃烧的远征</a>.*?'
                       '<a class="font12 color666" target="_blank" .*?>(.*?)</a>.*?'
                       '<a class="font12 color666" target="_blank" .*?>(.*?)</a>.*?'
                       '<a class="font12 color666" target="_blank" .*?>(.*?)</a>',
                           html, re.S)
        gname = str.join('/', gname[0])

        data = re.findall('<div class="game-account-flag">.*?</i>(.*?)</div>.*?'
                          '信用等级：</span>(.*?)</p>.*?'
                          '<span class="font12">(.*?)</span>.*?'
                          '<p class="font12 colorFF5">(.*?)</p>.*?'
                          '<p class="font12 color666 m-t5">(.*?)</p>', html, re.S)
        # 对网页数据进行初步过滤。
        datas = []
        for i in data:
            danbao = re.sub(r'\s+', '', i[0])
            xinyong = re.sub(r'\s+', '', i[1])
            kucun = re.sub(r'\s+', '', i[2])
            proportion1 = re.sub(r'\s+', '', i[3])
            proportion2 = re.sub(r'\s+', '', i[4])
            l = [danbao, xinyong, kucun, proportion1, proportion2]
            datas.append(l)


        # 这里循环是为了筛选掉等级为一个心形或者交易的金在10000以下的交易商品，并且只取前7条记录入库，并且对等级进行处理。
        l1 = []
        for i in datas:
            coin = int(i[0].split('金')[0])
            count_heart = i[1].count('icon-heart')
            count_bluediamond = i[1].count('icon-bluediamond')
            count_crown = i[1].count('icon-crown')
            if count_heart == 1 and coin < 10000:
                continue
            elif len(l1) < 7:
                # 下面的判断是对等级字段进行入库的时候进行的处理，
                # 心形就是h1,h2,h3,h4,h5,钻石就是b1,b2,b3,b4,b5,皇冠就是c1,c2,c3,c4,c4
                if count_heart > 1:
                    i[1] = '心形' + str(count_heart)
                if count_bluediamond >= 1:
                    i[1] = '蓝钻' + str(count_bluediamond)
                if count_crown >= 1:
                    i[1] = '皇冠' + str(count_crown)
                l1.append(i)


        return gname, l1





    def connectDBBuy(self, *args, **kwargs):
        '''买方数据入库'''
        # print('爬买方数据')
        gname, datas = args[0], args[1]
        db = pymysql.connect(**MYSQLCONFIG1)
        cursor = db.cursor()
        try:
            for data in datas:
                duration_time = re.sub(r'\s+', '', data[0])  # 交易时间
                proportion1 = re.sub(r'\s+', '', data[2]) # 比例1
                proportion2 = re.sub(r'\s+', '', data[3]) # 比例2
                quantity = int(re.sub(r'\s+', '', data[4])) # 数量
                minnum = int(re.sub(r'\s+', '', data[5][:-1])) # 最低数量
                maxnum = int(re.sub(r'\s+', '', data[6][:-1])) # 最高数量
                gid = re.sub(r'\s+', '', data[7]) # 用户ID

                # 先查询是否有商家的记录，如果没有就直接插入，如果有就更新商家的数据。
                sql = "select gid from gamecoinbuyrecord where gid='{}' and gname='{}';".format(gid, gname)
                count = cursor.execute(sql)
                # print(count)
                if count >= 1:
                    sql1 = "update gamecoinbuyrecord set duration_time='{}', proportion1='{}', " \
                          "proportion2='{}', quantity='{}', minnum={}, maxnum={} WHERE gid='{}' and gname='{}';"\
                        .format(duration_time, proportion1, proportion2, quantity, minnum, maxnum, gid, gname)
                    cursor.execute(sql1)
                    # print('更新数据成功')
                elif count == 0:
                    sql2 = "insert into gamecoinbuyrecord set gname='{}', duration_time='{}', proportion1='{}', " \
                           "proportion2='{}', quantity='{}', minnum='{}', maxnum='{}', gid='{}';"\
                        .format(gname, duration_time, proportion1, proportion2, quantity, minnum, maxnum, gid)
                    cursor.execute(sql2)
                    # print('插入数据成功')
                db.commit()
        except Exception as e:
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            msg = "[{}    数据入库失败:]      ".format(time) + str(e) + '\n'
            asyncio.run(logFile(msg, self.flag))
        finally:
            cursor.close()
            db.close()






    def connectDBSell(self, *args, **kwargs):
        '''卖方数据入库'''
        # print('爬卖方数据')
        gname, datas = args[0], args[1]
        db = pymysql.connect(**MYSQLCONFIG1)
        cursor = db.cursor()
        try:
            for data in datas:

                danbao = data[0]
                degree = data[1]
                inventory = int(data[2])
                proportion1 = data[3]
                proportion2 = data[4]
                timeadd = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                sql = "insert into gamecoinsellrecord set gname='{}', danbao='{}', degree='{}', inventory='{}'," \
                      "proportion1='{}', proportion2='{}', timeadd='{}';"\
                    .format(gname, danbao, degree, inventory, proportion1, proportion2, timeadd)

                cursor.execute(sql)
                db.commit()
                # print('数据库入库成功')
        except Exception as e:
            # print('数据入库失败')
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            msg = "[{}    数据入库失败:]      ".format(time) + str(e) + '\n'
            asyncio.run(logFile(msg, self.flag))
        finally:
            cursor.close()
            db.close()





    async def getProxy(self):
        '''异步获取代理IP'''
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(PROXY_URL) as resp:
                    if resp.status == 200:
                        proxy = await resp.text()
                        proxy = "http://" + proxy
                        return proxy
            except Exception as e:
                time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                msg = "[{}    获取代理失败:]      ".format(time) + str(e) + '\n'
                asyncio.run(logFile(msg, self.flag))



    # async def req(self, proxy):
    async def req(self):
        '''异步发送请求的函数，发送后异步获取响应'''
        async with aiohttp.ClientSession() as session:
            # async with session.get(self.url, headers=HEADERS, proxy=proxy) as response:
            try:
                async with session.get(self.url, headers=HEADERS) as response:
                    if response.status == 200:
                        html = await response.text()
                        return html
                    else:
                        return ''
            except Exception as e:
                time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                msg = "[{}    页面请求失败:]      ".format(time) + str(e) + '\n'
                asyncio.run(logFile(msg, self.flag))




def main(thread_pool, url_pool, flag):

    for url in url_pool:
        t = Crawler(url, flag)
        thread_pool.append(t)

    for t in thread_pool:
        t.start()
        time.sleep(5)

    for t in thread_pool:
        t.join()






if __name__ == '__main__':

    thread_pool_buy = []
    thread_pool_sell = []

    # 买卖方的页面同时爬取，创建两个主线程
    t1 = threading.Thread(target=main,args=(thread_pool_buy, URL_POOL1, BUY))
    t2 = threading.Thread(target=main,args=(thread_pool_sell, URL_POOL2, SELL))
    t1.start()
    t2.start()
    t1.join()
    t2.join()







