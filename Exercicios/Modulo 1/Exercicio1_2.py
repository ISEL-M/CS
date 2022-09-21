import matplotlib.pyplot as plt
from collections import Counter
from caesar import caesar_encrypt
import textdistance

most_used = {}
start_most = {}
end_most = {}

english_letters = {'E': 12.0,
                   'T': 9.10,
                   'A': 8.12,
                   'O': 7.68,
                   'I': 7.31,
                   'N': 6.95,
                   'S': 6.28,
                   'R': 6.02,
                   'H': 5.92,
                   'D': 4.32,
                   'L': 3.98,
                   'U': 2.88,
                   'C': 2.71,
                   'M': 2.61,
                   'F': 2.30,
                   'Y': 2.11,
                   'W': 2.09,
                   'G': 2.03,
                   'P': 1.82,
                   'B': 1.49,
                   'V': 1.11,
                   'K': 0.69,
                   'X': 0.17,
                   'Q': 0.11,
                   'J': 0.10,
                   'Z': 0.07}

most_used['EN'] = ''.join([letter for letter, _ in sorted(english_letters.items(), key=lambda m: -m[1])])
# extra info (unused)
start_most['EN'] = 'taodw'
end_most['EN'] = 'esdt'

portuguese_letters = {'E': 13.19,
                      'A': 12.21,
                      'O': 10.22,
                      'S': 7.35,
                      'R': 6.73,
                      'I': 5.49,
                      'M': 5.07,
                      'T': 5.07,
                      'N': 5.02,
                      'U': 4.46,
                      'D': 4.21,
                      'C': 3.35,
                      'P': 3.01,
                      'L': 3.00,
                      'V': 1.72,
                      'H': 1.22,
                      'Q': 1.10,
                      'G': 1.08,
                      'F': 1.07,
                      'B': 1.01,
                      'Ã': 0.83,
                      'É': 0.52,
                      'Z': 0.45,
                      'Á': 0.41,
                      'Ç': 0.40,
                      'Ê': 0.36,
                      'J': 0.30,
                      'X': 0.28,
                      'Í': 0.18,
                      'Ó': 0.17,
                      'K': 0.13,
                      'Ú': 0.11,
                      'W': 0.05,
                      'À': 0.04,
                      'Õ': 0.04,
                      'Y': 0.04,
                      'Â': 0.03,
                      'Ô': 0.01}
most_used['PT'] = ''.join([letter for letter, _ in sorted(portuguese_letters.items(), key=lambda n: -n[1])])

en = english_letters
plt.title('English word frequency')
plt.plot(en.keys(), en.values())
#plt.show()

pt = portuguese_letters
plt.title('Portuguese word frequency')
plt.plot(pt.keys(), pt.values())
#plt.show()

cyphertext = 'DFLIUDGHFHVDU'
counts = Counter(cyphertext.upper())
# convert absolute to relative? divide all counts by sum
cypheralphabet = ''.join([letter for letter, _ in sorted(counts.items(), key=lambda i: i[1])])
print('Encrypted alphabet: {}'.format(cypheralphabet))
test_against = most_used['PT'][:len(cypheralphabet)]
print('Portuguese alphabet: {}'.format(test_against))

# brute force distance between alphabets
result = {}
for i in range(1, len(most_used['PT'])):
    decrypt_alph = caesar_encrypt(cypheralphabet.lower(), i)
    print("{} vs {}".format(decrypt_alph, test_against))
    result[i] = textdistance.ratcliff_obershelp(decrypt_alph.lower(), test_against.lower())
print(result)

best_result = min(result, key=result.get)
decrypt = caesar_encrypt(cyphertext.lower(), best_result)
print('Closest key found: {}'.format(best_result))
print('Decryption result: {}'.format(decrypt.upper()))
