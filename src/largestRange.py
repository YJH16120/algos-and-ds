"""
Problem: Given a list of negative, and positive numbers. Find the largest range of consecutive numbers.
Example:
[1, 2, 3, 4, 5, 9, 10, 72, 90], largest range would be 1 to 5 so return an array like this [1, 5]
"""

def largestRange(array: list) -> list:
    numbers = {x:0 for x in array}
    left = right = 0

    for number in array:
        if numbers[number] == 0:
            leftCount = number - 1
            rightCount = number + 1

            while leftCount in numbers:
                numbers[leftCount] = 1
                leftCount -= 1

            leftCount += 1

            while rightCount in numbers:
                numbers[rightCount] = 1
                rightCount += 1

            rightCount -= 1

            if (right - left) <= (rightCount - leftCount):
                right = rightCount
                left = leftCount

                return [left, right]

    return []


array = [-1, -3, -2, 1, 8, 9, 2, 3, 4, 5]
out = largestRange(array)
print(out)


"""
Concept to take away from this. Use a dictionary to make things go faster, because it's lookup time is O(1).
Use this formula when you need to do an array operation, and need to keep track of the current element, and traverse it.
"""
