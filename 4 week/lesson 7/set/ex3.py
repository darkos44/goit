def is_unique(chekist):
    return len(chekist) == len(set(chekist))


print(is_unique([1,2,3,4,5,5,]))