---
status: accepted
date: 2026-11-02
decision-makers: Responsável pelo projeto
consulted: —
informed: —
---

# Publicação restrita a static

## Contexto e problema

O repositório contém documentação, fontes privadas e dados pessoais ignorados pelo Git.
O GitHub Pages publica apenas o que o workflow envia.
Publicar a raiz poderia expor arquivos que não pertencem ao site.

## Drivers

- separar site publicado de documentação interna;
- permissões mínimas;
- ações fixadas por SHA;
- publicação previsível a cada push.

## Opções consideradas

- publicar a raiz do repositório;
- publicar somente `static/`;
- gerar uma pasta de build antes da publicação.

## Decisão

Escolhida: **publicar somente `static/`**.
O workflow copia `static/` para uma pasta temporária e a envia ao Pages.
As ações são fixadas por SHA e as permissões são mínimas.

## Consequências

- Boa: documentação e base privada não são publicadas.
- Boa: o conteúdo publicado é o mesmo que se testa localmente.
- Ruim: todo arquivo do site precisa estar em `static/`.
- Ruim: o deploy depende do workflow e do push na `main`.

## Confirmação

Conferir o passo que copia `static/.` e o caminho enviado.
Conferir `contents: read`, `pages: write` e `id-token: write`.
Abrir a página publicada após o push.
