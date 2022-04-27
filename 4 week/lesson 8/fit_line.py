from __future__ import print_function


def best_fit_line(data: list[tuple]) -> tuple:
    list_x = []
    list_y = []
    for coord in data:
        list_x.append(coord[0])
        list_y.append(coord[1])
    n = len(data)
    m1 = 0.0
    m3 = 0.0
    for _ in range(n):
        m1 += list_x[_] * list_y[_]
        m3 += list_x[_] ** 2

    m2 = (sum(list_x) * sum(list_y)) / n
    m4 = (sum(list_x) ** 2) / 2

    m = round((m1 - m2) / (m3 - m4),2)
    b = round(sum(list_y) / n - m * sum(list_x) / n,2)
    return m, b

def main():
    data = []
    x = input('Введите координату х (Enter для выхода) ')
    while x != '':
        y = input('Введите координату у ')
        data.extend([(float(x),float(y))])
        x = input('Введите координату х (Enter для выхода) ')


    m,b = best_fit_line(data)
    print(f'y = x{m} + {b}')

if __name__ == '__main__':
    main()