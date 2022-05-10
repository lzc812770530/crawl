import scrapy
from ..items import *

class MymoshouSpider(scrapy.Spider):
    name = 'mymoshou'
    allowed_domains = ['dd373.com']
    start_urls = ['https://www.dd373.com/s-eja7u2-ht6h6g-8kttb0-uq3wwt-0-0-jk5sj0-0-0-recycle-0-0-1-0-0-0.html']

    def parse(self, response,**kwargs):
        gname = response.xpath('//div[@class="current-right-box"]/a/h1/span/text()').get().split('-')[1:4]
        gname1 = '-'.join(gname)
        rusult = response.text
        ul_list = response.xpath('//div[@class="platform-receive-content"]/ul')
        for ul in ul_list:
            duration_time = ul.xpath('./li[@class="width185 p-l6"]/p/span[@class="font12 colorFF5"]/text()').get() # 平常时长的时间
            proportion1 = ul.xpath('./li[@class="width198"]/p[@class="font12 colorFF5 m-t9 clear"]/text()').get() # 比例
            proportion2 = ul.xpath('./li[@class="width198"]/p[@class="font12 color666 m-t9"]/text()').get()  # 比例
            quantity = ul.xpath('./li[@class="width185 p-l40"]/p/span[@class="font12 colorFF5 f-left"]/text()').get() # 收货数量
            price_min = ul.xpath('./li[@class="width185 p-l40"]/p[@class="line-height14 m-t9"]/span/text()')[1].get() # 最低收货
            price_max = ul.xpath('./li[@class="width185 p-l40"]/p[@class="line-height14 m-t9"]/span/text()')[3].get() # 最高收货
            gid = ul.xpath('./li[@class="width310 p-l40"]/div/@id').get()
            yield MoshouItem(
                gid=gid,
                gname=gname1,
                duration_time=duration_time,
                proportion1=proportion1,
                proportion2=proportion2,
                quantity=quantity,
                price_min=price_min,
                price_max=price_max
            )