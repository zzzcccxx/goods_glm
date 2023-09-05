import csv
import json

with open('../my_data/input/test.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = []
    for row in reader:
        text = row['text'].replace(' ', '')
        bio = row['bio'].split()
        pola = row['pola'].split()
        summary = ''
        for i, tag in enumerate(bio):
            # import pdb;pdb.set_trace()
            if tag == 'B-ASP':
                start = i
                while i+1 < len(bio) and bio[i+1] == 'I-ASP':
                    i += 1
                end = i
                aspect = text[start:end+1]
                sentiment = '好评' if pola[start] == '2' else '差评'
                # summary += f'主体为：{aspect}，情感为：{sentiment}。'
                summary += f'{aspect}，{sentiment}'
        data.append({'content': text, 'summary': summary})

with open('../my_data/input/test.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)