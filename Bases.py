baseD = 10 # Base destino

baseO = 4 # Base origen

numero = 333 # Número a convertir

numero = str(numero)[::-1] # Se invierte el número convirtiendolo en str
numero = int(numero) # Se regresa a int

numeroS = [int(x) for x in list(str(numero))] # Almacenamos los digitos del número

fNumero = [] # Variable para almacenar el número final

decimal = 0 # Número convertido en decimal


# Primero convertimos cualquier número a decimal
for i in range(len(numeroS)):
    decimal += numeroS[i] * baseO**i

# Convertimos de decimal a la base solicitada

numero = decimal
while (numero != 0):
    fNumero +=[numero%baseD]
    numero = numero//baseD

# Imprimimos el nuevo numerito
fNumero = list(reversed(fNumero))
for i in fNumero:
    print(i, end='')
