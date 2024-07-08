def add(a,b):
    c=a+b
    return c
def sub(a,b):
    c=a-b
    return c
def mul(a,b):
    c=a*b
    return c
def div(a,b):
    c=a/b
    return c


while True:
    print("Welcome to Canlulator word")
    print("Press 1 for Addition")
    print("Press 2  for Substration")
    print("Press 3  for Multiplication")
    print("Press 4  for Division")
    print("Press 5  for Exit")

    choice = input("Choice the value between (1 to 5) :")
    if choice == "5":
        break
    

    x=int(input("Enter First Value :"))
    y=int(input("Enter Second Value :"))
    if choice == "1":
        z = add(x,y)
        print(f"Addition of {x} + {y} = {z}")
    elif choice == "2":
        z = sub(x,y)
        print(f"Substraction of {x} - {y} = {z}")
    elif choice == "3":
        z = mul(x,y)
        print(f"Multiplication of {x} * {y} = {z}")
    elif choice == "4":
        z = div(x,y)
        print(f"Division of {x} + {y} / {z}")
    else:
        print("Invalid Number")

    cont = input("Continue? (y/n): ")
    if cont.lower() != "y":
        break
    print("+++++++++++++++++++++++++++++++++++++++++++++")

