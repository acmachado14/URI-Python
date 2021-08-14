distance = 0
numOfFriends = 0

while True:
    try:
        input()
        distance += int(input())
        numOfFriends += 1
    except:
        break

print("{:.1f}".format(distance / numOfFriends))