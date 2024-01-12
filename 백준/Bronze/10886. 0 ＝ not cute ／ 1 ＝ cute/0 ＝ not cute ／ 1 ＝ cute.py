n = int(input())
votes = []

for i in range(n):
    vote = int(input())
    votes.append(vote)
    
if votes.count(1)>votes.count(0):
    print("Junhee is cute!")
elif votes.count(1)<votes.count(0):
    print("Junhee is not cute!")
