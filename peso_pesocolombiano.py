# Conversión simple de peso (MXN) a peso colombiano (COP)

pesos = float(input("Ingresa el monto en pesos: "))
tasa = 214.26  # 1 MXN ≈ 235 COP (valor aproximado)

cop = pesos * tasa
print("Equivale a", cop, "pesos colombianos")
