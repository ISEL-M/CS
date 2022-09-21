def scytale_encrypt(plaintext, rows, group_size=1):
    groups = [plaintext[i:i + group_size] for i in range(0, len(plaintext), group_size)]
    cyphertext = ''.join([s for i, s in sorted(list(enumerate(groups)), key=lambda i: i[0] % rows)])
    return cyphertext


'''
m : texto limpo
c : texto cifrado
k : chave
ek : metodo para cifrar
dk : metodo para decifrar
'''

if __name__ == '__main__':
    m = 'acitalaeumsistemadecifrausadonaantigagrecia'
    print("3. Texto limpo: {}".format(m))

    k1 = (4, 1)
    c1 = scytale_encrypt(m, *k1)
    print("\ta) Texto cifrado: {}".format(c1.upper()))

    k2 = (6, 1)
    c2 = scytale_encrypt(m, *k2)
    print("\tb) Texto cifrado: {}".format(c2.upper()))

    k2 = (5, 1)
    c2 = scytale_encrypt(m, *k2)
    print("\tb) Texto cifrado: {}".format(c2.upper()))

    # find scytale sizes to decrypt
