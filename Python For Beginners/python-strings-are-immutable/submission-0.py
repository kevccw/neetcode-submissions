def remove_fourth_character(word: str) -> str:
    output = word[0:3] + word[4:]
    return output


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
