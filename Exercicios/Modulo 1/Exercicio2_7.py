"""
ISEL | DEETC | MEET, MEIC, MEIM (2021/2022)
Cibersegurança (CS): Módulo I - Mecanismos para proteção da informação
"""
__author__ = "46307 Diogo Ribeiro"
__version__ = "1.0.0"


# (b) [Implementação]
def padd_oneandzeroes(sequencia_bits, n_bits=8):
    """Realiza o padding OneAndZeroes.

    :param sequencia_bits: sequência de bits
    :type sequencia_bits: str|list
    :param n_bits: comprimento n de cada bloco do padding
    :return: sequência de bits, com o preenchimento completo"""
    # limpeza do formato dos dados
    sequencia_bits = sequencia_bits.replace('0b', '') if isinstance(sequencia_bits, str) else sequencia_bits

    # adicionar um 1
    sequencia_pad = ''.join(map(str, sequencia_bits)) + '1'

    # se necessário, adicionar bits com valor 0 ao fim dos dados até que o tamanho destes seja múltiplo de n.
    n_zeros = n_bits - len(sequencia_pad) % n_bits
    pad = '0' * n_zeros
    sequencia_pad += pad

    return sequencia_pad


def padd_trailingbitcom(sequencia_bits, n_bits=8):
    """Realiza o padding TrailingBitComplement.

    :param sequencia_bits: sequência de bits
    :type sequencia_bits: str|list
    :param n_bits: comprimento n de cada bloco do padding
    :return: sequência de bits, com o preenchimento completo"""

    # limpeza do formato dos dados
    sequencia_bits = sequencia_bits.replace('0b', '') if isinstance(sequencia_bits, str) else sequencia_bits

    # escolher o bit oposto ao último
    val = ('0', '1')
    ref = val[sequencia_bits[-1] is val[0]]

    # calcular tamanho do padding
    n = n_bits - len(sequencia_bits) % n_bits
    if not n:
        n = 8
    pad = ref * n
    sequencia_pad = ''.join(map(str, sequencia_bits)) + pad

    return sequencia_pad


def unpadd_oneandzeroes(sequencia_bits, n_bits=8):
    """Retira o padding OneAndZeroes.

    :param sequencia_bits: sequência de bits
    :type sequencia_bits: str|list
    :param n_bits: comprimento n de cada bloco do padding
    :return: sequência de bits, com o preenchimento removido"""

    # cortar a partir do último 1
    idx = sequencia_bits.rfind('1')
    return sequencia_bits[:idx]


def unpadd_trailingbitcom(sequencia_bits, n_bits=8):
    """Retira o padding TrailingBitComplement.

    :param sequencia_bits: sequência de bits
    :type sequencia_bits: str|list
    :param n_bits: comprimento n de cada bloco do padding
    :return: sequência de bits, com o preenchimento removido"""

    # escolher o bit oposto ao último
    val = ('0', '1')
    ref = val[sequencia_bits[-1] is val[0]]

    # cortar a partir do primeiro bit complementado
    idx = sequencia_bits.rfind(ref) + 1
    return sequencia_bits[:idx]


# (a1) Considere os arrays de bits
m = '00101111101'
m_ = '01011111'

# i. Realize o padding dos arrays m e m′ usando o OneAndZeroes para blocos de 8-bits;
R_m1 = padd_oneandzeroes(sequencia_bits=m, n_bits=8)
'''Outros formatos válidos exemplo:
    R_m = padd_oneandzeroes(sequencia_bits='0b00101111101', n_bits=8)
    R_m = padd_oneandzeroes(sequencia_bits=[0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1], n_bits=8)'''
print(f'a1.i)\n\tpad(m): {m} ({len(m)} bits) => {R_m1} ({len(R_m1)} bits)')

R_m_1 = padd_oneandzeroes(sequencia_bits=m_, n_bits=8)
print(f'\tpad(m\'): {m_} ({len(m_)} bits) => {R_m_1} ({len(R_m_1)} bits)')

# ii. Realize o padding do arrays m e m′ usando o TrailingBitComplement para blocos de 8-bits.
R_m2 = padd_trailingbitcom(sequencia_bits=m, n_bits=8)
'''Outros formatos válidos exemplo:
    R_m = padd_oneandzeroes(sequencia_bits='0b00101111101', n_bits=8)
    R_m = padd_oneandzeroes(sequencia_bits=[0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1], n_bits=8)'''
print(f'a1.ii)\n\tpad(m): {m} ({len(m)} bits) => {R_m2} ({len(R_m2)} bits)')

R_m_2 = padd_trailingbitcom(sequencia_bits=m_, n_bits=8)
print(f'\tpad(m\'): {m_} ({len(m_)} bits) => {R_m_2} ({len(R_m_2)} bits)')

# (a2) Dado o array de 16 bits
m__ = '0000111100001111'
# indique:

# i. O array original se m′′ for o resultado de um OneAndZeroes para blocos de 4 bits;
R_m__1 = unpadd_oneandzeroes(sequencia_bits=m__, n_bits=4)
print(f'a2.i) unpad(m\'\'): {m__} ({len(m__)} bits) => {R_m__1} ({len(R_m__1)} bits)')

# ii. O array original se m′′ for o resultado de um TrailingBitComplement para blocos de 4-bits.
R_m__2 = unpadd_trailingbitcom(sequencia_bits=m__, n_bits=4)
print(f'a2.ii) unpad(m\'\'): {m__} ({len(m__)} bits) => {R_m__2} ({len(R_m__2)} bits)')
