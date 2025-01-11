import pandas as pd

# 读取文件
file_path = r'D:/code/my_code/fraudulent.csv'
data = pd.read_csv(file_path)

# 查看数据的前几行
print(data.head())

# 查看每列的数据类型和缺失值情况
print(data.info())
print(data.isnull().sum())

# 删除缺失值过多的列（例如，缺失值超过50%的列）
threshold = len(data) * 0.5
data = data.dropna(thresh=threshold, axis=1)

# 使用众数填充剩余的缺失值
data = data.fillna(data.mode().iloc[0])

# 再次检查缺失值
print(data.isnull().sum())

from sklearn.model_selection import train_test_split

# 特征和标签
X = data.drop('y', axis=1)
y = data['y']

# 分割数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import f1_score

# 初始化模型
models = {
    'KNN': KNeighborsClassifier(), # K-近邻分类器
    'Decision Tree': DecisionTreeClassifier(random_state=1), #  决策树
    'Logistic Regression': LogisticRegression(max_iter=1000, random_state=1), # 逻辑回归
    'SVM': SVC(random_state=1) # 支持向量机
}
X_test = X_test.values # 避免数据类型不兼容，将 Pandas DataFrame 转换为 NumPy 数组

# 训练模型并计算F1值
f1_scores = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test) # 预测结果
    f1_scores[name] = f1_score(y_test, y_pred)

# 打印F1值
for name, score in f1_scores.items():
    print(f'{name} F1 Score: {score:.4f}')
# F1分数的取值范围是0到1，值越接近1表示模型的性能越好