def caesar (texto, bagunça, criptograf = True):
    if not isinstance(bagunça, int):
        return 'Baguça deve ser um valor inteiro.'

    if bagunça < 1 or bagunça > 25:
        return 'Bagunça deve ser um valor maior que 1 e menor que 25'
    if not criptograf:
        bagunça = - bagunça
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    alfabeto_misturado = alfabeto[bagunça:] + alfabeto[:bagunça]

    tradutor = str.maketrans(alfabeto + alfabeto.upper(), alfabeto_misturado + alfabeto_misturado.upper())

    return texto.translate(tradutor)

def criptografar(texto, bagunça):
    return caesar(texto, bagunça)

def decriptografar(texto, bagunça):
    return caesar(texto, bagunça, criptograf=False)

texto_criptografado = criptografar('Matheus', 13)
texto_decriptografado = decriptografar(texto_criptografado, 13)

print(texto_criptografado)
print(texto_decriptografado)
