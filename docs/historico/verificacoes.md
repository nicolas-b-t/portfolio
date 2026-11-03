# Verificações de 02/11/2026

Evidência histórica dos ensaios realizados nesta data.
Este documento não é procedimento. O guia vigente está em [Manutenção](../manutencao.md).

## Página de projetos em pt-BR

Objetivo e decisão: separar a apresentação dos projetos, com acesso no início do currículo, reutilizando o CSS comum e preservando integralmente as descrições. Fundamentação: HTML Living Standard, seções de navegação, conteúdo principal e links; WCAG 2.2, critérios de reorganização, propósito do link e foco visível. A restrição desta entrega ao pt-BR é decisão do responsável.

Verificação em 02/11/2026: navegação de ida, três cartões na nova página, links e âncoras locais, um main por página, link de salto por teclado com foco visível, temas claro/escuro e larguras de 1280 e 320 CSS px no Chromium local. Não houve transbordamento horizontal; 320 CSS px cobre a largura equivalente a 400% de zoom em 1280 px. Em mídia de impressão, a cópia oculta permanece invisível e os 17 cursos aparecem na lista de impressão do currículo. Inspeção visual de capturas e cálculo amostral de contraste realizados.

Limites: zoom real e paginação física não ensaiados; sem validação externa de HTML, leitor de tela ou declaração de conformidade WCAG. A estrutura pt-BR foi conferida por listagem local. Sem publicação nesta entrega.

## Ícones Lucide em pt-BR

Objetivo, decisão e fundamentação: centralizar a manutenção dos ícones em uma única pasta e no CSS compartilhado, mantendo HTML/CSS estáticos sem JavaScript e herança automática de cor nos temas claro, escuro, `:hover` e impressão. Fundamentação: HTML Living Standard (atributos `data-*`), CSS Color Level 4 (`currentcolor`), CSS Values and Units Level 4 (resolução de URLs relativas ao arquivo CSS), WCAG 2.2 (critérios `1.1.1` — Conteúdo Não Textual / Decoração e `1.4.11` — Contraste Não Textual) e CSS Color Adjustment Level 1 (`prefers-color-scheme` e `print-color-adjust: exact`). A restrição desta entrega ao pt-BR é decisão do responsável.

Verificação em 02/11/2026 (inspeção de código e checagem estática): conferência dos 28 arquivos SVG em `static/assets/icons/`, correspondência de todos os seletores `[data-icon]` em `static/assets/css/styles.css` com as ocorrências em `static/pt-BR/*.html`, preservação de `#dados-curriculo` e `#dados-projetos` sem atributos visuais, preservação dos 17 cursos na cópia de tela e de impressão, e `git diff --check` sem erros.

Limitações: verificação realizada por inspeção estática de código; ensaio visual interativo em navegador (renderização de `mask`, teclado, foco, contraste amostral, largura de 320 CSS px, zoom de 400%, alternância de temas claro/escuro e paginação física de impressão) pendente de execução no servidor local (`http://127.0.0.1:8001/pt-BR/`). Demais idiomas não alterados por decisão de escopo do responsável.
