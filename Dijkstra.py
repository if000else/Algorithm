'''
在算法之前，降讲到 '乐谱换钢琴问题 '，'愿意'一词代表了两个节点之间的方向，而且是单向的。unilateral
里面说"我愿意拿我的海报跟你换乐谱"，旨在说明，海报一定能换到乐谱。但是反过来，就变成了不充分必要的条件了。
并没有说愿意拿乐谱换海报，愿意这个词很重要。
这个算法，零零碎碎看了3天。。。
'''
# initial data
graph = {
    'start': {'post': 0, 'album': 5},
    'post': {'guitar': 30, 'drum': 35},
    'album': {'guitar': 15, 'drum': 20},
    'guitar': {'end': 20, },
    'drum': {'end': 10, },
    'end': {},
}
costs = {}
processed = []
parent = {}


# function
def lowest_node():
    #初始化操作，默认第一步是‘start’
    local_node = None
    lowest_cost = float('inf')
    if not processed:
        for k, v in graph['start'].items():
            costs[k] = v
            parent[k]='start'
        processed.append('start')
        local_node='start'

    #在列表中插找最小值，找到就赋值给变量
    for k, v in costs.items():
        if v < lowest_cost and k not in processed:
            local_node = k
            lowest_cost = v
    return local_node


# main

node = lowest_node()
while node:
    for neighbor in graph[node].keys():
        new_cost = costs[node] + graph[node][neighbor]
        if neighbor not in costs:#避免取不到数据
            costs[neighbor]=float('inf')
        if new_cost < costs[neighbor]:#查找到最小，就赋值给变量
            costs[neighbor] = new_cost
            parent[neighbor] = node
    processed.append(node)#当前节点已处理（可能在列表中会重复，但不影响）

    node = lowest_node()#继续取下一个节点
print(costs)


'''
迪克斯特拉算法总结：
使用范围：非负加权图中查找最短路径（负边权要用贝尔曼-福德算法）
核心思想：在数据中循环查找
'''


