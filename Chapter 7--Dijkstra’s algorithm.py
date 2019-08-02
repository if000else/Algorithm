'''
在算法之前，降讲到 '乐谱换钢琴问题 '，'愿意'一词代表了两个节点之间的方向，而且是单向的。
里面说"我愿意拿我的海报跟你换乐谱"，旨在说明，海报一定能换到乐谱。但是反过来，就变成了不充分必要的条件了。
并没有说愿意拿乐谱换海报，愿意这个词很重要。
此外，对于第七章这个章节，迪克斯拉这个算法讲的不是很好。至少我看的不是很明白。读完以后，我甚至还在想，是不是遍历了所有的路径，然后找到最优解？
如果变成了这个问题，那就不叫算法了，是简单的数学问题，排列组合嘛。
还有一个问题，当吉他到钢琴的权值为15时，就有两条路径都是35，那这个算法会找出两个吗？
可能这个算法的实际用途在地图方面更加广泛，缺乏这方面的知识，不敢妄下结论。
'''
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node
    
