# 1. Create a dictionary containing details of an employee. Print Employee Name,
# Department, Salary, Designation by accessing the values using their keys.
employee = {"name":"abhishek gautam" , "department":"cse_aiml" , "salary":"80000" , "designation":"developer"}
print("employee name =",employee["name"])
print("employee department =", employee["department"])
print("employee salary =",employee["salary"])
print("employee designation =", employee["designation"])


# 2. Write a program to add the following new key-value pairs to an existing dictionary:
# * Email * Phone Number. Print the updated dictionary.
employee = {"Name": "abhishek gautam","Department": "aiml", "Salary": 80000,"Designation": "developer"}
employee["Email"] = "abhishek@gmail.in"
employee["Phone Number"] = "9667621255"
print("Updated Dictionary")
print(employee)

# 3. Write a program to update the salary of an employee stored in a dictionary.
# Example: Before: {'Name':'Amit','Salary':45000}
# After: {'Name':'Amit','Salary':52000}
employee = {"name":"abhishek gautam" , "salary":"45000"}
print("before employee data")
print(employee)
employee["salary"]="52000"
print("after employee data")
print(employee)

# 4. Write a Python program to remove: * specific key * last inserted item
# Display the dictionary after each operation.
employee = {"Name": "abhishek gautam","Salary": 80000,"Designation": "developer","Email": "abhi@gmail.in"}
print("Original Dictionary \n",employee)
employee.pop("Email")
print("remove last specific key")
print(employee)
employee.popitem()
print(" After remove last key:value:")
print(employee)
print("dictionary after each operation:=",employee)


# 5. Given the dictionary: student = {"Roll":101,"Name":"Rahul","Branch":"CSE", "Sem":5}
# Write a program to: * Print all keys, all values and all key-value pairs.
student = {"Roll":101,"Name":"Rahul","Branch":"CSE", "Sem":5}
print("all keys",student.keys())
print("all values",student.values())
print("all key_value pairs",student.items())


# 6. Write a Python program to check whether a given key exists in a dictionary.
#Example: Input Key: Name Output: Key Found Otherwise display: Key Not Found

student = {"Name": "abhishek gautam","Roll no": 00000000,"Branch": "CSE AIML", "Sem": 3}
key = input("enter the key name:=")

if key in student:
    print("Key Found")
else:
    print("Key Not Found")

# 7. Write a program to count the total number of key-value pairs present in a dictionary.
dic = {"name":"abhishek gautam" , "salary":"45000"}
count = len(dic)
print("Total key-value pairs :", count)

# 8. Write a Python program to create a dictionary from the following two lists.
# keys = ["ID","Name","Age","City"]
# values = [101,"Ankit",20,"Delhi"]
# Expected Output: {'ID':101,'Name':'Ankit','Age':20,'City':'Delhi’}
keys = ["ID", "Name", "Age", "City"]
values = [101, "Ankit", 20, "Delhi"]
result = dict(zip(keys, values))
print(result)

# 9. Create a nested dictionary to store details of three students. Each student should
# have: Name, Branch, Semester, CGPA
# Print the complete nested dictionary.
# Nested dictionary storing details of three students
students = {"a": {"Name":"Aman","Branch":"CSE","Semester":5,"CGPA":8.6},
    "b": {"Name":"Neha","Branch":"ECE","Semester":4,"CGPA":8.2},
    "c": {"Name":"Rohit","Branch":"ME","Semester":6,"CGPA":7.9}  }
print("Complete Nested Dictionary:=",students)

# 10. Using the nested dictionary created in Question 11, print only:
# * Name of Student 2 * Branch of Student 3 * CGPA of Student 1
students = {"a": {"Name":"Aman","Branch":"CSE","Semester":5,"CGPA":8.6},
    "b": {"Name":"Neha","Branch":"ECE","Semester":4,"CGPA":8.2},
    "c": {"Name":"Rohit","Branch":"ME","Semester":6,"CGPA":7.9}  }
print("Name of Student 2:", students["b"]["Name"])
print("Branch of Student 3:", students["c"]["Branch"])
print("CGPA of Student 1:", students["a"]["CGPA"])


















