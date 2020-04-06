
answer = []

# Function to find the minimum weight Hamiltonian Cycle / Travelling Salesman problem


def tsp(graph, v, currPos, n, count, cost):
    # T - O(n!)
    # If last node is reached and it has a link to the starting node
    # i.e the source then keep the minimum value out of the total cost of traversal and "ans"
    # Finally return to check for more possible values
    if (count == n and graph[currPos][0]):
        answer.append(cost + graph[currPos][0])
        return

    # BACKTRACKING STEP
    # Loop to traverse the adjacency list
    # of currPos node and increasing the count
    # by 1 and cost by graph[currPos][i] value
    for i in range(n):
        if (v[i] == False and graph[currPos][i]):  # if not visited and not self (0)
            # Mark as visited
            v[i] = True
            tsp(graph, v, i, n, count + 1, cost + graph[currPos][i])
            # Mark ith node as unvisited
            v[i] = False

# n is the number of nodes i.e. V
if __name__ == '__main__':

    graph = [[0, 10, 15, 20],
             [10, 0, 35, 25],
             [15, 35, 0, 30],
             [20, 25, 30, 0]]

    # Boolean array to check if a node has been visited or not
    v = [False for i in range(n)]

    # Mark 0th node as visited
    v[0] = True
    n = 4 # 4 vertex
    # Find the minimum weight Hamiltonian Cycle
    tsp(graph, v, 0, n, 1, 0)

    # ans is the minimum weight Hamiltonian Cycle
    print(min(answer))
