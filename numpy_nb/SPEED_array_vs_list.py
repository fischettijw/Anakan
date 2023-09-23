import numpy as np
import time
import os; os.system("cls")

# Size of the data structures
size = 10**8

# Create a Python list and a NumPy array with the same data
py_list = list(range(size))
np_array = np.arange(size)

# Addition
start_time = time.time()
py_list_result = [x + 2 for x in py_list]
py_list_time = time.time() - start_time

start_time = time.time()
np_array_result = np_array + 2
np_array_time = time.time() - start_time

print("Addition:")
print(f"Python list took {py_list_time:.6f} seconds")
print(f"NumPy array took {np_array_time:.6f} seconds")
print(f"SPEED RATIO (Py/Np) = {(py_list_time/np_array_time):.2f}\n")

# Multiplication
start_time = time.time()
py_list_result = [x * 2 for x in py_list]
py_list_time = time.time() - start_time

start_time = time.time()
np_array_result = np_array * 2
np_array_time = time.time() - start_time

print("Multiplication:")
print(f"Python list took {py_list_time:.6f} seconds")
print(f"NumPy array took {np_array_time:.6f} seconds")
print(f"SPEED RATIO (Py/Np) = {(py_list_time/np_array_time):.2f}\n")

# Element-wise operation
def square_root(x):
    return x**0.5

start_time = time.time()
py_list_result = [square_root(x) for x in py_list]
py_list_time = time.time() - start_time

start_time = time.time()
np_array_result = np.sqrt(np_array)
np_array_time = time.time() - start_time

print("Element-wise Square Root:")
print(f"Python list took {py_list_time:.6f} seconds")
print(f"NumPy array took {np_array_time:.6f} seconds")
print(f"SPEED RATIO (Py/Np) = {(py_list_time/np_array_time):.2f}\n")
