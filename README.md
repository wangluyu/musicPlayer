
#### 需求分析
在网易云音乐(以下简称网易云)听歌时,遇到喜欢的歌曲想下载,有时候因为版权原因,需要购买会员才能下载,可是我是穷逼没有钱,所以这个需求就应运而生୧(๑•̀◡•́๑)૭

#### 所用技术
- 前端:
    - vue : https://cn.vuejs.org/index.html
    - vux : https://vux.li/#/
- 后端:
    - python
    - Django
- 数据库
    - MySQL
#### 实现思路
- 做一个页面,通过用户id获取到用户的歌单,列出来,在后面放一个下载按钮
- 通过分析网易云音乐的http请求包来解析出MP3的url,从而实现下载功能
- 用到Wireshark等工具

#### 预计开发时间:一个月(因为只有周末有时间)

#### 目录结构
├── backend                 后端
|   ├── views.py
|   └── models.py
├── frontend                前端
|   ├── src
|   |   ├── assets
|   |   ├── components
|   |   ├── router
|   |   ├── App.vue
|   |   └── main.js
|   ├── config
|   └── package.json
├── musicPlayer
|   ├── footer.html
|   └── header.html
└── README.md
#### url&api
- 歌曲
    - https://music.163.com/#/song?id=408532862
    -
