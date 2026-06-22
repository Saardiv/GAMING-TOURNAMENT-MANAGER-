def title():
    print("========== GAMING TOURNAMENT MANAGER ===========")
title()
num=int(input("Total no. of Player:"))
players=[]
for i in range(num):
    player={}
    
    name=input("Player Name:")
    level=int(input("Level:"))
    score=int(input("Score:"))

    player["name"]=name
    player["level"]=level
    player["score"]=score

    players.append(player)

for player in players:
    print(player["name"],"->",player["score"])

high=0
low=0

for player in players:
    if player["score"]>=300:
        high+=1
    else:
        low+=1

print("Player with Score >=300:",high)
print("Player with Score <300:",low)

highest=players[0]["score"]

for player in players:
    if player["score"]>highest:
        highest=player["score"]
        
print("Highest Score:",highest)

cham=players[0]["name"]

for player in players:
    if highest==player["score"]:
        cham=player["name"]
print("Champion Name:",cham)

hlevel=players[0]["level"]

for player in players:
    if player["level"]>hlevel:
        hlevel=player["level"]
print("Highest Level:",hlevel)

for player in players:
    if player["level"]==hlevel:
        print("Player Name:",player["name"],        "(Highest level Player)")
search=input("Enter player name:")

found=False
for player in players:
    if search==player["name"]:
        print("Player Found")
        print("Level:",player["level"])
        print("Score:",player["score"])
        if player["level"]>=20:
            print("Rank:Master")
        elif player["level"]>=10:
            print("Rank:Pro")
        else:
            print("Rank:Beginner")
        print(player["name"][0],end="")
        print(player["level"],end="")
        print(player["name"][-1],end="")
        print(player["score"])
    
    
        found=True
if not found:
    print("Player Not Found")


              

    
