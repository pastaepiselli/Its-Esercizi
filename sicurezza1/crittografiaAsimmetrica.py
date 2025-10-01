# 1 prendere una stringa e covertirla in un numero intero 
pub_exp = 3
mess = 'Ehi popa, come va?'
mess = int(mess.encode('utf-8').hex(), 16)


# 2 convertire il modulo della chiave in un numero 

with open('sicurezza1/modulo.txt', mode='r') as f:
    modulo = f.read()
# rimuovo : , \n , e spazi
modulo = modulo.replace(':', '')
modulo = modulo.replace('\n', '')
modulo = modulo.replace(' ', '')
# # print(modulo)
# modulo = int(modulo, 16)

with open('sicurezza1/chiave_priv.txt', 'r') as b:
    chiave_privata = b.read()

chiave_privata = chiave_privata.replace(':', '')
chiave_privata = chiave_privata.replace('\n', '')
chiave_privata = chiave_privata.replace(' ', '')
# # print(chiave_privata)
# chiave_privata = int(chiave_privata, 16)


# # 3 crittografare

# messaggio_crittografato = pow(mess, pub_exp) % modulo

# print(messaggio_crittografato)



# mess_decript = pow(messaggio_crittografato, chiave_privata) % modulo

# ora sistemo cn una funzione 
# pub_exp = chiave pubblica
def conversione_hexadecimale(text: str) -> int:
    return int(text, 16)

def conversione_mess_numero(mess: str) -> int:
    return int(mess.encode('utf-8').hex(), 16)

def crittografia(mess: str, pub_exp: int, modulo: str) -> int:
    return pow(conversione_mess_numero(mess), pub_exp) % conversione_hexadecimale(modulo)

def decriptare(mess_cript: int, modulo: str, chiave_privata: str):
    segreto = pow(mess_cript, conversione_hexadecimale(chiave_privata)) % conversione_hexadecimale(modulo)
    return segreto

print(crittografia('Ciao!', 3, modulo))
print(crittografia('Ciao!', 3, modulo), modulo, chiave_privata)

# posso farlo meglio ora non ho voglia  


