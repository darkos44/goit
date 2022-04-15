
my_list = [1,1,2,3,5,8,13,21,7,5,100]
#print(type(my_list))
#print(my_list[-1])
#print(len(my_list))
#for _ in my_list:
#    print(_)
#print(*my_list)
#my_list.append(5)
#my_list.insert(5,50)
#my_list.remove(5)
#my_list.pop()
##new_list = [1,2,3,4,]
#my_list.extend(new_list)
#print(*my_list)
#if 5 in my_list:
#    print(my_list.index(5))

#print(my_list.count(5))

new_list = my_list
my_list.remove(5)
new_list = my_list.copy()
my_list.remove(5)

sorted_list = sorted(my_list)
print(*sorted_list)
print(*my_list)
my_list.sort()
my_list.clear()