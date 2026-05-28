# Sistema de Análise de Desastres Naturais

**Autores:** Igor e Vitor  
**Disciplina:** Python  
**Entrega:** Global Solution (GS)

---

## Descrição

Sistema de registro e análise de eventos de desastres naturais via terminal. O usuário cadastra múltiplos eventos e o programa gera um relatório com análises estatísticas.

---

## Funcionalidades

- Cadastro de múltiplos eventos com validação de entrada
- Cálculo de área total afetada e média de intensidade
- Identificação da região com maior número de ocorrências
- Contagem de eventos acima da média de intensidade
- Densidade média de ocorrências por km²
- Identificação do evento mais crítico (maior intensidade; em empate, maior área)

---

## Dados de Entrada por Evento

| Campo | Tipo | Restrição |
|---|---|---|
| Tipo de evento | texto | — |
| País | texto | — |
| Região | texto | — |
| Cidade | texto | — |
| Área afetada | decimal | maior que 0 |
| Intensidade | inteiro | entre 1 e 10 |
| Ocorrências | inteiro | maior que 0 |

---

## Como Executar

```bash
python 26.1.GS.Igor.Vitor.py
```

Informe a quantidade de eventos quando solicitado e preencha os dados de cada um. Ao final, o relatório é exibido no terminal.

---

## Exemplo de Saída

```
========================================
        RELATÓRIO DE ANÁLISE
========================================

Total de eventos registrados: 2

----------------------------------------
Resumo Geral
----------------------------------------
Área total afetada: 1500 km²
Média de intensidade: 7.5

----------------------------------------
Análises
----------------------------------------
Região com maior número de ocorrências: Sudeste
Quantidade de eventos acima da média de intensidade: 1
Densidade média de ocorrências: 0.03 ocorrências/km²

----------------------------------------
Evento Mais Crítico
----------------------------------------
Tipo: Enchente
Local: São Paulo, Sudeste, Brasil
Intensidade: 9
Área afetada: 1000 km²

========================================
Total de desastres registrados: 2
```
