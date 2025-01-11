# -*- coding: utf-8 -*-
# 导入必要的库
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 设置matplotlib支持中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 1. 加载数据
iris = load_iris()
X = iris.data
y = iris.target  # 真实标签，仅用于比较

# 2. 直接聚类
kmeans = KMeans(n_clusters=3, random_state=0)
clusters = kmeans.fit_predict(X)

# 3. PCA降维后可视化
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# 绘制直接聚类的结果
plt.figure(figsize=(12, 5))
plt.subplot(121)
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=clusters, cmap='viridis')
plt.title('直接聚类后的结果')
plt.xlabel('第一主成分')
plt.ylabel('第二主成分')
plt.colorbar(scatter)

# 4. 先降维再聚类
kmeans_pca = KMeans(n_clusters=3, random_state=0)
clusters_pca = kmeans_pca.fit_predict(X_pca)

# 绘制先降维再聚类的结果
plt.subplot(122)
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=clusters_pca, cmap='viridis')
plt.title('PCA降维后聚类的结果')
plt.xlabel('第一主成分')
plt.ylabel('第二主成分')
plt.colorbar(scatter)
plt.tight_layout()
plt.show()

# 5. 计算并比较轮廓系数
silhouette_direct = silhouette_score(X, clusters)
silhouette_pca = silhouette_score(X_pca, clusters_pca)

print("聚类效果评估（轮廓系数）：")
print(f"直接聚类的轮廓系数: {silhouette_direct:.4f}")
print(f"PCA降维后聚类的轮廓系数: {silhouette_pca:.4f}")

# 6. 绘制不同聚类数的轮廓系数
silhouette_scores = []
K = range(2, 11)

for k in K:
    kmeans = KMeans(n_clusters=k, random_state=0)
    clusters = kmeans.fit_predict(X)
    silhouette_scores.append(silhouette_score(X, clusters))

plt.figure(figsize=(10, 6))
plt.plot(K, silhouette_scores, 'bo-')
plt.xlabel('聚类数量')
plt.ylabel('轮廓系数')
plt.title('轮廓系数与聚类数量的关系')
plt.grid(True)
plt.show()

# 7. 计算并显示最佳聚类数
best_k = K[np.argmax(silhouette_scores)]
print(f"\n根据轮廓系数，最佳聚类数量为: {best_k}") 