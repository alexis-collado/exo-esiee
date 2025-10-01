a = int(input("Entrez un nombre : "))

def premier(n):
    for i in range(2,n):
        if(n%i)==0:
            print(f"{n} = {i} x {n // i} : False")
            break
    else:
        print(str(n)+" : True")
    
premier(a)