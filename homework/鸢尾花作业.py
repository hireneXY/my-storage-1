import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 加载数据
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 数据划分
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 数据可视化：以花萼长度为横轴，花萼宽度为纵轴绘制数据的散点图
plt.figure(figsize=(10, 5))

# 绘制训练集
plt.subplot(1, 2, 1)
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='viridis', edgecolor='k', s=50)
plt.title('Training Set: Length & Width')
plt.xlabel('Length')
plt.ylabel('Width')

# 绘制测试集
plt.subplot(1, 2, 2)
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap='viridis', edgecolor='k', s=50)
plt.title('Test Set: Length & Width')
plt.xlabel('Length')
plt.ylabel('Width')

plt.tight_layout()
plt.show()

# PCA 降维
# 标准化特征
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)

plt.figure(figsize=(8, 6))
# 训练集散点图
plt.scatter(X_train_pca[:, 0], X_train_pca[:, 1], c=y_train, cmap='viridis', s=50, label='Train')
# 测试集散点图
plt.scatter(X_test_pca[:, 0], X_test_pca[:, 1], c=y_test, cmap='viridis', s=50, marker='x', label='Test')
plt.title('PCA')
plt.xlabel('Component 1')
plt.ylabel('Component 2')
plt.legend()
plt.show()

# 训练 KNN 分类器
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_pca, y_train)

# 模型评估
y_predict = knn.predict(X_test_pca)
accuracy = accuracy_score(y_test, y_predict)
print(f'Classification Accuracy: {accuracy: .2f}')