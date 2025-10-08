def syracuse(n):
    n0 = n;u = n;tv = 0;am = n;tva = None 

    while u!=1:
        if u%2==0:
            u//=2
        else:
            u=3*u+1
        tv+=1
        if u>am:
            am=u
        if tva is None and u < n0:
            tva=tv
    if tva is None:
        tva=0

    return tv, tva-1, am

def main():
    n=15
    tv,tva,am =syracuse(n)
    print(n,tv,tva,am)

if __name__ == "__main__":
    main()