age=int(input("Enter Age:"))
try:
    if age<0:
        raise ValueError ("Invalid age")
    print("Your age is:",age)
except ValueError as v:
    print(v)
finally:
    print("HUM CHECK KAR RAHE H RAISE KO")


