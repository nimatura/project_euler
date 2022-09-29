"""
Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for
Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value,
taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text,
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random
bytes. The user would keep the encrypted message and the encryption key in different locations, and without both
"halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the
password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The
balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using p059_cipher.txt
(right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the
plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original
text.
"""

from string import ascii_lowercase
from itertools import permutations

from functions.cryptography import xor_encryption


with open('../../data/p059_cipher.txt', 'r') as f:
    contents = f.read()


common_words = ['the', 'be', 'and']  # top 3 most common english words according to COCA rank


encrypted = [int(c) for c in contents.split(',')]


for password in permutations(ascii_lowercase, 3):
    key = [ord(c) for c in password]
    decrypted = xor_encryption(encrypted, key)
    decrypted_text = ''.join(chr(c) for c in decrypted)
    common_words_count = {w: decrypted_text.count(w) for w in common_words}
    mean_word_length = sum(len(w) for w in decrypted_text.split()) / len(decrypted_text.split())
    if mean_word_length <= 10 and sum(common_words_count.values()) >= 20:
        print(decrypted_text)
        print(sum(decrypted))
# 129448
