

def reverse(a):
    s=a[::-1]
    return s


while True:
    print("String programs")
    print("1. Reverse String")


    search = input("Enter the values between (1 to 40)")

    if search == "1":
        s=input("Enter the String you want to Reverse :")
        print(f"Rerver value of {s} is : {reverse(s)}")
    
    count = input("Do you want to check another program? (Yes/No)")
    if count.lower() != "yes":
        break


