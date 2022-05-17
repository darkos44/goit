def all_sub_lists(data):
    result = [[]]
    for x in range(len(data) + 1):
        for y in range(x + 1, len(data) + 1):
            result.append(data[x:y])
    print(result)
    result.sort(key=lambda x: len(x))
    print(result)
    return result