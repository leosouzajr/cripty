def ksa(key):
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def prga(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        yield S[(S[i] + S[j]) % 256]

def rc4_encrypt(text, key):
    key = [ord(c) for c in key]
    S = ksa(key)
    keystream = prga(S)
    encrypted_text = [format((ord(char) ^ next(keystream)), '02x') for char in text]
    return ''.join(encrypted_text)

# Recebe a mensagem e a chave do usuário
mensagem = input("Digite a mensagem que deseja criptografar: ")
chave = input("Digite a chave de criptografia: ")

# Criptografa a mensagem usando o RC4
mensagem_criptografada = rc4_encrypt(mensagem, chave)

# Imprime a mensagem criptografada
print("Mensagem criptografada: ", mensagem_criptografada)


















#passowrdmain
