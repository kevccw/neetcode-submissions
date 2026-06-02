def add_two_numbers() -> int:
    strings = input().split(",")
    ints = []
    result = 0
    for s in strings:
        ints.append(int(s))
    for i in ints:
        result += i
    return result


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
