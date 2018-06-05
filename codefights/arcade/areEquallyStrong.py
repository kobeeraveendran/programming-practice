def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    mymax = max(yourLeft, yourRight)
    mymin = min(yourLeft, yourRight)
    friendmax = max(friendsLeft, friendsRight)
    friendmin = min(friendsLeft, friendsRight)

    return mymax == friendmax and mymin == friendmin