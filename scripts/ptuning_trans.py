import json

with open('../my_data/input/test.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('../my_data/input/pt_test.json', 'w', encoding='utf-8') as f:
    for item in data:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')
