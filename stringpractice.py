def evenstring(a):
    print("Orignal String:" + a)
    s=a.split()
    for i in s:
        if len(i)%2 ==0:
            print(i,end=" ")
    print("/n")
def length(a):
    return len(a)

def reverse(a):
    return a[::-1]
def palindrome(a):
    return a==a[::-1]
def vowel(a):
    return a.count("a")+a.count("e")+a.count("i")+a.count("o")+a.count("u")
def remove(a):
   print("Enter your Choice")
   print("1. Remove only selected letter")
   print("2. Remove complete string")

   choice = int(input("Enter your Choice"))

   if choice==1:
       r=input("Enter the letter you want me to remove from Charactor :")
       return a.replace(r,"")
   elif choice==2:
       return a.replace("","")         
   else:
       print("Enter Correct Choice")
    
def cap(a):
    s=a.split(" ")
    res=[]
    x=""
    for i in s:
        x=i[0].upper()+i[1:-1]+i[-1].upper()
        res.append(x)
    res=" ".join(res)
    return res


while True:
    
    print("==============================")
    print("Lets play with string, select your choice from below")
    print("1.Length of the string")
    print("2.Reverse of the string")
    print("3.Palindrome of the string")
    print("4.Vowel in the string")
    print("5.After removing String from charactor ")
    print("6. Print even Character from given Sentence")
    print("7.Capitalize the first and last character of each word in a string")
    print("=========================================")

    
   
    choice = int(input("Enter the choice: "))
    if choice==1:
        print("Enter the string")
        a=input()
        print(f"Length of the string :{length(a)}")
    elif choice==2:
        print("Enter the string")
        a=input()
        print(f"Reverse of the string :{reverse(a)}")
    elif choice ==3:
        print("Enter the string")
        a=input()
        print(f"Palindrome of the string: {palindrome(a)}")
        # print(palindrome(a))
    elif choice==4:
        print("Enter the string")
        a=input()
        print(f"Vowel in the string : {vowel(a)}")
    elif choice ==5:
        print("Enter the string")
        a=input()
        print(f"Remove the character from the string : {remove(a)}")
    elif choice == 6:
        print("Enter the string")
        s=input()
        # print(f"Even String from Given Sentence are : {evenstring(s)}")
        evenstring(s)
    elif choice == 7:
        print("Enter the string")
        s=input("Orignal String :")
        print(f"Result :{cap(s)}")
    else:
        print("Invalid choice")
    
    print("Try Again? (y/n): ")
    choice = input()
    if choice == 'n':
        break


    





        
  