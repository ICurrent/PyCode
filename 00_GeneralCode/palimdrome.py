def palimdrome(word):
    lst = list(word)
    if "".join(lst[::-1]) == word:
        return True
    else:
        return False

print(palimdrome('sees'))