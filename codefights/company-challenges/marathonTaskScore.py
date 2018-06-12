def marathonTaskScore(marathonLength, maxScore, submissions, successfulSubmissionTime):
    if successfulSubmissionTime == -1:
        return 0
    
    attempt_penalty = 10 * (submissions - 1)
    time_penalty = successfulSubmissionTime * (maxScore / 2) * (1 / marathonLength) if successfulSubmissionTime > 1 else 0

    return max(maxScore - sum([attempt_penalty, int(time_penalty)]), maxScore // 2)
