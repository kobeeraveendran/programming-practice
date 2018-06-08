def electionsWinners(votes, k):
    votes.sort()
    num_winners = 0
    
    if k == 0:
        if votes[-1] == votes[-2]:
            return 0
        else:
            return 1
    else:
        for i in range(0, len(votes)):
            if votes[i] + k > votes[-1]:
                num_winners += 1
            
    return num_winners