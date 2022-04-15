list1 = [25,50,23,16,16,50,53]
list2 = [26,5,3,50,16,]

set1 = set(list1)
set2 = set(list2)

set_union = set1 | set2
print(*set_union)

set_cros = set1 & set2
print(*set_cros)