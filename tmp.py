import json
with open('test_jsons/extended.json') as f:
    templates = json.load(f)
js = templates
result = []
for check in js['checks']:
    result.append([check['checkId'],check["code"],check["checkStatus"]["code"]])
    
print(result)