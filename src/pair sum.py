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
            output.add((min(number, remainder), max(number, remainder)))

    return "\n".join(map(str, list(output)))

array = [1, 3, 2, 2]
target = 4

out = pairSum(array, target)
print(out)

array = [4, 4, 15, 1]
target = 16

print("")
out = pairSum(array, target)
print(out)

array = [1, 2, 3, 4]
target = 8

print("")
out = pairSum(array, target)
print(out)
