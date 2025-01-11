import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 读取文件
data = pd.read_csv('bike.csv')

# 剔除id列
data.drop(columns=['id'], inplace=True)

# 筛选并剔除city列
data = data[data['city'] == 1]
data.drop(columns=['city'], inplace=True)
data['hour'] = data['hour'].apply(lambda x: 1 if 6 <= x <= 18 else 0)

# 提取y列为预测目标，并转换为numpy列向量，剔除原y列
y = data['y'].values
data.drop(columns=['y'], inplace=True)

# 将DataFrame对象转换为Numpy数组
X = data.values

# 划分原始数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 分别归一化
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 构建一个线性回归模型,调整模型参数,优化预测性能
model = LinearRegression()
model.fit(X_train, y_train)

# 利用测试集对训练好的模型进行评估
y_predict = model.predict(X_test)

# 模型评估
rmse = np.sqrt(mean_squared_error(y_test, y_predict))
print(f'RMSE: {rmse}')
