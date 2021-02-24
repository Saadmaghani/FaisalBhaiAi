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

all_data = pd.read_csv('./data/data_v1.csv')
print("Shape:", all_data.shape)
print(all_data.head())



