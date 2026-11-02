---
status: accepted
date: 2026-11-02
decision-makers: Responsável pelo projeto
consulted: —
informed: —
---

# Site estático sem JavaScript

## Contexto e problema

O site publica currículo, projetos, galeria e recomendações em cinco variantes.
O conteúdo muda por edição manual e não há login, formulário ou dado de entrada.
A hospedagem é o GitHub Pages, sem orçamento próprio.

## Drivers

- simplicidade de operação e manutenção;
- segurança e menor superfície de ataque;
- acessibilidade e leitura por máquina;
- publicação sem etapa de build;
- custo zero.

## Opções consideradas

- HTML e CSS estáticos;
- aplicação de página única com JavaScript;
- gerador de site com etapa de build.

## Decisão

Escolhida: **HTML e CSS estáticos**.
O site não usa JavaScript, formulário, iframe ou rastreador.

## Consequências

- Boa: páginas rápidas, previsíveis e fáceis de auditar.
- Boa: publicação direta de `static/`, sem dependência de build.
- Ruim: sem interatividade, formulário ou analytics.
- Ruim: atualização manual e sem CMS.

## Confirmação

Conferir ausência de `<script>`, `<form>` e `<iframe>` nas 22 páginas.
Conferir que o workflow copia `static/` sem etapa de build.
