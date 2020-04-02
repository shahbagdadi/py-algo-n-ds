## Knapsack 

Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. 

![Sample](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Knapsack.svg/500px-Knapsack.svg.png)  

In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively.    
Also given an integer W which represents knapsack capacity, find out the maximum value subset such that sum of the weights of this subset is smaller than or equal to W.  
You cannot break an item, either pick the complete item, or don’t pick it (0-1 property)   

```
Sample 1 
    input wt : [1,3,4,5]
    input value : [1,4,5,7]
    intput max weigth : 7
    Output (max value) : 9


Sample 2
    input wt : [1,1,1]
    input value : [10,20,30]
    intput max weigth : 2
    Output : 50

```

[Explanation](https://www.youtube.com/watch?v=8LusJS5-AGo)  

[Solution](./Solution.py)