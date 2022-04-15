list_daria = ['Red', 'Green', 'Black', 'White']
list_oleg = ['Red', 'Black', 'White','Yelloy']

list_onli_daria = list(set(list_daria) - set(list_oleg))
print(*list_onli_daria)

list_u = list(set(list_daria) | set(list_oleg))
print(*list_u)

list_x = list(set(list_daria) ^ set(list_oleg))
print(*list_x)