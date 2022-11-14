## Count Basins problem

Given the altitudes of the regions on a surface, determine the basins where water would collect if poured onto that surface.  

Region whose four neighbors (right, left, up and down) are all higher in altitude is called a sink. All the water would collect in sinks. If a region is not a sink, it is guaranteed to have a single lowest neighbor where water will drain to. All regions that drain to a particular sink–directly or indirectly–collectively form one basin. Partition the surface into the basins and return their sizes in the non-decreasing order.  

‍

Example One
```
Input:

[[1, 5, 2],

 [2, 4, 7],

 [3, 6, 9]]

Output: [2, 7]

There are two basins, one consists of two cells and the other consists of seven. They are labeled with A’s and B’s here:

 B B A

 B B A

 B B B

The sink of basin A is cell (0, 2). The sink of basin B is cell (0, 0).
```


Example Two  
```
Input:

[[0, 2, 1, 3],

 [2, 1, 0, 4],

 [3, 3, 3, 3],

 [5, 5, 2, 1]]

Output: [4, 5, 7]

There are three basins. They are labeled with A, B and C here: 

B B C C

B C C C

B C C A

B A A A

The sinks of basins A, B and C are (3, 3), (0, 0) and (1, 2) respectively.

```

Notes 
- Input Parameters: The function has one argument, a two-dimensional array of integers representing the altitudes of the regions of a rectangular surface.

- Output: Return an array of integers representing the sizes of basins in the non-decreasing order.







