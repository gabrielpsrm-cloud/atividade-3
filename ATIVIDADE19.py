peso_atual = 46
limite_maximo = 50

if peso_atual + 5 > limite_maximo:
    print("Inventario cheio")
else:
    peso_atual += 5
    print("Item adicionato")
