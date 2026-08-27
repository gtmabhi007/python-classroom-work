# 1. Create a tuple of five integers and print all elements. Access the first, last, and
# middle elements of a tuple.
a = (12,11,22,33,44)
prin#t("all the element is ",a)
print(a[0],a[3],a[1],a[2])

# 2. Count occurrence of a specific value. Also, find the index of a given element.
a = (10,20,30,20,50,20)
print(a.count(3))
print(a.index(5))


# 3. Concatenate two tuples & display the result. Also, Repeat a tuple three times.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2
print(result)
print(result)
print(result)


# 4. Reverse a tuple using slicing, find the max, min, sum, & average.
a = (10, 25, 5, 40, 15)

print(a[::-1])

print(min(a))
print(max(a))
print(sum(a))
print(sum(a)/len(a))

# 5. Convert a list into a tuple and a tuple into a list.
my_list = [1, 2, 3, 4, 5]
converted_tuple = tuple(my_list)
print("List converted into Tuple:", converted_tuple)
my_tuple = ('A', 'B', 'C', 'D')
converted_list = list(my_tuple)
print("Tuple converted into List:", converted_list)

# 6. Perform tuple packing and unpacking for student details. Demonstrate
# extended unpacking.
student = ("ravi", 21, "Computer Science", "A+", "Basketball")

print("Packed Tuple:", student)
name, age, course, grade, hobby = student

print("Name:", name)
print("Age:", age)
print("Course:", course)
print("Grade:", grade)
print("Hobby:", hobby)


student_details = ("ram", 22, "Mathematics", "B+", "Chess", "Swimming", "Music")
name, age, *extras = student_details

print("\nExtended Unpacking Example:")
print("Name:", name)
print("Age:", age)
print("Other Details:", extras)


first, *middle, last = student_details
print("\nCapturing Middle Values:")
print("First:", first)
print("Middle:", middle)
print("Last:", last)

# 7. Create a nested tuple and access inner elements.

student = ("ravi", 18,("Computer Science", "A+", ("Basketball", "Chess")))
print("Nested Tuple:", student)

print("\nAccessing Inner Elements:")
print("Name:", student[0])                
print("Age:", student[1])                
print("Course:", student[2][0])          
print("Grade:", student[2][1])            
print("Hobby 1:", student[2][2][0])       
print("Hobby 2:", student[2][2][1])       

name, age, (course, grade, (hobby1, hobby2)) = student

print("\nUnpacking Nested Tuple:")
print("Name:", name)
print("Age:", age)
print("Course:", course)
print("Grade:", grade)
print("Hobby 1:", hobby1)
print("Hobby 2:", hobby2)

# 8. Store student records as tuples inside a list and display names with marks.
# students = [("ravi", 85),("ram", 92),("harsh", 76), ("shivam", 89)]

print("Student Names with Marks:\n")

for student in students:
    name, marks = student   
    print(f"Name: {name}, Marks: {marks}")

# 9. Swap two variables using tuple unpacking.
a = 10
b = 20

a, b = b, a
print("a =", a)
print("b =", b)

# 10.Generate squares of numbers from 1 to 10 and store them in a tuple using
tuple(x*x for x in range(1, 11)).
squares = tuple(x * x for x in range(1, 11))
print(squares)






































