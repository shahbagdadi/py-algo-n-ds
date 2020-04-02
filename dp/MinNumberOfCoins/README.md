# Minimum number of Coins
Given a value V, if we want to make change for V cents, and we have infinite supply of each of C = { C1, C2, .. , Cm} valued coins,
 what is the minimum number of coins to make the change?

```

Examples:

Input: coins[] = {25, 10, 5}, V = 30
Output: Minimum 2 coins required
We can use one coin of 25 cents and one of 5 cents

Input: coins[] = {9, 6, 5, 1}, V = 11
Output: Minimum 2 coins required
We can use one coin of 6 cents and 1 coin of 5 cents
```

```
Tips for DP
1.  Write as Recursive first as recursive is typically easier for such problems.
2.  Map recursive to DP using the following steps
   1.  Create dp[] of size+1 of the varying parameter(s) in the recursive function
   2.  Set the base values in the dp[]
   3.  Create a loop (with start excluding the base values set in step b.) to run till dp.length to replace the recursion. Generally need as many loops as varying parameters in recurring function
   4.  Mimic the rest of the logic in the recursive function.
```

[Solution](./Solution.py)