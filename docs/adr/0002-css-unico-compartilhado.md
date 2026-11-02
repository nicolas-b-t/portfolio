---
status: accepted
date: 2026-11-02
decision-makers: Responsável pelo projeto
consulted: —
informed: —
---

# CSS único compartilhado

## Contexto e problema

As cinco variantes usam a mesma identidade visual e a mesma estrutura de página.
Copiar o CSS por variante criaria divergência e retrabalho.
O projeto não usa framework nem pré-processador.

## Drivers

- consistência visual entre variantes;
- manutenção em um único lugar;
- ausência de dependência externa;
- simplicidade de publicação.

## Opções consideradas

- um CSS comum em `static/assets/css/styles.css`;
- um CSS por variante;
- framework ou pré-processador.

## Decisão

Escolhida: **um CSS comum**, referenciado por todas as páginas.
Não há cópia por idioma.

## Consequências

- Boa: uma alteração visual vale para todas as variantes.
- Boa: menos arquivos e menos divergência.
- Ruim: uma regressão afeta todas as páginas.
- Ruim: a folha cresce e exige organização por seções.

## Confirmação

Conferir um único arquivo CSS e o mesmo caminho em todas as páginas.
Conferir impressão, temas e `prefers-reduced-motion` após mudança visual.
