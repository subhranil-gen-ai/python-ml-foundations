# Q3. Write a program:
## Input marks -> If marks ≥ 40 → Pass Else → Fail

marks=int(input('Enter your marks:'))
if 0 <= marks <= 100:
    if marks>=40:
         print("Pass")
    else:
        print("Fail")
else:
    print("Invalid Marks")
