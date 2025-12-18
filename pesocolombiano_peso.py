# Tasa de cambio aproximada (1 COP ≈ 0.0046 MXN)
tasa_cambio = 0.0046

cop = float(input("Ingrese la cantidad en pesos colombianos (COP): "))
mxn = cop * tasa_cambio

print(f"{cop} COP equivalen a {mxn:.2f} MXN")

