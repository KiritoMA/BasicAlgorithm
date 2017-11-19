graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["jonny", "thom"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

'deque is object in collections'
from collections import deque
search_queue = deque()
search_queue += graph["you"]

while search_queue:
    person = search_queue.popleft()
    if person_is_seller(person):
        print(person + "is a mango seller!")
        return True
    else:
            search_queue += graph[person]
return False

def person_is_seller(name):
    return name[-1] == 'm'
