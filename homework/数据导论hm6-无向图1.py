import networkx as nx
import matplotlib.pyplot as plt

# 用户和边的数据
user = [1, 2, 3, 4]
edge = [(1, 2), (2, 3), (3, 4), (4, 1)]

# 创建无向图
G_undirected = nx.Graph()
G_undirected.add_nodes_from(user)
G_undirected.add_edges_from(edge)

# 可视化无向图
plt.figure(figsize=(8, 6))
nx.draw(G_undirected, with_labels=True, node_color='skyblue', node_size=2000, font_size=16, font_weight='bold')
plt.title("无向图")
plt.show()