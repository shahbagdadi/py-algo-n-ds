
import itertools
import sys


def travel(w):
    #  T - O(2^n * n²)
    n = len(w)
    # initial value of 0 to all other points. frozenset is used as key needs to be immutable
    A = {(frozenset([0, i+1]), i+1): (cost, [0, i+1])
         for i, cost in enumerate(w[0][1:])}
    # print(A)

    for m in range(2, n):
        B = {}
        for C in itertools.combinations(range(1, n), m): # try all possible paths
            S = frozenset(C) | {0}                       # union with start node
            for j in S - {0}:                            # for each node
                min_cost = (sys.maxsize, [])
                for k in S:
                    if k != 0 and k != j:
                        ccost = A[(S-{j}, k)][0] + w[k][j]      # cost upto node j via k is cost till node k + cost from k to j
                        cpath = A[(S-{j}, k)][1] + [j]
                        min_cost = min(min_cost, (ccost, cpath))    
                        B[S, j] = min_cost

        A = B
    # Start path and end path are now added
    res = min([(A[d][0] + w[0][d[1]], A[d][1]) for d in iter(A)])
    # Once the minimum value is found, the optimal solution is available.

    result = res[0], ["City "+str(i+1) for i in res[1]]

    # with the ordering of costs, you just have to show which is the route to follow in the trip, that is
    # Cities are positioned in relation to their costs
    return result


# n is the number of nodes i.e. V
if __name__ == '__main__':
    w = [[0, 10, 15, 20],
         [10, 0, 35, 25],
         [15, 35, 0, 30],
         [20, 25, 30, 0]]
    cost, city = travel(w)
    print(
        f"Best route with return to city 1 is:{city} with a total cost of:{cost}")
