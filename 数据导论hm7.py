import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# 导入文件
file_path = r'D:/code/my_code/github_bot_raw_data.csv'
raw_data = pd.read_csv(file_path)

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 列字段解读
columns = [
    'actor_id',  # GitHub用户的ID (示例值: 1081405)
    'label',  # 用户标签（"Human"或"Bot"） (示例值: Human)
    'login',  # GitHub用户的登录名 (示例值: dlazesz)
    'id',  # 用户的GitHub ID (示例值: 1081405)
    'node_id',  # 用户的GitHub节点ID (示例值: MDQ6VXNlcjEwODE0MDU=)
    'avatar_url',  # GitHub头像URL (示例值: https://avatars.githubusercontent.com/u/1081405?v=4)
    'gravatar_id',  # Gravatar ID (示例值: None)
    'url',  # GitHub用户的URL (示例值: https://api.github.com/users/dlazesz)
    'html_url',  # GitHub用户的HTML URL (示例值: https://github.com/dlazesz)
    'followers_url',  # GitHub用户的粉丝URL (示例值: https://api.github.com/users/dlazesz/followers)
    'following_url',  # GitHub用户的关注URL (示例值: https://api.github.com/users/dlazesz/following{/other_user})
    'gists_url',  # 用户的GitHub Gists URL (示例值: https://api.github.com/users/dlazesz/gists{/gist_id})
    'starred_url',  # 用户的GitHub Starred URL (示例值: https://api.github.com/users/dlazesz/starred{/owner}{/repo})
    'subscriptions_url',  # 用户的GitHub订阅URL (示例值: https://api.github.com/users/dlazesz/subscriptions)
    'organizations_url',  # 用户的GitHub组织URL (示例值: https://api.github.com/users/dlazesz/orgs)
    'repos_url',  # 用户的GitHub仓库URL (示例值: https://api.github.com/users/dlazesz/repos)
    'events_url',  # 用户的GitHub事件URL (示例值: https://api.github.com/users/dlazesz/events{/privacy})
    'received_events_url',  # 用户的GitHub接收事件URL (示例值: https://api.github.com/users/dlazesz/received_events)
    'type',  # 用户类型，通常为"User" (示例值: User)
    'site_admin',  # 表示用户是否是GitHub网站管理员的标志 (示例值: False)
    'name',  # 用户的姓名 (示例值: Indig Balázs)
    'company',  # 用户所在公司 (示例值: None)
    'blog',  # 用户的博客 (示例值: None)
    'location',  # 用户的位置 (示例值: None)
    'email',  # 用户的电子邮件 (示例值: None)
    'hireable',  # 表示用户是否愿意被雇佣的标志 (示例值: None)
    'bio',  # 用户在其GitHub资料中提供的自我介绍或个人简介 (示例值: None)
    'twitter_username',  # 用户的Twitter用户名 (示例值: None)
    'public_repos',  # 用户在GitHub上的公共代码仓库数量 (示例值: 26)
    'public_gists',  # 用户的公共Gists数量 (示例值: 1)
    'followers',  # 关注该用户的其他GitHub用户数量 (示例值: 5)
    'following',  # 该用户关注的其他GitHub用户数量 (示例值: 1)
    'created_at',  # 用户的GitHub帐户创建日期 (示例值: 2011-09-26T17:27:03Z)
    'updated_at',  # 用户的GitHub帐户最后更新日期 (示例值: 2023-10-13T11:21:10Z)
]

data = raw_data[columns]

# 1. 删除重复数据，并输出去重前后的数据量
print(f"原始数据量: {len(data)}")
data.drop_duplicates(inplace=True)
print(f"去重后的数据量: {len(data)}")

# 2. 缺失值处理
# 去掉 gravatar_id 列
data.drop(columns=['gravatar_id'], inplace=True)

# 查看各列的缺失值情况
print(data.isnull().sum())

# 将 site_admin 转换为布尔类型
data['site_admin'] = data['site_admin'].astype(bool)

# 将 hireable 转换为布尔类型，注意 hireable 可能包含 NaN，需要先填充后再转换
data['hireable'] = data['hireable'].fillna(False).astype(bool)

# 填充文本数据的空值
text_columns = ['name', 'company', 'blog', 'location', 'email', 'bio', 'twitter_username']
data[text_columns] = data[text_columns].fillna('')

# 再次查看各列的缺失值情况
print(data.isnull().sum())

# 3. 数据变换，将 created_at、updated_at 转为时间戳
data['created_at'] = pd.to_datetime(data['created_at']).apply(lambda x: int(x.timestamp()))
data['updated_at'] = pd.to_datetime(data['updated_at']).apply(lambda x: int(x.timestamp()))

# 4. 数据可视化
# 4.1 可视化 bot 和 human 类型的情况
label_counts = data['label'].value_counts()
plt.figure(figsize=(8, 6))
sns.barplot(x=label_counts.index, y=label_counts.values)
plt.title('Bot 和 Human 类型的数量')
plt.xlabel('类型')
plt.ylabel('数量')
plt.show()

# 4.2 可视化 bot 类型账号的 created_at 情况
bot_data = data[data['label'] == 'Bot']
plt.figure(figsize=(12, 6))
plt.hist(bot_data['created_at'], bins=30, color='blue', alpha=0.7)
plt.title('Bot 账号创建时间分布')
plt.xlabel('创建时间 (时间戳)')
plt.ylabel('数量')
plt.show()

# 4.3 可视化 human 类型账号的 created_at 情况
human_data = data[data['label'] == 'Human']
plt.figure(figsize=(12, 6))
plt.hist(human_data['created_at'], bins=30, color='green', alpha=0.7)
plt.title('Human 账号创建时间分布')
plt.xlabel('创建时间 (时间戳)')
plt.ylabel('数量')
plt.show()

# 4.4 可视化 bot 类型账号的 followers 和 following 情况
plt.figure(figsize=(10, 6))
plt.scatter(bot_data['followers'], bot_data['following'], alpha=0.5, color='red')
plt.title('Bot 账号的 Followers 和 Following 关系')
plt.xlabel('Followers')
plt.ylabel('Following')
plt.show()

# 4.5 可视化 human 类型账号的 followers 和 following 情况
plt.figure(figsize=(10, 6))
plt.scatter(human_data['followers'], human_data['following'], alpha=0.5, color='purple')
plt.title('Human 账号的 Followers 和 Following 关系')
plt.xlabel('Followers')
plt.ylabel('Following')
plt.show()