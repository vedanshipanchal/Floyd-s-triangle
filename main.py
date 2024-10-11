n=int(input("Enter rows:"))
number = 1 

for row in range(1,n+1): #row range range depends on  input
    for col in range(1,row+1): #number val on col
        print(number,end="  ")
        number = number + 1 # number increases by 2
    print("\n")
        
    