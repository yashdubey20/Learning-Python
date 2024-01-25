def second_largest(numbers):
    if len(numbers) < 2:
        return None

    first, second = numbers[0], numbers[1]
    if first < second:
        first, second = second, first

    for n in numbers[2:]:
        if n > first:
            first, second = n, first
        elif n > second:
            second = n

    return second

res = second_largest([1,19,20,21,5])
print(res)