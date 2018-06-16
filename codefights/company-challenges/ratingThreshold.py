def ratingThreshold(threshold, ratings):
    to_review = []

    for i in range(len(ratings)):
        temp_mean = sum(ratings[i]) / len(ratings[i])
        if temp_mean < threshold:
            to_review.append(i)

    return to_review