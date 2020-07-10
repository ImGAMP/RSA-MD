'''

Codigo RSA
'''
'''
Funciones
'''
def mcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a
def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
def coprimes(a):
    l = []
    for x in range(2, a):
        if mcd(a, x) == 1 and modinv(x,phi) != None:
            l.append(x)
    for x in l:
        if x == modinv(x,phi):
            l.remove(x)
    return l
def encrypt_block(m):
    c = modinv(m**e, n)
    if c == None: print('Sin inversa multiplicativa modular para bloque ' + str(m) + '.')
    return c
def decrypt_block(c):
    m = modinv(c**d, n)
    if m == None: print('Sin inversa multiplicativa modular para bloque ' + str(c) + '.')
    return m
def encrypt_string(s):
    return ''.join([chr(encrypt_block(ord(x))) for x in list(s)])
def decrypt_string(s):
    return ''.join([chr(decrypt_block(ord(x))) for x in list(s)])

'''
Presentacion
'''
print ("Escoge la opcion que deseas aplicar: \n 1. Desencriptar mensaje \n 2. Encriptar mensaje \n 3. Añadir valores nuevos")
e=(input('Opcion: '))
    

r = e.lower() in ['1', '2', '3']
if not r:
    print('"{0}" no es una opcion valida'.format(e))
    print('Favor de volverlo a intentar.')

while not r:
    print("Escoge la opcion que deseas aplicar: \n 1. Desencriptar mensaje \n 2. Encriptar mensaje \n 3. Añadir valores nuevos")
    e=(input('Opcion: '))
    r = e.lower() in ['1', '2', '3']
    
    if not r:
        print('"{0}" no es una opcion valida'.format(e))
        print('Favor de volverlo a intentar.')   
print("Usted escogio la opcion: " + str(e))
'''
----------RECOMENDACION-------------------
Encriptado: ;Y| , zJzJ 
Desencriptado: hol  , COCO

'''
if e == "1":
    p = 11
    q = 23
    n = p*q
    phi=(p-1)*(q-1)
    e = 7
    d = modinv(e,phi)
    s = input("Ingresa palabra a desencriptar: ")
    print("\nSu mensaje  es:" + s + "\n")
    dec = decrypt_string(s)
    print("Mensaje desencriptado: " + dec + "\n")
if e == "2":
    p = 11
    q = 23
    n = p*q
    phi=(p-1)*(q-1)
    e = 7
    d = modinv(e,phi)
    s = input("Ingresa palabra a encriptar: ")
    print("\nSu mensaje  es: " + s + "\n")
    enc = encrypt_string(s)
    print("Mensaje encriptado: " + enc + "\n")
if e == "3":
    p=int(input('Escoger primo p: '))
    q=int(input('Escoger primo q: '))
    print("Los primos escogidos fueron :\np=" + str(p) + ", q=" + str(q) + "\n")
    n=p*q
    print("n = p * q = " + str(n) + "\n")
    phi=(p-1)*(q-1)
    print("La función de Euler (totient) [phi(n)]: " + str(phi) + "\n")
    print("Seleccione el primo e:\n")
    print(str(coprimes(phi)) + "\n")
    e=int(input())
    d=modinv(e,phi)
    print("\nLa llave publica es el conjunto (e=" + str(e) + ", n=" + str(n) + ").\n")
    print("La llave privada es el conjunto (d=" + str(d) + ", n=" + str(n) + ").\n")
    s = input("Seleccione el mensaje a encriptar ")
    print("\nEl mensaje original: " + s + "\n")
    enc = encrypt_string(s)
    print("Mensaje encriptado: " + enc + "\n")
    dec = decrypt_string(enc)
    print("Mensaje desencriptado: " + dec + "\n")

    
    
    


