from typing import List

def read_integers() -> List[int]:
    strings = input().split(",")
    ints = []
    for string in strings:
        ints.append(int(string))
    return ints

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
