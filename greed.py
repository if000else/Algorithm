'''
贪婪算法，是寻找最优解的一种近似方法。把大问题分解为小问题，小问题中每次都取最优。
作用：化繁为简，快速，近似最优
例子：背包问题，教室调度问题，集合覆盖问题，旅行商问题
'''

#集合覆盖问题：在未选择的省份里，每次都尽可能选覆盖最多的

stations = {}

stations["kone"] = {"id", "nv", "ut"}
stations["ktwo"] = {"wa", "id", "mt"}
stations["kthree"] = {"or", "nv", "ca"}
stations["kfour"] = {"nv", "ut"}
stations["kfive"] = {"ca", "az"}
remain = set()
final_stations = set()

for k, v in stations.items():
    remain |= v
print("All states need to be covered:", remain)
# main()

while remain:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = remain & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    remain -= states_covered
    final_stations.add(best_station)
print(final_stations)
