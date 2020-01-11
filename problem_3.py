
try:   
    number = int(input("Enter Number: "))
    factors = []
    while number!=1:
        i = 1
        while True:
            i = i+1
            if number%i==0:
                factors.append(i)
                number=number/i
                break 
    print(max(factors))
except:
    print("Imput Number!!")

