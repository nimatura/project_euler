def xor_encryption(message, key):
    assert len(message) >= len(key)
    full_key = list(key)
    i = 0
    while len(full_key) < len(message):
        full_key.append(key[i])
        i = i + 1 if i + 1 < len(key) else 0

    encrypted = []
    for j, c in enumerate(message):
        encrypted.append(c ^ full_key[j])
    return encrypted
