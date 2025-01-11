import networkx as nx
import matplotlib.pyplot as plt
import math


# 用户和边的数据
users = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
edges = [(0, 1), (1, 0), (0, 2), (2, 0), (1, 2), (2, 1), (1, 3), (2, 3), (3, 4), (5, 4), (5, 6), (7, 5), (6, 8), (8, 7), (8, 9)]

# 创建有向图
G_directed = nx.DiGraph()
G_directed.add_nodes_from(users)
G_directed.add_edges_from(edges)

# 可视化有向图
plt.figure(figsize=(10, 8))
nx.draw(G_directed, with_labels=True, node_color='lightgreen', node_size=2000, font_size=12, font_weight='bold', arrows=True)
plt.title("有向图")
plt.show()


# 计算PageRank值
pagerank_values = nx.pagerank(G_directed)

# 打印PageRank值
for node, rank in pagerank_values.items():
    print(f"Node {node}: PageRank = {rank:.4f}")

# 根据PageRank值调整节点大小
node_sizes = [(2*v - 0.1) * 20000 for v in pagerank_values.values()]
print(node_sizes)

# 可视化调整后的有向图
plt.figure(figsize=(10, 8))
nx.draw(G_directed, with_labels=True, node_color='lightcoral', node_size=node_sizes, font_size=12, font_weight='bold', arrows=True)
plt.title("PageRank:")
plt.show()