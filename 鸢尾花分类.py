# -*- coding: utf-8 -*-
# 导入必要的库
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, recall_score, f1_score, confusion_matrix
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 设置matplotlib支持中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 1. 加载数据
iris = load_iris()
X = iris.data
y = iris.target

# 2. 划分数据集
# 测试集比例0.2，随机种子42
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. 创建并训练SVM模型
# 使用线性核函数，随机种子42
svm_model = SVC(kernel='linear', random_state=42)
svm_model.fit(X_train, y_train)

# 4. 预测
y_pred = svm_model.predict(X_test)

# 5. 评估模型
# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
# 计算召回率（多分类使用macro平均）
recall = recall_score(y_test, y_pred, average='macro')
# 计算F1分数（多分类使用macro平均）
f1 = f1_score(y_test, y_pred, average='macro')
# 计算混淆矩阵
conf_matrix = confusion_matrix(y_test, y_pred)

# 打印评估结果
print(f'准确率 (Accuracy): {accuracy:.4f}')
print(f'召回率 (Recall): {recall:.4f}')
print(f'F1分数 (F1 Score): {f1:.4f}')
print('\n混淆矩阵 (Confusion Matrix):')
print(conf_matrix)

# 6. 可视化混淆矩阵
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.title('SVM分类器的混淆矩阵')
plt.xlabel('预测类别')
plt.ylabel('真实类别')
plt.show() 