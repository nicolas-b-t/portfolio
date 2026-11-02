---
status: accepted
date: 2026-11-02
decision-makers: Responsável pelo projeto
consulted: —
informed: —
---

# Ícones por máscara CSS

## Contexto e problema

As páginas usam ícones pequenos em títulos, listas e botões.
Os ícones precisam acompanhar a cor do texto nos temas claro e escuro.
O projeto não usa JavaScript nem fonte de ícones externa.

## Drivers

- herança automática de cor;
- recursos locais;
- ausência de requisição externa;
- repetição mínima no HTML.

## Opções consideradas

- SVG embutido em cada ocorrência;
- fonte de ícones;
- máscara CSS com SVG local e atributo `data-icon`.

## Decisão

Escolhida: **máscara CSS** com SVGs em `static/assets/icons/`.
O seletor `[data-icon]` usa `mask-image` e `currentcolor`.

## Consequências

- Boa: a cor acompanha o texto e os temas.
- Boa: o HTML fica curto.
- Boa: os arquivos são locais e cacheados.
- Ruim: depende de suporte a `mask`.
- Ruim: os ícones Lucide exigem aviso de licença.

## Confirmação

Conferir os 29 SVGs e os seletores `[data-icon]`.
Conferir ausência de fonte de ícones externa.
Incluir o aviso ISC dos ícones Lucide.
