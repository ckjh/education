import urllib, sys,json
import ssl
import requests
# 获取鉴权机制中的token
def BaiduAi(p):
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=W9iKdZZWbjFo8oDWbFG5alKL&client_secret=60XZh0mcWeZbStjXAOddg0R3dT5X8KBu'
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    response = requests.post(url=host, headers=headers)
    content = json.loads(response.text)
    # print(content)
    access_token = content['access_token']
    # 调用接口判断语言是否违规
    host = 'https://aip.baidubce.com/rest/2.0/antispam/v2/spam?access_token=24.02e943f00454ed45a3ddfaee96aabd8f.2592000.1574321549.282335-17592823'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    params = {'content': p}
    response = requests.post(url=host, headers=headers, data=params)
    result = json.loads(response.text)  # 0表示非违禁，1表示违禁，2表示建议人工复审
    ret = result['result']['spam']
    dict={}
    dict['code'] = ret
    if dict['code']==0:
        dict['mes']='审核通过'
    elif dict['code']==1:
        dict['mes']='审核未通过'
    else:
        dict['mes']='建议人工复审'
    print(dict)
