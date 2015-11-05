#!/usr/bin/env python
#encoding:utf-8
import requests
import re
import random_user_agent
import json
from memberlist import uid
import time
import string

#send group not finish
_member = uid.getuid()

p1 = re.compile(r'"st":"\w{6}"')

#p4 get weibo
p4 = re.compile(r'm.weibo.cn\\/\d+\\/\w+')

#get comment_id
p5 = re.compile(r'"id":\d+')
t_p = re.compile(r'"st":"\w+')


class Weibo(object):
    def __init__(self, username, password):
        login_header= {
            'Host': 'passport.weibo.cn',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:41.0) Gecko/20100101 \
            Firefox/41.0',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Referer': 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel& \
            wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F',
            'Connection': 'keep-alive'
        }
        data = {
            'ec':'0',
            'entry':'mweibo',
            'pagerefer':'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=\
                http%3A%2F%2Fm.weibo.cn%2F&wm=3349&vt=4',
            'password':password,
            'savestate':'1',
            'username':username
        }
        self.s = requests.Session()
        self.request_login = self.s.post('https://passport.weibo.cn/sso/login', \
        data = data, headers = login_header)
    
    def sendmessage(self, uid, content):
        chat_header = {
            'Host': 'm.weibo.cn',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:41.0) \
             Gecko/20100101 Firefox/41.0',
            'Accept': 'application/json',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'http://m.weibo.cn/msg/chat?uid=',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache'
        }
        chat_header['Referer'] = chat_header['Referer'] + uid
        datas = {
            'content':content,
            'st':None,
            'uid':uid
        }
        _t = self.s.get('http://m.weibo.cn/msg/chat?uid=' + uid).content
        get_st = p1.findall(_t)[0][6:-1]
        datas['st'] = get_st
        datas['content'] = content
        datas['uid'] = uid
        print self.s.post('http://m.weibo.cn/msgDeal/sendMsg?', datas, headers=chat_header).content
    
    def comment(self, uid, content):
        _head = {
            'Host': 'm.weibo.cn',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Connection': 'keep-alive'
        }
        res = self.s.get('http://m.weibo.cn/u/' + uid)

        _tm = str(time.time())
        en = _tm[0:10]+_tm[-2:]+'1_6'
        weibo_url_1 = 'http://m.weibo.cn/page/card?itemid=100505'
        weibo_url_2 = '_-_WEIBO_INDEX_PROFILE_WEIBO_GROUP_OBJ&callback=_'+en
        weibo_url = weibo_url_1 + uid + weibo_url_2 
        zzz = self.s.get(weibo_url).content
        weibo_u = p4.findall(zzz)[0].split('\/')[2]
        _ul = 'http://m.weibo.cn/' + uid + '/' + weibo_u
        c1 = self.s.get(_ul).content
        st = t_p.findall(c1)[0].split(':"')[1].strip("'")
        comment_id = p5.findall(c1)
        _xt = comment_id[0].split('":')[1]
        po_data={
            'content' : content,
            'id' : _xt,
            'st' : st
        }
        self.s.headers['Referer'] = 'http://m.weibo.cn/comment?id=' + _xt
        print self.s.post('http://m.weibo.cn/commentDeal/addCmt', data = po_data).content

if __name__ == '__main__':
    #test
    pass
