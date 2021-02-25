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



all_data = pd.read_csv('./data/data_v1.csv')
print("Shape:", all_data.shape)
print(all_data.head())

all_data = all_data.astype({'Arbitrator_id': 'object'})
for col in all_data.columns:
    if all_data.dtypes[col] == "object":
        all_data[col] = LabelEncoder().fit_transform(all_data[col])

print(all_data.Case_nature.head())



