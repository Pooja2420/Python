# Name: Pooja Venugopal Baskaran
# Date : 15 November 2023
# Honour Statement: I have not given or received any unauthorized assistance on this assignment.
# Video Link: https://www.youtube.com/watch?v=RS1nZaTyRho

# 1. Import NumPy
import numpy as np

# 2. Use arange to create a NumPy array with 100 equally spaced values in the range 0 through 100 (not including 100). Name this NumPy array a.
a = np.arange(0, 100, 1)
print (a)

# 3. Use arange to create a NumPy array with 10 equally spaced values in the range 0 through 100 (not including 100). Name this NumPy array b.
b = np.arange(0, 100, 10)

# 4. Use linspace to create a NumPy array in the range 0 through 10 (inclusive) with values spaced at 0.1. Call this NumPy array c.
c = np.linspace(0, 10, num=101)

# 5. Create a random two-dimensional array with the dimensions 10 by 10. Call this NumPy array d.
d = np.random.rand(10, 10)

# 6. Reshape a so that it is a two-dimensional array with the dimensions 10 by 10.
a = a.reshape(10, 10)
print("Results of reshape of a : ",np.round(a,2))

# 7. Show the results of “a[4,5]”.
print("Results of a[4,5]: ",a[4,5])

# 8. Show the results of “a[4]”.
print("Results of a[4]: ",a[4])

# 9. Show the sum of d.
print("Sum of d = ", np.round(np.sum(d),2))

# 10. Show the max of a.
print("Max of a = ",np.round(np.max(a),2))

# 11. Show the transpose of b.
print("Transpose of b = \n", np.round(b.T,2))

# 12. Show the results of adding a and d.
print("Results of adding a and d: \n",np.round(a + d,2))

# 13. Show the results of multiplying a and d.
print("Results of multiplying a and d: \n", np.round(a * d,2))

# 14. Show the results of computing the dot product of a and d.
print("Dot product of a and d = \n", np.round(np.dot(a, d),2))
