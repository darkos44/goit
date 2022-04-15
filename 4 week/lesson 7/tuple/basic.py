from turtle import circle


my_tuple = (1, 1, 2, 3, 5, 8, 13, 21, 7, 5, 100)

print(my_tuple[3])

print(my_tuple[3:])

print(list(my_tuple))

circle = {(0,0):"Center of circle",
        (1,0):"0 or 360",
        (0,1):"90",
        (-1,0):"180",
        (0,-1):"270",
        }

print(circle.get((1,0)))

x = 10
y = -1
x,y = y,x