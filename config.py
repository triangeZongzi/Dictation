class Config():
    def __init__(self):
        self.hd = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
        self.regular = r'<li>(.*?)</li>'
        self.listionUrl_AM = r'http://dict.youdao.com/dictvoice?type=0&audio=' # 美音(type=0)  英音(type=1)
        self.listionUrl_EN = r'http://dict.youdao.com/dictvoice?type=1&audio=' # 美音(0)  英音(1)
        self.er = ['<a href="#" rel="eng" class="current">中英</a>', '<a href="#" rel="fr">中法</a>', '<a href="#" rel="ko">中韩</a>', '<a href="#" rel="jap">中日</a>']
        # self.url = r"http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
        # self.fdata = {
        #     'i': 'word',
        #     'from': 'AUTO',
        #     'to': 'AUTO',
        #     'smartresult': 'dict',
        #     'client': 'fanyideskweb',
        #     'salt': '16008451647541',
        #     'sign': 'b653d9bdea7545237c3f2ae9f077d3f4',
        #     'lts': '1600845164754',
        #     'bv': '5b2e9b3c54358519b916b1be9e5e4a6a',
        #     'doctype': 'json',
        #     'version': '2.1',
        #     'keyfrom': 'fanyi.web',
        #     'action': 'FY_BY_REALTlME'
        # }
        # self.regular = r'"tgt":"(.*?)"}]]'