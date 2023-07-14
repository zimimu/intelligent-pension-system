import urllib.parse
import urllib.request
import json

def sendMobile_test(id, content):

    phoneurl = "http://localhost:8000/manage/getGuartionPhone/?id=" + id
    phoneRequest = urllib.request.Request(phoneurl)
    phoneResponse = urllib.request.urlopen(phoneRequest)
    phoneRes = phoneResponse.read()
    mobile = json.loads(phoneRes).get("phone")

    # 接口地址
    url = 'https://106.ihuyi.com/webservice/sms.php?method=Submit'

    # 定义请求的数据
    values = {
        'account': 'C21449632',
        'password': '7ebf2a47df890290908a9c9f968c1063',
        'mobile': mobile,
        'content': "您的验证码是：0001。请不要把验证码泄露给其他人。",
        'format': 'json',
    }
    # 将数据进行编码
    data = urllib.parse.urlencode(values).encode(encoding='UTF8')
    # 发起请求
    req = urllib.request.Request(url, data)
    response = urllib.request.urlopen(req)
    res = response.read()

    # 打印结果
    print(res.decode("utf8"))


