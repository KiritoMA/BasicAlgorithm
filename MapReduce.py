arr1 = [1,2,3,4,5]
#map get a iterator
#in python3 list() is needed
arr2 = list(map(lambda x: 2 * x, arr1))
print(arr2)
from functools  import reduce
def f4(x,y):
    return (x+y)
arr3 = reduce(f4 ,arr1)
print(arr3)
