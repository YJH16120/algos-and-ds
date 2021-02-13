# BigO notation
- Used to measure how long it will take to complete a given task called that is called Time complexity.
- can also be used to check how much memory a given tasks takes. That is called space complexity.

```py
def f(n):
    return 45*n**3 + 20*n**3 + 19

print(f(1)) # 84
print(f(2)) # 469
print(f(10)) # 47019
```

With `f(1) = 84`, `f(2) = 459`, 19 doesn't contribute much to the overall value. If `f(10) = 47019`. Neither n^2 or 19 contributes much, as 20(10)^2 contributes 4% to the total amount, while 19 contribtues 0.04% to the total amount. The trick is to only take note of the highest power.

Therefore, BigO of `f(n)` would be `O(n^3)`

## Note:  
To find out what the BigO notiation is always consider the **worst** case scenario. That is what the BigO notation is meant to do.  
As an example:
1. `O(1 + n/2 + 10)` = `O(n)`
Constants fall off as n gets larger, there of it is `O(n)`
2. `O(1+n)` = `O(n)` because you can ignore all constants
