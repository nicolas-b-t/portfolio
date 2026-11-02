---
status: accepted
date: 2026-11-02
decision-makers: Responsável pelo projeto
consulted: —
informed: —
---

# Cinco variantes linguísticas com base em pt-BR

## Contexto e problema

O currículo atende públicos de Brasil, Portugal, América do Sul e Espanha, além de leitores de inglês.
Cada variante tem termos, níveis e convenções próprias.
Há risco de divergência factual entre idiomas.

## Drivers

- alcance internacional;
- precisão factual;
- respeito às variantes de português e espanhol;
- uso de inglês norte-americano em `en/`;
- expansão futura para outros idiomas.

## Opções consideradas

- uma única língua;
- tradução automática sem revisão;
- cinco variantes mantidas manualmente, com base em pt-BR.

## Decisão

Escolhida: **cinco variantes**, com `pt-BR` como base factual.
`en/` usa inglês norte-americano e `lang="en-US"`.
`es-419` e `es-ES` preservam as diferenças editoriais.

## Consequências

- Boa: cada público lê na sua variante.
- Boa: a base factual fica explícita.
- Ruim: toda mudança de fato exige sincronização.
- Ruim: o custo cresce com novos idiomas.

## Confirmação

Conferir as cinco pastas, o `lang` de cada página e os links `hreflang`.
Comparar fatos com `pt-BR` ou registrar a divergência.
