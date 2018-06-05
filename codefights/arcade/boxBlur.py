def boxBlur(image):
    # number of centers given length is:
    # 3x3 -> 1
    # 4x4 -> 4
    # 5x5 -> 9
    # 6x6 -> 16
    # gen. rule is (len(image) - 2) ** 2
    # and they're located at all non-edge regions
    # of the image ([1][1] ... [len - 2][len - 2])

    center_means = []
    row_means = []

    for i in range(1, len(image) - 1):
        for j in range(1, len(image[0]) - 1):
            row1 = sum(image[i - 1][y] for y in range(j - 1, j + 2))
            row2 = sum(image[i][y] for y in range(j - 1, j + 2))
            row3 = sum(image[i + 1][y] for y in range(j - 1, j + 2))
            temp_mean = sum([row1, row2, row3]) // 9
            row_means.append(temp_mean)

        center_means.append(row_means)
        row_means = []

    return center_means