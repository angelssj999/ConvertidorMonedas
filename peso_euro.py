# Conversor de pesos a euros

# Tasa de cambio (ejemplo: peso mexicano a euro)
# Cambia este valor según el país y la tasa actual
tasa_cambio = 18.50  

pesos = float(input("Ingresa la cantidad en pesos: "))
euros = pesos / tasa_cambio

print(f"{pesos} pesos equivalen a {euros:.2f} euros")
