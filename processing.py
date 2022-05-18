import os
import json
import requests

url = 'https://br.crossfire.z8games.com/rest/ranking.json'
headers = {
    'Accept': '*/*',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5',
    'Connection': 'keep-alive',    
    'Referer': 'https://br.crossfire.z8games.com/playerranking.html',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Security-Request': 'required',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

def getValue(data, key):
    if data == None:
        pass
    else:
        return data.get(key)

def getResponse(url, params):
    response = requests.get(url, params, headers=headers).json()
    if getValue(response, 'Ranking') == None:
      pass
    else:
      ranklist = getValue(getValue(response, 'Ranking'), 'RankList')
      if ranklist == None:
        pass
      else:
        for s in range(len(ranklist)):
            value = getValue(ranklist[s], 'ign')
            if value != getValue(params, 'name'):
                pass
            else:
                return ranklist[s]

def process_data(input_data):
    if os.path.exists("result/perfis.txt"):
      os.remove("result/perfis.txt")
    else:
      pass
      
    result=[]
    for nick in input_data.splitlines():
      params = {'startrow': 0,
          'endrow': 9999,
          'name': nick,
          'rankType': 'user',
          'period': 'all'}
      Response = getResponse(url, params)
      if Response == None:
        result.append(str(getValue(params, 'name'))+" -> Nickname não encontrado!")
        pass
      else:
        result.append('https://br.crossfire.z8games.com/profile/'+str(getValue(Response, 'usn'))) 
    return result

