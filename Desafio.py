#1 
def rev_frase(frase):
    palavras = frase.split()
    palavras_rev = palavras[::-1]
    frase_rev = ' '.join(palavras_rev)
    return frase_rev
frase = 'Hello, World! OpenAI is Amazing.'
frase_rev = rev_frase(frase)
print(frase_rev)

#2 
def rem_car_dup(frase):
    carac_unicos = []
    for caracter in frase:
        if caracter not in carac_unicos:
            carac_unicos.append(caracter)
    frase_sem_duplicados = ''.join(carac_unicos)
    return frase_sem_duplicados
frase = 'Hello, World!'
frase_sem_duplicados = rem_car_dup(frase)
print(frase_sem_duplicados)

#4 
def capitalizar_primeira_letra_palavras(string):
    palavras = string.split()
    palavras_capitalizadas = [palavra.capitalize() for palavra in palavras]
    string_capitalizada = ' '.join(palavras_capitalizadas)
    return string_capitalizada
string = "hello, how are you? i'm fine, thank you."
string_capitalizada = capitalizar_primeira_letra_palavras(string)
print(string_capitalizada)

#5 
def verificar_anagrama_palindromo(string):
    contador = {}
       
    for char in string:
        contador[char] = contador.get(char, 0) + 1
    
    contador_impares = 0
    for count in contador.values():
        if count % 2 != 0:
            contador_impares += 1
    
    if contador_impares <= 1:
        return True
    else:
        return False

string = "racecar"
resultado = verificar_anagrama_palindromo(string)
print(resultado)