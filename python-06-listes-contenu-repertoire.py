import os

def scand(r):
    
    d=[f.path for f in os.scandir(r) if f.is_dir()]
    f=[f for f in os.listdir(r) if os.path.isfile(os.path.join(r, f))]
    return f, d

def main():
    # votre code de test ici...
    # Exemple
    f, d = scand('.')
    print("file ", f)
    print("dir", d)
    pass

if __name__ == '__main__':
    main()