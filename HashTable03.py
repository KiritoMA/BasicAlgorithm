vote = {}

def check_vote(name):
    if vote.get(name):
        print("kick him out")
    else:
        vote[name] = True
        print("let him vote")

print(check_vote("tom"))
print(check_vote("mike"))
print(check_vote("mike"))
