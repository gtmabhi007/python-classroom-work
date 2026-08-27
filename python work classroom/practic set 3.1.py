# 1. Create a list of your five favorite movies and display the list.
movies = ["spiderman","dark","lost","avatar","god father"]
print("my five favorite movies is", movies)

# 2. Create a list containing 10 numbers and display: First, Last, Middle element
numbers = [1,2,3,4,5,6,7,8,9,10]
print("first element", numbers[0])
print("last element", numbers[-1])
print("middle element",numbers[5])

# 3. Create a list of five cities and print the list in reverse order using slicing.
city = ["agra","mumbai","delhi","punjab","gujarat"]
print(city[ : :-1])


# 4. Create two lists of five numbers each and combine.
a = [1,2,3,4,5]
b = [6,7,8,9,10]
c = a+b
print(c)

# 5. Create a list and display it three times.
a = [1,2,3,4,5,6]
print(a*3)

# 6. Create a list of five fruits and add one more fruit. Now, Insert your favorite color
#  at the second position of a list.

fruits = ["apple","mango","orange","grapes","banana"]
fruits.append("fig")
fruits[0]="green"
print(fruits)

 # 7 Create two lists & combine them using `extend()`.Now, remove last element.
a = [1,2,3,4]
b = [5,6,7,8]
a.extend(b)
a.pop()
print(a)

# 8. Remove the third element using `del`. Now, remove all elements.
a = ["toy","boy","sun","hii","pen"]
del a[2]
print("after del", a)
a.clear()
print("after remove all element", a)

# 9. Create a list of numbers and sort it in ascending and descending order.
a = [9,19,20,90,12,16]
a.sort()
print("ascending order",a)
a.sort(reverse=True)
print("descending order",a)

# 10. Reverse a list using the `reverse()` method.
a = ["one","two","three","four"]
a.reverse()
print("reversed",a)

# 11. Create a copy of a list using `copy()` and print both lists.
original_element = [1,2,3,4]
copy_element = original_element.copy()
print("all original elements is",original_element)
print("copy element is",copy_element)

# 12. Create a list containing duplicate values and count the occurrence of a particular
value using `count()`.
repeats = [1,2,3,2,4,2,5,2,]
count = repeats.count(2)
print("occurrence of 2",count)

# 13. Find the index of a given element using the `index()`.
number =["1","2","3","4"]
index = number.index("3")
print("index of '3'=",index)

# 14. Create a nested list representing a 3×3 matrix and print it.
# Create a 3x3 matrix using a nested list
matrix = [
    [1, 2, 3],  
    [4, 5, 6],  
    [7, 8, 9]   
]

print("3*3 Matrix")
for row in matrix:
    print(row)  

# 15. Perform the following slicing operations on a list of numbers from 1 to 10:
# First 5 elements, Last 5 elements, Every second element, Reverse the list
a= list(range(1,11))
print("first 5 element is ",a[:5])
print("last 5 element is ",a[-5:])
print("every second",a[::2])
print("reversed",a[::-1])




