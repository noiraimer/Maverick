# -*- coding: utf-8 -*-
"""Sample Configuration
"""

# For Maverick
site_prefix = "/"
template = "Kepler"
index_page_size = 10
archives_page_size = 30
fetch_remote_imgs = False
enable_jsdelivr = {
    "enabled": False,
    "repo": ""
}
locale = "Asia/Shanghai"
category_by_folder = True

enable_jsdelivr = {
    "enabled": True,
    "repo": "noiraimer/Mavrick@gh-pages"
}

# 站点设置
site_name = "解语知识"
site_logo = "${static_prefix}logo.png"
site_build_date = "2020/1/31 16:51"
author = "无尽藏海"
email = ""
author_homepage = "https://noiramr.cn"
description = "温故而知新"
key_words = ['blog']
language = 'zh-CN'
external_links = [
    {
        "name": "解语知音",
        "url": "https://noiramr.cn",
        "brief": "温故而知新",
        "target": "_self"
    },

]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "RSS",
        "url": "https://noiramr.cn/feed/index.xml",
        "icon": ""
    },
    {
        "name": "GitHub",
        "url": "https://github.com/noiraimer",
        "icon": ""
    },
        {
        "name": "邮件",
        "url": "mailto:liushu1187419589@live.com",
        "icon": ""
    },
    {
        "name": "语雀",
        "url": "https://www.yuque.com/blancaimer",
        "icon": ""
    },
]

valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "A5LqJrDsqGpBkcSAG6rOaquz-gzGzoHsz",
    "appKey": "MpkTdroEzvOmHrw5l1vnX8Oq",
    "placeholder": "想破脑袋也不知道提示语写啥"
}

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
<link rel="dns-prefetch" href="//noiramr.cn" />
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/noiraimer/Blog-With-GitHub-Boilerplate@gh-pages/css/custom.css">
<script src="https://cdn.jsdelivr.net/gh/noiraimer/Blog-With-GitHub-Boilerplate@gh-pages/js/instant.js" type="module" defer integrity="sha384-OeDn4XE77tdHo8pGtE1apMPmAipjoxUQ++eeJa6EtJCfHlvijigWiJpD7VDPWXV1"></script>
<script src="https://cdn.jsdelivr.net/gh/noiraimer/Blog-With-GitHub-Boilerplate@gh-pages/js/email-decode.min.js"></script>
<link rel="shortcut icon" href="${static_prefix}favicon.ico?v=yyLyaqbyRG">
'''

footer_addon = r'''

'''

body_addon = r'''

'''
main_addon = r'''

'''
