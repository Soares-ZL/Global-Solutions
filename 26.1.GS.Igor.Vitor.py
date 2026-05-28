tipos_eventos = []
paises = []
regioes = []
cidades = []
areas_afetadas = []
intensidades = []
ocorrencias = []

quantidade = int(input("Insira a quantidade de eventos: "))

for i in range(quantidade):
    print(f"\n--- Evento {i + 1} ---")
    tipo = input("Tipo: ")
    pais = input("País: ")
    regiao = input("Região: ")
    cidade = input("Cidade: ")

    while True:
        try:
            area = float(input("Área: "))
            if area > 0:
                break
            else:
                print("A área deve ser maior que zero.")
        except ValueError:
            print("Digite um número válido.")

    while True:
        try:
            intensidade = int(input("Intensidade: "))
            if intensidade >= 1 and intensidade <= 10:
                break
            else:
                print("A intensidade deve estar entre 1 e 10.")
        except ValueError:
            print("Digite um número inteiro válido.")

    while True:
        try:
            num_ocorrencias = int(input("Ocorrências: "))
            if num_ocorrencias > 0:
                break
            else:
                print("O número de ocorrências deve ser maior que zero.")
        except ValueError:
            print("Digite um número inteiro válido.")

    tipos_eventos.append(tipo)
    paises.append(pais)
    regioes.append(regiao)
    cidades.append(cidade)
    areas_afetadas.append(area)
    intensidades.append(intensidade)
    ocorrencias.append(num_ocorrencias)

# calculos de análise
total_eventos = len(tipos_eventos)
area_total = sum(areas_afetadas)
media_intensidade = sum(intensidades) / total_eventos
densidade_media = sum(ocorrencias) / area_total

# evento com maior área 
idx_maior_area = areas_afetadas.index(max(areas_afetadas))

# região com mais ocorrências
idx_mais_ocorrencias = ocorrencias.index(max(ocorrencias))

# quantidade de eventos acima da média de intensidade
eventos_acima_media = 0
for intens in intensidades:
    if intens > media_intensidade:
        eventos_acima_media += 1

# evento mais crítico: maior intensidade, em caso de empate usa a maior área
idx_critico = 0
for i in range(total_eventos):
    if intensidades[i] > intensidades[idx_critico]:
        idx_critico = i
    elif intensidades[i] == intensidades[idx_critico]:
        if areas_afetadas[i] > areas_afetadas[idx_critico]:
            idx_critico = i

# relatório final
print("\n========================================")
print("        RELATÓRIO DE ANÁLISE")
print("========================================")
print(f"\nTotal de eventos registrados: {total_eventos}")

print("\n----------------------------------------")
print("Resumo Geral")
print("----------------------------------------")
print(f"Área total afetada: {area_total:g} km²")
print(f"Média de intensidade: {media_intensidade:.1f}")

print("\n----------------------------------------")
print("Análises")
print("----------------------------------------")
print(f"Região com maior número de ocorrências: {regioes[idx_mais_ocorrencias]}")
print(f"Quantidade de eventos acima da média de intensidade: {eventos_acima_media}")
print(f"Densidade média de ocorrências: {densidade_media:.2f} ocorrências/km²")

print("\n----------------------------------------")
print("Evento Mais Crítico")
print("----------------------------------------")
print(f"Tipo: {tipos_eventos[idx_critico]}")
print(f"Local: {cidades[idx_critico]}, {regioes[idx_critico]}, {paises[idx_critico]}")
print(f"Intensidade: {intensidades[idx_critico]}")
print(f"Área afetada: {areas_afetadas[idx_critico]:g} km²")

print("\n========================================")
print(f"Total de desastres registrados: {total_eventos}")
