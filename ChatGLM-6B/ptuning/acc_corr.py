import json
from scipy.stats import pearsonr
from sklearn.preprocessing import LabelEncoder

# '/root/autodl-tmp/ChatGLM_6B/ptuning/output/4bit_1000step_e3lr-chatglm-6b-pt-128-5e-3/generated_predictions.txt'
with open('/root/autodl-tmp/ChatGLM_6B/ptuning/output/1000step_e3lr-chatglm-6b-pt-64-5e-3/generated_predictions.txt', 'r') as f:
    data = f.readlines()

correct = 0
total = 0
labels = []
predicts = []

for line in data:
    line_data = json.loads(line)
    label = line_data['labels']
    predict = line_data['predict']
    if label == predict:
        correct += 1
    total += 1
    labels.append(label)
    predicts.append(predict)

le = LabelEncoder()
le.fit(labels + predicts)
labels = le.transform(labels)
predicts = le.transform(predicts)
# import pdb;pdb.set_trace()
acc = correct / total
corr, _ = pearsonr(labels, predicts)

print(f'准确率: {acc}')
print(f'相关性: {corr}')
