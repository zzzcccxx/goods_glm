import json
import random

with open('/root/autodl-tmp/my_data/input/train.json', 'r') as f:
    data = json.load(f)

random.shuffle(data)

with open('/root/autodl-tmp/my_data/input/shuffle_train.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
