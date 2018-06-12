def companyBotStrategy(trainingData):
    avg_time = 0
    corr_count = 0
    for i in range(len(trainingData)):
        if trainingData[i][1] == 1:
            avg_time += trainingData[i][0]
            corr_count += 1
    
    if corr_count == 0:
        return 0
    
    avg_time /= corr_count
    
    return avg_time

print(companyBotStrategy([[1, 1], [3, 0], [3, 1], [2, 1]]))