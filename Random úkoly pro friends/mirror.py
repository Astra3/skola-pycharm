def mirror(word: str) -> str:
    """
    Functions that returns first half of the word reversed
    :param word: word to be reversed
    :return: reversed word
    """
    if (length := len(word)) % 2 == 1:
        length -= 1
    length = length // 2 - 1
    new_word = ""
    for i in range(length, -1, -1):  # beginning, end, step
        new_word += word[i]
    new_word += word[length + 1:]
    return new_word


a = input("word: ")
print(mirror(a))
