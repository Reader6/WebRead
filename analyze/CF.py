import math
from operator import *


dic = {'A': ('西游记', '红楼梦', '水浒传'), 'B': ('西游记', '红楼梦','活着'), 'C': ('三生三世', '红楼梦'), 'D': ('西游记', '美人鱼', '哪吒'),'E':('西游记','挪威的森林')}  # 简单粗暴，记得加''


# 计算用户兴趣相似度
def Usersim(dicc):
    # 建立物品-用户倒排表
    item_user = dict()
    for u, items in dicc.items():
        for i in items:
            if i not in item_user.keys():
                item_user[i] = set()  # 保证其不重复。
            item_user[i].add(u)  # 向集合中添加用户。

    C = dict()  # 书籍名为字符，使用字典。
    N = dict()
    for item, users in item_user.items():
        for u in users:
            if u not in N.keys():
                N[u] = 0  # 字典无初始值不用相加
            N[u] += 1  # 每个商品下用户出现一次就加一次，就是计算每个用户一共购买的商品个数。
            for v in users:
                if u == v:
                    continue
                if (u, v) not in C.keys():
                    C[u, v] = 0 # 同上，没有初始值不能+1
                C[u, v] += 1

    # 倒排阵建立好，下面计算相似度。
    W = dict()
    for co_user, cuv in C.items():
        W[co_user] = cuv / math.sqrt(N[co_user[0]] * N[co_user[1]])
    return W


def Recommend(user, dicc, W2, K):
    rvi = 1  # 因为不涉及评分等级因此重要程度都设为1,实际中可能每个用户对书本的喜爱程度不一样。
    rank = dict()
    related_user = []
    interacted_items = dicc[user]
    for co_user, item in W2.items():
        if co_user[0] == user:
            related_user.append((co_user[1], item))  # 先建立一个和待推荐用户兴趣相关的所有的用户列表。
    for v, wuv in sorted(related_user, key=itemgetter(1), reverse=True)[0:K]:
        # 找到K个相关用户以及对应兴趣相似度，按兴趣相似度从大到小排列。
        for i in dicc[v]:
            if i in interacted_items:
                continue
            if i not in rank.keys():
                rank[i] = 0
            rank[i] += wuv * rvi
    return rank


if __name__ == '__main__':
    W3 = Usersim(dic)
    Last_Rank = Recommend('A', dic, W3, 2)
    print(Last_Rank)