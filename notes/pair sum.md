# Problem
Given an array of `[1, 3, 2, 2]` find out which values will add up to 4.  
Examples:  
1. `[1, 2, 2, 4]` find out which values will add up to 5.  
    Output: `(1, 4)`
2. `[3, 4, 6, 1]` find out which values will add up to 7.  
    Output:  
    `(3, 4)`  
    `(6, 1)`

Order of pairs during output doesn't matter, as long as the pairs add up to the target.

# Solution
```py
def pairSum(array: list, target: int) -> str:
    if len(array) < 2:
        return "Array size too small."

    seen = set()
    output = set()

    for number in array:
        remainder = target - number
        if remainder not in seen:
            seen.add(number)
        else:
            pair = (min(number, remainder), max(number, remainder))
            output.add(pair)

    return "\n".join(map(str, list(output)))
```
use this style, for when you have an array, and the solution is via pairs.