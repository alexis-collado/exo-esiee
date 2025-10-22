def is_cyclope(n):
    n=str(n)
    mid=(len(n)//2)
    c=n[mid]
    if len(n)%2!=0:
        if(c=="0"):
            return True
    else:
        return False
    
    """retourne la vérité de "n est un nombre cyclope"

    Args:
        n (int): nombre à tester

    Returns:
        bool: True si "n est un nombre cyclope". False sinon
    
    >>> n = 1230456
    >>> is_cyclope(n)
    True
    >>> n = 1237456
    >>> is_cyclope(n)
    False
    >>> n = 120056
    >>> is_cyclope(n)
    False
    """
    return False

def main():
    print(is_cyclope(1230456))
    print(is_cyclope(1237456))
    print(is_cyclope(120056))
    pass

if __name__ == "__main__":
    main()
