import itertools
import numpy as np

"""Hello, here is the algorithm for the bonus project 3 at the algebra course """


""" 
Here you input your number for the dimension
"""
n = int(input(f"Please input your number: "))



""" 
Here I generate using the product function from the itertools library all the possible vectors of dimension n in Z2.
"""
vector_list = [list(i) for i in itertools.product([0, 1], repeat=n)]


"""
Here I remove the zero vector from the list because there cannot be any basis with a zero vector.
"""
zero_vector = [0] * n
if zero_vector in vector_list:
    vector_list.remove(zero_vector)

"""
Here I transform the lists in tuples for a better print.
"""
vector_list = tuple(tuple(i) for i in vector_list)


"""
Here I will use the counter variable to count all the bases of the vector space.
"""
counter = 0

for possible_basis in itertools.permutations(vector_list, n):
    if np.linalg.det(possible_basis) % 2 == 1:
        counter += 1

f = open("output.txt", "w")
f.write(f"1. The number of bases of the vector space is {counter}")
"""
Here I output the number of bases of the vector space after counting them.
"""

f = open("output.txt", "a")
f.write('\n')
f.write(f"2. The vectors of each such basis are: ")
"""
Afterwards I use the same algorithm that I used for checking the bases, but instead of counting them i print them.

With the permutations function from the itertools library I generate all the possible n combinations of the vectors
and afterwards I check which one of them are bases.

First of all I need to check if the vectors are linearly independent. To do that i use the linalg.det function from the
numpy library which puts my vectors into a n x n matrix and calculates its determinant. Since we are in Z2 I need to 
do the modulus of the determinant by 2. If the determinant is 0 it means that the system of vectors has a solution and 
the vectors are linearly dependant. If it is 1 then it means that the vectors are linearly independent. If they are 
linearly independent and there are n vectors that means that they can span the vector space and therefore they form a 
basis. Every time I find a basis in the set of the permutations I write it down.
"""

for possible_basis in itertools.permutations(vector_list, n):
    if np.linalg.det(possible_basis) % 2 == 1:
        f.write('\n')
        f.write(str(possible_basis))
        



