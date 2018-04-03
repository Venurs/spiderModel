import requests
from urllib import error


#  使用requests模块中的session发起请求,可以携带请求头,参数,代理
#  若请求方式为get,需要将12行的post方法改为get
def get_for_session(url, headers={}, params={}, proxies={}):
    try:
        session = requests.Session()
        session.headers.update(headers)
        session.proxies.update(proxies)
        response = session.post(url=url, data=params)
    except error.HTTPError:
        print(url + "  url请求发生错误")
    except error.URLError:
        print(url + "  http请求错误")
    else:
        return response.content.decode()


if __name__ == '__main__':
    # url = "https://www.v2ex.com/?tab=jobs"
    # print(get_for_session(url=url))
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
    print(get_for_session(url=json_url, headers=headers, params=params))