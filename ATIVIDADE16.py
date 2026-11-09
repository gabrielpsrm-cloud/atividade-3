escudo_ativo = True
dano_base = 20

if escudo_ativo:
    dano_final = dano_base * 0.5

else:
    dano_final = dano_base

print(f"O dano final recebido foi {dano_final}")