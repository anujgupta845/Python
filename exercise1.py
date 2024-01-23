n = int(input("Enter the time %H (1 to 24): "))
if(n >= 1  and n <= 12):
    print("Good Morning")
elif(n >= 13 and n <= 16):
    print("Good Afternoon")
elif(n >= 17 and n <= 20):
    print("Good Evening")
else:
    print("Good Night")