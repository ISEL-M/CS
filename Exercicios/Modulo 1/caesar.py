import string


def indexOrMax(s, query):
    try:
        i = s.index(query)
    except ValueError:
        return len(s)
    return i


def caesar_encrypt(plaintext, offset=3):
    alphabet = string.ascii_lowercase
    indices = map(lambda char: indexOrMax(alphabet, char), plaintext)
    cyphertext = ''.join([alphabet[(i + offset) % len(alphabet)] for i in indices])
    return cyphertext


if __name__ == '__main__':
    m = 'acifradecesar'
    c = caesar_encrypt(m)

    print("Texto limpo: {}".format(m))
    print("Texto cifrado: {}".format(c.upper()))

    # find caesar offset to decrypt
