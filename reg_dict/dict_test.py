# -*- encoding: utf-8 -*-
import json
from pprint import pprint
scores = {'(yuwen)': {'(语文)': 89, 'math': 92, 'english': 93}, 'math': 92, 'english': 93}
print(scores)
with open('./data.json','w',encoding="utf-8") as f:
    #f.write(json.dumps(scores))
    json.dump(scores,f,ensure_ascii=False,indent=4)
    #json.dump(scores,f)
with open('./data.json','r',encoding="utf-8") as f:
    #f.write(json.dumps(scores))
    ret=json.load(f)
    print(ret['(yuwen)'])
    print(ret['math'])
    print(ret)
    pprint(ret)
