import numpy as np
import time

# Define the vectors as NumPy arrays
vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])

# Measure execution time for the inner product
start_time = time.time()
inner_product_result = np.dot(vector_a, vector_b)
end_time = time.time()
elapsed_time_inner = end_time - start_time
# Measure execution time for the outer product
start_time = time.time()
outer_product_result = np.outer(vector_a, vector_b)
end_time = time.time()
elapsed_time_outer = end_time - start_time

# Print results and execution times
print("Vector A:", vector_a)
print("Vector B:", vector_b)
print("NumPy Inner Product Result:", inner_product_result)
print("NumPy Outer Product Result:")
print(outer_product_result)
