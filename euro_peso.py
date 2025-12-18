# Conversor de euros a pesos

# Tasa de cambio (ejemplo: peso mexicano)
# Cambia este valor según el país y la tasa actual
tasa_cambio = 18.50  

euros = float(input("Ingresa la cantidad en euros: "))
pesos = euros * tasa_cambio

print(f"{euros} euros equivalen a {pesos:.2f} pesos")
