from urllib import request, parse, error
from http import cookiejar
import json


#  以下返回值为相应的网页代码的字符串，并非字节类型
#  若返回json数据，需要用json.loads()进行处理后方能取值
# 普通请求
def get_url(url):
    try:
        response = request.urlopen(url=url)
    except error.HTTPError:
        print(url + "  url请求发生错误")
    except error.URLError:
        print(url + "  http请求错误")
    else:
        return response.read().decode()


# 加请求头
def get_url_header(url, headers={}, params={}):
    try:
        resq = request.Request(url=url, headers=headers)
        data = parse.urlencode(params).encode()
        if data:
            response = request.urlopen(resq, data=data)
        else:
            response = request.urlopen(resq)
    except error.URLError:
        print(url + "  url请求发生错误")
    except error.URLError:
        print(url + "  http请求错误")
    else:
        return response.read().decode()


# 可以添加代理和cookie
def get_url_proxy(url, headers={}, params={}, proxies={}):
    try:
        hander = request.ProxyHandler(proxies=proxies)
        # 登录时获得cookie, 创建cookieJar对象，并创建cookie处理器
        # cookie = cookiejar.CookieJar()
        # hander_cookie = request.HTTPCookieProcessor(cookie)
        opener = request.build_opener(hander)
        resq = request.Request(url=url, headers=headers)
        data = parse.urlencode(params).encode()
        if data:
            response = opener.open(resq, data=data)
        else:
            response = opener.open(resq)
    except error.URLError:
        print(url + "  url请求发生错误")
    except error.URLError:
        print(url + "  http请求错误")
    else:
        return response.read().decode()


if __name__ == '__main__':
    url = "https://www.v2ex.com/?tab=jobs"
    json_url = "http://fanyi.baidu.com/v2transapi"
    params = {
        "from": "zh",
        "to": "en",
        "query": "你阿虎哦",
        "transtype": "realtime",
        "simple_means_flag": "3",
        "sign": "21412.307349",
        "token": "758fabc439dedf55f68c6e8a64f4d3a1",
    }
    headers = {
        "Accept": "*/*",
        # "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "152",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "BAIDUID=7AF8A8EE39CF33E65F3E3FC530E7B04C:FG=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BIDUPSID=7AF8A8EE39CF33E65F3E3FC530E7B04C; PSTM=1522122198; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1522209820,1522374540,1522491815,1522722782; H_PS_PSSID=1424_21081_22159; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1522763333; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D",
        "Host": "fanyi.baidu.com",
        "Origin": "http://fanyi.baidu.com",
        "Referer": "http://fanyi.baidu.com/",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }
    json_data = get_url_proxy(json_url, params=params, headers=headers)
    # print(json_data)
    data = json.loads(json_data)
    print(data.get("trans_result").get("data"))
