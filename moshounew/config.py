# 商家收购游戏币的页面(买家)
URL_POOL1 = [
        'https://www.dd373.com/s-eja7u2-0r2mut-0acvkr-67492s-0-0-jk5sj0-0-0-recycle-0-0-1-0-0-0.html', # 一区/哈霍兰(PVP)/联盟
        'https://www.dd373.com/s-eja7u2-0r2mut-ac0ct4-q7s0fm-0-0-jk5sj0-0-0-recycle-0-0-1-0-0-0.html', # 一区/辛迪加(RPPVP)/联盟
        'https://www.dd373.com/s-eja7u2-0r2mut-vjg8bk-9m9u8f-0-0-jk5sj0-0-0-recycle-0-0-1-0-0-0.html', # 一区/碧玉矿洞(普通)/联盟
    ]

# 商家出售游戏币的页面(卖家)
URL_POOL2 = [
    'https://www.dd373.com/s-eja7u2-c-jk5sj0-0r2mut-0acvkr.html', # 一区/哈霍兰(PVP)/联盟
    'https://www.dd373.com/s-eja7u2-c-jk5sj0-0r2mut-ac0ct4.html', # 一区/辛迪加(RPPVP)/联盟
    'https://www.dd373.com/s-eja7u2-c-jk5sj0-0r2mut-vjg8bk.html', # 一区/碧玉矿洞(普通)/联盟
]

BUY = 'buy'
SELL = 'sell'



HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}

# mysql本地配置
MYSQLCONFIG = {
    'host':'127.0.0.1',
    'port':3306,
    'user':'mysql',
    'passwd':'123456',
    'db':'ngf',
    'charset':'utf8',
}

# mysql测试配置
MYSQLCONFIG1 = {
    'host':'8.219.72.219',
    'port':3306,
    'user':'mysql',
    'passwd':'123456',
    'db':'ngf',
    'charset':'utf8',
}



# 多长时间获取一次数据，这里是2分钟
TIME_DELAY = 2 * 60

# 程序启动按钮
START = True

# 代理的生成API
PROXY_URL = 'http://tiqu.pyhttp.taolop.com/getip?count=1&neek=34459&type=1&yys=0&port=1&sb=&mr=1&sep=1'

# 信用等级
# 下面这个只是说明卖家等级，入库的时候，是以h1,b1,c1的形式入库的。
# DEGREE = {
#     'icon-heart': [h1, h2, h3, h4, h5],
#     'icon-bluediamond': [b1, b2, b3, b4, b5],
#     'icon-crown': [c1, c2, c3, c4, c5]
# }



