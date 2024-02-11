numero_str = input('Insira um número para dobrar: ')
try:
    print("STR: ", numero_str)
    numero_float = float(numero_str)
    print("Float: ", numero_float)
    print(f"O dobro de {numero_str} é {numero_float * 2}")
except:
    print("Isso não é um número")


    #Não se usa assim, apenas agora pois estou aprendendo