# !/usr/bin/env python3
"""

测试训练好的打分模型。

"""
import torch
from rich import print
from transformers import AutoTokenizer

device = 'cpu'
tokenizer = AutoTokenizer.from_pretrained('./checkpoints/reward_model/sentiment_analysis/model_best/')
model = torch.load('./checkpoints/reward_model/sentiment_analysis/model_best/model.pt')
model.to(device).eval()

texts = [
    '买过很多箱这个苹果了，一如既往的好，汁多味甜～',
    '一台充电很慢，信号不好！退了！又买一台竟然是次品。。服了。。'
]
inputs = tokenizer(
    texts, 
    max_length=128,
    padding='max_length', 
    return_tensors='pt'
)
r = model(**inputs)
print(r)