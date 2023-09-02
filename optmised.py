# https://www.youtube.com/shorts/P654ObISykA?feature=share


import os; os.system('cls')
import timeit
# from timeit import timeit

def normal_impl():
    return [i for i in (0,1,2,3,4)]   # List Comprehension

def optimised_impl():
    return [0,1,2,3,4]

print(normal_impl())
print(optimised_impl())

normal_time = timeit.timeit(stmt = normal_impl)
optimised_time = timeit.timeit(stmt = optimised_impl)

print(f'Normal: {normal_time}')
print(f'Optimsed: {optimised_time}')

print()