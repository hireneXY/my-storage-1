import json

# data.json 文件加载到变量 data
with open('data.json', 'r') as file:
    data = json.load(file)

nodes = data['nodes']  # 用户节点数据
edges = data['edges']  # 边关系数据

# 构建邻接字典
adjacency_dict = {node[0]: [] for node in nodes}

# 添加边关系
for edge in edges:
    user1, user2, weight = edge
    adjacency_dict[user1].append((user2, weight))
    adjacency_dict[user2].append((user1, weight))

# 获取每个用户的直接朋友
friends_list = {user: [friend for friend, _ in friends] for user, friends in adjacency_dict.items()}

# 打印每个用户的直接朋友
print("\n每个用户的朋友列表")
for user, friends in friends_list.items():
    print(f" {user}: {friends}")
    
# 计算每个用户的度数（即直接朋友数量）
degrees = {user: len(friends) for user, friends in friends_list.items()}

# 按度数降序排序
top_5_degrees = sorted(degrees.items(), key=lambda x: x[1], reverse=True)[:5]

# 打印度数最多的前5个用户及其朋友数量
print("\n度数排名")
for user, degree in top_5_degrees:
    print(f" {user}: {degree} 个朋友")

# 提取用户和影响力分数
influence_scores = {node[0]: node[1] for node in nodes}

# 按影响力分数降序排序
top_5_influence = sorted(influence_scores.items(), key=lambda x: x[1], reverse=True)[:5]

# 打印影响力最高的前5个用户
print("\n影响力排名")
for user, score in top_5_influence:
    print(f" {user}: 影响力分数 {score}")

# 计算综合影响力分数（影响力分数的50%和朋友数量的50%）
combined_influence = {user: (influence_scores[user] * 0.5 + degrees[user] * 0.5) for user in influence_scores}

# 按综合影响力分数降序排序
top_5_combined = sorted(combined_influence.items(), key=lambda x: x[1], reverse=True)[:5]

# 打印综合影响力最高的前5个用户
print("\n综合影响力排名")
for user, score in top_5_combined:
    print(f" {user}: 综合影响力分数 {score}")

def find_friends_of_friends(user):
    friends = friends_list[user]
    friends_of_friends = set()
    
    for friend in friends:
        friends_of_friends.update(friends_list[friend])
    
    # 去除用户自己和已有的朋友
    friends_of_friends.discard(user)
    friends_of_friends.difference_update(friends)
    
    return friends_of_friends

# 找出 Yanyan-Wang 的朋友的朋友
yanyan_friends_of_friends = find_friends_of_friends("Yanyan-Wang")

# 计算共同朋友的数量
common_friends_count = {friend: sum(1 for f in friends_list["Yanyan-Wang"] if f in friends_list[friend]) for friend in yanyan_friends_of_friends}

# 按共同朋友数量降序排序
recommended_friends = sorted(common_friends_count.items(), key=lambda x: x[1], reverse=True)

# 打印推荐的新朋友及其理由
print("\n在Yanyan-Wang朋友的朋友中为其推荐")
for friend, count in recommended_friends:
    if count == recommended_friends[0][1]:
        print(f" {friend} ")
print(f"因为Yanyan-Wang与之有 {recommended_friends[0][1]} 个最多的共同朋友")

# 获取 Yanyan-Wang 的所有连接
all_connections = {user: weight for user, weight in adjacency_dict["Yanyan-Wang"]}

# 按连接强度降序排序
top_5_connections = sorted(all_connections.items(), key=lambda x: x[1], reverse=True)[:5]

# 打印连接强度最高的5个用户
print("\n为Yanyan-Wang")
for user, weight in top_5_connections:
    print(f" 推荐 {user}，连接强度：{weight}")

