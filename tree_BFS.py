import queue

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

q = queue.Queue()


def search(name):
    q = queue.Queue()
    for p in graph[name]:
        q.put(p)
    checked = []
    while not q.empty():
        person = q.get()
        if find(person):
            print("%s is the mongo seller!!" % person)
            return person
        else:
            for q2 in graph[person]:
                q.put(q2)
            checked.append(person)
    print("Can not find any seller! list:", checked)


def find(person):
    if person[-1] == 'm':
        return True
    else:
        return False


search('you')
