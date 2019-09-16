import requests

def send(mobile,captcha):
    url='http://v.juhe.cn/sms/send'
    params={
        'mobile':mobile,
        'tpl_id':'170434',
        'tpl_value':'#code#='+captcha,
        'key':'aa6ae1728b5ae046b0a23cc81baaa99a'
    }

    response=requests.get(url,params=params)
    # print(response.json())
    result=response.json()
    if result['error_code']==0:
        return True
    else:
        return False