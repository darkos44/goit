# from my_package.foo import foo
# from my_package.baz.operation import mul, sum
# from my_package.bar.info import log
# from my_package import foo, mul, sum, log

# print(foo('Taras'))
# print(sum(3, 4))
# print(mul(3, 4))
# log('start proccess')

import my_package

print(my_package.foo('Taras'))
print(my_package.sum(3, 4))
print(my_package.mul(3, 4))
my_package.log('start proccess')