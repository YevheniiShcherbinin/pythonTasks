import random


class arrtwo():
    def __init__(self):
        pass

    def arr(self, arr, max1, max2):
        for i in range(1000):
            arr.append(random.randint(-1000, 1000))
        max1 = max(arr)
        max2 = min(arr)
        for n in arr:
            if n > max2 and n != max1:
                max2 = n
                return print(max1, max2)
