## Q4. Loop over a dict and print keys & values

student={
    "Name": "Neel",
    "Age": 21,
    "Marks": 80,
}
# First Option
for keys,values in student.items():
    print(f"{keys} is {values}")

# Second Option
for i in student.items():
    print(f"{i[0]} is {i[1]}")
