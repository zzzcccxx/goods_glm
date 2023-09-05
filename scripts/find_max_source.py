import json

with open('../my_data/input/train.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    max_length = max([len(item['content']) for item in data])
    print(f'最长的content的长度是: {max_length}')
