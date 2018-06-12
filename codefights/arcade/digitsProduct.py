import numpy as np

def digitsProduct(product):
    for i in range(1, 10000):
        if product == np.prod(list(map(int, str(i)))):
            return i

    return -1