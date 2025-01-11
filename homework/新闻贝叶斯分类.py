# -*- coding: utf-8 -*-
# 导入必要的库
# 使用新闻集也遇到403错误，只好使用一个更简单的数据集来演示朴素贝叶斯分类器：sklearn自带的手写数字数据集——digits数据集，代替新闻数据集
from sklearn.datasets import load_digits  # 改用digits数据集
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, f1_score, confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 设置matplotlib支持中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 1. 加载数据
print("正在加载数据...")
digits = load_digits()
X = digits.data
y = digits.target

# 2. 划分数据集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. 创建并训练朴素贝叶斯分类器
print("训练模型中...")
nb_classifier = MultinomialNB()
nb_classifier.fit(X_train, y_train)

# 4. 预测
y_pred = nb_classifier.predict(X_test)

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
print('\n模型评估结果：')
print(f'准确率 (Accuracy): {accuracy:.4f}')
print(f'召回率 (Recall): {recall:.4f}')
print(f'F1分数 (F1 Score): {f1:.4f}')

# 6. 可视化混淆矩阵
plt.figure(figsize=(10, 8))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.title('朴素贝叶斯分类器的混淆矩阵')
plt.xlabel('预测类别 (Predicted)')
plt.ylabel('真实类别 (Actual)')
plt.tight_layout()
plt.show()

# 7. 显示一些数字图像示例
plt.figure(figsize=(10, 5))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(digits.images[i], cmap='binary')
    plt.title(f'数字: {digits.target[i]}')
    plt.axis('off')
plt.tight_layout()
plt.show() 