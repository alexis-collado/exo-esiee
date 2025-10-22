# Vos import ici
import string

def check_password(password):

    s=str(password)
    if len(password)<=9:
        return False
    if any(i.isupper() for i in str(password)) and \
       any(i.islower() for i in str(password)) and \
       any(i.isdigit() for i in str(password)):
        return True

    else:
        return False
    """
    Teste la robustesse d'un password

    Args:
        password: chaine de caractÃ¨res

    Returns:
        True or False

    >>> check_password('A1213pokl')
    False
    >>> check_password('bAse730onE')
    True
    >>> check_password('asasasasasasasaas')
    False
    >>> check_password('QWERTYqwerty')
    False
    >>> check_password('123456123456')
    False
    >>> check_password('QwErTy911poqqqq')
    True
    """

    # Si la longueur n'est pas conforme, retourner False
    # Si l'un des caractÃ¨res n'est pas un chiffre, retourner False
    # Si l'un des caractÃ¨res n'est pas une lettre minuscule, retourner False
    # Si l'un des caractÃ¨res n'est pas une lettre majuscule, retourner False

    # Q : OÃ¹ puis je trouver l'ensemble des lettres et des chiffres sans le reconstituer moi mÃªme ? 
    # R : Jeter un oeil au module string
    
    return False

def main():
    result = check_password('bAseQwErTy911poqqqq730onE')
    print(result)
    pass

if __name__ == '__main__':
    main()