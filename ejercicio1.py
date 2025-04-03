def resolver_piramide(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover piedra de {origen} a {destino}")
    else:
        resolver_piramide(n - 1, origen, auxiliar, destino)
        print(f"Mover piedra de {origen} a {destino}")
        resolver_piramide(n - 1, auxiliar, destino, origen)

n_piedras = 5
resolver_piramide(n_piedras, "Columna A", "Columna C", "Columna B")
def ordenar_piedras(piedras):
    
    return sorted(piedras)


piedras = [5, 2, 8, 1, 3]
piedras_ordenadas = ordenar_piedras(piedras)
print(f"Piedras originales: {piedras}")
print(f"Piedras ordenadas: {piedras_ordenadas}")
