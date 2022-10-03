#Modulo hashlib
import hashlib

wlist = input("Wordlist: ")
hash = input("Hash: ")

#Leer el archivo
wlistlineas = open(wlist, "r").readlines()

#loop
for h in range(0,len(wlistlineas)):
    hashcomp = hashlib.md5(wlistlineas[h].replace("\n","").encode()).hexdigest()

    #Comparación
    if hash == hashcomp:
        print ("Resultado: "+ wlistlineas[h].replace("\n",""))
        exit()
print ("Error, no se ha encontrado ninguna contraseña")