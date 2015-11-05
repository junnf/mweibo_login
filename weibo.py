#!/usr/bin/env python
#encoding:utf-8
import requests
import re
import random_user_agent

from memberlist import uid

_member = uid.getuid()
p1 = re.compile(r'"st":"\w{6}"')
p2 = re.compile(r"'stageId':'\d{1,30}")
p3 = re.compile(r'data-jump="/\d{1,}/\w{1,}')
p3 = re.compile(r'data-jump=')
s = requests.Session()
login_header= {
    'Host': 'passport.weibo.cn',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Referer': 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F',
    #    'Cookie': '_T_WM=44f8e248f05dfd7bbc50a50ed88c31d8; SUHB=0oUZ0VH38QjkHn; H5_INDEX=0_all; H5_INDEX_TITLE=Demonc%E4%BF%8A%E5%AE%81',
    'Connection': 'keep-alive'
    }
data={
    'ec':'0',
    'entry':'mweibo',
    'pagerefer':'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F&wm=3349&vt=4',
    'password':'ljn7168396',
    'savestate':'1',
    'username':'13377881141'
    }
request_login = s.post('https://passport.weibo.cn/sso/login',data=data,headers=login_header)
#print x.status_code
_uid = [ x[0] for x in _member ]
new_header = {
    'Host': 'm.weibo.cn',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0',
    'Accept': 'application/json',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'http://m.weibo.cn/msg/chat?uid=',
    #'Cookie': '_T_WM=44f8e248f05dfd7bbc50a50ed88c31d8; SUHB=0btN1Al3SK2g5B; H5_INDEX=3; H5_INDEX_TITLE=Demonc%E4%BF%8A%E5%AE%81; M_WEIBOCN_PARAMS=luicode%3D20000173; WEIBOCN_WM=3349; backURL=http%3A%2F%2Fm.weibo.cn%2F; SUB=_2A257PcjtDeTxGeRP7VMX8ifPwj2IHXVYweilrDV6PUJbrdBeLXShkW1qvs2vP2AXGhmm8tk_chEfxjkE8Q..; SSOLoginState=1446623421',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'
    }
new_header['Referer'] = new_header['Referer'] + _uid[0]
datas = {
    'content':None,
    'st':None,
    'uid':None
    }
t = s.get('http://m.weibo.cn/msg/chat?uid='+_uid[0]).content
get_st = p1.findall(t)[0][6:-1]
datas['st'] = get_st
datas['content'] = 'nihao'
datas['uid'] = _uid
_head = {
'Host': 'm.weibo.cn',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
#Cookie: _T_WM=44f8e248f05dfd7bbc50a50ed88c31d8; SUHB=08JKvDsxQ_sFR8; H5_INDEX=3; H5_INDEX_TITLE=Demonc%E4%BF%8A%E5%AE%81; WEIBOCN_WM=3349; backURL=http%3A%2F%2Fm.weibo.cn%2F; SUB=_2A257PctBDeTxGeRP7VMX8ifPwj2IHXVYwdUJrDV6PUJbrdBeLW_5kW1MBFD1TsXPq_pr5Qcm3B0rHI90Bg..; SSOLoginState=1446624017; M_WEIBOCN_PARAMS=featurecode%3D20000181%26fid%3D1005053220473065%26uicode%3D20000058
'Connection': 'keep-alive'
}
res = s.get('http://m.weibo.cn/u/3220473065')
comment_url_head = 'http://m.weibo.cn/page/tpl?containerid='
comment_url_containerid = p2.findall(res.content)[0][11:]
comment_url_end = '_-_WEIBO_SECOND_PROFILE_WEIBO&itemid=&title=%E5%85%A8%E9%83%A8%E5%BE%AE%E5%8D%9A'
res = s.get(comment_url_head + comment_url_containerid + comment_url_end)
get_weibo = res.content
print get_weibo 
#print get_weibo
#p3.findall(get_weibo)[0]
#

