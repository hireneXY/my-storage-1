import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# 读取文件
file_path = r'D:/code/my_code/github_bot_processed_data.csv'
data = pd.read_csv(file_path)

# 设置Pandas显示选项
pd.set_option('display.max_rows', 100)  # 最多100行
pd.set_option('display.max_columns', 50)  # 最多50列

# 查看数据的前几行
print(data.head())

# 查看每列的数据类型
print(data.info())

# 数据的描述性统计信息
print(data.describe())

# 对数变换
data['log_public_repos'] = np.log1p(data['public_repos'])
data['log_public_gists'] = np.log1p(data['public_gists'])
data['log_followers'] = np.log1p(data['followers'])
data['log_following'] = np.log1p(data['following'])

# 查看对数变换后的数据
print(data[['public_repos', 'log_public_repos', 'public_gists', 'log_public_gists', 'followers', 'log_followers', 'following', 'log_following']].head())

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 条形图：展示 label 列的类别分布
label_counts = data['label'].value_counts()
plt.figure(figsize=(8, 6))
sns.barplot(x=label_counts.index, y=label_counts.values)
plt.title('Bot 和 Human 类型的数量')
plt.xlabel('类型')
plt.ylabel('数量')
plt.show()

# 堆积柱状图：展示多个布尔特征的分布
bool_features = ['site_admin', 'hireable']
stacked_data = data[bool_features + ['label']].groupby(['label']).sum()
stacked_data.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('布尔特征在不同标签中的分布')
plt.xlabel('类型')
plt.ylabel('数量')
plt.legend(title='布尔特征')
plt.show()

# 直方图：展示 log_public_repos 的对数变换后的数据分布
plt.figure(figsize=(12, 6))
plt.hist(data['log_public_repos'], bins=30, color='blue', alpha=0.7)
plt.title('log_public_repos 的分布')
plt.xlabel('log_public_repos')
plt.ylabel('数量')
plt.show()

# 散点图：展示 public_repos 与 followers 之间的关系
plt.figure(figsize=(10, 6))
plt.scatter(data['public_repos'], data['followers'], alpha=0.5, color='red')
plt.title('public_repos 与 followers 之间的关系')
plt.xlabel('public_repos')
plt.ylabel('followers')
plt.show()

# 散点矩阵：展示多个数值型特征之间的成对关系
numeric_features = ['public_repos', 'public_gists', 'followers', 'following', 'log_public_repos', 'log_public_gists', 'log_followers', 'log_following']
pd.plotting.scatter_matrix(data[numeric_features], figsize=(15, 15), alpha=0.5)
plt.suptitle('数值型特征之间的成对关系', y=1.02)
plt.show()

# 箱线图：展示不同 label 类别下 log_followers 的分布
plt.figure(figsize=(10, 6))
sns.boxplot(x='label', y='log_followers', data=data)
plt.title('不同标签类别下 log_followers 的分布')
plt.xlabel('类型')
plt.ylabel('log_followers')
plt.show()

# 成对图：展示不同特征之间的成对关系，并根据 label 分类
sns.pairplot(data[numeric_features + ['label']], hue='label', diag_kind='kde', plot_kws={'alpha': 0.5}, diag_kws={'shade': True})
plt.suptitle('不同特征之间的成对关系', y=1.02)
plt.show()

# 热图：展示 log_public_repos, log_public_gists, log_followers 和 log_following 等特征之间的相关性
correlation_matrix = data[numeric_features].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('特征之间的相关性')
plt.show()

# 小提琴图：展示 label 与 log_followers 之间的分布差异
plt.figure(figsize=(10, 6))
sns.violinplot(x='label', y='log_followers', data=data)
plt.title('不同标签类别下 log_followers 的分布差异')
plt.xlabel('类型')
plt.ylabel('log_followers')
plt.show()