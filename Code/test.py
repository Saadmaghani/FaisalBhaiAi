# from EK_modified import edmonds_karp
#
# import networkx as nx
#
# G = nx.DiGraph()
# G.add_edge("x", "a", capacity=3.0)
# G.add_edge("x", "b", capacity=1.0)
# G.add_edge("a", "c", capacity=3.0)
# G.add_edge("b", "c", capacity=5.0)
# G.add_edge("b", "d", capacity=4.0)
# G.add_edge("d", "e", capacity=2.0)
# G.add_edge("c", "y", capacity=2.0)
# G.add_edge("e", "y", capacity=3.0)
#
# R = edmonds_karp(G, "x", "y")
# flow_value = nx.maximum_flow_value(G, "x", "y")
# print(flow_value)
#
# flow_value == R.graph["flow_value"]
#
# print(flow_value)

# importing libraries

import pandas as pd
import numpy as np
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import torch
from torch.utils.data import Dataset, DataLoader
import torch.optim as torch_optim
import torch.nn as nn
import torch.nn.functional as F
from datetime import datetime


# importing data & viewing
raw_data = pd.read_csv('./data/data_v1.csv')
print("Shape:", raw_data.shape)
print(raw_data.head())

# onehot enocoding categorical data
mod1_data = raw_data.astype({'Arbitrator_id': 'object'})
mod2_data = mod1_data.copy()
for col in mod1_data.columns:
    if mod1_data.dtypes[col] == "object":
        mod1_data[col] = LabelEncoder().fit_transform(mod1_data[col])
        n = np.max(mod1_data[col])
        mod2_data[col] = torch.nn.functional.one_hot(torch.from_numpy(mod1_data[col].to_numpy()), int(n) + 1).tolist()

print(raw_data.head())
print(mod1_data.head())
print(mod2_data.head())

# splitting into train:validation:test
data_split = [0.6, 0.2, 0.2]
N = mod2_data.shape[0]
train_size = int(N*data_split[0])
valid_size = int(N*data_split[1])

train = mod2_data[:train_size]
valid = mod2_data[train_size: train_size + valid_size]
test = mod2_data[train_size+valid_size:]

print("train:", train.shape)
print("valid:", valid.shape)
print("test:", test.shape)

Ytrain = train.iloc[:, -1]
Xtrain = train.iloc[:, :-1]

Yvalid = valid.iloc[:, -1]
Xvalid = valid.iloc[:, :-1]

Ytest = test.iloc[:, -1]
Xtest = test.iloc[:, :-1]

# xTrain, xTest, yTrain, yTest, eyTrain, eyTest = train_test_split(self.fnames, self.labels, self.encoded_labels, test_size = pc_splits[-1], random_state=self.seed)
#         xVal = []
#         yVal = []
#         eyVal = []
#         if len(pc_splits) == 3:
#             xTrain, xVal, yTrain, yVal, eyTrain, eyVal = train_test_split(xTrain, yTrain, eyTrain, test_size = pc_splits[1]/(pc_splits[0]+pc_splits[1]), random_state=self.seed)
#
#         partition = {'train': xTrain, 'validation': xVal, 'test': xTest}
#         labels = {'train': yTrain, 'validation': yVal, 'test': yTest}
#         encoded = {'train': eyTrain, 'validation': eyVal, 'test': eyTest}
#         return (partition, labels, encoded)
#
#
