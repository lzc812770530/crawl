import aiohttp
import asyncio
import time
import threading
import re
import pymysql
from config import URL_POOL1, HEADERS, MYSQLONFIG, TIME_DELAY, START


class Crawler(threading.Thread):
    '''创建线程爬取不同的区服'''
    def __init__(self, url, *args, **kwargs):
        super(Crawler, self).__init__()
        self.url = url


    def run(self):
        while START:
            html = asyncio.run(self.req())
            if html:
                gname, data = self.parseHtml(html)
                self.connectDB(gname, data)


            time.sleep(TIME_DELAY)




    def parseHtml(self, html):
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



    def connectDB(self, *args, **kwargs):
        gname, datas = args[0], args[1]
        db = pymysql.connect(**MYSQLONFIG)
        cursor = db.cursor()
        try:
            for data in datas:
                # sql = "insert into gamecoindealrecord set gname='{}', duration_time='{}', " \
                #       "proportion1='{}', proportion2='{}', quantity='{}', minnum={}, maxnum={}, gid='{}';"\
                #     .format(gname, data[0], data[2], data[3], int(data[4]), int(data[5][:-1]), int(data[6][:-1]), data[7])
                # 先查询是否有商家的记录，如果没有就直接插入，如果有就更新商家的数据。
                sql = "insert into gamecoindealrecord(gname, duration_time,proportion1, proportion2, quantity, minnum, maxnum, gid) " \
                       "select '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}' from gamecoindealrecord " \
                       "where not exists (select * from gamecoindealrecord where gid='{}') limit 1;"\
                    .format(gname, data[0], data[2], data[3], int(data[4]), int(data[5][:-1]), int(data[6][:-1]), data[7], data[7])
                count = cursor.execute(sql)
                if count == 0:
                    sql1 = "update gamecoindealrecord set gname='{}', duration_time='{}', proportion1='{}', " \
                          "proportion2='{}', quantity='{}', minnum={}, maxnum={} WHERE gid = '{}';"\
                        .format(gname, data[0], data[2], data[3], int(data[4]), int(data[5][:-1]), int(data[6][:-1]), data[7])
                    cursor.execute(sql1)
                    print('更新数据成功')
                else:
                    print('插入数据成功')
                db.commit()
        # except Exception as e:
        #     pass
            # print(e)
            # print('数据入库失败')
        finally:
            cursor.close()
            db.close()



    async def req(self):
        '''异步发送请求的函数，发送后异步获取响应'''
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url, headers=HEADERS) as response:
                if response.status == 200:
                    html = await response.text()
                    return html
                else:
                    return ''




if __name__ == '__main__':
    headers3 = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    }


    thread_pool = []


    for url in URL_POOL1:
        t = Crawler(url)
        thread_pool.append(t)

    for t in thread_pool:
        t.start()
        time.sleep(0.5)

    for t in thread_pool:
        t.join()



