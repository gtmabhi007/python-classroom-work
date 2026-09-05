# # 1. to print all even & odd numbers separately from 1 to 50 using a loop and conditional statements.
# print("Even numbers")
# for i in range(1, 51):
#     if i % 2 == 0:
#         print(i, end=",")
# print("/n")
# print("Odd numbers")
# for i in range(1, 51):
#     if i % 2 != 0:
#         print(i, end=",")

# # 2. to find the sum of all numbers between 1 and 100 that are divisible by both 3 and 5.
# sum = 0

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         sum += i

# print("Sum =", sum)


# # 3. to accept 10 numbers from the user and count how many are positive, negative, and zero using a
# # loop and conditional statements.

# positive = 0
# negative = 0
# zero = 0

# for i in range(10):
#     num= int(input("Enter a number:= "))

#     if num > 0:
#         positive += 1
#     elif num < 0:
#         negative += 1
#     else:
#         zero += 1

# print("Positive numbers:", positive)
# print("Negative numbers:", negative)
# print("Zero:", zero)

# # 4. to check whether a given number is an Armstrong number or not using a loop and conditional
# # statements.
# num = int(input("Enter a number:= "))
# original = num
# sum = 0

# while num > 0:
#     digit = num % 10
#     sum = sum + (digit ** 3)
#     num = num // 10

# if sum == original:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")

# # 5. to generate the multiplication tables from 1 to 5. For each table, display only those multiples that
# # are even.


# for i in range(1, 6):
#     print("Table of", i)

#     for j in range(1, 11):
#         if (i * j) % 2 == 0:
#             print(i, "x", j, "=", i * j)
#     print()

# # 6. using nested loops to print the following pattern:
# for i in range(1, 6):
#     for j in range(i):
#         print("*", end="")
#     print()

# # 7. using nested loops to print all pairs (i, j) where i and j range from 1 to 5, but display only those
# # pairs whose sum is even.

# for i in range(1, 6):
#     for j in range(1, 6):
#         if (i + j) % 2 == 0:
#             print("(", i, ",", j, ")")


# # 8. using nested loop to print the multiplication tables from 2 to 5, with each table containing multiples
# # from 1 to 10. Use a conditional statement to display only the multiples that are divisible by 3.
# for i in range(2, 6):
#     print("Multiplication Table of", i)

#     for j in range(1, 11):
#         result = i * j

#         if result % 3 == 0:
#             print(i, "x", j, "=", result)

#     print()

# # 9. to print numbers from 1 to 20, but use continue to skip all numbers that are divisible by 3.
# for i in range(1, 21):
#     if i % 3 == 0:
#         continue
#     print(i)

# # 10. that repeatedly accepts numbers from the user and calculates their sum. Terminate the loop using
# # break when the user enters 0.

# sum = 0
# while True:
#     num = int(input("Enter a number:= "))

#     if num == 0:
#         break

#     sum = sum + num

# print("Sum =", sum)


# # 11. to print numbers from 1 to 10. Use pass when the number is 5 and observe that the loop
# # continues normally. Also display all the numbers.
# for i in range(1, 11):
#     if i == 5:
#         pass
#     print(i)


