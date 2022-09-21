import math

"""
ISEL | DEETC | MEET, MEIC, MEIM (2021/2022)
Cibersegurança (CS): Módulo I - Mecanismos para proteção da informação
"""
__author__ = "46307 Diogo Ribeiro"
__version__ = "1.0.0"


# (b) [Implementação]
def chave_partilhada_DH(p: int, alpha: int, x: int, y: int):
    """Gera a chave secreta partilhada
    a partir do conhecimento de ambas as chaves privadas.

    :param p: um número primo
    :param alpha: gerador multiplicativo de Zp
    :param x: chave privada de Alice
    :param y: chave privada de Bob
    :return: chave secreta partilhada
    """

    # chaves públicas
    A = alpha**x % p  # gerada pelo intelocutor
    print(f"Alice gera a sua chave pública, e envia pelo canal aberto para Bob: {A}")
    B = alpha**y % p  # recebida pelo canal
    print(f"Bob gera a sua chave pública, e envia pelo canal aberto para Alice: {B}")

    k = alpha**(x*y) % p
    assert A**y % p == B**x % p == alpha**(x*y) % p
    return k


def hack_DH(p: int, alpha: int, mensagemA: int, mensagemB: int):
    """Simula um ataque em que é conhecido p e alpha e lidas as mensagens entre Alice e Bob.
    Tenta resolver o logaritmo discreto.

    :param p: um número primo
    :param alpha: gerador multiplicativo módulo p
    :param mensagemA: um inteiro módulo p, chave pública de Alice
    :param mensagemB: um inteiro módulo p, chave pública de Bob
    :return: chaves privadas de A e B, ou seja, iguais aos expoentes x, y tais que α^x = mensagemA e α^y = mensagemB
    """
    assert alpha % p == alpha
    assert mensagemA % p == mensagemA
    assert mensagemB % p == mensagemB

    x, i = .1, 1
    while not x.is_integer():  # abs(x - int(x)) > 1e-10?
        x = math.log(i*p + mensagemA, alpha)
        i += 1

    y, j = .1, 1
    while not y.is_integer():  # abs(y - int(y)) > 1e-10?
        y = math.log(j*p + mensagemB, alpha)
        j += 1

    print(f"Sucesso! Iterações necessárias para o logaritmo discreto: {i + j}")
    return int(x), int(y)


if __name__ == '__main__':
    print(f"Chave secreta partilhada: {chave_partilhada_DH(p=13, alpha=6, x=4, y=2)}")

    # mensagens A e B recebidas pelo canal (chaves públicas)
    print(f"Chaves privadas: {hack_DH(p=13, alpha=6, mensagemA=9, mensagemB=10)}")
