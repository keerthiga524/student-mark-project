name = input("Enter student name: ")
m1 = int(input("Enter mark 1: "))
m2 = int(input("Enter mark 2: "))
m3 = int(input("Enter mark 3: "))

total = m1 + m2 + m3
avg = total / 3

print("Name:", name)
print("Total:", total)
print("Average:", avg)

if avg >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")
