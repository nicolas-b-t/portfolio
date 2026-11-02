---
status: accepted
date: 2026-11-02
decision-makers: Responsável pelo projeto
consulted: —
informed: —
---

# Cópia estruturada oculta

## Contexto e problema

Leitores automáticos, como sistemas de acompanhamento de candidaturas, precisam de texto simples e completo.
A página visível usa cartões, colunas e agrupamentos.
Duplicar todo o conteúdo de forma visível pioraria a leitura humana.

## Drivers

- leitura por máquina;
- uma única fonte de verdade;
- ausência de JavaScript;
- preservação da leitura visual e da impressão.

## Opções consideradas

- repetir o conteúdo em bloco visível;
- manter uma seção oculta no HTML;
- publicar um arquivo separado apenas para máquinas.

## Decisão

Escolhida: **seção oculta** `#dados-curriculo` e `#dados-projetos`.
A seção usa o atributo `hidden` e os mesmos fatos da tela.

## Consequências

- Boa: o conteúdo fica no mesmo documento e sem requisição extra.
- Boa: não altera a apresentação visual.
- Ruim: exige sincronização manual com a tela.
- Ruim: pode sair de sincronia sem aviso.

## Confirmação

Comparar os dados da cópia oculta com a tela.
Conferir que a cópia não aparece na tela nem na impressão.
