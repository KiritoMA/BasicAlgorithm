vote = {}

def check_vote(name):
    if vote.get(name):
        print("kick him out")
    else:
        vote[name] = True
        print("let him vote")

check_vote("tom")
check_vote("mike")
check_vote("mike")
