# Exercice 6.2 Liste des extensions

def searchext(l):
    return [
        name.rsplit('.', 1)[-1].lower()
        for name in l
        if '.' in name and name.rsplit('.', 1)[0]
    ]
    """
    Identifie les extensions de la liste de fichiers passÃ©e en argument

    Args:
        l : liste des noms de fichier sous forme de chaine de caractÃ¨res

    Returns:
        Liste des extensions sous forme de chaine de caractÃ¨res
        
    >>> l = searchext(['ARJ.PIF', 'atiogl.xml', 'ativpsrm.bin', 'bfsvc.exe'])
    >>> isinstance(l, list) # vrai si l est une liste
    True
    >>> print(l)
    ['pif', 'xml', 'bin', 'exe']

    >>> l = searchext(['HelpPane.exe', 'hh.exe', 'HPMProp.INI', 'IE9_main.log'])
    >>> isinstance(l, list) # vrai si l est une liste
    True
    >>> print(l)
    ['exe', 'exe', 'ini', 'log']

    >>> l = searchext(['win.ini', 'WindowsShell', 'WindowsUpdate.log', 'winhelp.exe'])
    >>> isinstance(l, list) # vrai si l est une liste
    True
    >>> print(l)
    ['ini', 'log', 'exe']

    >>> l = searchext(['Gfxv2_0.exe.config', 'pstask.dll', 'GfxValDisplayLog.bin'])
    >>> isinstance(l, list) # vrai si l est une liste
    True
    >>> print(l)
    ['config', 'dll', 'bin']
    """
    
    # une list comprehension e des extensions sous forme de chaine de caractÃ¨res
def main():
    l = searchext(['win.ini', 'WindowsShell', 'WindowsUpdate.log', 'winhelp.exe'])
    print(l)
    
main()