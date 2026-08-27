# 1. Write program to add following elements to an existing set: 25,35,45. Print new set.
a = {10, 20, 30}
a.update([25, 35, 45])
print("Updated set:=", a)

# 2. Write a Python program to remove elements from a set using:
# `remove()`, `discard()`, `pop()` Display the set after each operation.
# Initial set
numbers = {10, 20, 30, 40}
print ("original set",numbers)
numbers.remove(20)
print("After remove(20):", numbers)
numbers.discard(30)
print("After discard(30):", numbers)
remove = numbers.pop()
print("Element pop:",remove)

# 3. Write a Python program to create two sets and perform the following operations:
# Union, Intersection, Difference, Symmetric Difference. Display result of each operation.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)

union_result = set1.union(set2)       
print("Union:", union_result)
intersection_result = set1.intersection(set2)
print("Intersection :", intersection_result)

difference_a_b = set1.difference(set2)  
difference_b_a = set2.difference(set1)  
print("Difference b/w (A - B):", difference_a_b)
print("Difference b/w (B - A):", difference_b_a)

sym_diff = set1.symmetric_difference(set2)  
print("Symmetric Difference):", sym_diff)

# 4. Write a Python program to determine whether two sets are disjoint.
set1 = {1, 2, 3, 4}
set2 = {5, 6, 7}

if set1.isdisjoint(set2):
    print("Sets are disjoint")
else:
    print("Sets are not disjoint")




































