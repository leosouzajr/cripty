def ksa(chave):
    comprimento_chave = len(chave)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + chave[i % comprimento_chave]) % 256
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

def rc4_descriptografar(texto_criptografado, chave):
    chave = [ord(c) for c in chave]
    S = ksa(chave)
    fluxo_chave = prga(S)
    bytes_criptografados = [int(texto_criptografado[i:i+2], 16) for i in range(0, len(texto_criptografado), 2)]
    texto_descriptografado = ''.join([chr(byte ^ next(fluxo_chave)) for byte in bytes_criptografados])
    
    return texto_descriptografado

mensagem_criptografada = input("Digite a mensagem criptografada (em hexadecimal): ")
chave = input("Digite a chave de criptografia: ")
mensagem_descriptografada = rc4_descriptografar(mensagem_criptografada, chave)
print("Mensagem descriptografada: ", mensagem_descriptografada)




























#passowrdmain
