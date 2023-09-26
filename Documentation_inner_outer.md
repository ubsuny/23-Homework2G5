# **Documentation:**
## **Overview**
### **The Inner Product function:**
The inner product is calculated by multiplying the corresponding elements of the two vectors and summing the results.
The inner product of 2 vectors **a** and **b** =
## **\mathbfsum_{i=1}^N a_{i} b_{i}**


The **inner_product()** function can be used to calculate the inner product of any two vectors of the same length.

The inner product is a scalar value that represents the similarity between the two vectors.

#### **Input or Arguments**
The function takes two vectors as input. The vectors must be of the same length.

#### **Output**
The function returns the inner product of the two vectors.

### **The outer prouct function:**

The outer product is a matrix that is formed by multiplying the corresponding elements of the two vectors and storing the results in the corresponding elements of the matrix.
The **outer_product()** function can be used to calculate the outer product of any two vectors of any length.

The outer product of a and b can be represented by:
# **\sum_{i=1,j=1}^{n} a_{i} b_{j} $**

#### **Input or Arguments**
The function takes two vectors as input.

#### **Output**
The function returns a matrix that is the outer product of the two vectors. The matrix will have dimensions \begin{matrix} (len(a), len(b)) \end{matrix} where a and b are the two input vectors.


Sources: [Stover, Christopher and Weisstein, Eric W. "Einstein Summation." From MathWorld--A Wolfram Web Resource. ](https://mathworld.wolfram.com/EinsteinSummation.html)

Source: [EINSTEIN SUMMATION NOTATION](http://dslavsk.sites.luc.edu/courses/phys301/classnotes/einsteinsummationnotation.pdf)

Source: [NumPy reference](https://numpy.org/doc/stable/reference/index.html)

