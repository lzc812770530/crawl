# coding=utf-8
import requests
import re
import base64
import hashlib



def req(url, headers):
    try:
        # proxy = [
        #     'http:///125.77.166.138:59394'
        # ]
        resp = requests.get(url, headers=headers)
        return resp
    except:
        print("获取数据失败")


def dealData(text):
    gname = re.findall('<span class="color999">(.*?)</span>.*?<span class="color999">条</span>',text,re.S)

    data = re.findall('<span class="font12 colorFF5">(.*?)</span>.*?<span class="font12 colorFF5">(.*?)</span>.*?'
                      '<p class="font12 colorFF5 m-t9 clear">(.*?)</p>.*?<p class="font12 color666 m-t9">(.*?)</p>.*?'
                      '<span class="font12 colorFF5 f-left">(.*?)</span>.*?<span class="font12 color999 f-left">起收≥</span>.*?'
                      '<span class="font12 color666 f-left">(.*?)</span>.*?<span class="font12 color999 f-left">最高≤</span>.*?'
                      '<span class="font12 color666 f-left">(.*?)</span>.*?<div class="buy-number-box" id="(.*?)">',text,re.S)




def dealParams(params):

    d_sort = sorted(params.items(), key=lambda x:x[0]) # 对字典的键进行ascii排序
    print(d_sort)
    md5Source = ''
    for key, value in d_sort:
        if value:
            value = value.encode('utf-8')
            bs64value = base64.b64encode(value)
            value64str = str(bs64value, encoding='utf-8')
            md5Source += key + value64str
    md5Source += "jishiyu110dd373"
    md5Code = hashlib.md5(md5Source.encode(encoding='utf-8')).hexdigest()
    md5Code = md5Code.replace("-","")
    print(md5Code)

    params1 = {
        'GameCategory': str(base64.b64encode('6be4ca9f242f4541955f64e6ae17ca30'.encode('utf-8')),encoding='utf-8'),
        'UserName': str(base64.b64encode('Phone15397342953'.encode('utf-8')), encoding='utf-8'),
        'TotalNum': str(base64.b64encode('10000'.encode('utf-8')), encoding='utf-8'),
        'MinNum': str(base64.b64encode('1000'.encode('utf-8')), encoding='utf-8'),
        'SinglePrice': str(base64.b64encode('0.0004'.encode('utf-8')), encoding='utf-8'),
        'State': str(base64.b64encode('1'.encode('utf-8')), encoding='utf-8'),
        'ShopType': str(base64.b64encode('61b65070243c4453b653fa82c8b39bd1'.encode('utf-8')), encoding='utf-8'),
        'Sign': md5Code,
    }
    return params1






def reqpost():
    url = 'https://goods.dd373.com/Api/SDK/NeedReceiveShopUpdate'
    # params = {
    #     'GameCategory':str(base64.b64encode('0r2muta8fda3f1-33c9-41c2-bd98-3fc94d0659d3'.encode('utf-8')), encoding='utf-8'),
    #     'UserName':str(base64.b64encode('Phone15397342953'.encode('utf-8')), encoding='utf-8'),
    #     'TotalNum':str(base64.b64encode('9999'.encode('utf-8')), encoding='utf-8'),
    #     'MinNum':str(base64.b64encode('999'.encode('utf-8')), encoding='utf-8'),
    #     'SinglePrice':str(base64.b64encode('0.0004'.encode('utf-8')), encoding='utf-8'),
    #     'State':str(base64.b64encode('1'.encode('utf-8')), encoding='utf-8'),
    #     'ShopType': str(base64.b64encode('61b65070243c4453b653fa82c8b39bd1'.encode('utf-8')), encoding='utf-8'),
    # }

    params1 = {
        'GameCategory': '6be4ca9f242f4541955f64e6ae17ca30',
        'UserName': 'Phone15397342953',
        'TotalNum': '9999',
        'MinNum': '999',
        'SinglePrice': '0.0004',
        'State': '1',
        'ShopType': '61b65070243c4453b653fa82c8b39bd1',
        # 'NumUnit': '',
        # 'MaxNum': '',
    }

    params = dealParams(params1)
    print(params)

    try:
        resp = requests.post(url, headers=headers3, data=params)
        print(resp.text)
    except:
        print('请求失败')





if __name__ == '__main__':
    urls = [
        'https://www.dd373.com/s-eja7u2-0r2mut-0acvkr-67492s-0-0-jk5sj0-0-0-recycle-0-0-1-0-0-0.html',
        'https://www.dd373.com/s-eja7u2-0r2mut-vjg8bk-9m9u8f-0-0-jk5sj0-0-0-recycle-0-0-1-0-0-0.html',
        'https://www.dd373.com/s-eja7u2-0r2mut-ac0ct4-q7s0fm-0-0-jk5sj0-0-0-recycle-0-0-1-0-0-0.html',
    ]
    # headers1 = {
    #     ':authority': 'game.dd373.com',
    #     ':method': 'POST',
    #     ':path': '/Api/Game/GetGameInfoListByIds',
    #     ':scheme': 'https',
    #     'accept': '*/*',
    #     'accept-encoding': 'gzip, deflate, br',
    #     'accept-language': 'zh-CN,zh;q=0.9',
    #     'content-length': '951',
    #     'content-type': 'application/json',
    #     'cookie': 'member_session=; firstOpen_cc=true; Hm_lvt_b1609ca2c0a77d0130ec3cf8396eb4d5=1650259881,1650269519,1652062006;Hm_lpvt_b1609ca2c0a77d0130ec3cf8396eb4d5=1652063521;SERVERID=705e1e1067b40e3f7050790d3e23600c1652063532|1652062018',
    #     'origin': 'https://www.dd373.com',
    #     'referer': 'https://www.dd373.com/s-eja7u2-0r2mut-ac0ct4-q7s0fm-0-0-jk5sj0-0-0-recycle-0-0-1-0-0-0.html',
    #     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    #     'sec-ch-ua-mobile': '?0',
    #     'sec-ch-ua-platform': '"Windows"',
    #     'sec-fetch-dest': 'empty',
    #     'sec-fetch-mode': 'cors',
    #     'sec-fetch-site': 'same-site',
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    # }
    #
    # headers2 = {
    #     ':authority': 'www.dd373.com',
    #     ':method': 'GET',
    #     ':path': '/s-eja7u2-0r2mut-ac0ct4-q7s0fm-0-0-jk5sj0-0-0-recycle-0-0-1-0-0-0.html',
    #     ':scheme': 'https',
    #     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #     'accept-encoding': 'gzip, deflate, br',
    #     'accept-language': 'zh-CN,zh;q=0.9',
    #     'cache-control': 'max-age=0',
    #     'cookie': 'firstOpen_cc=true; member_session=; acw_tc=76b20fea16520620166901754e31a9dfb56452219033195683411a39e9eea1; Hm_lvt_b1609ca2c0a77d0130ec3cf8396eb4d5=1650259881,1650269519,1652062006; SERVERID=e53833d2587a4acaa22c8eb385ef8e38|1652063373|1652062016; Hm_lpvt_b1609ca2c0a77d0130ec3cf8396eb4d5=1652063362',
    #     'referer': 'https://www.dd373.com/s-eja7u2-c-jk5sj0-0r2mut-ac0ct4-q7s0fm.html',
    #     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    #     'sec-ch-ua-mobile': '?0',
    #     'sec-ch-ua-platform': '"Windows"',
    #     'sec-fetch-dest': 'document',
    #     'sec-fetch-mode': 'navigate',
    #     'sec-fetch-site': 'same-origin',
    #     'sec-fetch-user': '?1',
    #     'upgrade-insecure-requests': '1',
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    # }



    headers3 = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    }
    #
    #
    # for url in urls:
    #     resp = req(url, headers3)
    #     data = dealData(resp)

    # url = 'https://www.dd373.com/s-eja7u2-0r2mut-ac0ct4-q7s0fm-0-0-jk5sj0-0-0-recycle-0-0-1-0-0-0.html'
    # resp = req(url, headers3)
    # print(resp.text)






    t1 = '''
<!DOCTYPE html>
<html>
<head>
    <meta name="referrer" content="always">
    <meta charset="utf-8">
    <meta name="format-detection" content="telephone=no">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <title>WOW怀旧服魔兽世界燃烧的远征游戏币交易平台-游戏币交易比例-DD373.COM</title>
    <meta name="description" content="WOW怀旧服魔兽世界燃烧的远征游戏币交易平台，游戏帐号，找回包赔帐号，游戏币，点卡，低折扣月卡，超值游戏币、极品帐号，DD373不只提高你的战斗力!">
    <meta name="keywords" content="WOW怀旧服魔兽世界燃烧的远征游戏币交易平台,游戏币装备帐号交易">
    <link href="//cdnimg.dd373.com/file/general/images/favicon.ico" rel="shortcut icon">
    <link rel="stylesheet" href="//sta.dd373.com/newfile/common/stlye/common.css">
    <link rel="stylesheet" href="//sta.dd373.com/file/general/Css/idangerous.swiper.css">
    <link rel="stylesheet" href="//sta.dd373.com/newfile/common/style/default/common_sprite.css">
    <link rel="stylesheet" href="//sta.dd373.com/newfile/common/style/default/icon_sprite.css">
    <link rel="stylesheet" href="//sta.dd373.com/newfile/common/style/default/common_style.css">
    <link rel="stylesheet" href="//sta.dd373.com/newfile/common/style/default/footer_icons.css">
    <link rel="stylesheet" href="//sta.dd373.com/newfile/common/stlye/right_hover.css">
    
    <link rel="stylesheet" href="//sta.dd373.com/newfile/goods/style/default/goods_comm.css">
    <link rel="stylesheet" href="//sta.dd373.com/newfile/goods/style/default/goods_list_sprite.css">
    <link rel="stylesheet" href="//sta.dd373.com/newfile/common/style/default/page_pagination.css">
    <link rel="stylesheet" href="//sta.dd373.com/newfile/goods/style/default/goods_list.css">

</head>
<body>
    <div class="header">

        <!--顶部菜单-->
        <div class='top'><div class='row'><ul class='fr menu-wrap' id='topMenus'><li class='item'><a href='//www.dd373.com/' ><span style=' '>DD373首页</span></a><span class='right-line'></span></li><li class='item'><a href='//order.dd373.com/usercenter/order_details.html'target='_blank' ><span style='color:#FF5B01 '>订单聊天</span></a><span class='right-line'></span></li><li class='item'><a href='//newuser.dd373.com/usercenter/index.html'target='_blank' class='two-select-menu'><span style=' '>我的DD373</span><i class='arrow'></i></a><div class='dropdown-menu'><ul class='wsn mt6'><li><a href ='https://newuser.dd373.com/usercenter/index.html'  class='b' style=' '>我是买家</a><ul class='wsn'><li><a href ='//game.dd373.com/y-0-2.html' target='_blank' class='' style=' '>我要买</a></li></ul><ul class='wsn'><li><a href ='//order.dd373.com/usercenter/buyer/buy_orders.html' target='_blank' class='' style=' '>买家订单管理</a></li></ul><ul class='wsn'><li><a href ='https://order.dd373.com/usercenter/buyer/bargain_goods_list.html' target='_blank' class='' style=' '>求降价的商品</a></li></ul><li><a href ='https://newuser.dd373.com/usercenter/index.html'  class='b' style=' '>我是卖家</a><ul class='wsn'><li><a href ='//game.dd373.com/default/sell/sell_goods.html'  class='' style=' '>我要卖</a></li></ul><ul class='wsn'><li><a href ='//order.dd373.com/usercenter/seller/sale_orders.html'  class='' style=' '>卖家订单管理</a></li></ul><ul class='wsn'><li><a href ='//goods.dd373.com/usercenter/seller/sell_goods_list.html'  class='' style=' '>卖家商品管理</a></li></ul></li></ul></div><i class='fukie'></i><span class='right-line'></span></li><li class='item'><a href='//newpay.dd373.com/usercenter/diamond_exchange.html'target='_blank' ><span style=' '>钻石兑换</span></a><span class='right-line'></span></li><li class='item'><a href='//kf.dd373.com/'target='_blank' class='two-select-menu'><span style=' '>客服中心</span><i class='arrow'></i></a><div class='dropdown-menu'><ul class='wsn '><li><a href ='//kf.dd373.com/ServiceCenter/HelpCenter'  class='' style=' '>帮助中心</a></li></ul><ul class='wsn '><li><a href ='//kf.dd373.com/ServiceCenter/SafeCenter'  class='' style=' '>安全中心</a></li></ul><ul class='wsn '><li><a href ='//kf.dd373.com/ServiceCenter/ConsultCenter'  class='' style=' '>咨询中心</a></li></ul><ul class='wsn '><li><a href ='//kf.dd373.com/ServiceCenter/AppealCenter	'  class='' style=' '>申诉中心</a></li></ul><ul class='wsn '><li><a href ='//kf.dd373.com/ServiceCenter/NoticeCenter'  class='' style=' '>公告中心</a></li></ul></div><i class='fukie'></i><span class='right-line'></span></li><li class='item'><a href='' class='two-select-menu'><span style=' '>网站导航</span><i class='arrow'></i></a><div class='dropdown-menu'><ul class='wsn mt6'><li><a href ='//www.dd373.com'  class='b' style=' '>游戏交易</a><ul class='wsn'><li><a href ='//www.dd373.com'  class='' style=' '>端游交易</a><li><a href ='//game.dd373.com/mg.html'  class='' style=' '>手游交易</a></li></ul><ul class='wsn'><li><a href ='//da.dd373.com/Account/Index'  class='' style=' '>帐号交易</a><li><a href ='//www.dd373.com/coin/index'  class='' style=' '>金币交易</a></li></ul></li></ul><ul class='wsn mt6'><li><a href =''  class='b' style=' '>特色服务</a><ul class='wsn'><li><a href ='//gift.dd373.com/GiftBag/Index'  class='' style=' '>游戏礼包</a><li><a href ='//kf.dd373.com/Information/index'  class='' style=' '>游戏资讯</a></li></ul><ul class='wsn'><li><a href ='//da.dd373.com/account/RecyclePage'  class='' style=' '>帐号回收</a><li><a href ='//www.dd373.com/Account/Valuation'  class='' style=' '>帐号估价</a></li></ul></li></ul><ul class='wsn mt6'><li><a href =''  class='b' style=' '>更多精选</a><ul class='wsn'><li><a href ='//kf.dd373.com/'  class='' style=' '>客服中心</a><li><a href ='https://point.dd373.com/default/m_club_index.html'  class='' style=' '>会员俱乐部</a></li></ul><ul class='wsn'><li><a href ='https://tg.dd373.com/default/index.html'  class='' style=' '>推广联盟</a><li><a href ='//gift.dd373.com/usercenter/cdkey_exchange.html' target='_blank' class='' style=' '>CDKEY兑换</a></li></ul><ul class='wsn'><li><a href ='//merchant.dd373.com/usercenter/management.html'  class='' style=' '>商家认证</a></li></ul></li></ul></div><i class='fukie'></i><span class='right-line'></span></li><li class='item'><a href='//cms.dd373.com/default/app_down.html'target='_blank' class='two-select-menu'><span style='color:#333 '>手机APP</span><i class='arrow'></i></a><div class='dropdown-menu'><ul class='wsn ' style='white-space:normal'><li class='code-li'><div class='code-div'><img class='db' src='//publicimg.dd373.com/Upload/2020-09-15/be563b8ae82a4bc2a06fcfdaeefcb27e.png' /></div><a href ='//cms.dd373.com/default/app_down.html' target='_blank' class='' style=';word-break:break-all'> 交易平台APP</a></li></ul></div><i class='fukie'></i></li></ul> </div ></div > 

        <!-- logo and search -->
        <div class="cont clear">
            <div class="row ovh">
                <div class="fl logo-wrap">
                    <h1>
                        <a title="嘟嘟网络游戏服务网" href=//www.dd373.com><img alt="嘟嘟网络游戏服务网" src="//publicimg.dd373.com/SitePic/2021-02-05/794c52e2078a4ef8aeb0eea81de99cbe.jpg" style="width:227px;height:100px"></a>
                    </h1>
                </div>


                <div class="fr">
                    <div class="ovh search-wrap">
                        <ul class="ovh search-tab-title">
                            <li class="fl advanced-btn active">搜商品</li>
                            <li class="fl general-btn "><a href="//dl.dd373.com/" target="_blank">搜代练</a></li>
                        </ul>
                        <div class="fl search-tab-cont">
                            <div class="advanced ovh" id="advancedGameArea">
                                <ul class="fl">
                                    <li data-leveltype="1"><span>游戏名称</span> <i class="arrow"></i></li>
                                    <li data-leveltype="2" data-lastleveltype="1"><span>商品类型</span> <i class="arrow"></i></li>
                                </ul>
                                <div class="fl input-search">
                                    <i class="icon-search"></i>
                                    <input type="text" placeholder="请输入商品编号或标题关键字" value="">
                                </div>
                                <button class="fr btn-search">搜 索</button>
                            </div>
                        </div>
                    </div>

                    <table class="ovh hot-search">
                        <tr>
                            <td class="title">热门搜索：</td>
                            <td class="hot-items">
                                <div class="elip">
                                                <a class="item" href="//www.dd373.com/s-rbg22w.html" id="7100fe84-ef8a-4f0a-8547-a8682a78e555" title="地下城与勇士" target="_blank">地下城与勇士</a>
                                                <a class="item" href="//www.dd373.com/s-e3nw98.html" id="7a091ddf-a7d4-4632-b292-10b7fe8e02b0" title="征途2S" target="_blank">征途2S</a>
                                                <a class="item" href="//www.dd373.com/s-49pbxm.html" id="7a7b84dc-74c9-441f-bb23-f3374169d4ff" title="流放之路" target="_blank">流放之路</a>
                                                <a class="item" href="//www.dd373.com/s-eja7u2.html" id="a8fda3f1-33c9-41c2-bd98-3fc94d0659d3" title="魔兽世界燃烧的远征" target="_blank">魔兽世界燃烧的远征</a>
                                                <a class="item" href="//www.dd373.com/s-u7udm8.html" id="6f5ea82514764eef8ae192eeb619635c" title="新天龙八部怀旧服" target="_blank">新天龙八部怀旧服</a>
                                                <a class="item" href="//www.dd373.com/s-5eu4fw.html" id="3abf25b6-bfd1-4c59-aaef-bf589b0f5037" title="剑灵" target="_blank">剑灵</a>
                                                <a class="item" href="//www.dd373.com/s-s9t07r.html" id="e0de2768-7b49-48d4-ba21-cef6ed2abb6e" title="永恒之塔怀旧版" target="_blank">永恒之塔怀旧版</a>
                                                <a class="item" href="//www.dd373.com/s-nc6cax.html" id="efb6e8d235ee42eb99f6d362ffe9e444" title="千古风流" target="_blank">千古风流</a>
                                                <a class="item" href="//www.dd373.com/s-qcgvm9.html" id="16b7a9a8ec164ac189f6a8648833e5bc" title="魔兽世界经典怀旧服(60)" target="_blank">魔兽世界经典怀旧服(60)</a>
                                                <a class="item" href="//www.dd373.com/s-uuuw1v.html" id="0227d060-7dff-4dcc-9317-08ee7dce7f04" title="原神" target="_blank">原神</a>
                                </div>
                            </td>
                        </tr>
                    </table>

                </div>
            </div>
        </div>
        <!-- /logo and search -->

        <div class="nav">
            <div class="row ovh">
                <!-- <div class="fl title">服务分类</div> -->
                <ul class="goods-top-left">
                                <li>
                                    <a href="//www.dd373.com/"  >首页</a>
                                </li>
                                <li>
                                    <a href="//game.dd373.com/y-0-0.html"  >游戏列表</a>
                                </li>
                                <li>
                                    <a href="//www.dd373.com/coin/index"  >金币交易</a>
                                </li>
                                <li>
                                    <a href="//da.dd373.com/Account/Index"  >帐号交易</a>
                                </li>
                                <li>
                                    <a href="//da.dd373.com/account/RecyclePage"  >帐号回收</a>
                                </li>
                                <li>
                                    <a href="//game.dd373.com/mg.html"  >手游交易</a>
                                </li>
                                <li>
                                        <img src="//publicimg.dd373.com/Upload/2021-08-27/bf8ec06f-ecb5-48a5-9f55-f82253e92e22.gif" alt="">
                                    <a href="https://dd373.com/7e3"  target=_blank>嘟嘟电竞</a>
                                </li>
                </ul>
                <ul class="goods-top-right">
                                <li>
                                    <a href="//kf.dd373.com/Information/index"  >游戏资讯</a>
                                </li>
                                <li>
                                    <a href="https://point.dd373.com/default/m_club_index.html"  >会员俱乐部</a>
                                </li>
                                <li>
                                    <a href="//tg.dd373.com/default/index.html"  >推广联盟</a>
                                </li>
                                <li>
                                    <a href="//kf.dd373.com/"  >客服中心</a>
                                </li>
                                <li>
                                        <img src="//publicimg.dd373.com/Upload/2021-12-01/321150e4-b0f9-4649-b0bb-a85f9484fddf.png" alt="">
                                    <a href="//cms.dd373.com/default/app_down.html"  target=_blank>手机APP</a>
                                </li>
                </ul>
            </div>
        </div>
    </div>


    <div class="main">
    <div class="user-info-bg">
        <!-- 配置链接 -->
        <a id="topAdLink">
            <div class="user-info-box">
                <div class="user-person-info">
                        <p class="usre-img" style="background:url(//publicimg.dd373.com/SitePic/2021-06-04/375d44b5-5e12-4b6e-a6b8-52df6b69c63a.png) no-repeat;background-size:cover;"></p>
                        <div class="user-name-box">
                            <p class="same-name">魔兽世界燃烧的远征</p>
                            <p>
                                <span class="seller-style">网络游戏</span>
                            </p>
                        </div>

                </div>
            </div>
        </a>
    </div>
    <div class="goods-select-condition-box">
        <!-- 右侧筛选几热卖商城 -->
        <div class="goods-select-condition">
            <!-- 左侧广告 及热卖商城收货-->
            <div class="top-left-content">
                <!-- 热卖商城收货,所选商品类型开通商城才显示此区域 -->

            </div>
            <div class="current-address">
                <div>
                    <span class="color999 font12">您的位置：</span>
                    <a href="//www.dd373.com">首页</a>
                    <a href="//game.dd373.com/y-0-0.html">游戏列表</a>
                    <span class="color999 font12">商品列表</span>
                </div>
                <div class="current-right-box">
                    <a href="/s-eja7u2-0r2mut-ac0ct4-q7s0fm-0-0-jk5sj0-0-0-recycle-0-0-1-0-0-0.html" target="_blank">
                        <h1>
                            <span class="color999">为您找到：魔兽世界燃烧的远征-一区-辛迪加(RPPVP)-联盟-游戏币交易相关记录</span>
                            <span class="colorFF5">9</span>
                            <span class="color999">条</span>
                        </h1>
                    </a>
                    <p id="retract-all-select" data-status="1">
                        <span>收起筛选</span>
                        <i class="icon-list-top bottom3"></i>
                    </p>
                </div>
            </div>

            <!--路由信息-->
            <div class="goods-select-content"><div class="goods-select-item"><div class="goods-select-title"><span>您的选择</span></div><div class="your-select-value"><div class="your-select-item"><div class="m-r25 your-attr" data-formaturl="/s-eja7u2-c-typeid-0r2mut-ac0ct4-q7s0fm.html" data-request="a8fda3f1-33c9-41c2-bd98-3fc94d0659d3"><a href="/s-eja7u2-0r2mut-ac0ct4-q7s0fm.html" class="next-dir">游戏币<i class="icon-list-4"></i></a></div><div class="m-r25 your-attr" data-formaturl="/s-eja7u2-c-jk5sj0-gameother.html" data-request="a8fda3f1-33c9-41c2-bd98-3fc94d0659d3"><a href="/s-eja7u2-c-jk5sj0.html" class="next-dir">一区<i class="icon-list-4"></i></a></div><div class="m-r25 your-attr" data-formaturl="/s-eja7u2-c-jk5sj0-0r2mut-gameother.html" data-request="bc497606319a4ccf876d6ee77876e7f6"><a href="/s-eja7u2-c-jk5sj0-0r2mut.html" class="next-dir">辛迪加(RPPVP)<i class="icon-list-4"></i></a></div><div class="m-r25 your-attr" data-formaturl="/s-eja7u2-c-jk5sj0-0r2mut-ac0ct4-gameother.html" data-request="847cb60dd31e4823b227341755a1fcb7"><a href="/s-eja7u2-c-jk5sj0-0r2mut-ac0ct4.html" class="next-dir">联盟<i class="icon-list-4"></i></a></div><a href="/s-eja7u2.html"><i class="icon-list-del"></i><span class="clear-attr">清空筛选</span></a></div></div></div><div class="goods-select-item"><div class="goods-select-title"><span>商品类型</span></div><div class="goods-select-value"><a href="/s-eja7u2-0r2mut-ac0ct4-q7s0fm.html">全部</a><a class="" href="/s-eja7u2-c-tawfpp-0r2mut-ac0ct4-q7s0fm.html">游戏帐号</a><a class="" href="/s-eja7u2-c-xsdhck-0r2mut-ac0ct4-q7s0fm.html">找回包赔帐号</a><a class="active" href="/s-eja7u2-c-jk5sj0-0r2mut-ac0ct4-q7s0fm.html">游戏币</a><a class="" href="/s-eja7u2-c-3g681q-0r2mut-ac0ct4-q7s0fm.html">点卡</a><a class="" href="/s-eja7u2-c-sbu21m-0r2mut-ac0ct4-q7s0fm.html">低折扣月卡</a><a class="" href="/s-eja7u2-c-ukq06q-0r2mut-ac0ct4-q7s0fm.html">装备</a><a class="" href="/s-eja7u2-c-gr6ax6-0r2mut-ac0ct4-q7s0fm.html">坐骑</a><a class="" href="/s-eja7u2-c-ms6cvv-0r2mut-ac0ct4-q7s0fm.html">三无号</a><a class="" href="/s-eja7u2-c-ad99bs-0r2mut-ac0ct4-q7s0fm.html">其它</a><a class="" href="/s-eja7u2-c-b0u676-0r2mut-ac0ct4-q7s0fm.html">奥术水晶</a><a class="" href="/s-eja7u2-c-dnb4kb-0r2mut-ac0ct4-q7s0fm.html">合剂</a><a class="" href="/s-eja7u2-c-tag22s-0r2mut-ac0ct4-q7s0fm.html">材料/配方</a><a class="" href="/s-eja7u2-c-qjhp64-0r2mut-ac0ct4-q7s0fm.html">黑莲花</a><a class="" href="/s-eja7u2-c-ue4fcg-0r2mut-ac0ct4-q7s0fm.html">法力蓟</a><a class="" href="/s-eja7u2-c-ed7p5h-0r2mut-ac0ct4-q7s0fm.html">药剂</a><a class="" href="/s-eja7u2-c-dnrn4t-0r2mut-ac0ct4-q7s0fm.html">冻结号</a><a class="" href="/s-eja7u2-c-tk2mek-0r2mut-ac0ct4-q7s0fm.html">帐号回收</a><a class="" href="https://dj.dd373.com/" target="_blank" data-flag="1" >游戏陪玩</a></div></div></div>

            <!-- 热门商城 -->

        </div>
    </div>
    <div class="goods-list-content">
        <div class="goods-type-box">

                <!--平台收货-->
                <div class="platform-receiving">
                    
    <!-- 商品内容 -->
    <div class="hot-shopping">
        <p class="list-hot-top"></p>
        <p class="list-hot-down"></p>
        <div class="hot-goods ">
            <div class="hot-title-box">
                <ul>
                    <li class="width190 font12 color666 bold p-l16">商品信息</li>
                    <li class="width211 font12 color666 bold p-l40">比例</li>
                    <li class="width185 font12 color666 bold p-l40">收货数量</li>
                    <li class="width310 p-l40 font12 color666 bold">出货数量</li>
                    <li class="width184 p-l40 font12 color666">服务保障</li>
                </ul>
            </div>
            <div class="platform-receive-content">
                    <ul>
                        <li class="width185 p-l6">
                            <div class="hot-game-area">
                                <p class="font12 receiveQufu0">
                                    
                                </p>
                            </div>
                            <p class="line-height14">
                                <span class="font12 color666">交易均时</span>
                                <span class="font12 colorFF5">8分钟17秒</span>
                            </p>
                            <p class="line-height14 m-t9">
                                <span class="font12 color666">成交率</span>
                                <span class="font12 colorFF5">98.00%</span>
                            </p>
                        </li>
                        <li class="width198">
                            <div class="receive-lable">
                                        <span>当面</span>
                                        <span>拍卖</span>
                                        <span>摆摊</span>
                            </div>
                            <p class="font12 colorFF5 m-t9 clear">1元=33.23金</p>
                            <p class="font12 color666 m-t9">0.03009元/金</p>
                        </li>
                        <li class="width185 p-l40">
                            <p class="line-height14">
                                <span class="font12 colorFF5 f-left">9999999</span>
                                <span class="font12 color666 f-left">金</span>
                            </p>
                            <p class="line-height14 m-t9">
                                <span class="font12 color999 f-left">起收≥</span>
                                <span class="font12 color666 f-left">6000金</span>
                            </p>
                            <p class="line-height14 m-t9">
                                <span class="font12 color999 f-left">最高≤</span>
                                <span class="font12 color666 f-left">30000金</span>
                            </p>
                        </li>
                        <li class="width310 p-l40">
                            <div class="buy-number-box" id="receive-boxSH20200814110359-77006">
                                <!-- receive-box1 1是唯一的-->
                                <div class="buy-num buy-box">
                                    <input id="receiveInputSH20200814110359-77006" type="text" data-min="6000" data-max="30000" data-bili="33.233632436025257560651379196" value="6000"> <!-- data-min="1" data-max="9999" 最大价格和最小价格 -->
                                    <span>金</span>
                                    <img src="//cdnimg.dd373.com/newfile/common/images/default/icons/search_clear_btn.png" class="input-clear-btn" alt="">
                                </div>
                                <div class="top5">
                                    <span class="font14 m-r6 m-l6 f-left">=</span>
                                    <span class="font14 colorFF5 fontMT bold f-left yuan">180.54</span>
                                    <span class="font14 colorFF5 f-left">元</span>
                                </div>
                            </div>

                        </li>
                        <li class="width184 p-l40">
                            <p class="server-guarantee">
                                <i class="icon-lh"></i>
                                <span class="font12 color666">灵活出货</span>
                            </p>
                            <p class="server-guarantee">
                                <i class="icon-goods-28"></i>
                                <span class="font12 color666">现金秒结</span>
                            </p>
                            <p class="server-guarantee">
                                <i class="icon-peifu"></i>
                                <span class="font12 color666">拒收赔付</span>
                            </p>
                            <p class="server-guarantee m-b0">
                                <i class="icon-shopR"></i>
                                <span class="font12 color666">商家认证</span>
                            </p>
                        </li>
                        <li class="width116">
                            <a onclick="jumpReceive('SH20200814110359-77006')" class="hot-buy-btn" data-index="1">立即出售</a> <!-- data-index="1" 1是唯一的-->
                        </li>
                    </ul>
                    <ul>
                        <li class="width185 p-l6">
                            <div class="hot-game-area">
                                <p class="font12 receiveQufu1">
                                    
                                </p>
                            </div>
                            <p class="line-height14">
                                <span class="font12 color666">交易均时</span>
                                <span class="font12 colorFF5">5分钟6秒</span>
                            </p>
                            <p class="line-height14 m-t9">
                                <span class="font12 color666">成交率</span>
                                <span class="font12 colorFF5">100.00%</span>
                            </p>
                        </li>
                        <li class="width198">
                            <div class="receive-lable">
                                        <span>当面</span>
                            </div>
                            <p class="font12 colorFF5 m-t9 clear">1元=33.24金</p>
                            <p class="font12 color666 m-t9">0.03008元/金</p>
                        </li>
                        <li class="width185 p-l40">
                            <p class="line-height14">
                                <span class="font12 colorFF5 f-left">99999</span>
                                <span class="font12 color666 f-left">金</span>
                            </p>
                            <p class="line-height14 m-t9">
                                <span class="font12 color999 f-left">起收≥</span>
                                <span class="font12 color666 f-left">800金</span>
                            </p>
                            <p class="line-height14 m-t9">
                                <span class="font12 color999 f-left">最高≤</span>
                                <span class="font12 color666 f-left">5000金</span>
                            </p>
                        </li>
                        <li class="width310 p-l40">
                            <div class="buy-number-box" id="receive-boxSH20200220212919-10002">
                                <!-- receive-box1 1是唯一的-->
                                <div class="buy-num buy-box">
                                    <input id="receiveInputSH20200220212919-10002" type="text" data-min="800" data-max="5000" data-bili="33.244680851063829787234042553" value="800"> <!-- data-min="1" data-max="9999" 最大价格和最小价格 -->
                                    <span>金</span>
                                    <img src="//cdnimg.dd373.com/newfile/common/images/default/icons/search_clear_btn.png" class="input-clear-btn" alt="">
                                </div>
                                <div class="top5">
                                    <span class="font14 m-r6 m-l6 f-left">=</span>
                                    <span class="font14 colorFF5 fontMT bold f-left yuan">24.06</span>
                                    <span class="font14 colorFF5 f-left">元</span>
                                </div>
                            </div>

                        </li>
                        <li class="width184 p-l40">
                            <p class="server-guarantee">
                                <i class="icon-lh"></i>
                                <span class="font12 color666">灵活出货</span>
                            </p>
                            <p class="server-guarantee">
                                <i class="icon-goods-28"></i>
                                <span class="font12 color666">现金秒结</span>
                            </p>
                            <p class="server-guarantee">
                                <i class="icon-peifu"></i>
                                <span class="font12 color666">拒收赔付</span>
                            </p>
                            <p class="server-guarantee m-b0">
                                <i class="icon-shopR"></i>
                                <span class="font12 color666">商家认证</span>
                            </p>
                        </li>
                        <li class="width116">
                            <a onclick="jumpReceive('SH20200220212919-10002')" class="hot-buy-btn" data-index="1">立即出售</a> <!-- data-index="1" 1是唯一的-->
                        </li>
                    </ul>
                    <ul>
                        <li class="width185 p-l6">
                            <div class="hot-game-area">
                                <p class="font12 receiveQufu2">
                                    
                                </p>
                            </div>
                            <p class="line-height14">
                                <span class="font12 color666">交易均时</span>
                                <span class="font12 colorFF5">14分钟10秒</span>
                            </p>
                            <p class="line-height14 m-t9">
                                <span class="font12 color666">成交率</span>
                                <span class="font12 colorFF5">100.00%</span>
                            </p>
                        </li>
                        <li class="width198">
                            <div class="receive-lable">
                                        <span>当面</span>
                            </div>
                            <p class="font12 colorFF5 m-t9 clear">1元=33.27金</p>
                            <p class="font12 color666 m-t9">0.03006元/金</p>
                        </li>
                        <li class="width185 p-l40">
                            <p class="line-height14">
                                <span class="font12 colorFF5 f-left">4970000</span>
                                <span class="font12 color666 f-left">金</span>
                            </p>
                            <p class="line-height14 m-t9">
                                <span class="font12 color999 f-left">起收≥</span>
                                <span class="font12 color666 f-left">10000金</span>
                            </p>
                            <p class="line-height14 m-t9">
                                <span class="font12 color999 f-left">最高≤</span>
                                <span class="font12 color666 f-left">300000金</span>
                            </p>
                        </li>
                        <li class="width310 p-l40">
                            <div class="buy-number-box" id="receive-boxSH20201222114526-36001">
                                <!-- receive-box1 1是唯一的-->
                                <div class="buy-num buy-box">
                                    <input id="receiveInputSH20201222114526-36001" type="text" data-min="10000" data-max="300000" data-bili="33.266799733865602129075182967" value="10000"> <!-- data-min="1" data-max="9999" 最大价格和最小价格 -->
                                    <span>金</span>
                                    <img src="//cdnimg.dd373.com/newfile/common/images/default/icons/search_clear_btn.png" class="input-clear-btn" alt="">
                                </div>
                                <div class="top5">
                                    <span class="font14 m-r6 m-l6 f-left">=</span>
                                    <span class="font14 colorFF5 fontMT bold f-left yuan">300.60</span>
                                    <span class="font14 colorFF5 f-left">元</span>
                                </div>
                            </div>

                        </li>
                        <li class="width184 p-l40">
                            <p class="server-guarantee">
                                <i class="icon-lh"></i>
                                <span class="font12 color666">灵活出货</span>
                            </p>
                            <p class="server-guarantee">
                                <i class="icon-goods-28"></i>
                                <span class="font12 color666">现金秒结</span>
                            </p>
                            <p class="server-guarantee">
                                <i class="icon-peifu"></i>
                                <span class="font12 color666">拒收赔付</span>
                            </p>
                            <p class="server-guarantee m-b0">
                                <i class="icon-shopR"></i>
                                <span class="font12 color666">商家认证</span>
                            </p>
                        </li>
                        <li class="width116">
                            <a onclick="jumpReceive('SH20201222114526-36001')" class="hot-buy-btn" data-index="1">立即出售</a> <!-- data-index="1" 1是唯一的-->
                        </li>
                    </ul>
                    <ul>
                        <li class="width185 p-l6">
                            <div class="hot-game-area">
                                <p class="font12 receiveQufu3">
                                    
                                </p>
                            </div>
                            <p class="line-height14">
                                <span class="font12 color666">交易均时</span>
                                <span class="font12 colorFF5">72分钟43秒</span>
                            </p>
                            <p class="line-height14 m-t9">
                                <span class="font12 color666">成交率</span>
                                <span class="font12 colorFF5">99.00%</span>
                            </p>
                        </li>
                        <li class="width198">
                            <div class="receive-lable">
                                        <span>当面</span>
                                        <span>邮寄</span>
                            </div>
                            <p class="font12 colorFF5 m-t9 clear">1元=33.60金</p>
                            <p class="font12 color666 m-t9">0.02976元/金</p>
                        </li>
                        <li class="width185 p-l40">
                            <p class="line-height14">
                                <span class="font12 colorFF5 f-left">9617402</span>
                                <span class="font12 color666 f-left">金</span>
                            </p>
                            <p class="line-height14 m-t9">
                                <span class="font12 color999 f-left">起收≥</span>
                                <span class="font12 color666 f-left">1000金</span>
                            </p>
                            <p class="line-height14 m-t9">
                                <span class="font12 color999 f-left">最高≤</span>
                                <span class="font12 color666 f-left">100000金</span>
                            </p>
                        </li>
                        <li class="width310 p-l40">
                            <div class="buy-number-box" id="receive-boxSH20220106104234-72002">
                                <!-- receive-box1 1是唯一的-->
                                <div class="buy-num buy-box">
                                    <input id="receiveInputSH20220106104234-72002" type="text" data-min="1000" data-max="100000" data-bili="33.602150537634408602150537634" value="1000"> <!-- data-min="1" data-max="9999" 最大价格和最小价格 -->
                                    <span>金</span>
                                    <img src="//cdnimg.dd373.com/newfile/common/images/default/icons/search_clear_btn.png" class="input-clear-btn" alt="">
                                </div>
                                <div class="top5">
                                    <span class="font14 m-r6 m-l6 f-left">=</span>
                                    <span class="font14 colorFF5 fontMT bold f-left yuan">29.76</span>
                                    <span class="font14 colorFF5 f-left">元</span>
                                </div>
                            </div>

                        </li>
                        <li class="width184 p-l40">
                            <p class="server-guarantee">
                                <i class="icon-lh"></i>
                                <span class="font12 color666">灵活出货</span>
                            </p>
                            <p class="server-guarantee">
                                <i class="icon-goods-28"></i>
                                <span class="font12 color666">现金秒结</span>
                            </p>
                            <p class="server-guarantee">
                                <i class="icon-peifu"></i>
                                <span class="font12 color666">拒收赔付</span>
                            </p>
                            <p class="server-guarantee m-b0">
                                <i class="icon-shopR"></i>
                                <span class="font12 color666">商家认证</span>
                            </p>
                        </li>
                        <li class="width116">
                            <a onclick="jumpReceive('SH20220106104234-72002')" class="hot-buy-btn" data-index="1">立即出售</a> <!-- data-index="1" 1是唯一的-->
                        </li>
                    </ul>
                    <ul>
                        <li class="width185 p-l6">
                            <div class="hot-game-area">
                                <p class="font12 receiveQufu4">
                                    
                                </p>
                            </div>
                            <p class="line-height14">
                                <span class="font12 color666">交易均时</span>
                                <span class="font12 colorFF5">13分钟7秒</span>
                            </p>
                            <p class="line-height14 m-t9">
                                <span class="font12 color666">成交率</span>
                                <span class="font12 colorFF5">99.00%</span>
                            </p>
                        </li>
                        <li class="width198">
                            <div class="receive-lable">
                                        <span>当面</span>
                            </div>
                            <p class="font12 colorFF5 m-t9 clear">1元=33.78金</p>
                            <p class="font12 color666 m-t9">0.02960元/金</p>
                        </li>
                        <li class="width185 p-l40">
                            <p class="line-height14">
                                <span class="font12 colorFF5 f-left">9305545</span>
                                <span class="font12 color666 f-left">金</span>
                            </p>
                            <p class="line-height14 m-t9">
                                <span class="font12 color999 f-left">起收≥</span>
                                <span class="font12 color666 f-left">1000金</span>
                            </p>
                            <p class="line-height14 m-t9">
                                <span class="font12 color999 f-left">最高≤</span>
                                <span class="font12 color666 f-left">90000金</span>
                            </p>
                        </li>
                        <li class="width310 p-l40">
                            <div class="buy-number-box" id="receive-boxSH20200705140333-31002">
                                <!-- receive-box1 1是唯一的-->
                                <div class="buy-num buy-box">
                                    <input id="receiveInputSH20200705140333-31002" type="text" data-min="1000" data-max="90000" data-bili="33.783783783783783783783783784" value="1000"> <!-- data-min="1" data-max="9999" 最大价格和最小价格 -->
                                    <span>金</span>
                                    <img src="//cdnimg.dd373.com/newfile/common/images/default/icons/search_clear_btn.png" class="input-clear-btn" alt="">
                                </div>
                                <div class="top5">
                                    <span class="font14 m-r6 m-l6 f-left">=</span>
                                    <span class="font14 colorFF5 fontMT bold f-left yuan">29.60</span>
                                    <span class="font14 colorFF5 f-left">元</span>
                                </div>
                            </div>

                        </li>
                        <li class="width184 p-l40">
                            <p class="server-guarantee">
                                <i class="icon-lh"></i>
                                <span class="font12 color666">灵活出货</span>
                            </p>
                            <p class="server-guarantee">
                                <i class="icon-goods-28"></i>
                                <span class="font12 color666">现金秒结</span>
                            </p>
                            <p class="server-guarantee">
                                <i class="icon-peifu"></i>
                                <span class="font12 color666">拒收赔付</span>
                            </p>
                            <p class="server-guarantee m-b0">
                                <i class="icon-shopR"></i>
                                <span class="font12 color666">商家认证</span>
                            </p>
                        </li>
                        <li class="width116">
                            <a onclick="jumpReceive('SH20200705140333-31002')" class="hot-buy-btn" data-index="1">立即出售</a> <!-- data-index="1" 1是唯一的-->
                        </li>
                    </ul>
                    <ul>
                        <li class="width185 p-l6">
                            <div class="hot-game-area">
                                <p class="font12 receiveQufu5">
                                    
                                </p>
                            </div>
                            <p class="line-height14">
                                <span class="font12 color666">交易均时</span>
                                <span class="font12 colorFF5">18分钟21秒</span>
                            </p>
                            <p class="line-height14 m-t9">
                                <span class="font12 color666">成交率</span>
                                <span class="font12 colorFF5">93.00%</span>
                            </p>
                        </li>
                        <li class="width198">
                            <div class="receive-lable">
                                        <span>当面</span>
                                        <span>拍卖</span>
                            </div>
                            <p class="font12 colorFF5 m-t9 clear">1元=36.63金</p>
                            <p class="font12 color666 m-t9">0.02730元/金</p>
                        </li>
                        <li class="width185 p-l40">
                            <p class="line-height14">
                                <span class="font12 colorFF5 f-left">999999999</span>
                                <span class="font12 color666 f-left">金</span>
                            </p>
                            <p class="line-height14 m-t9">
                                <span class="font12 color999 f-left">起收≥</span>
                                <span class="font12 color666 f-left">15008金</span>
                            </p>
                            <p class="line-height14 m-t9">
                                <span class="font12 color999 f-left">最高≤</span>
                                <span class="font12 color666 f-left">60000金</span>
                            </p>
                        </li>
                        <li class="width310 p-l40">
                            <div class="buy-number-box" id="receive-boxSH20191231154023-51003">
                                <!-- receive-box1 1是唯一的-->
                                <div class="buy-num buy-box">
                                    <input id="receiveInputSH20191231154023-51003" type="text" data-min="15008" data-max="60000" data-bili="36.63003663003663003663003663" value="15008"> <!-- data-min="1" data-max="9999" 最大价格和最小价格 -->
                                    <span>金</span>
                                    <img src="//cdnimg.dd373.com/newfile/common/images/default/icons/search_clear_btn.png" class="input-clear-btn" alt="">
                                </div>
                                <div class="top5">
                                    <span class="font14 m-r6 m-l6 f-left">=</span>
                                    <span class="font14 colorFF5 fontMT bold f-left yuan">409.72</span>
                                    <span class="font14 colorFF5 f-left">元</span>
                                </div>
                            </div>

                        </li>
                        <li class="width184 p-l40">
                            <p class="server-guarantee">
                                <i class="icon-lh"></i>
                                <span class="font12 color666">灵活出货</span>
                            </p>
                            <p class="server-guarantee">
                                <i class="icon-goods-28"></i>
                                <span class="font12 color666">现金秒结</span>
                            </p>
                            <p class="server-guarantee">
                                <i class="icon-peifu"></i>
                                <span class="font12 color666">拒收赔付</span>
                            </p>
                            <p class="server-guarantee m-b0">
                                <i class="icon-shopR"></i>
                                <span class="font12 color666">商家认证</span>
                            </p>
                        </li>
                        <li class="width116">
                            <a onclick="jumpReceive('SH20191231154023-51003')" class="hot-buy-btn" data-index="1">立即出售</a> <!-- data-index="1" 1是唯一的-->
                        </li>
                    </ul>
                    <ul>
                        <li class="width185 p-l6">
                            <div class="hot-game-area">
                                <p class="font12 receiveQufu6">
                                    
                                </p>
                            </div>
                            <p class="line-height14">
                                <span class="font12 color666">交易均时</span>
                                <span class="font12 colorFF5">12分钟26秒</span>
                            </p>
                            <p class="line-height14 m-t9">
                                <span class="font12 color666">成交率</span>
                                <span class="font12 colorFF5">100.00%</span>
                            </p>
                        </li>
                        <li class="width198">
                            <div class="receive-lable">
                                        <span>当面</span>
                                        <span>邮寄</span>
                            </div>
                            <p class="font12 colorFF5 m-t9 clear">1元=39.00金</p>
                            <p class="font12 color666 m-t9">0.02564元/金</p>
                        </li>
                        <li class="width185 p-l40">
                            <p class="line-height14">
                                <span class="font12 colorFF5 f-left">91600</span>
                                <span class="font12 color666 f-left">金</span>
                            </p>
                            <p class="line-height14 m-t9">
                                <span class="font12 color999 f-left">起收≥</span>
                                <span class="font12 color666 f-left">5000金</span>
                            </p>
                            <p class="line-height14 m-t9">
                                <span class="font12 color999 f-left">最高≤</span>
                                <span class="font12 color666 f-left">20000金</span>
                            </p>
                        </li>
                        <li class="width310 p-l40">
                            <div class="buy-number-box" id="receive-boxSH20210628132548-50003">
                                <!-- receive-box1 1是唯一的-->
                                <div class="buy-num buy-box">
                                    <input id="receiveInputSH20210628132548-50003" type="text" data-min="5000" data-max="20000" data-bili="39.00156006240249609984399376" value="5000"> <!-- data-min="1" data-max="9999" 最大价格和最小价格 -->
                                    <span>金</span>
                                    <img src="//cdnimg.dd373.com/newfile/common/images/default/icons/search_clear_btn.png" class="input-clear-btn" alt="">
                                </div>
                                <div class="top5">
                                    <span class="font14 m-r6 m-l6 f-left">=</span>
                                    <span class="font14 colorFF5 fontMT bold f-left yuan">128.20</span>
                                    <span class="font14 colorFF5 f-left">元</span>
                                </div>
                            </div>

                        </li>
                        <li class="width184 p-l40">
                            <p class="server-guarantee">
                                <i class="icon-lh"></i>
                                <span class="font12 color666">灵活出货</span>
                            </p>
                            <p class="server-guarantee">
                                <i class="icon-goods-28"></i>
                                <span class="font12 color666">现金秒结</span>
                            </p>
                            <p class="server-guarantee">
                                <i class="icon-peifu"></i>
                                <span class="font12 color666">拒收赔付</span>
                            </p>
                            <p class="server-guarantee m-b0">
                                <i class="icon-shopR"></i>
                                <span class="font12 color666">商家认证</span>
                            </p>
                        </li>
                        <li class="width116">
                            <a onclick="jumpReceive('SH20210628132548-50003')" class="hot-buy-btn" data-index="1">立即出售</a> <!-- data-index="1" 1是唯一的-->
                        </li>
                    </ul>
                    <ul>
                        <li class="width185 p-l6">
                            <div class="hot-game-area">
                                <p class="font12 receiveQufu7">
                                    
                                </p>
                            </div>
                            <p class="line-height14">
                                <span class="font12 color666">交易均时</span>
                                <span class="font12 colorFF5">0秒</span>
                            </p>
                            <p class="line-height14 m-t9">
                                <span class="font12 color666">成交率</span>
                                <span class="font12 colorFF5">0.00%</span>
                            </p>
                        </li>
                        <li class="width198">
                            <div class="receive-lable">
                                        <span>当面</span>
                                        <span>邮寄</span>
                                        <span>拍卖</span>
                                        <span>摆摊</span>
                            </div>
                            <p class="font12 colorFF5 m-t9 clear">1元=45.17金</p>
                            <p class="font12 color666 m-t9">0.02214元/金</p>
                        </li>
                        <li class="width185 p-l40">
                            <p class="line-height14">
                                <span class="font12 colorFF5 f-left">200000</span>
                                <span class="font12 color666 f-left">金</span>
                            </p>
                            <p class="line-height14 m-t9">
                                <span class="font12 color999 f-left">起收≥</span>
                                <span class="font12 color666 f-left">500金</span>
                            </p>
                            <p class="line-height14 m-t9">
                                <span class="font12 color999 f-left">最高≤</span>
                                <span class="font12 color666 f-left">50000金</span>
                            </p>
                        </li>
                        <li class="width310 p-l40">
                            <div class="buy-number-box" id="receive-boxSH20220402094854-93003">
                                <!-- receive-box1 1是唯一的-->
                                <div class="buy-num buy-box">
                                    <input id="receiveInputSH20220402094854-93003" type="text" data-min="500" data-max="50000" data-bili="45.16711833785004516711833785" value="500"> <!-- data-min="1" data-max="9999" 最大价格和最小价格 -->
                                    <span>金</span>
                                    <img src="//cdnimg.dd373.com/newfile/common/images/default/icons/search_clear_btn.png" class="input-clear-btn" alt="">
                                </div>
                                <div class="top5">
                                    <span class="font14 m-r6 m-l6 f-left">=</span>
                                    <span class="font14 colorFF5 fontMT bold f-left yuan">11.07</span>
                                    <span class="font14 colorFF5 f-left">元</span>
                                </div>
                            </div>

                        </li>
                        <li class="width184 p-l40">
                            <p class="server-guarantee">
                                <i class="icon-lh"></i>
                                <span class="font12 color666">灵活出货</span>
                            </p>
                            <p class="server-guarantee">
                                <i class="icon-goods-28"></i>
                                <span class="font12 color666">现金秒结</span>
                            </p>
                            <p class="server-guarantee">
                                <i class="icon-peifu"></i>
                                <span class="font12 color666">拒收赔付</span>
                            </p>
                            <p class="server-guarantee m-b0">
                                <i class="icon-shopR"></i>
                                <span class="font12 color666">商家认证</span>
                            </p>
                        </li>
                        <li class="width116">
                            <a onclick="jumpReceive('SH20220402094854-93003')" class="hot-buy-btn" data-index="1">立即出售</a> <!-- data-index="1" 1是唯一的-->
                        </li>
                    </ul>
                    <ul>
                        <li class="width185 p-l6">
                            <div class="hot-game-area">
                                <p class="font12 receiveQufu8">
                                    
                                </p>
                            </div>
                            <p class="line-height14">
                                <span class="font12 color666">交易均时</span>
                                <span class="font12 colorFF5">0秒</span>
                            </p>
                            <p class="line-height14 m-t9">
                                <span class="font12 color666">成交率</span>
                                <span class="font12 colorFF5">0.00%</span>
                            </p>
                        </li>
                        <li class="width198">
                            <div class="receive-lable">
                                        <span>当面</span>
                            </div>
                            <p class="font12 colorFF5 m-t9 clear">1元=60.00金</p>
                            <p class="font12 color666 m-t9">0.01667元/金</p>
                        </li>
                        <li class="width185 p-l40">
                            <p class="line-height14">
                                <span class="font12 colorFF5 f-left">388888</span>
                                <span class="font12 color666 f-left">金</span>
                            </p>
                            <p class="line-height14 m-t9">
                                <span class="font12 color999 f-left">起收≥</span>
                                <span class="font12 color666 f-left">28888金</span>
                            </p>
                            <p class="line-height14 m-t9">
                                <span class="font12 color999 f-left">最高≤</span>
                                <span class="font12 color666 f-left">88888金</span>
                            </p>
                        </li>
                        <li class="width310 p-l40">
                            <div class="buy-number-box" id="receive-boxSH20210615190542-16003">
                                <!-- receive-box1 1是唯一的-->
                                <div class="buy-num buy-box">
                                    <input id="receiveInputSH20210615190542-16003" type="text" data-min="28888" data-max="88888" data-bili="59.988002399520095980803839232" value="28888"> <!-- data-min="1" data-max="9999" 最大价格和最小价格 -->
                                    <span>金</span>
                                    <img src="//cdnimg.dd373.com/newfile/common/images/default/icons/search_clear_btn.png" class="input-clear-btn" alt="">
                                </div>
                                <div class="top5">
                                    <span class="font14 m-r6 m-l6 f-left">=</span>
                                    <span class="font14 colorFF5 fontMT bold f-left yuan">481.56</span>
                                    <span class="font14 colorFF5 f-left">元</span>
                                </div>
                            </div>

                        </li>
                        <li class="width184 p-l40">
                            <p class="server-guarantee">
                                <i class="icon-lh"></i>
                                <span class="font12 color666">灵活出货</span>
                            </p>
                            <p class="server-guarantee">
                                <i class="icon-goods-28"></i>
                                <span class="font12 color666">现金秒结</span>
                            </p>
                            <p class="server-guarantee">
                                <i class="icon-peifu"></i>
                                <span class="font12 color666">拒收赔付</span>
                            </p>
                            <p class="server-guarantee m-b0">
                                <i class="icon-shopR"></i>
                                <span class="font12 color666">商家认证</span>
                            </p>
                        </li>
                        <li class="width116">
                            <a onclick="jumpReceive('SH20210615190542-16003')" class="hot-buy-btn" data-index="1">立即出售</a> <!-- data-index="1" 1是唯一的-->
                        </li>
                    </ul>
            </div>
        </div>
    </div>
    <!-- 分页 -->
    <div class="footer-pagination">
        <p class="f-left">
            <span class="font12 color999">为您找到</span>
            <span class="font12 colorFF5">9</span>
            <span class="font12 color999">条记录</span>
        </p>
        <div id="pagination-box"><div class="ui-pagination-container"><a href="/s-eja7u2-0r2mut-ac0ct4-q7s0fm-0-0-jk5sj0-0-0-recycle-0-0-1-0-0-0.html" class="ui-pagination-page-item active">1</a><span class="font-color m-l14">20</span><span class="font-color m-r16">条/页</span><span class="font-color">共</span><span class="font-colorff5b max-number">1</span><span class="font-color m-r16">页</span><span class="font-color m-r10">到</span><div class="current-index-box"><input type="text" placeholder="页码" class="current-index" value="1"><div class="top-down-btn-box"><div class="top-btn icon-top"></div><div class="down-btn icon-down"></div></div></div><span class="font-color m-lr10">页</span><a class="ui-pagination-page-btn" href="javascript:void(0);">确定</a></div></div>
    </div>

                </div>

            <div id="invisibleData" data-jsData="{&quot;requestModel&quot;:{&quot;LastId&quot;:&quot;f3ebb8f4ba3a45e092ce7c1d78a4bc42&quot;,&quot;GoodsTypeId&quot;:&quot;61b65070243c4453b653fa82c8b39bd1&quot;,&quot;GameId&quot;:&quot;eja7u2&quot;,&quot;QuId&quot;:&quot;0r2mut&quot;,&quot;FuId&quot;:&quot;ac0ct4&quot;,&quot;ZYId&quot;:&quot;q7s0fm&quot;,&quot;OperatorId&quot;:&quot;0&quot;,&quot;OSId&quot;:&quot;0&quot;,&quot;TypeId&quot;:&quot;jk5sj0&quot;,&quot;SubTypeId&quot;:&quot;0&quot;,&quot;DealType&quot;:&quot;0&quot;,&quot;Column&quot;:&quot;recycle&quot;,&quot;Property&quot;:&quot;0&quot;,&quot;AttachProperty&quot;:&quot;0&quot;,&quot;PageIndex&quot;:1,&quot;PageSize&quot;:0,&quot;Order&quot;:&quot;0&quot;,&quot;Issearch&quot;:&quot;0&quot;,&quot;KeyWord&quot;:null,&quot;MinPrice&quot;:null,&quot;MaxPrice&quot;:null},&quot;page1Href&quot;:&quot;/s-eja7u2-0r2mut-ac0ct4-q7s0fm-0-0-jk5sj0-0-0-recycle-0-0-1-0-0-0.html&quot;,&quot;pageGt1Href&quot;:&quot;/s-eja7u2-0r2mut-ac0ct4-q7s0fm-0-0-jk5sj0-0-0-recycle-0-0-####-0-0-0.html&quot;,&quot;hotGoods&quot;:[{&quot;GoodsType&quot;:&quot;61b65070243c4453b653fa82c8b39bd1&quot;,&quot;LastId&quot;:&quot;f3ebb8f4ba3a45e092ce7c1d78a4bc42&quot;},{&quot;GoodsType&quot;:&quot;61b65070243c4453b653fa82c8b39bd1&quot;,&quot;LastId&quot;:&quot;f3ebb8f4ba3a45e092ce7c1d78a4bc42&quot;},{&quot;GoodsType&quot;:&quot;61b65070243c4453b653fa82c8b39bd1&quot;,&quot;LastId&quot;:&quot;f3ebb8f4ba3a45e092ce7c1d78a4bc42&quot;},{&quot;GoodsType&quot;:&quot;61b65070243c4453b653fa82c8b39bd1&quot;,&quot;LastId&quot;:&quot;f3ebb8f4ba3a45e092ce7c1d78a4bc42&quot;},{&quot;GoodsType&quot;:&quot;61b65070243c4453b653fa82c8b39bd1&quot;,&quot;LastId&quot;:&quot;f3ebb8f4ba3a45e092ce7c1d78a4bc42&quot;},{&quot;GoodsType&quot;:&quot;61b65070243c4453b653fa82c8b39bd1&quot;,&quot;LastId&quot;:&quot;f3ebb8f4ba3a45e092ce7c1d78a4bc42&quot;},{&quot;GoodsType&quot;:&quot;61b65070243c4453b653fa82c8b39bd1&quot;,&quot;LastId&quot;:&quot;f3ebb8f4ba3a45e092ce7c1d78a4bc42&quot;},{&quot;GoodsType&quot;:&quot;61b65070243c4453b653fa82c8b39bd1&quot;,&quot;LastId&quot;:&quot;f3ebb8f4ba3a45e092ce7c1d78a4bc42&quot;},{&quot;GoodsType&quot;:&quot;61b65070243c4453b653fa82c8b39bd1&quot;,&quot;LastId&quot;:&quot;f3ebb8f4ba3a45e092ce7c1d78a4bc42&quot;}],&quot;receiveGoods&quot;:[{&quot;GoodsType&quot;:&quot;61b65070243c4453b653fa82c8b39bd1&quot;,&quot;LastId&quot;:&quot;f3ebb8f4ba3a45e092ce7c1d78a4bc42&quot;},{&quot;GoodsType&quot;:&quot;61b65070243c4453b653fa82c8b39bd1&quot;,&quot;LastId&quot;:&quot;f3ebb8f4ba3a45e092ce7c1d78a4bc42&quot;},{&quot;GoodsType&quot;:&quot;61b65070243c4453b653fa82c8b39bd1&quot;,&quot;LastId&quot;:&quot;f3ebb8f4ba3a45e092ce7c1d78a4bc42&quot;},{&quot;GoodsType&quot;:&quot;61b65070243c4453b653fa82c8b39bd1&quot;,&quot;LastId&quot;:&quot;f3ebb8f4ba3a45e092ce7c1d78a4bc42&quot;},{&quot;GoodsType&quot;:&quot;61b65070243c4453b653fa82c8b39bd1&quot;,&quot;LastId&quot;:&quot;f3ebb8f4ba3a45e092ce7c1d78a4bc42&quot;},{&quot;GoodsType&quot;:&quot;61b65070243c4453b653fa82c8b39bd1&quot;,&quot;LastId&quot;:&quot;f3ebb8f4ba3a45e092ce7c1d78a4bc42&quot;},{&quot;GoodsType&quot;:&quot;61b65070243c4453b653fa82c8b39bd1&quot;,&quot;LastId&quot;:&quot;f3ebb8f4ba3a45e092ce7c1d78a4bc42&quot;},{&quot;GoodsType&quot;:&quot;61b65070243c4453b653fa82c8b39bd1&quot;,&quot;LastId&quot;:&quot;f3ebb8f4ba3a45e092ce7c1d78a4bc42&quot;},{&quot;GoodsType&quot;:&quot;61b65070243c4453b653fa82c8b39bd1&quot;,&quot;LastId&quot;:&quot;f3ebb8f4ba3a45e092ce7c1d78a4bc42&quot;}],&quot;topCount&quot;:9,&quot;hotPicKeyWord&quot;:&quot;魔兽世界燃烧的远征游戏币&quot;,&quot;configurationList&quot;:[],&quot;interPicLastId&quot;:&quot;f3ebb8f4ba3a45e092ce7c1d78a4bc42&quot;,&quot;interPicGoodsType&quot;:&quot;61b65070243c4453b653fa82c8b39bd1&quot;,&quot;gameId&quot;:&quot;a8fda3f1-33c9-41c2-bd98-3fc94d0659d3&quot;}"></div>
        </div>
    </div>

</div>







    <div class="footer-box">
        <div class="footer1">            <div class="footer1-box">                <div class="footer1-item">                    <p class="icon-footer-style"><i class="icon-footer04"></i></p>                    <div>                        <p class="colorfff">无货超时赔付</p>                        <p class="colorfff">资金保障，交易更放心</p>                    </div>                </div>                <div class="footer1-item">                    <p class="icon-footer-style"><i class="icon-footer02"></i></p>                    <div>                        <p class="colorfff">安全保障</p>                        <p class="colorfff">防盗措施，保障交易安全</p>                    </div>                </div>                <div class="footer1-item">                    <p class="icon-footer-style"><i class="icon-footer05"></i></p>                    <div>                        <p class="colorfff">专业团队</p>                        <p class="colorfff">高效专业引导完成交易</p>                    </div>                </div>                <div class="footer1-item">                    <p class="icon-footer-style"><i class="icon-footer01"></i></p>                    <div>                        <p class="colorfff">7×24小时客服</p>                        <p class="colorfff">优质客服贴心服务，全年无休</p>                    </div>                </div>            </div>        </div>
        <div class="footer2">
            <div class="footer2-left">
                            <div class="footer2-item width164">
                                <p class="footer-title">新手入门</p>
                                <ul>
                                            <li>
                                                <a href="https://kf.dd373.com/helpdetail/88c4c567d7af41cbb7ee9f3704922965.html">担保交易</a>
                                            </li>
                                            <li>
                                                <a href="https://kf.dd373.com/helpdetail/71e4ab5bd97d4962bc816d9f55d67713.html">寄售交易</a>
                                            </li>
                                            <li>
                                                <a href="https://kf.dd373.com/helpdetail/39732072dd674b3e8159af197af05457.html">联系接手客服</a>
                                            </li>
                                            <li>
                                                <a href="https://kf.dd373.com/helpdetail/67c59caa23b7497aa8c1571b3b3ec062.html">登录DD373账户</a>
                                            </li>
                                </ul>
                            </div>
                            <div class="footer2-item width164">
                                <p class="footer-title">购买项目</p>
                                <ul>
                                            <li>
                                                <a href="https://kf.dd373.com/helpdetail/3894e247726f467b83a1b70e2d6f8b43.html">搜索商品</a>
                                            </li>
                                            <li>
                                                <a href="https://kf.dd373.com/helpdetail/e746dc8f2ed9478ca42e290f6f194980.html">购买商品</a>
                                            </li>
                                            <li>
                                                <a href="https://kf.dd373.com/helpdetail/840e85568ec141468953e72be6f7242c.html">购买求降价</a>
                                            </li>
                                            <li>
                                                <a href="https://kf.dd373.com/helpdetail/8d8faf8454a343dda7262efba32502fb.html">购买商城商品</a>
                                            </li>
                                </ul>
                            </div>
                            <div class="footer2-item width164">
                                <p class="footer-title">出售项目</p>
                                <ul>
                                            <li>
                                                <a href="https://kf.dd373.com/helpdetail/0d46178fb77e4f889e097ac077750cc3.html">发布商品</a>
                                            </li>
                                            <li>
                                                <a href="https://kf.dd373.com/helpdetail/78e1f90efede4860b513412ce5c32570.html">出货给收货商家</a>
                                            </li>
                                            <li>
                                                <a href="https://kf.dd373.com/helpdetail/9fa33de35a114f1dab54eabf473b64a2.html">管理发布的商品</a>
                                            </li>
                                            <li>
                                                <a href="https://kf.dd373.com/helpdetail/c12b3acec9224d59be610208db89674a.html">编辑发布的商品</a>
                                            </li>
                                </ul>
                            </div>
                            <div class="footer2-item width164">
                                <p class="footer-title">账户安全</p>
                                <ul>
                                            <li>
                                                <a href="https://kf.dd373.com/helpdetail/8003162d9ba547238b5dc3ab8bf1c9f9.html">实名认证</a>
                                            </li>
                                            <li>
                                                <a href="https://kf.dd373.com/helpdetail/b417d795c41e4799a5f65df93876a02e.html">绑定手机</a>
                                            </li>
                                            <li>
                                                <a href="https://kf.dd373.com/helpdetail/35c42b2a611748cdba72ec7c18e4839a.html">换绑邮箱</a>
                                            </li>
                                            <li>
                                                <a href="https://kf.dd373.com/helpdetail/e05d6795f52d4824a75f21ebbf881944.html">设置支付密码</a>
                                            </li>
                                            <li>
                                                <a href="https://kf.dd373.com/helpdetail/8adf1e4d4c804cd89acd9f83d5e73ffb.html">更换绑定手机</a>
                                            </li>
                                            <li>
                                                <a href="https://kf.dd373.com/helpdetail/a0baf96eb8cd4dc6aec36ef1583768eb.html">修改登录密码</a>
                                            </li>
                                </ul>
                            </div>
                            <div class="footer2-item width164">
                                <p class="footer-title">协议条款</p>
                                <ul>
                                            <li>
                                                <a href="https://kf.dd373.com/ServiceCenter/HelpDetail?id=a3c0dad4109b4a179197f1beb8865287">隐私政策</a>
                                            </li>
                                            <li>
                                                <a href="https://kf.dd373.com/helpdetail/78dba8ca31b44712aef8e923f6c61984.html">用户服务协议</a>
                                            </li>
                                </ul>
                            </div>
            </div>



            <div class="footer2-item2-right">
                <p class="footer-phone">0373-5805373</p>
                <p class="footer-phone-title">7×24小时客服热线</p>
                <p class="font12 color666 m-t17">（仅能呼入不能呼出，凡接到此来电必为诈骗）</p>
                <p class="advisory" onclick="OpenConsult()"><i class="icon-footer03"></i><span>24小时在线咨询</span></p>
                <p class="footer-phone-title m-t9">推荐在线咨询</p>
            </div>
            <p class="clear"></p>
        </div>
    </div>
    <div class="footer">        <!-- 用户中心底部-->        <div class="row ovh">            <div class="user-bottom">                <ul class="user-btmenu ovh">                    <li><a href="//about.dd373.com/" target="_blank">关于我们</a></li>                    <li><a href="//about.dd373.com/Index.html?catenum=3736" target="_blank">联系我们</a></li>                    <li><a href="//cms.dd373.com/default/complaint_opinion.html" target="_blank">投诉建议</a></li>                                        <li><a href="//about.dd373.com/Index.html?catenum=3734" target="_blank">诚聘英才</a></li>                    <li><a href="//publicimg.dd373.com/Upload/2021-02-02/11214897c2bf4696af4927ed454d9dd9.jpg" target="_blank">营业执照</a></li>                    <li><a href="//about.dd373.com/Index.html?catenum=3732&childcatenum=37325" target="_blank">免责声明</a></li>                   <li><a href="//tg.dd373.com/default/index.html" target="_blank">推广联盟</a></li>                    <li><a href="//point.dd373.com/default/m_club_index.html" target="_blank">会员俱乐部</a></li>                    <li><a href="//kf.dd373.com" target="_blank">客服中心</a></li>                    <li><a href="#">返回顶部</a></li>                </ul>                <ul class="ovh ko-record">                    <li><a href="http://sq.ccm.gov.cn/ccnt/sczr/service/business/emark/toDetail/92EFD34EEC9843F986C5166E32C2C1D6" target="_blank">豫网文[2017]1656-014号</a></li>                    <li><a href="https://beian.miit.gov.cn/" target="_blank"  rel="nofollow">豫ICP备10201480号</a></li>                    <li><a href="//publicimg.pp373.com/Upload/2021-07-13/9ddeef68-f89d-48d3-aead-b795bed7d42a.jpg" target="_blank">ICP证：豫B2-20110028</a></li>                    <li><a href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=41070202000193" target="_blank"  rel="nofollow"><i class="safe"></i>豫公网安备 41070202000193号</a></li>                </ul>                <p>Copyright&nbsp;&copy; 2008-现在<a href="//www.dd373.com" target="_blank">&nbsp;<span>DD373.com</span>&nbsp;新乡市嘟嘟网络技术有限公司</a>&nbsp;版权所有</p>            </div>            <div class="user-bticon" style="line-height:58px;">                <ul>                    <li><a href="http://sq.ccm.gov.cn/ccnt/sczr/service/business/emark/toDetail/92EFD34EEC9843F986C5166E32C2C1D6" target="_blank"  rel="nofollow"><img src="//cdnimg.dd373.com/newfile/common/images/default/bt01.png" alt="互联网文化经营单位"></a></li>                    <li><a href="http://www.cyberpolice.cn/wfjb/" target="_blank"  rel="nofollow"><img src="//cdnimg.dd373.com/newfile/common/images/default/bt02.png" alt="网络警察提醒您"></a></li>                    <li><a href="//ss.knet.cn/verifyseal.dll?sn=e13092911010042696ahvg000000&amp;comefrom=trust&amp;trustKey=dn&amp;trustValue=www.dd373.com" target="_blank"  rel="nofollow"><img src="//cdnimg.dd373.com/newfile/common/images/default/bt03.png" alt="可信网站身份认证"></a></li>                    <li><a href="//v.anquan.org/cert/site/?site=www.dd373.com&at=realname" target="_blank"  rel="nofollow"><img src="//cdnimg.dd373.com/newfile/usercenter/images/bt05.png" alt="安全联盟品牌验证"></a></li>                    <li><a href="https://v.pinpaibao.com.cn/authenticate/cert/?site=www.dd373.com&at=business" target="_blank"  rel="nofollow" style="background-color:#fff;"><img src="//cdnimg.dd373.com/newfile/usercenter/images/bt06.png" alt="安全联盟行业验证" width="96" height="36"></a></li>                </ul>            </div>        </div>    </div><script>(function(){    var bp = document.createElement('script');    var curProtocol = window.location.protocol.split(':')[0];    if (curProtocol === 'https') {        bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';    }    else {        bp.src = 'http://push.zhanzhang.baidu.com/push.js';    }    var s = document.getElementsByTagName("script")[0];    s.parentNode.insertBefore(bp, s);})();</script><script>(function(e){function t(e){var t=location.href,n=t.split("").reverse(),r=e.split(""),i=[];for(var s=0,o=16;s<o;s++)i.push(r[s]+(n[s]||""));return i.join("")}var n=/([http|https]:\/\/[a-zA-Z0-9\_\.]+\.so\.com)/gi,r=e.location.href;if(r&&!n.test(r)&&window.navigator.appName){var i="//s.360.cn/so/zz.gif",o="ab77b6ea7f3fbf79",u=t(o),a=new Image;r&&(i+="?url="+encodeURIComponent(r)),o&&(i+="&sid="+o),u&&(i+="&token="+u),o&&(a.src=i)}})(window);</script>
    <script src="//sta.dd373.com/file/general/Scripts/jquery-1.12.3.min.js"></script>
    <script src="//sta.dd373.com/newfile/common/js/game_area_selector.js"></script>
    <script src="//sta.dd373.com/file/general/Scripts/layer/layer.js"></script>
    <!--[if lt IE 10]>
        <script src="//sta.dd373.com/newfile/general/Scripts/jquery.placeholder.min.js"></script>
    <![endif]-->
    <!--[if lt IE 9]>
        <script src="//sta.dd373.com/file/general/Scripts/html5.js" type="text/javascript"></script>
    <![endif]-->

    <script src="//sta.dd373.com/newfile/common/js/ajax_filter.js"></script>
    <script src="//sta.dd373.com/newfile/consult/scripts/loadchat.js"></script>
    <script src="//sta.dd373.com/file/general/Scripts/idangerous.swiper.min.js"></script>
    <script src="//sta.dd373.com/newfile/common/js/default/mvc_header.js"></script>
    <script src="//sta.dd373.com/newfile/common/js/default/common.js"></script>
    <script src="//sta.dd373.com/newfile/common/js/right_hover.js"></script>
    <script src="//sta.dd373.com/file/general/Scripts/jquery.lazyload.min.js"></script>
    <script type="text/javascript" src=" //sta.dd373.com/newfile/common/js/default/bd_statistics.js"></script>
    
    <script src="//sta.dd373.com/newfile/common/js/default/slides.min.jquery.js"></script>
    <script src="//sta.dd373.com/newfile/goods/js/default/goods_list.js"></script>

    <script type='text/javascript'>
        $(function () {
            transferInfo({
                appid: "00c90442c2a3446d89eb80744bf88f73",
                showBtn: 0 //是否显示用户咨询入口  0：不显示   1：显示

            });
        })

        //举报
        function OpenConsult() {
            handAppend();
        }
    </script>
</body>
</html>'''
    # dealData(t1)

    reqpost()


