def rotateImage(a):
    length = len(a)
    num_layers = length // 2

    # for each layer
    for i in range(num_circles):
        # edges:
        # 0,1 -> 1,1; 1,1 -> 2,1
        
        # corners:
        # 0,0 -> 0,2; 0,2 -> 2,2; 2,2 -> 2,0; 2,0 -> 0,0
        for j in range((4 * length) - 4):
