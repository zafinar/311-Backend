print(2+1)
print(2-1)
print(2**4)
print(4**0.5)
a2 = 5
print(a2)

array = [1,2,3]
array2 = [1,array,'LOL',2.1]
print(array2)
print(len(array2))
print(array2[::2])
print(array2[::3])
print(array2[1:3])
array2.append(array)
print(array2)
array2.extend(array)
print(array2)
lol = array2.pop()
print(lol)
array2.reverse()
print(array2)
print(array2[2][0])
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matrix[0][0])
first_col = [row[0] for row in matrix]
print(first_col)

a_dictionary = {"a":"illidan","b":2,"c":"extra"}
print(a_dictionary["a"])
#TUPLES,SETS,BOOLEANS
