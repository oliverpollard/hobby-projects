import numpy as np
from scipy.optimize import linear_sum_assignment

names = ["Hilda", "Ham", "Pol", "Joe M", "Joe A", "Minnie", "Erin"]
choices = np.array(
    [
        [1, 2, 3, 4, 5, 6, 7],
        [2, 1, 3, 4, 5, 6, 7],
        [3, 1, 2, 4, 5, 6, 7],
        [4, 1, 2, 3, 5, 6, 7],
        [5, 1, 2, 3, 4, 6, 7],
        [6, 1, 2, 3, 4, 5, 7],
        [7, 1, 2, 3, 4, 5, 6],
    ]
)
solution = linear_sum_assignment(choices)[1]
for index, room in enumerate(solution):
    print(names[index], "get room " + str(room + 1))
