points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    len_coordinates = len(coordinates)
    sum_distance = 0
    if len_coordinates < 2:
        return 0
    for x in range(len_coordinates - 1):
        list_for_tuple = list()
        list_for_tuple.append(coordinates[x])
        list_for_tuple.append(coordinates[x + 1])
        points_tuple = tuple(sorted(list_for_tuple))
        sum_distance += points.get(points_tuple, 0)
        print(*list_for_tuple, sum_distance)
    print(sum_distance)
    return sum_distance


calculate_distance([0, 1, 3, 2, 0, 2])
