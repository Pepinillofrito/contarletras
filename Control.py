abc = ["a", "b", "c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

palabra = "Melocoton"
diccionario = {}

for letra in palabra:
    if (letra.upper() not in diccionario):
        diccionario[letra.upper()]=1
    else:
        diccionario[letra.upper()]+=1    
    
print diccionario
